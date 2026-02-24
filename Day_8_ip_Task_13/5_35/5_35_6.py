from ipaddress import ip_address, ip_network

net = ip_network('45.172.106.203/255.255.252.0', 0)
print(min(net.hosts()))