print("Welcome to Gia's Mad Libs. This is a fun game where you will input words to fill in the blanks of a story. You will have 2 different stories to choose from. Let's get started!")

# Choose a story
while True:
    story_choice = input("Please choose a story by entering 1 or 2: ")
    if story_choice in ['1', '2']:
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Story 1
if story_choice == '1':
    print("You chose Story 1: The Interview")
    emotion1 = input("Enter an emotion: ")
    company1 = input("Enter a company name: ")
    emotion2 = input("Enter a facial expression (e.g., smile, frown): ")
    adjectiive1 = input("Enter an adjective: ")
    item1 = input("Enter an item: ")
    number1 = input("Enter a number: ")
    body_part1 = input("Enter a body part: ")
    planet1 = input("Enter a planet: ")
    adjective2 = input("Enter an adjective: ")
    verb_ending_ing1 = input("Enter a verb ending in -ing: ")
    object1 = input("Enter an object: ")
    liquid1 = input("Enter a liquid: ")
    clothing_item1 = input("Enter a piece of clothing: ")
    number2 = input("Enter a number: ")

    
    story1 = f"That day I walked into the office feeling {emotion1}. I was there for an interview at {company1}. The receptionist greeted me with a {emotion2} look and told me to have a seat next to the {adjectiive1} {item1} over in the corner. After {number1} minutes, the hiring manager called my name. I shook his {body_part1} and he looked at me as if I was from {planet1}. We had begun the interview and he asked 'What is one word to describe yourself?' I took a deep breath and said, '{adjective2}.' Then he asked about my biggest weakness, and I said '{verb_ending_ing1} too hard.' Halfway through, I accidentally knocked over a cup full of {liquid1} all over his {object1} and {clothing_item1}. It's been {number2} years since I have heard from them."
    print(story1)
    print("Thank you for playing!")

# Story 2
if story_choice == '2':
    print("You chose Story 2: Superhero")
    name1 = input("Enter a name: ")
    city1 = input("Enter a city name: ")
    adjective3 = input("Enter an adjective: ")
    clothing_item2 = input("Enter a piece of clothing: ")
    celebrity1 = input("Enter a celebrity: ")
    verb_ending_ing2 = input("Enter a verb ending in -ing: ")
    verb_ending_ing3 = input("Enter a verb ending in -ing: ")
    adjective4 = input("Enter an adjective: ")
    noun1 = input("Enter a singular noun: ")
    interjection1 = input("Enter an interjection (e.g., Wow, ouch): ")

    story2 = f"There once was a superhero named {name1} who lived in {city1}. Every morning. they put on their {adjective3} {clothing_item2}. One day, a {adjective4} villian named {celebrity1} appeared and started {verb_ending_ing2} all over the city! The villian tried to escape by {verb_ending_ing3}, but {name1} stopped them with a powerful {adjective4} {noun1}. The city was saved and everyone cheered '{interjection1}!' "
    print(story2)
    print("Thank you for playing!")

