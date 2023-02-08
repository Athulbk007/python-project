import random
#print(random.randint(0,16777215))
rand=random.randint(0,16777215)
hex_num = str(hex(rand))
hex_num = "#"+hex_num[2:]
print(hex_num)
#print(random.choice("qwertyuwert"))
