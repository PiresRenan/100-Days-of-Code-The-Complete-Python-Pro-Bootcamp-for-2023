####### SCOPE #########
# 2. Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies #Global keyword modifica uma variavel em qualquer lugar do codigo
#     # enemies += 2
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1 

# increase_enemies()
# print(f"enemies outside function: {enemies}")

###### LOCAL SCOPE ######

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

###### GLOBAL SCOPE ########
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
# game()    

##### THERE IS NO BLOCK SCOPE #####

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)
# create_enemy()

##### GLOBAL CONSTANTS #####

# A global constant.
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calc():
    TWITTER_HANDLE = "@cleiton"
    print(TWITTER_HANDLE)

calc()