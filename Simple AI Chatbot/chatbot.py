import json
import nltk
import random

# Download NLTK tokenizer if not already downloaded
nltk.download('punkt')

# Load intents
with open("intents.json", encoding='utf-8') as file:
    data = json.load(file)

# Define interview flow
interview_flow = [
    {"tag": "name", "question": "What's your full name?"},
    {"tag": "experience", "question": "How many years of experience do you have in React Native?"},
    {"tag": "notice_period", "question": "What is your current notice period?"},
    {"tag": "current_ctc", "question": "What is your current CTC?"},
    {"tag": "expected_ctc", "question": "What is your expected CTC?"},
    {"tag": "relocation", "question": "Are you open to relocation?"},
]

# Find responses by tag
def get_response_by_tag(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Thanks for your answer."

# Chat loop
print("🤖 Interview Bot: Hello! Let's start the React Native interview. Type 'quit' to exit.\n")

answers = {}
for step in interview_flow:
    tag = step["tag"]
    print("🤖 Interview Bot:", step["question"])
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("🤖 Interview Bot: Interview ended. Thank you!")
        break

    # Optionally store answers
    answers[tag] = user_input

    # Respond after each answer
    bot_response = get_response_by_tag(tag)
    print("🤖 Interview Bot:", bot_response)
    print()

# End message
print("🤖 Interview Bot: Thank you for your responses. All the best for your interview!")
