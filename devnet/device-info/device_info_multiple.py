with open('device-multiple.txt.txt','r') as f:
    file_info = f.readline().strip()
    print(file_info)
    device_info = file_info.split(',')
    print(device_info)
