import random  # import random for random number or digits or choices 
import string  # import string for using string special function to generate the password


password = 8
char_values = string.ascii_letters + string.digits + string.punctuation # this is variablee to store A-Z,a-z,0-9 and Punctuation to create random password

passw = ""  # this empty string to store our password
for i in range(password): # this is loop to travel 8 times to generate different char
    passw += random.choice(char_values) # random_choice add the char in passw variable 

print("Here is Your Password: ",passw) # print the password


# using list comprehension 

result = "".join([random.choice(char_values) for i in range(password)])
print("Your Generated Password Is Here:",result)