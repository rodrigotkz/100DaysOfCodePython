# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number))

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit
print(two_digit_number)

#Calculadora IMC

Altura = (input("Digite a sua altura em metros: "))
Peso = (input("Digite o seu peso em kg: "))

peso_int = int(Peso)
altura_float = float(Altura)

calculo_imc = peso_int / altura_float ** 2 
imc_int = int(calculo_imc)

print(imc_int)

