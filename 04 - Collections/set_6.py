estudantes_python = {"Julia", "Daniel", "Evelyn", "Simone", "Alexandre", "Pedro", "Rafael", "Matheus", "Arthur"}
estudantes_java = {"Julia", "Sophia", "Guilherme", "Henrique", "Matheus", "Arthur"}

print("----------------------------------------------------------------------------------------------------")

print(len(estudantes_python))
print(len(estudantes_java))

print("----------------------------------------------------------------------------------------------------")

estudantes_unicos = estudantes_python.union(estudantes_java) # Forma 1 de união de conjuntos
print(estudantes_unicos)

print("----------------------------------------------------------------------------------------------------")

print(f" São {len(estudantes_unicos)} estudantes em todos os cursos.")

print("----------------------------------------------------------------------------------------------------")

print(len(estudantes_python))
print(len(estudantes_java))

print("----------------------------------------------------------------------------------------------------")

estudantes_unicos = estudantes_python | estudantes_java # Forma 2 de união de conjuntos.
print(estudantes_unicos)

print("----------------------------------------------------------------------------------------------------")

print(f" São {len(estudantes_unicos)} estudantes em todos os cursos.")

print("----------------------------------------------------------------------------------------------------")

estudantes_ambos = estudantes_python.intersection(estudantes_java) # Forma 1 de intercessão de conjuntos.
print(estudantes_ambos)

print("----------------------------------------------------------------------------------------------------")

print(f" São {len(estudantes_ambos)} estudantes cursando os dois cursos.") # Forma 2 de intercessão de conjuntos.

print("----------------------------------------------------------------------------------------------------")

estudantes_ambos = estudantes_python & estudantes_java
print(estudantes_ambos)

print("----------------------------------------------------------------------------------------------------")

print(f" São {len(estudantes_ambos)} estudantes cursando os dois cursos.")

print("----------------------------------------------------------------------------------------------------")

estudantes_somente_python  =  estudantes_python.difference(estudantes_java)
print(estudantes_somente_python)

print("----------------------------------------------------------------------------------------------------")

print(len(estudantes_somente_python))

print("----------------------------------------------------------------------------------------------------")

estudantes_somente_java  = estudantes_java.difference(estudantes_python)
print(estudantes_somente_java)

print("----------------------------------------------------------------------------------------------------")

print(len(estudantes_somente_java))

print("----------------------------------------------------------------------------------------------------")
