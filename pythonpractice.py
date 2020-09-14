# item_name = input('Enter food item name:\n')
# 
# # FIXME (1): Finish reading item price and quantity, then output a receipt
# 
# item_price = float(input('Enter item price:\n'))
# item_qnt = int(input('Enter item quantity:\n'))
# item_cost = item_price*item_qnt
# 
# print()
# print('RECEIPT')
# print(item_qnt, item_name, '@', '${:.2f}'.format(item_price), '=', '${:.2f}'.format(item_cost))
# print('Total cost:', '${:.2f}'.format(item_cost))
#    
# # FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
# print()
# print()
# item2_name = input('Enter second food item name:\n')
# item2_price = float(input('Enter item price:\n'))
# item2_qnt = int(input('Enter item quantity:\n'))
# item2_cost = item2_price*item2_qnt
# 
# total_cost = item_cost + item2_cost
# 
# print()
# print('RECEIPT')
# print(item_qnt, item_name, '@', '${:.2f}'.format(item_price), '=', '${:.2f}'.format(item_cost))
# print(item2_qnt, item2_name, '@', '${:.2f}'.format(item2_price), '=', '${:.2f}'.format(item2_cost))
# print('Total cost:', '${:.2f}'.format(total_cost))
#  
# # FIXME (3): Add a gratuity and total with tip to the second receipt
# tip_percent = 15
# tip_amt = total_cost * tip_percent/100
# print()
# print('{:.0f}%'.format(tip_percent),'gratuity:', '${:.2f}'.format(tip_amt))
# print('Total with tip:', '${:.2f}'.format(total_cost+tip_amt))
# 
# 


# current_time = '2014-07-26 02:12:18:'
# my_city = ''
# my_state = ''
# log_entry = ''
# 
# ''' Your solution goes here '''
# 
# my_city = 'Houston'
# my_state = 'Texas'
# log_entry = current_time + ' ' + my_city + ' ' + my_state
# 
# 
# print(log_entry)
# 
# 


# 
# list = [1,2,3,4,5,6,7,8,9,10]
# 
# a = list.index(6)
# print(a)
# 
# 
# 
# 
# 
# 
# 
# 
# 

# 
# # FIXME (1): Finish reading another word and an integer into variables. 
# # Output all the values on a single line
# favoriteColor = input('Enter favorite color:\n')
# petName = input('Enter pet\'s name:\n')
# num = input('Enter a number:\n')
# 
# print('You entered: {} {} {}'.format(favoriteColor, petName, num))
# 
# 
# # FIXME (2): Output two password options
# password1 = favoriteColor+'_'+petName
# password2 = num+favoriteColor+num
# 
# print('\nFirst password:',password1)
# print('Second password:',password2)
# 
# # FIXME (3): Output the length of the two password options
# 
# len_p1= len(password1)
# len_p2= len(password2)
# 
# print('\nNumber of characters in {}: {}'.format(password1,len_p1))
# print('Number of characters in {}: {}'.format(password2,len_p2))


# 
# x = int(8005551212)
# a = str(x % 10000)
# b = str((x % 10000000) // 10000)
# c = str(x//10000000)
# 
# print('({}) {}-{}'.format(c,b,a))
#

# x = float(input())
# a = x /2 
# b = a/2
# c = b/2
# 
# ''' Type your code here. '''
# 
# print('After 6 hours: {:.2} mg'.format(a))
# print('After 12 hours: {:.2} mg'.format(b))
# print('After 24 hours: {:.2} mg'.format(c))
# 
# 


# current_price = int(200000)
# last_months_price = int(210000)
# 
# change = current_price - last_months_price
# 
# mortgage = float((current_price*0.051)/12)
# 
# 
# ''' Type your code here. '''
# 
# 
# print('This house is ${}. The change is ${} since last month.'.format(current_price, change))
# print('The estimate monthly mortgage is ${:.2f}.'.format(mortgage))
#    
# 


