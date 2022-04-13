import random

names = [
    'james',
    'kory',
    'julien',
    'ashley',
]

#random.randint(1,5) --> random number between 1 and 5
#random.choice(array) --> random item in this array

def main():
    guess = input('if you can guess which name I am thinking, I will give you money').lower()
    selection = random.choice(names)  #random name selection
    if guess == selection:
        print(f'you got it !! how did you know that? {selection}')
    else:
        print(f'nope not it! haha!, guess again?-- {selection}, {guess}')
        
main()