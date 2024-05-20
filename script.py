#!/usr/bin/python3

import socket
from ipaddress import ip_address

def reverse_ip_lookup(ip):
    try:
        # Validate the IP address
        ip_address(ip)
        # Perform the reverse lookup
        return socket.gethostbyaddr(ip)
    except ValueError:
        return "Error: Invalid IP address format."
    except socket.herror:
        return "Error: No host found for the given IP address."
    except socket.gaierror:
        return "Error: Network-related error occurred during the lookup."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


ip_to_lookup = input("Enter the IP address:")
result = reverse_ip_lookup(ip_to_lookup)
print(result)

