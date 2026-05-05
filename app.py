def divide(a, b):
    return a / b  # bug: no zero division check

def get_user(users, id):
    for user in users:
        if user["id"] = id:  # bug: assignment instead of comparison
            return user

result = divide(10, 0)
print(result)
