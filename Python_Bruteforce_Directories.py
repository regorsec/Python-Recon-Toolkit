import requests
import argparse

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Target URL', required=True)
parser.add_argument('-w', '--wordlist', help='Path to dictionary file', required=True)
parser.add_argument('-H', '--header', help='Custom HTTP header to include in GET requests')
args = parser.parse_args()

# Read the wordlist file
with open(args.wordlist, 'r') as f:
    wordlist = f.read().splitlines()

# Make HTTP requests to each directory in the wordlist
for word in wordlist:
    url = args.target + word
    headers = {'User-Agent': 'Mozilla/5.0'} # Default user agent header
    if args.header:
        header_key, header_value = args.header.split(":")
        headers[header_key] = header_value

    response = requests.get(url, headers=headers)

    # Check if the response is a 200 or 301 status code
    if response.status_code in [200, 301]:
        print(f"{url} - Status code: {response.status_code}")

