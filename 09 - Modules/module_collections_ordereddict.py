from collections import OrderedDict

print("----------------------------------------------------------------------------------------------------")

dict_1 = {"a": "1", "b": "2", "c": "3"}
dict_2 = {"b": "2", "c": "3", "a": "1"}

print(dict_1 == dict_2) # Verdadeiro, pois em um dicionário comum, a ordem dos elementos não importa.

# ord_dict_1 = {"a": "1", "b": "2", "c": "3"}
# ord_dict_2 = {"b": "2", "c": "3", "a": "1"}

print("----------------------------------------------------------------------------------------------------")

ord_dict_1 = OrderedDict(dict_1)
ord_dict_2 = OrderedDict(dict_2)

print(ord_dict_1 == ord_dict_2) # Falso, pois utilizando a função OrderedDict do modulo collections, a ordem importa.

print("----------------------------------------------------------------------------------------------------")
