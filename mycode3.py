import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Sample responses and patterns
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you",
        ["I'm good, thank you! How about you?", "I'm just a bot, but I'm doing well!"]
    ],
    [
        r"(.*) your name",
        ["I'm a chatbot created to assist you!", "You can call me ChatBot!"]
    ],
    [
        r"what can you do",
        ["I can chat with you, answer some basic questions, and keep you company!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "That's interesting! Tell me more."]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(test_inputs=None):
    print("ChatBot: Hello! Type 'bye' to exit.")
    if test_inputs is None:
        test_inputs = ["hello", "how are you", "what can you do", "bye"]
   
    for user_input in test_inputs:
        print(f"You: {user_input}")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot_response()

