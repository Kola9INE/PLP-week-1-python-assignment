def get_user_details():
    name = input("\nHello! I am 🐍. You may know me as Python. You are? \n")
    age = input("\nHow old are you? \n")
    location = input("\nWhere do you live? \n")
    return (f"\nHello {name}, you are {age} years old. You live in {location}. Nice meeting you!\n")

if __name__ == '__main__':
    print(get_user_details())