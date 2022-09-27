#String
#print('123' + '456')
#Integer
#print(123+456)
#num_char = len(input("Qual teu nome?"))
#new_num_char = str(num_char)
#print("Seu nome tem " + new_num_char + " caracteres.")
#BMI calculator
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
#bmi = int(weight)/float(height)**2
#print(round(bmi))
#print(3 + 3 * 3 / 3 - 3)
#print(8 / 3)
#print(int(8 / 3))
#print(round(8 / 3))
#print(round(8 / 3,2))
#print(round(2.66666666666,2))
#print(8//3)
#print(type(8//3))
#print(round(8/3,3))
#print(type(8/3))
#result = 4 / 2
#result /= 2
#print(result)
#score = 0
#print(score)
#score += 1
#print(score)
#score = 3
#height = 1.8
#isWinning = True 
#print(f"your score is {score}")
#print(f"your heighr is {height}")
#print(f"you are winning is {isWinning}")
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
#print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#people = int(input("How many people to split the bill?"))
#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill + total_tip_amount
#bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)
# FAQ: How to round to 2 decimal places?
# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
#print(f"Each person should pay:${final_amount}")
print('Bem vindo a calculadora de gorgeta!')
conta = float(input("Quanto deu a conta? $"))
gorgeta = int(input('Quanto quer deixar de gorgeta? 10, 12, ou 15?'))
pessoas = int(input('Quantas pessoas dividirao a conta?'))
gorgeta_porcentagem = gorgeta / 100
total_gorgeta = conta * gorgeta_porcentagem
total_conta = conta + total_gorgeta
conta_por_pessoa = total_conta / pessoas
total_a_pagar = round(conta_por_pessoa, 2)
print(f"Cada pessoa deve pagar: ${total_a_pagar}")
#idade = input("Quantos anos você tem?")

#idade_como_int =int(idade)

#anos_restantes = 90 - idade_como_int
#dias_restantes = anos_restantes * 365
#semanas_restantes = anos_restantes * 52
#meses_restantes = anos_restantes * 12

#print(f'Você tem {dias_restantes} dias, {semanas_restantes} semanas, e {meses_restantes} meses restantes.')

#print(6 + 4 / 2 - (1 * 2))