#an exercise to validate username
# 1. username should be less than 12 characters
# 2. username should have no spaces
# 3. username should have no digits

username = input("Please create your username:")
results = username.find(" ")

if len(username) > 12 :
    print("Your username should be less than 12 characters.")

elif not results == -1:
     print("Username should not contain any spaces")

elif not username.isalpha():
    print("User name should not contain any digits")
    
else:
     print(f"Welcome {username}")