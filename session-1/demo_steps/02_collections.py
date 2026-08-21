tags = ["authentication", "password-reset", "urgent"]

ticket = {
    "customer": "Asha Menon",
    "issue": "Unable to sign in",
    "priority": "high",
    "tags": tags,
}

print(tags[0])
print(ticket["priority"])

for tag in ticket["tags"]:
    print(f"- {tag}")
