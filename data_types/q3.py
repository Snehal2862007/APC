server_ip=("192.168.1.1",)
allowed_ips=["192.168.1.2","192.168.1.3"]
def update_allowed_ip(ip):
    allowed_ips.append(ip)
print("server IP:",server_ip)
print("allowed IPs:",allowed_ips)
ip=input("enter new allowed IP: ")
update_allowed_ip(ip)
print("cannot change Server IP ")
print("Updated Configuration")
print("server IP:",server_ip)
print("allowed IPs:",allowed_ips)