#listas

lista_numeros = [3, 7, 1, 4, 9, 2, 10, 4]

soma = 0 

for numero in lista_numeros:
    #soma += numero
    #print(f"A soma dos elementos da lista é: {soma}")

input("-------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = 0 

for numero in numeros:
    #if numero % 2 == 0:
        #soma_pares += numero

print(f"A soma dos números pares é: {soma_pares}")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = 0 
soma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
    elif numero % 2 != 0: 
      soma_impares += numero 
        

print(f"A soma dos números pares é: {soma_pares} e a soma dos valores impares é: {soma_impares}")

input("------------------")

#dicionário 

notas = {
  "portugues": "10.0",
  "matematica": "9.5",
  "geografia": "8.0", 
  "fisica": "9.6"
}

materia = input("Digite a matéria: ")

if materia in notas: 
  nota = notas[materia]
  print(f"A nota da matéria {materia} é: {nota}.")
  
else:
  print("Matéria não encontrada.")
  