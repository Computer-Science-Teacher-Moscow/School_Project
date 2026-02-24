from ipaddress import ip_network, ip_address

net = ip_network('218.194.82.148/255.255.255.192', 0)
for ip in net:
    print(ip)
print('----' * 5)
print((max(net.hosts())))
