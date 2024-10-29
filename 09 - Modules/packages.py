# Módulo é um arquivo Python contendo diversas funções para serem utilizadas.
# Pacote é um diretório contendo vários módulos.

# Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado "__init__.py" .
# Nas versões mais recentes do Python esse arquivo não é obrigatório, mas, ainda é utilizado para manter compatibilidade com outras versões.

# Para demonstração, criei o pacote "package_1" na raiz e o sub-diretório "sub_package_1", dentro do pacote "package_1".

from package_1 import module_1, module_2

print("----------------------------------------------------------------------------------------------------")

print(module_1.pi)
print(module_1.func_1(4,6))
print(module_2.func_2())

print("----------------------------------------------------------------------------------------------------")

from package_1.sub_package_1 import module_3, module_4

print(module_3.func_3())
print(module_4.func_4())

print("----------------------------------------------------------------------------------------------------")

# Obs.: Outra maneira de importar uma função seria por exemplo:  from package_1.sub_package_1.module_3 import funcao_3
