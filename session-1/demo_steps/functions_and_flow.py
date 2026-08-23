ALLOWED_PRIORITIES = {"low", "medium", "high"} # data type of the variable is set

# Set is unordered collection of unique elements
set1 ={"low", "medium", "high", 100, 25.24, "medium", "high"}
print(f"Set 1: {set1}")

def greeting(name: str) -> str: # Type hinting - not enforced by Python, but used by IDEs and linters
    return f"Hello {name}! Welcome to the world of Python"

def append(list_1: list, item: str) -> list:
    list_1.append(item) # in place modification of the list
    return list_1

l1 = [1,2,3,4,5]
for i in l1:
    print(f"{i}")
    if i == 3: # <, > , != , ==, <=, >=
        print("i is 3")
    else: # else is optional
        print("i is not 3")

print("--------------------------------")
l1 = [1,2,3,4,5]
for i in l1:
    print(f"{i}")
    if i == 3: # <, > , != , ==, <=, >=
        break # break the loop
    print("i is not 3")

print("--------------------------------")
l1 = [1,2,3,4,5]
for i in l1:
    print(f"{i}")
    if i == 3: # <, > , != , ==, <=, >=
        continue # continue the loop but not continue the current iteration
    print("i is not 3")

def normalise_priority(value: str) -> str:
    priority = value.strip().lower()
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError(f"Unsupported priority: {value}")
    return priority


def parse_line(line: str) -> tuple[str, str]:
    key, value = line.split(":", maxsplit=1)
    return key.strip().lower(), value.strip()

print(greeting("Asha"))  # built-in function
print(greeting(12345))
# key, value = parse_line("Priority: HIGH")
# print(key)
# print(normalise_priority(value))

l1 = [1,2,3,4,5]
print(f"List 1 before append: {l1}")
l2 = append(l1, 6)
print(f"List 2 after append: {l2}")

# import keyword
# print("Keywords in Python:")
# print(keyword.kwlist)

#result =normalise_priority("HIGH")
# result =normalise_priority("hello")
# print(f"Result: {result}")

key, value = parse_line("Customer: Asha Menon")
print(f"Key: {key}")
print(f"Value: {value}")