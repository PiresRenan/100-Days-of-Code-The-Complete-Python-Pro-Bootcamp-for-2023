def new_func():
    """
    This function asks the user for the name of the city they grew up in and the name of their pet. It
    then prints out a band name by combining the city name and pet name
    """
    print("Welcome to the Band Name Generator")
    city =input("What's name of the city you grew up in?")
    a = input("What's your pet's name?")
    print("Your band name could be " + city + " " + a)

new_func()