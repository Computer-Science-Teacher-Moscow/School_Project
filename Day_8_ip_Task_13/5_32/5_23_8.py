from ipaddress import ip_network, ip_address

net = ip_network('192.168.0.1/255.255.240.0', 0)
print(net.num_addresses - 2)

for ip in net:
    print(ip)
