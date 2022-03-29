def check_even(num):
    return num%2 == 0

mynum = [1,2,3,4,5,6]

for n in filter(check_even,mynum):
    print(n)