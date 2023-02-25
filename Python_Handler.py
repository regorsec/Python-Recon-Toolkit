import argparse
import socket
import sys
import select
import threading

parser = argparse.ArgumentParser(description='Listen for incoming connections on a specified port.')
parser.add_argument('-p', '--port', type=int, required=True, help='the port number to listen on')
args = parser.parse_args()

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = args.port  # Use the specified port number

# Create a TCP socket and bind it to the specified address and port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)  # Allow only one client to connect

    # Wait for an incoming connection
    conn, addr = s.accept()
    print('Connected by', addr)

    # Define a function to read input from the terminal in a separate thread
    def terminal_input():
        while True:
            data = input()
            if not data:
                conn.shutdown(socket.SHUT_WR)
                break
            conn.sendall(data.encode())

    # Start the thread to read input from the terminal
    t = threading.Thread(target=terminal_input)
    t.daemon = True
    t.start()
 
    # Handle the connection
    while True:
        # Use select to wait for input from either the client or the thread
        read, write, error = select.select([conn], [], [])

        if conn in read:
            # If the input is from the client, receive data and print it to the terminal
            data = conn.recv(1024)
            if not data:
                print('Connection closed by remote end.')
                break
            else:
                sys.stdout.write(data.decode())
                sys.stdout.flush()
