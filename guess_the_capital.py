import random

def play_game(german_states_capitals):
    correct = 0
    incorrect = 0
    play_more = "y"
    while play_more == "y":
        random_german_states_capitals = random.choice(list(german_states_capitals))
        guess = input("Enter the Capital City of {}: ".format(random_german_states_capitals))

        if guess.lower() == german_states_capitals[random_german_states_capitals].lower():
            correct += 1
            print("Great!")
        else:
            incorrect += 1
            print("Not right!")
        play_more = input("You want to play more. Type 'y'. Else Type any other key to exit  the Game! ")
    return correct, incorrect

def result():
    german_states_capitals = {
    "Baden-Württemberg": "Stuttgart",
    "Bavaria (Bayern)": "Munich (München)",
    "Berlin": "Berlin",
    "Brandenburg": "Potsdam",
    "Bremen": "Bremen",
    "Hamburg": "Hamburg",
    "Hesse (Hessen)": "Wiesbaden",
    "Lower Saxony (Niedersachsen)": "Hanover (Hannover)",
    "Mecklenburg-Vorpommern": "Schwerin",
    "North Rhine-Westphalia (Nordrhein-Westfalen)": "Düsseldorf",
    "Rhineland-Palatinate (Rheinland-Pfalz)": "Mainz",
    "Saarland": "Saarbrücken",
    "Saxony (Sachsen)": "Dresden",
    "Saxony-Anhalt (Sachsen-Anhalt)": "Magdeburg",
    "Schleswig-Holstein": "Kiel",
    "Thuringia (Thüringen)": "Erfurt"
   }
    correct, incorrect = play_game(german_states_capitals)
    print(f"You got it correct {correct} out of {correct + incorrect}")

result()
