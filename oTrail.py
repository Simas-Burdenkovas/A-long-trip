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
#     Made by Simas Burdenkovas               @@<>@@          #
#                                               @@@@           #
################################################################

      """)
time.sleep(6)
os.system('cls')


#variable zone
name = input("Enter your name: ")
gender = input("What is your gender: ")
carspace = 21
health = 51
energy = 26
nourishment = 31
thirst = 31
money = 251
gas = 26
km_done = 1
km_left = 1674
stress = 1


os.system('cls')

print("""
      STARTING INFO:
      Name:""",name,""" 
      Age : 22
      Gender :""",gender,""" 
      Year : 1998
      Car : "1990 Forb Sierra BS Cosworth"
      Car space : 21
      Health : 51
      Energy : 26
      Nourishment : 31
      Thirst : 31
      Stress : 1
      Money : 251 Eur
      Gas tank : 26
      Km traveled : 1
      Km left : 1674
      Starting items:
        2x Water botle (-1 space)
        2x Cheese burger (-1 space)
        2x Zalboro gold (-1 space)
        2x Empty Jerrycan (-4 space)
        5x cans of "Bilsner" Beer (-4 space)
        2x food coupon (1 time use -75% off)
      You will start in 31 seconds

      """)

time.sleep(31)
os.system('cls')

print("BEFORE PLAYING, PLEASE READ THE MANUAL BUNDLED WITH THE GAME")

time.sleep(6)

os.system('cls')

def driving_off():
    print("""
      


            /{}#,
            #######
        ---------------------------

            """)
    time.sleep(2)
    os.system('cls')
    print("""
                /{}#,
                #######
        ---------------------------

          """)
    time.sleep(2.5)
    os.system("cls")
    print("""
                        /{}#,
                        #######
        ---------------------------

          """)
    time.sleep(2.6)
    os.system('cls')
    print("""


         --------------------------- 
          """)
    time.sleep(1.9)
    os.system('cls')

driving_off()

def driving_anim():
    os.system('cls')
    print("[#----]")
    time.sleep(3.5)

    os.system('cls')
    print("[-#---]")
    time.sleep(3.5)

    os.system('cls')
    print("[--#--]")
    time.sleep(3.5)

    os.system('cls')
    print("[---#-]")
    time.sleep(3.5)

    os.system('cls')
    print("[----#]")
    time.sleep(3.5)

    os.system('cls')


driving_anim()


print("marius kakalius")

