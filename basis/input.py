
"""input输入的类型都是str类型"""

# name = input('Please input your name:')
# phone_number = input('Please input your phone number:')
# print (name, phone_number, sep='\n')
# # print('Name: {}\nPhone:{}' .format(name,phone_number))
# print (type(name))
# print (type(phone_number))


#因为input输入的类型是%s str，所以使用%d print的时候会有问题

#
# print('Name: %s\nPhone:%d' %(name,phone_number))
# print (type(name))
# print (type(phone_number))

""""Validate User Input"""
def user_choice():
    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # TWO CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE == FALSE
    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number (0-10): ')

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry, please input a digit.")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Please input the number in range.')
    return int(choice)
user_choice()












