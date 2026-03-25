#Spēle Akmens Šķēres Papīrīts.
#Izveidoja: Markuss Jānis Pommers

from time import sleep 
import os

print("Datorspēle - Akmens, Šķēres, Papīrīts")
sleep(1)

def clear():
  os.system('cls' if os.name=='nt' else 'clear')
clear()

player1_choice = str(input("Spēlētājs 1. izvēlies: akmens, šķēres vai papīrs: "))

def clear():
  os.system('cls' if os.name=='nt' else 'clear')
clear()

player2_choice = str(input("Spēlētājs 2. izvēlies: akmens, šķēres vai papīrs: "))

def clear():
  os.system('cls' if os.name=='nt' else 'clear')
clear()

for atkartosanas_skaits in range(4):
    print('  bq', end="\r")
    sleep(0.25)
    print('  dp', end="\r")
    sleep(0.25)
    print('  qb', end="\r")
    sleep(0.25)
    print('  pd', end="\r")
    sleep(0.25)

if player1_choice == player2_choice:
    print("Neizšķirts!")
elif player1_choice =="akmens" and player2_choice =="šķēres":
    print("Spēlētājs 1. uzverējā")
elif player1_choice =="šķēres" and player2_choice =="papīrs":
    print("Spēlētājs 1. uzverējā")
elif player1_choice =="papīrs" and player2_choice =="akmens":
    print("Spēlētājs 1. uzverējā")
elif player2_choice =="akmens" and player1_choice =="šķēres":
    print("Spēlētājs 2. uzverējā")
elif player2_choice =="šķēres" and player1_choice =="papīrs":
    print("Spēlētājs 2. uzverējā")
elif player2_choice =="papīrs" and player1_choice =="akmens":
    print("Spēlētājs 2. uzverējā")

