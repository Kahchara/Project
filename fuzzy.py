#The necessary libraries rto run the code
##---------------------------------------------------------------##
import argparse
import requests

#The directory_fuzzer function which will be called on in the main function
##----------------------------------------------------------------##
def directory_fuzzer(url, wordlist):
    found_paths = []
#With open will allow the directories to be loaded in from a separate text file
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            test_url = f'{url}/{word}'
#This try function will test if the url/subdomain has the status code 200, which would tell us that the site exists            
            try:
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(f'[+] Found: {test_url}')
                    found_paths.append(test_url)
                else:
                    print(f'[-] Not found: {test_url}')
            except requests.RequestException as e:
                print(f'Problem with connecting to {test_url}: {e}')
    return found_paths

#Main function which will call on the earlier directory_fuzzer function, allowing it to be run from the terminal using the argparse library
##------------------------------------------------------------------##
def main():
    parser = argparse.ArgumentParser(description="A simple directory fuzzer")
    parser.add_argument("--url", required=True, help="The target url")
    parser.add_argument("--wordlist", required=True, help="The path to the wordlist file")

    args = parser.parse_args()

#This will print out the results from the scan to the terminal
    found = directory_fuzzer(args.url, args.wordlist)
    if found:
        print("\n[+] Discovered paths:")
        for path in found:
            print(path)
    else:
        print("[-] No path found")


if __name__ == "__main__":
    main()
