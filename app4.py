def divid(a, b):
    if b != 0:
        return a / b
    else:
        return 0

def get_user(id):
    if id == 1:
        return 'admin'
    else:
        return 'user'

def main():
    result = divid(10, 1)
    user = get_user(1)
    print(user)

if __name__ == "__main__":
    main()
