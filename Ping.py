#The necessary libraries to run the code
##------------------------------------------------------##
import argparse
import subprocess  

#The ping_sweep function that will be responsible for sending out the pings to the targeted IP-adresses
##-------------------------------------------------------##
def ping_sweep(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))

    active_hosts = []

    print(f"Scanning ip:{start_ip} to {end_ip}")
    #This part is responsible for looping through all of the IP-adresses and ensures that they are formatted correctly
    for i in range(start[3], end[3] + 1):
        ip = f"{start[0]}.{start[1]}.{start[2]}.{i}"

        try:
            result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            #If the program gets a response it will indicate that the IP is active
            if result.returncode == 0:
                print(f"[+] Host {ip} is active")
                active_hosts.append(ip)
            
            else: 
                print(f"[-] Host {ip} is inactive")
        
        except Exception as e:
            print(f"A problem has occured: {e}")
    return active_hosts

#The main argparse function that will allow the program to be run in the terminal and will call on the previous ping_sweep function
##---------------------------------------------------------##
def main():
    parser = argparse.ArgumentParser(description="A ping sweeper tool")
    parser.add_argument("--start-ip", required=True, help="The starting IP-adress of the range (1.1.1.1)")
    parser.add_argument("--end-ip", required=True, help="The end of the IP-adress range (1.1.1.999)")

    args = parser.parse_args()

    active_hosts = ping_sweep(args.start_ip, args.end_ip)
    
    #This will print out the results to the terminal 
    if active_hosts:
        print("\n[+] Active IP-adresses found:")
        for host in active_hosts:
            print(host)
    else:
        print("[-] No active hosts found")

if __name__ == "__main__":
    main()
