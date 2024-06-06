"""
Exercise 1: 
    
    *Predecessor and Successor of a number: 
        -> Write a Python program that reads a number and represents its predecessor and its successor, using assignment operators 
    
    *Average of 4 Grades: 
        -> Write a Python program that reads four numbers and calculates the average between these numbers
        
"""
# Predecessor and Successor of a number:
num = int(input("Digite um numero: "))
print(f"O antecessor de {num} é {num-1} \ne seu sucessor {num+1}.")

# Average of 4 Grades:
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
num4 = float(input("Digite a quarta nota: "))

avarage = (num1+num2+num3+num4)/4

print(f"A média das notas inseridas é: {avarage}")