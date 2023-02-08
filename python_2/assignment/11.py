#write a prg to print the string that start with the letter 'c' and end with the letter 'b'
names=['acs','ewd','acsh','sabd','cdszvcb']
new_names=[name for name in names if name.endswith('b')& name.startswith('c')]
print(new_names)
