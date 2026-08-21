customer = "Asha Menon"
attempts = 3
is_urgent = True

print(customer, type(customer))
print(attempts, type(attempts))
print(is_urgent, type(is_urgent))

summary = f"{customer} has tried {attempts} times. Urgent: {is_urgent}"
print(summary)
