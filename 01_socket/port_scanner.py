# Simple Port Scanner using socket
# Works in Google Colab / any Python environment

import socket

# Define Target and ports
target_ip = ""  # Put your target IP here
ports = [21, 22, 23, 25, 53, 80, 110, 443]

# Create a scanning function
def scan_port(ip, port):
    """
    This function tries to connect to a specific port
    on the target IP using TCP.
    """
    try:
        # Create a socket object (IPv4, TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout so it doesn't keep waiting
        sock.settimeout(1)
        # Try to connect to port
        result = sock.connect_ex((ip, port))
        
        # if result == 0, port is open
        if result == 0:
            print(f"Port {port} on {ip} is OPEN")
        else:
            print(f"Port {port} on {ip} is CLOSED")
        
        sock.close()
        
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

# Start scan
print(f"Starting scan on target: {target_ip}")

# Loop through each port in the list
for port in ports:
    scan_port(target_ip, port)

print("Scan complete.")
