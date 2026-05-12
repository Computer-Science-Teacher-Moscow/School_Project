from ipaddress import ip_network

net = ip_network('134.80.0.0/255.240.0.0')
res = []

for ip in list(net.hosts())[::-1]:
    ip_b = f'{ip:b}'
    if ip_b.count('1') == 16:
        print(ip)
        input(-)

