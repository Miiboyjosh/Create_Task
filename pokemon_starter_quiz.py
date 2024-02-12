regionList = ["Alolan", "Galar", "Hoenn", "Johto", "Kalos", "Kanto", "Paldea", "Sinnoh", "Unova"]
alolaList = ["Rowlet", "Litten", "Popplio"]
galarList = ["Grookey", "Scorbunny", "Sobble"]
hoennList = ["Treecko", "Torchic", "Mudkip"]
johtoList = ["Chikorita", "Cyndaquil", "Totodile"]
kalosList = ["Chespin", "Fennekin", "Froakie"]
kantoList = ["Bulbasaur", "Charmander", "Squirtle"]
paldeaList = ["Sprigatito", "Fuecoco", "Quaxly"]
sinnohList = ["Turtwig", "Chimchar", "Piplup"]
unovaList = ["Snivy", "Tepig", "Oshawtt"]

#Greet the User
trainer_name = input("What is your name?")
print("Welcome",trainer_name, "to your Perfect Pokemon Match!")
#Give the user a brief description
print("This quiz will help you find you best suiting starter pokemon to join you on your pokemon adventure")
#Ask the First Question
def ques_1():
    global answer
    print("Where is the Place You Would Associate Yourself With?")
    print("1. Hawaii\n2. The United Kingdom\n3. Japan\n4. Metropolitan France\n5. Spain\n6. New York City")
    input("\nAnswer:")
    for regions in regionList:
        if answer == 3:
            print()
ques_1()