# to run this file use in terminal 'JonathanPauda@MacBook-Pro projects % python3 python_practice.py'


# # How to assign a variable in python 
# x = 5 
# y = "Hello"
# z = 3.14

# # How to check type
# print(type(x))  # Output: <class 'int'>
# print(type(y))  # Output: <class 'str'>
# print(type(z))  # Output: <class 'float'>

# # Print the types of the variables
# print("Type of x:", type(x))  # Output: <class 'int'>
# print("Type of y:", type(y))  # Output: <class 'str'>
# print("Type of z:", type(z))  # Output: <class 'float'>

# # basic operations
# # + (addition), - (subtraction), * (multiplication), / (division), ** (exponentiation), % (modulo), and // (floor division).
# a = 10
# b = 3
# print (a + b)
# print (a ** b) # a raised to the power of b so 10 raised to 3 or 10 x 10 x 10 = 1000
# print (a % b) # a modulo b means a divided by b and remainder equals the value, 10/3 = 9 with remainder of 1 

# # How do you create a list, access elements, and modify it in Python?
# # Lists are ordered collections in Python. You can create a list using square brackets [], access elements by index, and modify elements directly.

# # creating a list 
# my_list = [10, 20, 30, 40, 50]

# # Accessing elements
# first_element = my_list[0] # get value of first element at index 0
# print(first_element)
# third_element = my_list[2] # index 2
# print(third_element) 

# # modifying an element
# my_list[1] = 25
# print(my_list)

# # adding an element to the list
# my_list.append(60) # adds 60 to the end of the list
# print(my_list)

# # removing an element 
# my_list.remove(30) # removes the value 30 form the list
# print(my_list)

# # for Loop:
# # The for loop is used to iterate over sequences (like lists or strings).
# my_list_1 = [1, 2, 3, 4]

# for num in my_list_1:
#     print(num)

# # while Loop:
# # The while loop continues to execute as long as a condition is True.

# counter = 0

# while counter < 5:
#     print ("Counter is:", counter)
#     counter += 1 # increments the counter to avoid and infinite loop

# # further while loop that uses length of list as counter
# my_list_1 = [1, 2, 3, 4]
# index = 0 # start with first index (0)
# while index < len(my_list_1):
#     print(my_list_1[index]) # print the current element
#     index += 1 # increment the index to move to the next element


# Q6: How do you define and call a function in Python, and how can you pass arguments to it?

# Defining a Function:

# You define a function in Python using the def keyword, followed by the function name and parentheses ().

from typing import List


def say_hello():
    print("Hello!")

#call the function
say_hello() # will output Hello!

# Passing Arguments to a Function:

# You can pass values (arguments) to a function, and the function can use those arguments to perform operations.

#Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# call the function with an argument
greet("Jonathan")

# pass multiple arguments
def add_numbers(a, b):
    return a + b
#call the function with two arguments
result = add_numbers(5, 3)
print(result)


# if, elif, and else Statements:

# Conditional statements allow you to execute different blocks of code based on certain conditions.

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")


# Creating a Dictionary:

# A dictionary in Python is a collection of key-value pairs. You can create a dictionary using curly braces {} where each key is associated with a value.

# creating a dictionary
person = {
    "name": "Jonathan",
    "age": 30,
    "city": "New York"
}

# Accessing Dictionary Values:

# You can access values in the dictionary by using the corresponding key inside square brackets [].

# Modifying Dictionary:

# You can change the value for a specific key, or add new key-value pairs to the dictionary.

#accessing a value by key
print(person["name"])

# modifying a value 
person["age"] = 31 # changes age to 31

#adding a new key-value pair
person["profession"] = "Engineer"

#iterating over a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# removes the last inserted key-value pair
person.popitem()
#print the person dictionary on a single line
print(person)


# 9. List Comprehensions in Python

# A list comprehension is a concise way to create a new list by applying an expression to each item in an existing iterable (like a list or range), 
# optionally filtering them using a condition.

# Basic Syntax:
# new_list = [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