# 
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
# num4 = float(input())
# 
# prod = num1 * num2 * num3 * num4
# avg = (num1 + num2 + num3 + num4)/4
# 
# print('{:.0f} {:.0f}'.format(prod, avg))
# print('{:.3f} {:.3f}'.format(prod, avg))
# 
# 
# 
# 
# 













# import math as mt
# 
# # Dictionary of paint colors and cost per gallon
# paint_colors = {
#    'red': 35,
#    'blue': 25,
#    'green': 23
# }
# 
# # FIXME (1): Prompt user to input wall's width
# # Calculate and output wall area
# wall_height = int(input('Enter wall height (feet):\n'))
# wall_width = int(input('Enter wall width (feet):\n'))
# 
# area = wall_height*wall_width
# paint = area/350
# 
# print('Wall area: {} square feet'.format(area))
# 
# # FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
# paint = area/350
# print('Paint needed: {:.2f} gallons'.format(paint))
# # FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
# cans = mt.ceil(paint)
# print('Cans needed: {} can(s)\n'.format(cans))
# 
# # FIXME (4): Calculate and output the total cost of paint can needed depending on color
# 
# 
# color = input('Choose a color to paint the wall:\n')
# colorPrice_chosen = int(paint_colors[color]) * cans
# 
# 
# print('Cost of purchasing {} paint: ${}'.format(color, colorPrice_chosen))
# 
# 
# 
# 
# 
# 

# car_year = 1995
# 
# if car_year <= 1969:
#     print('Few safety features.\n')
# if car_year >= 1970:
#     print('Probably has seat belts.\n')
# if car_year >= 1990:
#     print('Probably has antilock brakes.\n')
# if car_year >= 2000:
#     print('Probably has airbags.\n')
# 
# 

# r = int(input())
# g = int(input())
# b = int(input())
# 
# rgb_inputs = [r, g, b]
# 
# if min(rgb_inputs) == r:
#     rgb_min = r
# elif min(rgb_inputs) == g:
#     rgb_min = g
# else:
#     rgb_min = b
#     
# rgb2 = [x-rgb_min for x in rgb_inputs]
# 
# print(*rgb2, sep =' ')


# hw_num = int(input())
# 
# if 0 < hw_num <= 99:
#     hw_type = 'primary'
# elif 100 <= hw_num <= 999:
#     hw_type = 'auxiliary'
# else:
#     hw_type = 'none'
# 
# 
# hw_dir = 'east/west' if hw_num%2 == 0 else 'north/south'
# 
# if hw_type == 'primary':
#     print('I-{} is {}, going {}.'.format(hw_num, hw_type, hw_dir))
# elif hw_type == 'auxiliary':
#     hw_serve = hw_num%100
#     print('I-{} is {}, serving I-{}, going {}.'.format(hw_num, hw_type, hw_serve, hw_dir))
# else:
#     print('{} is not a valid interstate highway number.'.format(hw_num))
# 
#





# input_month = str(input())
# input_day = int(input())
# season = ''
# 
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']
# autumn = ['September','October','November']
# winter = ['December','January','February']
# 
# if input_month in months and (input_day >= 1 and input_day <= 31):
#     if input_month in spring:
#         season = 'Spring'
#     elif input_month in summer:
#         season = 'Summer'
#     elif input_month in autumn:
#         season = 'Autumn'
#     else:
#         season = 'Winter'  
# else:
#     season = 'Invalid'
#     
#     
# if input_month == 'March' and input_day <= 19:
#     season = 'Winter'
# elif input_month == 'June' and input_day <= 20:
#     season = 'Spring'
# elif input_month == 'September' and input_day <= 21:
#     season = 'Summer'
# elif input_month == 'December' and input_day <= 20:
#     season = 'Autumn'
#     
# if input_day < 0:
#     season = 'Invalid'
# 
# if input_month in ('April', 'June', 'September'):
#     if input_day >= 31:
#         season = 'Invalid'
#     else:
#         pass
# elif input_month == 'February':
#     if input_day >= 29:
#         season = 'Invalid'
#     else:
#         pass
#     
# print(season)
#

