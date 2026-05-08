def discy(price, discount):
    return price / discount  # bug: no zero check

def find_user(users, id):
    for user in users:
        if user["id"] = id:  # bug: assignment instead of comparison
            return user

def parse_config(config):
    return config["settings"]["timeout"]  # bug: no key existence check

result = discy(100, 0)  # will crash
print(result)
