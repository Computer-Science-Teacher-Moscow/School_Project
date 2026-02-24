from ipaddress import ip_network, ip_address

net = ip_network('45.172.106.203/255.255.252.0', 0)
for ip in net:
    print(ip)
print('----' * 10)
print((min(net.hosts())))