# amt = int(input())
# 
# dollar = 100
# q = 25
# d = 10
# n = 5
# p = 1
# 
# 
# if amt <= 0 :
#     print('No change')
#     exit()
# else:
#     dollar_back = int(amt // dollar)
#     new_total = amt - (dollar_back*dollar)
#     q_back = int(new_total // q)
#     new_total = new_total - (q_back*q)
#     d_back = int(new_total // d)
#     new_total = new_total - (d_back*d)
#     n_back = int(new_total // n)
#     new_total = new_total - (n_back*n)
#     p_back = int(new_total // p)
#     new_total = new_total - (p_back*p)
#     
# if dollar_back > 0:
#     if dollar_back >= 2:
#         print('{} Dollars'.format(dollar_back))
#     else:
#         print('{} Dollar'.format(dollar_back))
# if q_back > 0:
#     if q_back >= 2:
#         print('{} Quarters'.format(q_back))
#     else:
#         print('{} Quarter'.format(q_back))
# if d_back > 0:
#     if d_back >= 2:
#         print('{} Dimes'.format(d_back))
#     else:
#         print('{} Dime'.format(d_back))
# if n_back > 0:
#     if n_back >= 2:
#         print('{} Nickels'.format(n_back))
#     else:
#         print('{} Nickel'.format(n_back))
# if p_back > 0:
#     if p_back >= 2:
#         print('{} Pennies'.format(p_back))
#     else:
#         print('{} Penny'.format(p_back))
# 
#         
#         
# 
# 
# 

# is_leap_year = False
#    
# input_year = int(input())
# 
# if (input_year % 4) != 0:
#     is_leap_year = False
# elif (input_year % 100) != 0:
#     is_leap_year = True
# elif (input_year % 400) != 0:
#     is_leap_year = False
# else:
#     is_leap_year = True
# 
#     
# if is_leap_year == True:
#     print('{} - leap year'.format(input_year))
# else:
#     print('{} - not a leap year'.format(input_year))




# 
# need = input('Enter desired auto serivce:')
# enter = print('You entered:', need)
# 
# if need.lower() == 'oil change':
#     print('Oil change -- $35')
# elif need.lower() == 'tire rotation':
#     print('Tire rotation -- $19')
# elif need.lower() == 'car wash':
#     print('Car wash == $7')
# else:
#     print('Error: Requested service is not recognized')
# 
# 
# 

# services = {'oil change': 35, 'tire rotation': 19, 'car wash': 7, 'car wax': 12, 'No entry': 0
#             }
# print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')
# 
# input1 = input('Select first service:\n')
# input1x = input1.lower()
# input2 = input('Select second service:\n')
# input2x = input2.lower()
# 
# print('\nDavy\'s auto shop invoice')
# print()
# 
# total = 0 
# price1 = 0
# price2 = 0
# 
# if input1 == '-':
#     input1x = 'No entry'
#     price1 = 'No service'
#     print('Service 1: {}'.format(price1))
# else:
#     price1 = services[input1x]
#     print('Service 1: {}, ${}'.format(input1, price1))
# 
# if input2 == '-':
#     input2x = 'No entry'
#     price2 = 'No service'
#     print('Service 2: {}\n'.format(price2))
# else:
#     price2 = services[input2x]
#     print('Service 2: {}, ${}\n'.format(input2, price2))
# 
# total = services[input1x] + services[input2x]
# 
# 
# print('Total: ${}'.format(total))
# 
#     


# import random
# random.seed(5)
# 
# keep_going = '-'
# next_bid = 0
# 
# while keep_going == '-' or keep_going == 'y':
#    next_bid = next_bid + random.randint(1, 10)
#    print('I\'ll bid ${}!'.format(next_bid))
#    print('Continue bidding?', end=' ')
#    keep_going = input()





