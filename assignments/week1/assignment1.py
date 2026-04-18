print("Oh hello, dear fella. You've been visited by Doggy Long Neck.")

#cutie patootie doggy face (it's rough, I know)
print("""
    /\\____/\\
    | o o  |
    |  ▼   |
    |  ◡   |
    |      |""")

#function for the swirley curves of the long neck
def long_neck_loop():
    for a in range (2):
        for i in range(10):
            print(" " * (5) + " " * i + "\\      \\")
        for j in range(6):
            print(" " *(15) + "|      |")
        for k in range(10):
            print( " " *(14-k) + " " * 1 + "/      /")
        for j in range(6):
            print(" " *(5) + "|      |")

#suprise message every loop
texts=["Doggy Long Neck has seemingly gone where no dog has gone before!","I think I get, why he's called like that now...","Will this ever take an end lol"]
zähler=0

#while loop for the texts
while zähler<3:
    long_neck_loop()
    print(" " *5 + "|      |", texts[zähler])
    zähler = zähler+1
    long_neck_loop()

#doggy body
print(" " * 5 + "|      |")
print("""    ╭\\      /╮
    |   \\/   |/ \\
    |        |  /
    |        | /    Isn't Doggy Long Neck the best Boi?
    ◠________◠""")

#text box
print("_" * 40)

lr = "|" + " " * 2
rr = " " * 8 + "|"

print(lr + "＊ check" + " " * 15 + "＊ pet" + rr)
print(lr + "＊ pet" + " " * 17 + "＊ pet" + rr)
print(lr + "＊ pet" + " " * 17 + "＊ pet" + rr)

print("_" * 40)



