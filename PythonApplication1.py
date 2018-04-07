
import random
 
ids = ['pedra', 'papel', 'tissoura']
 
random.choice(ids) 

num = str(input('pedra, papel ou tissoura? \n')) 

if num == random.choice(ids):
    print ('empate')
elif num == 'pedra' and random.choice(ids) == 'papel' or num == 'tissoura' and random.choice(ids) == 'pedra' or num == 'papel' and random.choice(ids) == 'tissoura':
    print ('computador ganhou')
elif num == 'papel' and random.choice(ids) == 'pedra' or num == 'pedra' and random.choice(ids) == 'tissoura' or num == 'tissoura' and random.choice(ids) == 'papel':
    print ('voce ganhou')
else :
    print ('blz?')
