s = {1, 7, 2, 3, 8, 8, 9, 10, 8, 2}

print("----------------------------------------------------------------------------------------------------")

print(type(s))
print(s)

print("----------------------------------------------------------------------------------------------------")

t = (1, 5, 7, 9, 2, 3, 3)

print(type(t))
print(t)

print("----------------------------------------------------------------------------------------------------")

t = set(t)
print(type(t))
print(t)

print("----------------------------------------------------------------------------------------------------")

n = 0

if n in s:
    print(f"O número '{n}' existe no conjunto {s}")
else:
    print(f"O número '{n}' não existe no conjunto {s}")

print("----------------------------------------------------------------------------------------------------")