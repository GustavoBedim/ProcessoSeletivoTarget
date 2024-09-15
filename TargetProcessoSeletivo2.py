def contador_a(string):
    contador = string.lower().count('a')
    return contador

# Definindo a string
string = input("Digite uma string (frase): ")

contador = contador_a(string)

if contador > 0:
    print("A letra 'a' aparece {} vezes na string.".format(contador))
else:
    print("A letra 'a' não aparece na string.")
