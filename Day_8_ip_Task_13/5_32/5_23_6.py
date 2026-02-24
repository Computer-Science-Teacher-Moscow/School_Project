from ipaddress import ip_address, ip_network

ip_host = ip_address('173.103.25.118')
ip_net = ip_address('173.103.24.0')

for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == ip_net and net[0] < ip_host < net[-1]:
        print(32 - mask)
        break
