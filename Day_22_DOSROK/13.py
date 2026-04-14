from ipaddress import ip_address, ip_network

net = ip_network('146.180.173.153/255.192.0.0', 0)
print(net[-2])

print(net.num_addresses - 2)

# cnt = 0
# for ip in net:
#     cnt += 1
# print(cnt - 2)
