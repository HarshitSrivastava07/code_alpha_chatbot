#please download nltk before running this code
import random
import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help?"]),
    (r"how are you", ["I'm good! How about you?", "I'm just a bot, but I'm doing well!"]),
    (r"what is your name", ["I'm jarvis!", "You can call me jarvis."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! See you soon."]),
    (r"(.*) your name", ["My name is jarvis!", "I'm jarvis, your virtual assistant."]),
    (r"who created you", ["I was created by a Harshit Srivastava!to tackle real life problems given by code alpha", "Harshit Srivastava wrote my code to complete his internship in code alpha."]),
    (r"(.*)", ["I'm not sure I understand.", "Can you rephrase that?", "Interesting! Tell me more."])
]


chatbot = Chat(pairs, reflections)

print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
