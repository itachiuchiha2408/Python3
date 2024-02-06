import random
file=open("generate_random_psw.txt",'w')
str="zxcvbnmlkjhgfdsaqwertyuiopMNBVCXZASDFGHJKLPOIUYTREWQ1234567890!@#$%^&*"
password_length=int(input("Enter number for password length: "))
password=""
file.write("Enter number for password length: ")

file.write('\n')
for i in range(1,password_length+1):
    password+=random.choice(str)
file.write("Generated Password:")
file.write(password)
print(password)