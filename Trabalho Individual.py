




# Criar uma lista para armazenar os resultados
resultados = []

# Adicionar alguns resultados à lista
resultados.append ("e5_t10_p8_s8")
resultados.append ("e10_t7_p7_s8")
resultados.append ("e8_t5_p4_s9")
resultados.append ("e2_t2_p2_s1")
resultados.append ("e10_t10_p8_s9")

# Criar uma função que busca o candidato de acordo com o critério
def buscar_candidato (criterio):
    # Criar uma lista vazia para armazenar os candidatos encontrados
    candidatos = []
    # Percorrer a lista de resultados
    for resultado in resultados:
        # Verificar se o critério está contido no resultado
        if criterio in resultado:
            # Adicionar o resultado à lista de candidatos
            candidatos.append (resultado)
    # Retornar a lista de candidatos
    return candidatos

# Testar a função com alguns critérios ( 4, 4, 8, 8 )
print(buscar_candidato ("e4"))
print(buscar_candidato ("t4"))
print(buscar_candidato ("p8"))
print(buscar_candidato ("s8"))

print(resultados)





