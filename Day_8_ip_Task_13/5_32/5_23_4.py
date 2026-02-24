from ipaddress import ip_address, ip_network

ip_host_1 = ip_address('11.156.152.142')
ip_host_2 = ip_address('11.156.157.39')

for mask in range(32,0, -1):
    net_1 = ip_network(f'{ip_host_1}/{mask}', 0)
    net_2 = ip_network(f'{ip_host_2}/{mask}', 0)
    if net_1 == net_2 and net_1[0] < ip_host_1 < net_1[-1] and net_1[0] < ip_host_2 < net_1[-1]:
        print(net_1.netmask)
        break
