from ipaddress import ip_address, ip_network

net = ip_network('172.95.116.174/255.255.192.0', 0)

for ip in net:
    ip1 = f'{ip:b}'
    if ip1.count('1') % 5 == 0:
        print(ip)
        break