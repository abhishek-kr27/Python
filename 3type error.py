char= len(input("What is your name?"))
print(type(char)) #print the data type
new_char=str(char) #change integer into string
# print("Your name has " + char + " " + "characters.") 
# show error because string data type can't print the integer
new_char=str(char) #change integer into string
print("Your name has " + new_char + " " + "characters.")

a=12
print(type(a))
b=3.14
print(type(b))
c=True
print(type(c))

print(70+10.2) #80.2
print(70 + float(10.2)) #80.2
print(str(70) +str(80)) # 7080