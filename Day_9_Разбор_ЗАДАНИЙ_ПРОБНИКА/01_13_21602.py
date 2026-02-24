from ipaddress import ip_network, ip_address

wild_card_mask = ip_address('0.0.7.255')
wild_card_mask = f'{wild_card_mask:b}'
print(wild_card_mask)
mask = wild_card_mask.count('0')
net = ip_network(f'172.16.80.0/{mask}')
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 3 != 0:
        cnt += 1
print(cnt)
