# Customer: name, email, phone #, etc.
# Name: John Smith
# Email: john@gmail.com
# Phone: 1234

# Dictionary -- keys must be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))  # non-existent key is ok

print(customer.get("birthday"))  # none, which is like Java null
print(customer.get("birthday", "Jan 1 1980"))  # default values

customer["name"] = "Jack Smith"
print(customer["name"])

# Exercise
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

phone = input("Phone: ")
result = ""
# for index in range(len(phone)):
#     result += numbers.get(phone[index]) + " "
for ch in phone:
    result += numbers.get(ch, "Not a number!") + " "
result = result[:len(result) - 1]
print(result)
