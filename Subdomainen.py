
#Libraries necessary to run the code
##------------------------------------------------------------##
import argparse
import requests

#The primary function for the subdomain enumerator
##------------------------------------------------------------##
def subdomain_enum(domain, wordlist):
    found_subdomain = []

#With open will allow us to print out the found subdomains to a separate text document
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            subdomain = f'http://{word}.{domain}'


#This try function has a timeout of one second, and if the response status==200 means if the subdomain is up and found
            try:
                response = requests.get(subdomain, timeout=1)

                if response.status_code == 200:
                    print(f"[+] Found subdomain: {subdomain}")
                    found_subdomain.append(subdomain)
                else:
                    print(f"[-] Not found: {subdomain}")
            except requests.ConnectionError:
                print(f"[-] No response from subdomain")
            except requests.RequestException as e:
                print(f"An error has occured: {e}")
    return found_subdomain

#The main argparse function which will call on the subdomain enumerator above to run the program from the terminal
##-------------------------------------------------------------##
def main():
    parser = argparse.ArgumentParser(description="This is a subdomain enumerator :)")
    parser.add_argument("--domain", required=True, help="Domain to enumerate subdomain on")
    parser.add_argument("--wordlist", required=True, help="The path to the wordlist with the subdomains you wish to test")

    args = parser.parse_args()

#This code will print the result in the terminal as well, allowing for faster confirmation of which sites are up
    found = subdomain_enum(args.domain, args.wordlist)
    if found:
        print(f"\n[+] Discovered subdomains:")
        for sub in found:
            print(sub)
    else:
        print("[-] No subdomain found")


if __name__ == "__main__":
    main()
