import random 

vf= str(input("Quer jogar O dado?: responda com y ou n: "))

while vf == "y":
    number = random.randint(1,6)

    if number == 1:
        print("(- - -)")
        print("(- * -)")
        print("(- - -)")
    if number == 2:
        print("(- - *)")
        print("(- - -)")
        print("(* - -)")
    if number == 3:
        print("(- - *)")
        print("(- * -)")
        print("(* - -)")
    if number == 4:
        print("(* - *)")
        print("(- - -)")
        print("(* - *)")
    if number == 5:
        print("(* - *)")
        print("(- * -)")
        print("(* - *)")
    if number == 6:
        print("(* - *)")
        print("(* - *)")
        print("(* - *)")

    print("Quer jogar denovo?:")
    x = str(input())
    if x == "y":
        vf = x
    else:
        vf = "n"