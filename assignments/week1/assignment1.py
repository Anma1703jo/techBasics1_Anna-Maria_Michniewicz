# Hi, I thought we were supposed to write something about the code, but I wasn't sure where. But here we are, hope that's fine! 
#So for the ASCII Art I was inspired by the Lesser Dog from Undertale and thought that I could do some cool stuff with python by wiggling the neck or something. DataX didn't
#teach me much (or I didn't learn much) so I searched for some cool tips and found this: https://dev.to/reardon85/using-ascii-art-in-python-1ea1 
#I kind of got the hang of the string, but it was mostly guessing
#and honestly, if I did the code 100% without help it would be something like:
# for i in range(10):
#            print(" " * (5) + " " * i + "\\      \\")
 #       for j in range(6):
  #          print(" " *(15) + "|      |")
   #     for k in range(10):
    #        print( " " *(14-k) + " " * 1 + "/      /")
     #   for j in range(6):
      #      print(" " *(5) + "|      |")
      # then the first text and repeat of the lines above, do the next text, and repeat the lines above again
#I hope you get what I mean. But I showed my boyfriend what I am doing and he was like "You leanred how to do functions, why don't you use it?"
#he also helped me a bit to set the while loop, as I said, otherwise I'd sent in a really long code, but I am happy with the result and I actually understood what I did here (that's something new)
#(no AI, just trying things out, a lot and asking my boyfriend to explain some things to me)



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



