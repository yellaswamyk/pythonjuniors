#List:
#List is collection which ordered and changeable.Allows duplicates members.
#1 How to create a List.
#we can create list in 2 Ways.
#1.Using built in function

mylist1=list()
print(mylist1)
#2.Using sqaure brackets []
mylist2=[]
print(mylist2)

#create list of fruits
fruitlist=['banana','apple','jack fruit','mango','water melon','grapes','oranges','guava','dragon fruit']

print('Number of Fruits:',len(fruitlist))
print("*********Positive Indexing***********")
#Accessing list items using Postive indexing
print(fruitlist[0])
print(fruitlist[3])
print(fruitlist[5])

#Accessing list items using Negative indexing
print("************Nagative Indexing*******************")
print(fruitlist[-1])
print(fruitlist[-3])
print(fruitlist[-5])
print('========Unpacking List Items==========')
first_fruit,second_fruit,*rest=fruitlist
print(first_fruit)
print(second_fruit)
print(rest)
print('*** Slicing items from List**********')
all_fruits=fruitlist[0:4]
print(all_fruits)

print(fruitlist[1:3])
print(fruitlist[1:])
print(fruitlist[:2])


print(fruitlist[:-1])