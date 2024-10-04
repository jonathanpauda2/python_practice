# Create an empty dictionary
my_dict = {}

# Add some key-value pairs to the dictionary
my_dict["apple"] = 3
my_dict["banana"] = 2
my_dict["orange"] = 5

# # Retrieve a value from the dictionary using its key
# print(my_dict["apple"])  # Output: 3

# Update a value in the dictionary
my_dict["apple"] = 4

# # Check that the value has been updated
# print(my_dict["apple"])  # Output: 4

# # Retrieve a value from the dictionary using the get() method
# print(my_dict.get("banana"))  # Output: 2

# # Retrieve a value from the dictionary using the get() method with a default value
# print(my_dict.get("grape", 0))  # Output: 0 (because "grape" is not in the dictionary)

# # Check if a key is in the dictionary
# if "orange" in my_dict:
#     print("There are", my_dict["orange"], "oranges in the dictionary.")

# Print all key-value pairs in the dictionary
for key, value in my_dict.items():
    print(key, ":", value)