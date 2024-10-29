import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get user input for host and port
host = input("Enter the Host: ")
port = int(input("Enter the Port: "))  # Convert port to an integer

def portScanner(host, port):
    try:
        # Set a timeout for the connection attempt
        s.settimeout(1)
        # Attempt to connect to the specified host and port
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()  # Close the socket

# Call the port scanner function
portScanner(host, port)
