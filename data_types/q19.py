import re

def check_ip(ip):
    ipv4 = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4, ip) or re.match(ipv6, ip):
        return True
    return False

ip = input("enter ip address: ")

if check_ip(ip):
    print("valid ip address")
else:
    print("invalid ip address")
    