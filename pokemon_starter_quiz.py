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
print("Welcome",trainer_name,"to your Perfect Pokemon Match!")
# Give the user a brief description
print("This quiz will help you find you best suiting starter pokemon to join you on your pokemon adventure")
# Ask the First Question
def ques_1():
    print("Where is the Place You Would Associate Yourself With?")
    print("1. Hawaii\n2. The United Kingdom\n3. Japan\n4. Metropolitan France\n5. Spain\n6. New York City")
    response = input("\nAnswer:")
    if response == "3":
        japan_opt()

def japan_opt():
    print("Which of the Follow Geographies Would You Prefer")
    print("1. Volcanic\n2. Plains\n3. Mountainous\n4. Archipelago")
    response = input("\nAnswer:")
    if response == "1":


def ques_2():
    sdf



def score_sys(answer):
    global score
    if answer == "A":
        score += 1
    if answer == "B":
        score += 2
    if answer == "C":
        score += 3



ques_1()
