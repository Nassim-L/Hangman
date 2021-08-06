import hangman_art as main
import os

def clear():
    os.system( 'clear' )

def fonct1(b,k,l):

    c = input('chose your letter: \n')
    
    
    if c in b :
        for i in range(0,len(b)):
            if b[i] == c:
                k[i] = c 
            
    if not c in b:
        print(main.stages[l-1])
        lives = l
        print(f'{lives} left')
        l -= 1
    
    return k, l
        
    

        
        
    
        

         
            
            
    