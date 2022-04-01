my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])

# Add a new key
my_dict['key3'] = 'value3'
print(my_dict['key3'])

# Remove a key
del my_dict['key3']
# print(my_dict['key3'])

""" Dictionary with other Data Types """

dev1 = {'name':'xrv-0','ip':'10.1.1.1','user':'cisco'}
dev2 = {'name':'xrv-1','ip':'10.1.1.2','user':'cisco'}
dev3 = {'name':'xrv-2','ip':'10.1.1.3','user':'cisco'}

# Dictionaries with Lists
dev_list= list()
dev_list.append(dev1)
dev_list.append(dev2)
dev_list.append(dev3)
print(dev_list)


# Dictionaries with Dictionaries

devices = {}
devices['xrv-0'] = dev1
devices['xrv-1'] = dev1
devices['xrv-2'] = dev1

print(devices)
