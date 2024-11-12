""" 
Problem Statement
Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

If the user enters anything else we print out:

Sorry I only tell jokes
"""
import random

jokes = [
    "In Pakistan, when there's a sign saying 'Slower Traffic Keep Left,' everyone speeds up in the right lane instead! 😆",
    "Why don't Pakistani programmers play hide and seek? Because good luck hiding from console.log! 😜",
    "Why did the Python developer break up with JavaScript? Because JavaScript had too many 'issues'!",
    "Why do programmers prefer dark mode? Because the light attracts too many bugs! 🐞",
    "How do you know a programmer loves tea? Because they always debug their code! 🍵"
]
prompt:str="What do you want to do?"

def joke_bot():
    user_input:str=input(prompt)

    if user_input.lower() == "joke":
        print(random.choice(jokes))  #  Randomly select a joke from the list)
    elif user_input.lower() == "list":
        for joke in jokes:
            print(joke)  # Print all jokes in the list)
    else:
        print("Sorry, I only tell jokes. Type 'joke' to hear one or 'list' to see all jokes.")

joke_bot()