print("welcome to the rollercoaster!")
height = int(input('Whats your height in cm?'))
bill = 0

if height > 120:

    print('You can ride the rollercoaster!')
    age = int(input('Whats your age?'))
    if age < 12:
        bill = 5
        print('Child tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Younth tickets are $7')
    elif age > 18 and age < 45:
        bill = 12
        print('Adults tickets are $12')
    elif age >= 45 and age <= 55:
        bill = 0

    wants_photo = input('Do you want a photo taken? Y or N.') 
    if wants_photo == "Y":
        #add $3 to the bill   
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print('Sorry, you have to grow taller before you can ride.')

