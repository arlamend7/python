
import random
 
ids = ['pedra', 'papel', 'tissoura']
 
random.choice(ids) 

num = str(input('pedra, papel ou tesoura? \n')) 

if num == random.choice(ids):
    print ('empate')
elif num == 'pedra' and random.choice(ids) == 'papel' or num == 'tesoura' and random.choice(ids) == 'pedra' or num == 'papel' and random.choice(ids) == 'tesoura':
    print ('computador ganhou')
elif num == 'papel' and random.choice(ids) == 'pedra' or num == 'pedra' and random.choice(ids) == 'tesoura' or num == 'tesoura' and random.choice(ids) == 'papel':
    print ('voce ganhou')
else :
    print ('blz?')
