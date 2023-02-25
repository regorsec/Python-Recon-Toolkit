import socket
import argparse

# Setup argument parser for taking command line input
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Target IP address to scan")
parser.add_argument("-minp", "--minport", help="Minimum port to scan", type=int)
parser.add_argument("-maxp", "--maxport", help="Maximum port to scan", type=int)
args = parser.parse_args()

# Define Variables
TARGET_IP = args.target
MIN_PORT = args.minport
MAX_PORT = args.maxport

# Create a list for open ports
open_ports = []

# Loop through the range of ports to scan
for port in range(MIN_PORT, MAX_PORT + 1):
    # Create a new socket object for each port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    # Attempt to connect to the port
    result = sock.connect_ex((TARGET_IP, port))
    
    # If the connection was successful, add the port to the list of open ports
    if result == 0:
        open_ports.append(port)
    
    # Close the socket object
    sock.close()

# Print the list of open ports
print("Open ports on", TARGET_IP, "are:", open_ports)
