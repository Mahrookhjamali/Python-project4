import random
import string
def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation 
  password =  ''.join(random.choice(characters) for i in range(length))
  return password
length=int(input("enter the length of the password:"))
print("your password is:",generate_password(length))

#characters = string.ascii_letters + string.digits + string.punctuation
#password = ''.join(random.choice(characters) for i in range(length))