# using a list comprehension to square each number
squares = [num ** 2 for num in numbers]
print(squares)


# You can also add an if condition to filter items.
numbers = [1, 2, 3, 4, 5]
# Using list comprehension to get only even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# explanation:
# num: This is the variable that takes on each value from the numbers list one at a time.
# for num in numbers: This part iterates over each element in the numbers list.
# if num % 2 == 0: This condition filters the numbers. It checks if the number num is even (i.e., if the remainder of num divided by 2 is 0).
# num (in the list comprehension): The expression here is just num, which means that only numbers that satisfy the condition (even numbers) are included in the new list.


# Exception handling in Python is used to manage errors that occur during the execution of your program. The try block contains code that might cause an exception, and the except block contains code to handle the exception if it occurs.

# Basic Syntax:
# python
# Copy code
# try:
#     # Code that might cause an exception
#     risky_code()
# except SomeException as e:
#     # Code to run if an exception occurs
#     handle_exception(e)
# else:
#     # Code to run if no exception occurs
#     no_exception_code()
# finally:
#     # Code that always runs, regardless of whether an exception occurs
#     always_run_code()

try:
    # Try to divide numbers
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the division by zero error
    print("You can't divide by zero!")
    print(f"Error details: {e}")
else:
    # Code that runs if no exception occurs
    print(f"The result is {result}")
finally:
    # Code that always runs
    print("This will always execute.")



# Functions in Python are defined using the def keyword and are used to encapsulate code into reusable blocks. Functions can take parameters (inputs) and return values (outputs).

# Basic Syntax:
# def function_name(parameters):
#     # Code block
#     return value
# Components:
# Function Definition:
# def keyword is used to define a function.
# function_name is the name of the function.
# parameters are optional inputs that the function can take.
# The return statement is optional and specifies the output of the function.

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Jonathan")
print(message)  # Output: Hello, Jonathan!

# Functions with Multiple Parameters and Default Values:

def add_numbers(a, b=5):
    return a + b

# Calling the function with both arguments
sum1 = add_numbers(3, 4)  # Output: 7
print(sum1)

# Calling the function with only one argument
sum2 = add_numbers(3)    # Output: 8 (b defaults to 5)
print(sum2)
# Function with Default Value:
# b=5 provides a default value for b. If no value is provided for b when calling the function, it defaults to 5.

# Membership Tests
# Check if an item is in the list.

fruits = ['apple', 'banana', 'orange']
has_banana = 'banana' in fruits  # True


# Common Dictionary Operations:
# Accessing Values
# Access values using keys.

person = {'name': 'Alice', 'age': 30}
name = person['name']  # 'Alice'

# Adding/Updating Items
# Add new key-value pairs or update existing ones.

person = {'name': 'Alice'}
person['age'] = 30
# person is now {'name': 'Alice', 'age': 30}

# Deleting Items
# Use del to remove a specific key-value pair.

person = {'name': 'Alice', 'age': 30}
del person['age']
# person is now {'name': 'Alice'}

# Membership Tests
# Check if a key exists in the dictionary.

person = {'name': 'Alice', 'age': 30}
has_name = 'name' in person  # True
print(has_name)

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

nums=[1, 2, 3, 3]

class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            print(hashset)
        return False
        
# left off on problem number 1 on neetcode.io arrays & hashing problem list - problem called Contains duplicate 
# https://neetcode.io/roadmap

# solved problem #1

# worked on annogram #2 solved it by looking at the solution, study up the solution in detail tomorrow in AM

# helpful explanation on chatgpt:
# https://chatgpt.com/c/66df067c-8b30-8007-ba42-23d794b727c1

# Full Example for s = "anagram":
# Let's assume countS starts as an empty dictionary ({}):

