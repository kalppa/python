with open('device.txt','w') as f:
    f.write('device1,ios,10.3.21.5,user1,pass1')

with open('device.txt','r') as f:
    file_info = f.readline().strip()
    device_info_list = file_info.split(',')
    print(device_info_list)

    # Create my device info dictionary
    device_info = {}
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]

    print(device_info)

