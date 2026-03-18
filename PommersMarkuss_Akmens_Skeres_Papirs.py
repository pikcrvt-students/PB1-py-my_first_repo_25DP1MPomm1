#Spēle Akmens Šķēres Papīrīts.
#Izveidoja: Markuss Jānis Pommers

from time import sleep 

print("Datorspēle - Akmens, Šķēres, Papīrīts")

player1_choice = str(input("Spēlētājs 1. izvēlies: akmens, šķēres vai papīrs: "))
print(f"Spēlētājs 2. izvēlies: akmens, šķēres vai papīrs", end="\r")
player2_choice = str(input("Izvēle: "))

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