# 
# 
# 
# contact_emails = {
#     'Sue Reyn' : 's.reyn@email.com',
#     'Mike Filt': 'mike.filt@bmail.com',
#     'Nate Arty': 'narty042@nmail.com'
# }
# 
# new_contact = input()
# new_email = input()
# contact_emails[new_contact] = new_email
# 
# for name in contact_emails:
#     email = contact_emails[name]
#     print('{} is {}'.format(email, name))
# 
# 
# 
# 
# 
# import random
# 
# num_sixes = 0
# num_sevens = 0
# num_rolls = int(input('Enter number of rolls:\n'))
# 
# if num_rolls >= 1:
#     for i in range(num_rolls):
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         roll_total = die1 + die2
# 
#         #Count number of sixes and sevens
#         if roll_total == 6:
#             num_sixes = num_sixes + 1
#         if roll_total == 7:
#             num_sevens = num_sevens + 1
#         print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))
# 
#     print('\nDice roll statistics:')
#     print('6s:', num_sixes)
#     print('7s:', num_sevens)
# else:
#     print('Invalid number of rolls. Try again.')
#     
#     
# 
# 
# 
# triangle_char = input('Enter a character:\n')
# triangle_height = int(input('Enter triangle height:\n'))
# print('')
# 
# count = 1
# 
# for i in range(triangle_height):
#     print ((triangle_char + " ") * (i+1))
#         
#     
# 
# 
# 



# 
# user_text = 'Listen, Mr. Jones, calm down.'
# 
# count = 0
# new = user_text.replace(' ','')
# new = new.replace('\'', '')
# new = new.replace(',','')
# new = new.replace('.','')
# 
# for char in new:
#     count = count + 1
#     
# print(count)
# 
# 




word = input()
password = ''
count = 0


key = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'
    }

while count < len(word):
    for char in word:
        if char in key:
            new_char = char.replace(char,key[char])
            print(new_char,end='')
            count += 1
        else:
            print(char, end='')
            count += 1
    if count == len(word):
        print('q*s')



# 
# input1 = int(input())
# input2 = int(input())
# 
# if input1 < input2:
#     while input1 <= input2:
#         print(input1, end=' ')
#         input1 += 10
#         if input1 > input2:
#             print(' ')
# else:
#     print('Second integer can\'t be less than the first.')
# 
# 



 
# while True:
#        values = str(input())
#        if values == 'quit' or values == 'Quit' or values == 'q':
#               break
#        print(values[::-1])
# 
# 
# 
# 
# 
# 
# 
# x = int(input())
# 
# if 20<=x<=90:
#     while (x % 11) != 0:
#         print(x)
#         x -= 1
#     print(x)
# else:
#     print('Input must be 20-98')
# 
#    
# 
# 

# 
# ''' Read in first equation, ax + by = c '''
# a = 8
# b = 7
# c = 38
# 
# ''' Read in second equation, dx + ey = f '''
# d = 3
# e = -5
# f = -1
# 
# ans_x = 100
# ans_y = 100
# for x in range(-10,11):
#     for y in range(-10,11):
#         if ((a*x)+(b*y) - c) == ((d*x)+(e*y) - f) and ((a*x)+(b*y) - c) == 0:
#             ans_x = x
#             ans_y = y
# if ans_x != 100:
#     print(ans_x,ans_y)
# else:
#     print('No solution')
#         
# 
# ans_x = 100
# ans_y = 100
# for x in range(-10, 11):
#     for y in range(-10,11):
#         if ((a*x)+(b*y) - c) == ((d*x)+(e*y) - f) and ((a*x)+(b*y) - c) == 0:
#             ans_x = x
#             ans_y = y
# if ans_x != 100:
#     print(ans_x, ans_y)
# else:
#     print('No solution')
#     
# 
# 
# 
# 
# 

# 
# 
# user_inputs = []
# x = 1
# 
# while x > 0:
#     y = int(input())
#     if y > 0:
#         user_inputs.append(y)
#         x = user_inputs[len(user_inputs)-1]
#     else:
#         print(min(user_inputs),max(user_inputs))
# 
# 
# 
# 
# 




# 
# def swap(list):
#     first_to_last = list[0]
#     last_to_first = list[-1]
#     list.remove(first_to_last)
#     list.remove(last_to_first)
#     newlist.append(last_to_first)
#     for x in list:
#         newlist.append(x)
#     newlist.append(first_to_last)
#     return newlist

