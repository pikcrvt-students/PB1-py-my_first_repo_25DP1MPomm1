def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

skaitlis1 = int(input("Ievadiet pirmo skaitli: "))
skaitlis2 = int(unput('Ievadiet otro skaitlis: '))

lielakais = maximum(skaitlis1, skaitlis2)
print(lielakais)