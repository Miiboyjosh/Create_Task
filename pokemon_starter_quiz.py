# Self identifying lists
alolaList = ["Litten", "Rowlet", "Popplio"]
galarList = ["Scorbunny", "Grookey", "Sobble"]
hoennList = ["Torchic", "Treeko", "Mudkip"]
johtoList = ["Cyndaquil", "Chikorita", "Totodile"]
kalosList = ["Fennekin", "Chespin", "Froakie"]
kantoList = ["Charmander", "Bulbasaur", "Squirtle"]
paldeaList = ["Fuecoco", "Sprigatito", "Quaxly"]
sinnohList = ["Chimchar", "Turtwig", "Piplup"]
unovaList = ["Tepig", "Snivy", "Oshawtt"]
# Variables
score = 0
# Greet the User
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
        region = alolaList
        ques_2()
    if response == "2":
        print("Your region is Galar")
        region = galarList
        ques_2()
    if response == "3":
        japan_opt()
    if response == "4":
        print("Your region is Kalos")
        region = kalosList
        ques_2()
    if response == "5":
        print("Your region is Paldea")
        region = paldeaList
        ques_2()
    if response == "6":
        print("Your region is Unova")
        region = unovaList
        ques_2()
def japan_opt():
    global region
    print("Which of the Follow Geographies Would You Prefer")
    print("1. Volcanic\n2. Plains\n3. Mountainous\n4. Archipelago")
    jap_response = input("\nAnswer:")
    if jap_response == "1":
        print("Your region is Hoenn")
        region = hoennList
        ques_2()
    if jap_response == "2":
        print("Your region is Kanto")
        region = kantoList
        ques_2()
    if jap_response == "3":
        print("Your region is Sinnoh")
        region = sinnohList
        ques_2()
    if jap_response == "4":
        print("Your region is Johto")
        region = johtoList
        ques_2()
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
    print("A.Weightlifting\nB. Reading\nC. Hiking")
    answer = input("\nAnswer:")
    score_sys(answer)
    fin_results()
def score_sys(answer):
    global score
    if answer == "A" or "a":
        score += 3
    if answer == "B" or "b":
        score += 2
    if answer == "C" or "c":
        score += 1
def fin_results():
    global score
    if score >= 11:
        print("Congrats", trainer_name, "your starter Pokemon is", region[0])
    if score >= 8 or score <= 10:
        print("Congrats", trainer_name, "your starter Pokemon is", region[1])
    if score == 4:
        print("Congrats", trainer_name, "your starter Pokemon is", region[2])


ques_1()