# 
# x = ['four', 'two', 'three', 'one']
# 
# def swap(list):
#     list.insert(-1,list.pop(0))
#     list.insert(0,list.pop())
#     return list
# 
# 
# 
# 
# 
# swap(x)
# 
# 
# # newlist = []
# # values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# # swap(values_list)
# # 
# # print(values_list)
# # 
# # 
# # 
# # 
# # 
# # 
# 
# 



# 
# # FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# # add to the bill total, then divide by the number of diners.
# def split_check(bill, people, tax_percentage=0.15, tip_percentage=0.09):
#     total = bill + (bill*tax_percentage) + (bill*tip_percentage)
#     value = total / people
#     return value
# 
# bill = float(input())
# people = int(input())
# 
# # Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))
# 
# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())
# 
# # Cost per diner at different tax and tip percentages
# print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))
# 
# 
# 
# 
# # 
# 
# 
# 
# while True:
#     name = input('Enter input string:\n')
#     if name == 'q':
#         break
#     if ',' not in name:
#         print('Error: No comma in string.\n')
#     else:
#         sepInput = name.replace(' ', '')
#         sepInput = sepInput.split(',')
#         first_word = sepInput[0]
#         second_word = sepInput[1]
#         print('First word: {}'.format(first_word))
#         print('Second word: {}'.format(second_word))
#         
# # 
# # while True:
# #     name = input("Enter input string: \n")
# #     if name == "q":
# #         break
# #     if name.find(',') == -1:
# #         print("Error: No comma in string.")
# #     else:
# #         words = name.split(",")
# #         first = words[0].strip()
# #         last = words[1].strip()
# #         print("First word: " + first)
# #         print("Second word: " + last)
# #     print()    
# # 
# # 
# # 
# # 






# 
# user_string = input()
# 
# list = ['0','1','2','3','4','5','6','7','8','9']
# count = 0
# yes_count = 0
# no_count = 0
# 
# for char in user_string:
#     if char in list:
#         yes_count += 1
#         count += 1
#     else:
#         no_count += 1
#         count += 1
#         
# if yes_count == count:
#     print('yes')
# else:
#     print('no')
# 
# 
# 
# 
# 




# 
# name = input()
# 
# name_list = name.split(' ')
# last = []
# initials = []
# 
# if len(name_list) == 3:
#     last.append(name_list[-1])
#     name_list.remove(name_list[-1])
#     for word in name_list:
#         initials.append(word[0])
#     print('{}, {}.{}.'.format(last[0],initials[0],initials[1]))
# elif len(name_list) == 2:
#     last.append(name_list[-1])
#     name_list.remove(name_list[-1])
#     initials.append(name_list[0][0])
#     print('{}, {}.'.format(last[0],initials[0]))
# 



# y = 'n hey there howie'
# user_input= input().split()
# letter = []
# 
# letter.append(user_input[0])
# user_input.remove(user_input[0])
# 
# x = 1
# count = 0
# 
# for i in range(len(user_input)):
#     for char in user_input[i]:
#         if char == letter[0]:
#             count += 1
#     else:
#         pass
# print(count)
    








# x = 'hello there kane'
# y = x.split()
# 
# for i in range(len(y)):
#     for char in y[i]:
#         print(char)
# 





# 
# 
# num_guesses = int(input())
# user_guesses = []
# 
# for i in range(0,num_guesses):
#     x = input()
#     user_guesses.append(x)
#     
# print('user_guesses:', user_guesses)
# 

# 
# 
# 
# 
# user_input = input()
# hourly_temperature = user_input.split()
# x = len(hourly_temperature)
# 
# for i in range(x-1):
#     print(hourly_temperature[i], end='->')
#     
# print(hourly_temperature[x-1])
# 
# 

