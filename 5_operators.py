num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operadores Aritmeticos 

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2

mod = num1 % num2 # mod -> é o resto de uma divisão. 
exp = num1 ** num2 # exp -> é uma exponenciação, um numero elevado a outro.

#test
print(f"A soma entre {num1} e {num2} é: {sum}")
print(f"A subtração entre {num1} e {num2} é: {sub}")
print(f"A divisão entre {num1} e {num2} é: {div}")
print(f"A multiplicação entre {num1} e {num2} é: {mult}")

print(f"O resto da divisão entre {num1} e {num2} é: {mod}")
print(f"{num1} elevado a {num2} é: {exp}")

# Operadores de comparação 

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2 

#test
print(f"O numero {num1} é maior que {num2}? {bigger}")
print(f"O numero {num1} é menor que {num2}? {smaller}")
print(f"O numero {num1} é igual ao {num2}? {equal}")
print(f"O numero {num1} é diferente do {num2}? {different}")
print(f"O numero {num1} é maior ou igual a {num2}? {bigger_equal}")
print(f"O numero {num1} é menor ou igual a {num2}? {smaller_equal}")

# Operadores de Atribuição

num = num+1 # é o mesmo que: num = num+1
num = num-1 # é o mesmo que: num = num-1
num = num*1 # é o mesmo que: num = num*1
num = num/1 # é o mesmo que: num = num/1