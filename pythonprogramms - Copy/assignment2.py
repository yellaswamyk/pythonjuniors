Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Check the data type of all your variables using type() built-in function
10
10
type(10)
<class 'int'>
print(type(8.23))
<class 'float'>
print(type(52+3sj))
SyntaxError: invalid decimal literal
print(type(421+4j))
<class 'complex'>
print(type("anish"))
<class 'str'>
print(type([30,42,2,4]))
<class 'list'>
print(type({'name':'anish'}))
<class 'dict'>
print(type({34.32,42.4,32.5}))
<class 'set'>
print(type((4.32,48.4)))
<class 'tuple'>
#Using the len() built-in function, find the length of your first name
print(len("my name is anish"))
16
print(len("my father name is vamshi"))
24
print(len("my mother name is kavya"))
23
print(len("my sister name is achyuthapriya"))
31
#Compare the length of your first name and your last name
print(len("first name:'anish'"))
18
print(len("last name:'ch'"))
14
#Declare 5 as num_one and 4 as num_two
#i. Add num_one and num_two and assign the value to a variable total
1+1
2
2-1
1
2*1
2
1**2
1
3%2
1
1//2
0
#The radius of a circle is 30 meters.
#i. Calculate the area of a circle and assign the value to a variable name of area_of_circle

 

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

= RESTART: C:/Users/Hello/AppData/Local/Programs/Python/Python311/assignment2.py
my name is anish

= RESTART: C:/Users/Hello/AppData/Local/Programs/Python/Python311/assignment2.py
my name is anish
first name 'anish'


#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keyword

help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable name
print("
      
SyntaxError: incomplete input
print("First Name:",first name)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("First Name:",first_name)
...       
Traceback (most recent call last):
   File "<pyshell#49>", line 1, in <module>
    print("First Name:",first_name)
NameError: name 'first_name' is not defined
>>> 
= RESTART: C:/Users/Hello/AppData/Local/Programs/Python/Python311/assignment2.py
Traceback (most recent call last):
  File "C:/Users/Hello/AppData/Local/Programs/Python/Python311/assignment2.py", line 1, in <module>
    print("First Name:",first_name)
      
NameError: name 'first_name' is not defined
