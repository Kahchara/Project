import argparse
import requests

##----------------------------------------------------------------##

def directory_fuzzer(url, wordlist):
    found_paths = []

    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            test_url = f'{url}/{word}'
            try:
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(f'[+] Found: {test_url}')
                    found_paths.append({test_url})
                else:
                    print(f'[-] Not found: {test_url}')
            except requests.RequestException as e:
                print(f'Problem with connecting to {test_url}: {e}')
            break
    return found_paths

##------------------------------------------------------------------##
#Main function 
def main():
    parser = argparse.ArgumentParser(description="A simple directory fuzzer")
    parser.add_argument("--url", required=True, help="The target url")
    parser.add_argument("--wordlist", required=True, help="The path to the wordlist file")

    args = parser.parse_args()

    found = directory_fuzzer(args.url, args.wordlist)
    if found:
        print("\n[+] Discovered paths:")
        for path in found:
            print(path)
    else:
        print("[-] No path found")


if __name__ == "__main__":
    main()