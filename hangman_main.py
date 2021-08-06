import random
import hangman_fonction as test
import hangman_wordlist as list
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HANGMAN")

print(ascii_banner)
print('''
version : 0.0.1
Developed by Nassim.L
github : https://github.com/Nassim-L

      ''')


lives = 7
a = list.word_list

b = random.choice(a)

k = []

for i in b:
    k += '-'
endgame = False
print('Pssssss, the solution is ')
print(k)
    
while not endgame :
    k , lives = test.fonct1(b,k,lives)  
    
        
    if ('-' not in k):
        endgame = True
        
    else :
        endgame = False
        
        
    print(k)
        
    if lives == 0:
        endgame = True
        print('You have 0 lives')
        print('Game Over')
        print('the word is ')
        print([char for char in b])
        

        
   
    