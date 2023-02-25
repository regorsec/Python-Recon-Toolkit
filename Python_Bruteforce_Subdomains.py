import requests
import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description='HTTP requests to a target subdomain for each string in a file.')
parser.add_argument('-t', '--target', required=True, help='target domain name')
parser.add_argument('-w', '--wordlist', required=True, help='file containing strings (one per line)')
args = parser.parse_args()

# open wordlist file and read lines
with open(args.wordlist, 'r') as f:
    lines = f.readlines()

# remove newline characters from end of lines
lines = [line.strip() for line in lines]

# loop through lines and make HTTP request to target subdomain
for line in lines:
    url = f'https://{line}.{args.target}'
    try:
        response = requests.get(url)
        if response.status_code < 400:
            print(f'{url} --> {response.status_code}')
    except:
        pass
