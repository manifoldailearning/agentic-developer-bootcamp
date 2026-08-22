tags = ["authentication", "password-reset", "urgent", "important", 100.25, True]

ticket = {
    "customer": "Asha Menon",
    "issue": "Unable to sign in",
    "priority": "high",
    "tags": tags,
}
print(f"Tags: {tags}")
print(f"Data type of tags: {type(tags)}")
print(f"Ticket: {ticket}")
print(f"Data type of ticket: {type(ticket)}")
print("--------------------------------")
print(tags[0]) #  indexing starts from 0
print(ticket["priority"]) #  accessing dictionary values using keys


# in Dict, keys should be unique and immutable, values can be mutable
ticket = {
    "customer": "Asha Menon",
    "issue": "Unable to sign in",
    "priority": "high",
    "tags": tags,
    "customer": "Rajat Menon",
}
print(f"Ticket: {ticket}")
print(f"Data type of ticket: {type(ticket)}")

# access all the keys in the dictionary
print(f"Keys in the dictionary: {ticket.keys()}")
#access all the values in the dictionary
print(f"Values in the dictionary: {ticket.values()}")
#access all the items in the dictionary
print(f"Items in the dictionary: {ticket.items()}")


# Lists
# append - adding a new element to the end of the list
tags.append("new element")
print(f"Tags: {tags}")

# Tuple
# Tuple is immutable collection of elements
tags_tuple = ("authentication", "password-reset", "urgent", "important", 100.25, True)
print(f"Tags tuple: {tags_tuple}")
print(f"Data type of tags tuple: {type(tags_tuple)}")
# access all the elements in the tuple
print(f"Elements in the tuple: {tags_tuple[0]}")
# cant append the values
# tags_tuple.append("new element tuple")


"""
Assignment 2:
Create a python list with elements like this:
apple, banana, cherry, date

- Add a new element to the list - mango

Create a python dictionary with elements like this:
apple: 100, banana: 200, cherry: 300, date: 400

Access the value of apple from the dictionary
"""


# for tag in ticket["tags"]:
#     print(f"- {tag}")
