tple = (1,2,3,4,5,6,"abc",1.3)
# print(tple)
# print(type(tple))
# print(len(tple))
print(tple[0])
print(tple[0:4])
print(tple[-2])
print(tple[::-2])
print(tple[:-3])
print(tple[-4:-1])

#update
# tple = (1,"athul","rahul","abc",1.3)
# y =list(tple)
# y [0]="dona"
# tple = tuple(y)
# print(tple)

#append
#tple=(1,"athul","rahul","abc",1.3)
# y =list(tple)
# y.append("qwert")
# tple=tuple(y)
# print(y)
#add a tuple
# b = ("sree","amritha")
# tple +=b
# print(tple)

#remove
# x = list(tple)
# x.remove("abc")
# tple =tuple(x)
# print(tple)


#del
# new_tple=("athul",12,3,4)
# del new_tple
# print(new_tple)


#while loop

# new_tuple =("apple","banana","cherry")
# i=0
# while i< len(new_tuple):
#     print(new_tuple[i])
#     i+=1

#nested tuple

# new_tuple=("apple",[1,2,3,4,5],(9,8,6))
# print(new_tuple[2][0])
# print(new_tuple[0][1])
# new_tuple[1][2]=7#only in list
# print(new_tuple)

# a=(0,2,3,4,1,6)
# print(all(a))
# print(max(a))
# print(min(a))
# print(sorted(a))



#enumerate
# x= ('athul','qwer','asdfg')
# #z =[20,45,60]
# y =enumerate(x)
# print(tuple(y))

# name= ('athul','qwer','asdfg')
# age =(20,45,60)
# for i, (name,age) in enumerate(zip(name,age)):
#     print(i,name,age)


# letter=(['a','A'],['b','B'])
# for i, letter in enumerate(letter):
#     print(("Letter %d is %s%s") % (letter[0],letter[1]))



# l ={"athul","rahul","qwert"}
# test = tuple(map(tuple,l))
# print(test)

l =("athul","rahul","qwert")
test = tuple(map(set,l))
print(test)


