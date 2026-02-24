from ipaddress import ip_address, ip_network

net = ip_network('205.99.68.249/255.255.248.0', 0)
print(max(net.hosts()))