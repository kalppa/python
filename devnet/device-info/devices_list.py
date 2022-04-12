with open('device.txt','w') as f:
    f.write('device1,ios,10.3.21.5,user1,pass1')

with open('device.txt','r') as f:
    file_info = f.readline().strip()
    print(file_info)
    device_info = file_info.split(',')
    print(device_info)
