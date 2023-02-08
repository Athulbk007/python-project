'''List comprehension'''
# find all the word in string that are less than 4 letter

sentence=input("enter a sentence:")
words=sentence.split( )
print(words)
result=[x for x in words if len(x)<4]
print(result)