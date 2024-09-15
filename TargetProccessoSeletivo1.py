#TargetProccessoSeletivo

def eh_fibonacci(numero_usuario):
    a, b = 0, 1
    while b < numero_usuario:
        a, b = b, a + b
    if b == numero_usuario or numero_usuario == 0:
        return True
    return False

#Solicita numero pro usuário
numero_usuario = int(input("Informe um número: "))

if eh_fibonacci(numero_usuario):
    print(f"O número {numero_usuario} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_usuario} não pertence à sequência de Fibonacci.")
