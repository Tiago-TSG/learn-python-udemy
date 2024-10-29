print("----------------------------------------------------------------------------------------------------")

def soma(num1, num2):
    return(num1 + num2)

def subtração(num1, num2):
    return(num1 - num2)

def mat(num1, num2, fun=soma): # OBS.: A função soma é utilizada por padrão nesta função.
    return(fun(num1, num2))

print(soma(3, 7))
print(subtração(10, 3))

print("----------------------------------------------------------------------------------------------------")

print(mat(4, 6))
print(mat(10, 3, subtração))

print("----------------------------------------------------------------------------------------------------")