# 
# 
# user_input= '1 2 3, 2 4 6, 3 6 9'
# lines = user_input.split(',')
# 
# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
# 
# mult_table = [[int(num) for num in line.split()] for line in lines]
# 
# for i in mult_table:
#     for x in i:
#         print(i)
#         print(x)
# 
# 
# 
# 






# nums = [10, 20, 30, 40, 50]
# 
# for pos, value in enumerate(nums):
#     tmp = value / 2
#     if (tmp % 2) == 0:
#         nums[pos] = tmp
# 
# 
# 
# 
# 
# 
# 

# 
# 
# class Duration:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
# 
#     def __add__(self, other):
#         if not isinstance(other, Duration):
#             return None # Outputs 'None'
#         total_hours = self.hours + other.hours
#         total_minutes = self.minutes + other.minutes
#         if total_minutes >= 60:
#             total_hours += 1
#             total_minutes -= 60
#         return Duration(total_hours, total_minutes)
# 
#     def __int__(self):
#         return self.hours * 60 + self.minutes
# 
# flight_time = Duration(3, 53)
# drive_time = Duration(2, 56)
# 
# print(int(flight_time) + int(drive_time))
# print(int(flight_time + drive_time))
# 
# 
# 
# 
# 
# 
# 

# 
# user_input = input()
# while user_input != 'end':
#     try:
#         # Possible ValueError
#         divisor = int(user_input)
#         if divisor < 0:
#             # Possible NameError
#             print(compute(divisor), end=' ')
#         else:
#             # Possible ZeroDivisionError
#             print(20 // divisor, end=' ')     # // truncates to an integer
#     except ValueError:
#         print('v', end=' ')
#     except ZeroDivisionError:
#         print('z', end=' ')
#     except:
#         print('x', end=' ')
#     user_input = input()
# print('OK')
#






# def find(low, high):
#     mid = (high + low) // 2  # Midpoint of low..high
#     answer  = input('Is it {}? (l/h/y): '.format(mid))
# 
#     if (answer != 'l') and (answer != 'h'):  # Base case
#         print('Got it!')
#     else:
#         if answer == 'l':
#             find(low, mid)
#         else:
#             find(mid+1, high)
# 
# print('Choose a number from 0 to 100.')
# print('Answer with:')
# print('   l (your num is lower)')
# print('   h (your num is higher)')
# print(' any other key (guess is right).')
# 
# find(0, 100)
# 
# 







# # Returns number of pennies if pennies are doubled num_days times
# def double_pennies(num_pennies, num_days):
#     total_pennies = 0
# 
#     if num_days == 0:
#         total_pennies = 0
# 
#     else:
#         total_pennies = double_pennies((num_pennies * 2), (num_days - 1))
# 
#     return total_pennies
# 
# # Program computes pennies if you have 1 penny today,
# # 2 pennies after one day, 4 after two days, and so on
# starting_pennies = int(input())
# user_days = int(input())
# 
# print('Number of pennies after', user_days, 'days: ', end="")
# print(double_pennies(starting_pennies, user_days))
# 
# 

# def factorial_str(fact_counter, fact_value):
#     output_string = ''
# 
#     if fact_counter == 0:      # Base case: 0! = 1
#         output_string += '1'
#     elif fact_counter == 1:    # Base case: print 1 and result
#         output_string += str(fact_counter) +  ' = ' + str(fact_value)
#     else:                       # Recursive case
#         output_string += str(fact_counter) + ' * '
#         next_counter = fact_counter - 1
#         next_value = next_counter * fact_value
#         output_string += factorial_str(next_counter, next_value)
# 
#     return output_string
# 
# user_val = 
# print('{}! = '.format(user_val), end="")
# print(factorial_str(user_val, user_val))
# 
# 
# 



# def raise_to_power(base_val, exponent_val):
#    if exponent_val == 0:
#       result_val = 1
#    else:
#       result_val = base_val * raise_to_power(base_val, exponent_val-1)
# 
#    return result_val
# 
# user_base = 4
# user_exponent = 3
# 
# print('{}^{} = {}'.format(user_base, user_exponent,
#       raise_to_power(user_base, user_exponent)))






