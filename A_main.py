#welcome 
from C_titleart import *
from B_functions import *
from D_arts import *
from E_texts import *

print(The_Adventures_of, stickman)
print(' ')
cont = input("Type 'n' to continue: ")
# if cont == 'n':
#     clear()
#     next_slide(slide1, text1)
#     cont = input("'n' to continue: ")
 
# if cont == 'n':
#     clear()
#     next_slide(slide2, text2)

cont_var = 0 
while cont == 'n':
    clear()
    next_slide(arts[cont_var], texts[cont_var])
    cont = input("'n' to continue: ")
    cont_var += 1 