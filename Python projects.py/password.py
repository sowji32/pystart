import random
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
list2=['1','2','3','4','5','6','7','8','9','0']
list3=['!','@','#','$','%','^','&','*','(',')','<','>']
password=[]
a=int(input("enetr no of characters:"))
b=int(input("enter no of special characters:"))
c=int(input("enetr no of digits:"))
for i in range(1,a+1):
    d= random.choice(list1)
    password.append(d)
for i in range(1,b+1):
    d= random.choice(list3)
    password.append(d)
for i in range(1,c+1):
    d= random.choice(list2)
    password.append(d)
random.shuffle(password)
passwords=" "
for j in password:
    passwords+=j
print(passwords)
