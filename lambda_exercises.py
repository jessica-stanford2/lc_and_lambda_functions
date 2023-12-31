''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

int_list = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda num: (num %2 == 0 ), int_list))
odd_numbers = list(filter(lambda num: (num % 2 ==1), int_list))

print(even_numbers)
print(odd_numbers)






''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

filtered_days = list(filter(lambda day: (len(day) == 6), weekdays))
print(filtered_days)









''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
bad_colors = ['orange', 'black']

filtered_colors = list(filter(lambda color: color not in bad_colors, colors_list))
print(filtered_colors)









''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1=  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=  [2, 4, 6, 8]

filtered_num = list(filter(lambda num: num not in list2, list1))
print(filtered_num)




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
orig_list = ['red', 'black', 'white', 'green', 'orange']

ack_list = list(filter(lambda color: "ack" in color, orig_list))
print(ack_list)

abc_list = list(filter(lambda color: "abc" in color, orig_list))
print(abc_list)





''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
password_verification = lambda password: any(char.islower() for char in password) and any(char.isupper()for char in password) and (len(password) >= 8)


str1 = "Hello8world"
print(password_verification(str1))

str1 = "HELLO"
print(password_verification(str1))

str1= "hello"
print(password_verification(str1))






''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
''' 

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

original_scores.sort(reverse = False, key = lambda num: num[1])

print(original_scores)