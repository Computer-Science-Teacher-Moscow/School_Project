from ipaddress import ip_network, ip_address

ip_host = ip_address('143.131.211.37')

for mask in range(32,-1,-1):
    net = ip_network(f'{ip_host}/{mask}', 0)
    cnt_1 = 0
    for ip in net:
        ip = f'{ip:b}'
        if ip.count('1') == 10:
            cnt_1 +=1
    if cnt_1 == 15:
        print(mask)