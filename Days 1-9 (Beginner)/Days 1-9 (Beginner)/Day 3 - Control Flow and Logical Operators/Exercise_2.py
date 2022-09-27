print('Bem vindo ao calculador de indice de massa corporea')
altura = float(input("digite sua altura em m: "))
peso = float(input("digite seu peso em kg: "))

imc = peso / (altura**2)

if imc <= 18.5 :
    print(f'Seu imc é abaixo ou igual a {round(imc)}, você está abaixo do peso')
elif imc <= 25:
    print(f'Seu imc é abaixo ou igual a {round(imc)}, você está com peso normal')
elif imc <= 30:
    print(f'Seu imc é abaixo ou igual a {round(imc)}, você está com pouco sobrepeso')
elif imc <= 35:
    print(f'Seu imc é abaixo ou igual a {round(imc)}, você é obeso') 
else:
    print(f'Seu imc é abaixo ou igual a {round(imc)}, você é clinicamente obeso')   
    
#BMI 2.0
#Instructions
#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#Warning you should round the result to the nearest whole number. The interpretation message needs
#to include the words in bold from the interpretations above. e.g. underweight, normal weight, 
#overweight, obese, clinically obese.