


import psutil
 
# Iterate over all the keys in the dictionary
for interface in psutil.net_if_addrs():
    # Check if the interface has a valid MAC address
    if psutil.net_if_addrs()[interface][0].address:
        # Print the MAC address for the interface
        print(psutil.net_if_addrs()[interface][0].address)
        break