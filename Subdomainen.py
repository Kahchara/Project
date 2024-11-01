import argparse
import requests

##---------------------------------------------------------##

def subdomain_enum():
    found_subdomain = []

    with open(wordlist, 'r') as file:
        word = word.strip()
        subdomain = f'http://{word}.{domain}'


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

##-------------------------------------------------------------##

def main():
    parser = argparse.ArgumentParser(description="This is a subdomain enumerator :)")
    parser.add_argument("--domain", required=True, help="Domain to enumerate subdomain on")
    parser.add_argument("--worldist", required=True, help="The path to the wordlist with the subdomains you wish to test")

args = parser.parse_args()

found = subdomain_enum(args.domain, args.wordlist)
if found:
    print(f"\n[+] Discovered subdomains:")
    for sub in found:
        print(sub)
    else:
        print("[-] No subdomain found")


if __name__ == "__main__":
    main()