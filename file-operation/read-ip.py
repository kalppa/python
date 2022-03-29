f = open('device-ip.txt', 'r')
# print(f.readlines())
ip1 = f.readline()
ip2 = f.readline()
ip3 = f.readline()
print(f'IP1 = {ip1}')
print(f'IP2 = {ip2}')
print(f'IP3 = {ip3}')
# print(f.readline())
# ip1 = f.readline()
# print(ip1)
f.close()

""" Remove the '\n' at the end of each line """
# strip() only works for strings but not for lists, so strip() will not work with readlines()

f = open('device-ip.txt', 'r')
# print(f.readlines())
ip1 = f.readline().strip()
ip2 = f.readline().strip()
ip3 = f.readline().strip()
print(f'IP1 = {ip1}')
print(f'IP2 = {ip2}')
print(f'IP3 = {ip3}')
# print(f.readline())
# ip1 = f.readline()
# print(ip1)
f.close()


""" Use for loops """
print('\n'*2)
print('--- Using for loops ---')

f = open('device-ip.txt', 'r')
for ip in f.readlines():
    print(ip.strip())
    # print(ip)
f.close()

