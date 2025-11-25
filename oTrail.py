import os
import time

os.system('cls')

#main menu
print("""
################################################################
#::::::::$$$$$$::::::::::::::::::::::::::::::::::::::::::::::::#
#__::::::$$$:::::::::::::::::::::::::::::::::::::::::::::::::::#
#  \::::$$:::::::::::::::::::::::::::::::::::::::::::::::::::::#
#   \::_$_:::::::::::::::::::::::::::::::::::::::::::::::::::::#
#    \|___|::::::::::::::::::::::::::::::::::::::::::::::::::::#
#     \| |:::::::::::::::::::::::::::::::::::::::::::::::::::::#
#      \ |:::::::::::::::::::::::::::::::::::::::::::::::::::::#
#       \|;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#
#        \ ''''''''''''''''''''''''''''''''''''''''''''''''''''#
#         \ ''''''''''''''-----------''''''''''''''''''''''''''#
#          \ ''''''''''''|A long trip|'''''''''''''''''''''''''#
#           \ ''''''''''''-----------''''''''''''''''''''''''''#
#-----------|\ ''''''''''''''''''''''''''''''''''''''''''''''''#
#...........|''''''''''''''''''%'''''''''''''''''''''''''''''''#
#...........|'''''''''''''''''%%%'''''''''''''''''''''''''''''_#
#...........|'''''''''''''''%%%%%%%''''''''''''''''''''''''''/ #
#________...|''''''''''''''''''N''''''''''''''''''''''''''''/  #
#|      |...|'''''''''''''''''%%%''''''''''''''''''''''''''/   #
#|      |...|%$''''''''''%''%%%%%%% ''''''''''''''''''''''/    #
#|      |...|$%$''''''''%%%''''N''''''''''''''''''''ooooooooooo#
#|    []|...|%$$$%'''''''N''''%%%'''''''ooooooooooooooooooooooo#
#|      |...|$$%$'''''''%%%'%%%%%%%''00000OOOOOOOOOOOOOOOOOOOOO#
#|      |...|$$%$$$''''%%%%%'''N''''OOWWWOOOOOOOOOOOOOOOOOOOOOO#
#|      |...|%$$$$$$'''''N'''''N'''OOOOOOOOOOOOOOOOOOOOOOOOOOOO#
#-----------------------------------oooooooooooo@@@@ooooooooooo#
#                                   ooooooooooo@@<>@@oooooooooo#
#     Made by Simas Burdenkovas                @@<>@@          #
#                                               @@@@           #
################################################################

      """)
time.sleep(5)
os.system('cls')


#variable zone
name = input("Enter your name: ")
gender = input("What is your gender: ")
carspace = 20
health = 50
energy = 25
nourishment = 30
thirst = 30
money = 250
gas = 25
km_done = 0
km_left = 1673
stress = 0
drunkness = 0

# Item Variables

## Item space var
#Drinks
Water = -1
Cola = -1
Bilsner = -1
Feiniken = -1
Red = -1
Moon = -2
Coffe -1

#Cigs
Z-Gold = -1
Z-Red = -1
P-Royal_blue = -1
Unlcky-Strike = -1
B-Spirit = -1
Royal_M-Cigar = -2

#Foods
Burger = -1
Kebab = -1
Blocky-C = -2
Boat-S = -2
Ramen = -1
Gum -1
Tabbaco = -1
Snus = -1
Pickers = -1
Pays-C = -1
Babbel-C = -1
Hotdawg = -1
Baloney = -1
HotSchlong = -2

#Drugs
Weed = -1
Coke = -1
Meth = -1
Shrooms = -1

#Weapons
Knife = -1
Bat = -3
Snub = -2
Axe = -4

#Companion
Dan = -5 
Jenny = -4
Homless = -6
Carlos = -4

## Side affect
#drinks
Water_Thirst = 15 
Cola_Thirst = 10
Cola_Energy = 5




inventory = ["Water","Burger","Gold","Bilsner","Bilsner","Bilsner","Bilsner","Coupon" ]


os.system('cls')

print("""
      STARTING INFO:
      Name:""",name,""" 
      Age : 21
      Gender :""",gender,""" 
      Year : 1997
      Car : "1989 Forb Sierra BS Cosworth"
      Car space : 20
      Health : 50
      Energy : 25
      Nourishment : 30
      Thirst : 30
      Stress : 0
      Drunkness : 0
      Money : 250 Eur
      Gas tank : 25
      Km traveled : 0
      Km left : 1673
      Starting items:
        1x Water botle (-1 space)
        1x Cheese burger (-1 space)
        1x Zalboro gold (-1 space)
        4x cans of "Bilsner" Beer (-4 space)
        1x food coupon (1 time use -75% off)
      You will start in 30 seconds

      """)

time.sleep(30)
os.system('cls')

print("BEFORE PLAYING, PLEASE READ THE MANUAL BUNDLED WITH THE GAME")

time.sleep(5)

os.system('cls')

def driving_off():
    print("""
      


            /{}#,
            #######
        ---------------------------

            """)
    time.sleep(1)
    os.system('cls')
    print("""
                /{}#,
                #######
        ---------------------------

          """)
    time.sleep(1.5)
    os.system("cls")
    print("""
                        /{}#,
                        #######
        ---------------------------

          """)
    time.sleep(1.6)
    os.system('cls')
    print("""


         --------------------------- 
          """)
    time.sleep(0.9)
    os.system('cls')

driving_off()

def driving_anim():
    os.system('cls')
    print("[#----]")
    time.sleep(1.5)

    os.system('cls')
    print("[-#---]")
    time.sleep(1.5)

    os.system('cls')
    print("[--#--]")
    time.sleep(1.5)

    os.system('cls')
    print("[---#-]")
    time.sleep(1.5)

    os.system('cls')
    print("[----#]")
    time.sleep(1.5)

    os.system('cls')


driving_anim()


print("marius kakalius")

