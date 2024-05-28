#Declare an empty list
empty_list = []
print(empty_list)

#Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)

#Find the length of your list
length_of_list = len(my_list)
print(length_of_list)

#Get the first item, the middle item and the last item of the list
first_item = my_list[0]  
middle_item = my_list[len(my_list)//2]
last_item = my_list[-1]


#Declare a list variable named it_companies and assign initial values Facebook, 
#Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

#Print the number of companies in the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
num_companies = len(it_companies)
print("Number of companies:", num_companies)

#Print the first, middle and last company
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("First company:", it_companies[0])
middle_index = len(it_companies) // 2
print("Middle company:", it_companies[middle_index])
print("Last company:", it_companies[-1])

#Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[3] = 'Samsung'
print(it_companies)

#Add an IT company to it_companies
 it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
 it_companies append('Samsung')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Cisco')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for i in range(len(it_companies)):

if it_companies[i] != 'IBM':
# Change the company name to uppercase
 it_companies[i] = it_companies[i].upper()
print(it_companies)

#Join the it_companies with a string '#; '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
joined_companies = '#; '.join(it_companies)
print(joined_companies)

#check if a certain company exists in the it_companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
company_to_check = "Microsoft"

# Check if the company exists in the list
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")

#Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print("Sorted list of IT companies:")
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
it_companies.reverse()
print("List of IT companies in descending order:")
print(it_companies)

#Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three_companies = it_companies[:3]
print("First three companies:")
print(first_three_companies)

#Slice out the last 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_three_companies = it_companies[-3:]
print("Last three companies:")
print(last_three_companies)

#Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = [it_companies[middle_index]]
print("Middle IT company or companies:")
print(middle_companies)

# Remove the first IT company
first_company_removed = it_companies.pop(0)
print("Updated list after removing the first IT company:")
print(it_companies)
print("Removed IT company:", first_company_removed)

#Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    it_companies.pop(middle_index)
print("Updated list after removing the middle IT company or companies:")
print(it_companies)

#Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_company_removed = it_companies.pop()
print("Updated list after removing the last IT company:")
print(it_companies)
print("Removed IT company:", last_company_removed)

#Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = [company for company in it_companies if "IT" not in company]
print("Updated list after removing all IT companies:")
print(it_companies)

#Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = [company for company in it_companies if "IT" not in company]
print("Updated list after removing all IT companies:")
print(it_companies)

#Destroy the IT companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"
it_companies.clear()
print("Updated list after clearing:")
print(it_companies)

#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']                
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = [item for pair in zip(front_end, back_end) for item in pair]
print("Full stack technologies:")
print(full_stack)
                
#After joining the lists in question 26. Copy the joined list and assign it to a 
#variable full_stack. Then insert Python and SQL after Redux
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack_copy = full_stack[:]
insert_index = full_stack_copy.index('Redux') + 1
full_stack_copy.insert(insert_index, 'Python')
full_stack_copy.insert(insert_index + 1, 'SQL')
print("Full stack technologies with Python and SQL inserted:")
print(full_stack_copy)
                








