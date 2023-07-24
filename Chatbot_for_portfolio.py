#Chatbot for portfolio

#Import chatbot libraries...
from chatterbot import ChatBot 

#from chatterbot.trainers import ChatterBotCorpusTrainer

#Name of chatbot will be chatball based on NBA facts 
chatbot = ChatBot('Chatball')

running = True # Instance of system binary 

while running:
    user_input = str(input('What is your question? ').lower())

    if 'end' in user_input \
    or 'quit' in user_input \
    or 'exit' in user_input \
    or 'q' in user_input \
    or len(user_input) == 0:
        running = False
    else: 
        print(f'🏀 {chatbot.get_response(user_input)}')
        
