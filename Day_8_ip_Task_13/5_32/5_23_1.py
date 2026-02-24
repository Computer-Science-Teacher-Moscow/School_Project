from ipaddress import ip_address, ip_network

ip_host = ip_address('124.128.112.142')
ip_net = ip_address('124.128.64.0')

# print(f'{ip_host:b}')
# print(f'{ip_net:b}')
for mask in range(32,0, -1):
    net = ip_network(f'{ip_host}/{mask}', 0)
    # print(net.with_netmask)
    if net.network_address == ip_net and net[0] < ip_host < net[-1]:
        print(net.with_netmask)
        print(str(net.netmask).split('.')[-2])