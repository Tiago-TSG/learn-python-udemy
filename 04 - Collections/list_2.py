thislist = ["apple", "orange", "cherry"]

print("----------------------------------------------------------------------")

for i in thislist:
    print(i)
    
print("----------------------------------------------------------------------")

print(f"O tamanho da lista é: {len(thislist)}")

print("----------------------------------------------------------------------")

for x in range(len(thislist)):
	print(x)

print("----------------------------------------------------------------------")


for x in range(len(thislist)):
	print(thislist[x])

print("----------------------------------------------------------------------")

for x in range(-1, -len(thislist) - 1, -1):
	print(thislist[x])
	
print("----------------------------------------------------------------------")

for x in range(2, -1, -1):
	print(thislist[x])

print("----------------------------------------------------------------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])

print(thislist[-2:-5:-1])

print("----------------------------------------------------------------------")

print(thislist[1::])

print(thislist[-3::-1])
	
print("----------------------------------------------------------------------")

thislist.reverse()
print(thislist)

#--------- OU -----------

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[::-1])

print("----------------------------------------------------------------------")
