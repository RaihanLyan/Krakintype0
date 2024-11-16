

import random
import string

def generate_password(length= 12,lower_case=0,upperclass=0):
    password = []

    for _ in range(upperclass):
        password.append(random.choice(string.ascii_uppercase))

    for _ in range(lower_case):
        password.append(random.choice(string.ascii_lowercase))

    remaining_length = length - len(password)
    characters = string.ascii_letters + string.digits +string.punctuation
    password += random.choice(characters)



    return''.join (password)
if __name__ =="__main__":
    length = int(input("enter your length"))
    if length < 9:
        print("thats it!")
    else:
        upperclass= int(input('how many upper class characters do you want'))
        if upperclass <2:
            print('no')
        else:
            lower_case= int(input('how many lowercase characters do you want'))
            if lower_case < 2:
                print('no')
            else :
                generated_password = generate_password(length,upperclass,lower_case)
                print("Generated password is:", generated_password)
        

