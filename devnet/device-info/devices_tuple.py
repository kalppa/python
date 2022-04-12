from pprint import pprint

with open('tuple.txt','r') as f:
    device = f.readline()
    pprint(device)
    pprint(type(device))
