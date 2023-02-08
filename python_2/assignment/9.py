#write a program to extract numbers fro  by using list comprehension
strings='the room number 45 and 67 are vaccant'
new=[x for x in strings if x.isdigit()]
print(new)