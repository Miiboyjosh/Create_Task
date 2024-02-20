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
    global region
    print("Where is the Place You Would Associate Yourself With?")
    print("1. Hawaii\n2. The United Kingdom\n3. Japan\n4. Metropolitan France\n5. Spain\n6. New York City")
    response = input("\nAnswer:")
    if response == "1":
        print("Your region is Alola")
        ques_2()
    if response == "2":
        print("Your region is Galar")
        ques_2()
    if response == "3":
        japan_opt()
    if response == "4":
        print("Your region is Kalos")
        ques_2()
    if response == "5":
        print("Your region is Paldea")
        ques_2()
    if response == "6":
        print("Your region is Unova")
        ques_2()
def japan_opt():
    print("Which of the Follow Geographies Would You Prefer")
    print("1. Volcanic\n2. Plains\n3. Mountainous\n4. Archipelago")
    response = input("\nAnswer:")
    if response == "1":


def ques_2():
    print("What characteristic best describes you")
    print("A. Passionate\nB. Relaxed\nC. Sympathetic")
    answer = input("\nAnswer:")
    score_sys(answer)
    ques_3()
def ques_3():
    print("What is your favorite color?")
    print("A. Red\nB. Blue\nC. Green")
    answer = input("\nAnswer:")
    score_sys(answer)
    ques_4()
def ques_4():
    print("In any situation, what is your first move?")
    print("A. Face Head-On\nB. Analyze\nC. Use Creativity")
    answer = input("\nAnswer:")
    score_sys(answer)
    ques_5()
def ques_5():
    print("Which of these hobbies do you enjoy most?")
    print("A. Hiking\nB. Reading\nC. Weightlifting")
    answer = input("\nAnswer:")
    score_sys(answer)
def score_sys(answer):
    global score
    if answer == "A" or "a":
        score += 1
    if answer == "B" or "b":
        score += 2
    if answer == "C" or "c":
        score += 3

def fin_results():
    if score >= 5:
        print()

ques_1()
