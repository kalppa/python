
device = []
with open('device-multiple.txt','r') as f:
     for line in f:
         device_info_list = line.strip().split(',')
         # print(device_info_list)

         # Pute device info to a dictionary
         device_info = {}
         device_info['name'] = device_info_list[0]
         device_info['os-type'] = device_info_list[1]
         device_info['ip'] = device_info_list[2]
         device_info['username'] = device_info_list[3]
         device_info['password'] = device_info_list[4]
         print(device_info)

         # Create a device list
         device.append(device_info)
# print(device)

from pprint import pprint
pprint(device)
