import random #importing
f=["bob","jack","jasper","john","demitreus","freddy","dominic","daniel","jake","tyson"]
m = set(f)
for i in range(10):
    choice=input("Would you like to add or remove a friend?")
    if choice=="add":
        m.add(input("Who would you like to add?"))
    if choice=="remove":
        m.discard(input("Who would you like to remove?"))
print(m)