# When i = 0, s[0] = 'a'. countS.get(s[0], 0) will return 0 (since 'a' is not in countS yet).
# countS['a'] = 1 + 0 results in countS = {'a': 1}.
# When i = 1, s[1] = 'n'. countS.get(s[1], 0) will return 0 (since 'n' is not in countS yet).
# countS['n'] = 1 + 0 results in countS = {'a': 1, 'n': 1}.
# When i = 2, s[2] = 'a'. countS.get(s[2], 0) will return 1 (since 'a' is already in countS with a count of 1).
# countS['a'] = 1 + 1 results in countS = {'a': 2, 'n': 1}.


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # length need to be the same or false
            return False

        countS, countT = {}, {}

        for i in range(len(s)): # iterate through the string s (could use t also as they are the same) do this by getting lenth of s, and range through - exmaple lenght is 7 range would be 0-6
            countS[s[i]] = 1 + countS.get(s[i], 0) # in countS dictionary add count of each character from s (string) at key i (position i) increment the count if it exists, else set count to 0 by default
            countT[t[i]] = 1 + countT.get(t[i], 0) # do the same for t string
        return countS == countT # if the dicts are equal then return true 
    


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_1 = {} # empty dictionary storing val : index 
        for i, elem in enumerate(nums): # iterate through nums list giving the index i and element elem, so on each loop i is the index of the current element and elem is the value at that index
            diff = target - elem # diff is the value we are looking for
            if diff in nums_1: # checks if diff exists in nums_1
                return [nums_1[diff], i] # if it exists then we have found 2 numbers that sum to target, return the numbers indices 
                
            nums_1[elem] = i # assign the key and value, so on first iteration its adding to nums_1 dict {4,0} for the nums list [4,5,6]
            # i = 0
            # elem = 4
            # diff = 10 - 4 = 6
            # 4 = i

            print (i)
            print(nums_1)


class Solution4:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            #check for not alphanum (symbols, or punctuation) and increment or decrement to skip
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): #compare lower case of l to r, if not equal false
                return False
            # increment l and decrement r for each iteration
            l, r = l + 1, r -1
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


class Solution5:
    def check_ip_in_logs(self, lines, ip_address):
        # Split the lines into individual log entries
        log_entries = lines.split(',')

        # Loop through each log entry
        for entry in log_entries:
            # Extract the IP address by splitting the entry
            ip_in_entry = entry.strip().split()[0]

            # Check if the IP address matches the provided IP
            if ip_in_entry == ip_address:
                return True

        # Return False if no match is found
        return False

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
class Solution6(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n +1):
            if (i % 3 == 0) and (i % 5 == 0):
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

if __name__ == "__main__":
    # Test the first solution (check for duplicates)
    nums = [1, 2, 3, 3]
    solution1 = Solution1()
    print("Has duplicates:", solution1.hasDuplicate(nums))

    # Test the second solution (check if two strings are anagrams)
    s = "racecar"
    t = "carrace"
    solution2 = Solution2()
    print("Are anagrams:", solution2.isAnagram(s, t))

    # test 3rd solution (two sum)
    nums = [4,5,6, 8, 19, 10, -2, -3, 15, 17, 18, 2]
    target = 20
    solution3 = Solution3()
    # Get the indices of the two numbers that sum to the target
    indices = solution3.twoSum(nums, target)
    
    # Output the indices and their actual values
    if indices:
        print(f"indices {indices} with values {nums[indices[0]]} and {nums[indices[1]]} sum to {target}")
    else:
        print(f"No two numbers in {nums} sum to {target}.")
    
    # Test solution4 - Palindrome
    s="Was it a car or a cat I saw?"
    solution4 = Solution4()
    print(solution4.isPalindrome(s))

    # Test solution 5 - log lines - Example usage
    lines = """10.0.0.0.1  - frank [timestamp UTC format] - more text,
               10.0.0.0.2  - frank [timestamp UTC format] - more text,
               10.0.0.0.3  - frank [timestamp UTC format] - more text"""
    ip_to_check = "10.0.0.0.5"
    solution5 = Solution5()
    result = solution5.check_ip_in_logs(lines, ip_to_check)
    print(result)  # Output: True or False depending on the IP  

    # Test solution 6 - FizzBuzz
    n=20
    solution6 = Solution6()
    result = solution6.fizzBuzz(n)
    print(result)


