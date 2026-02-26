from ipaddress import ip_network, ip_address

net = ip_network('46.29.170.214/255.255.128.0', 0)

# for ip in (list(net))[::-1][1:-1]: # Если нужно сократить время вычисления (идем от максимального ip вниз)
for ip in list(net)[1:-1]:

    l = sorted([int(x) for x in str(ip).split('.')])
    if l[-1] == sum(l[:-1]):
        print(str(ip).replace('.',""))



