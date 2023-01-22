import sys
# Clase Mayor de 10
class NumberUpperTen(Exception):
    pass;

#Pedimos numeros
try:   
    lect = input("Introduce un numero entre 1 y 10 entero \n")
    
    number = int(lect)
    if(number > 10):
        raise NumberUpperTen
    
except NumberUpperTen:
    print("Please, 10 is the max value.")
except:
    print("An Error has ocurred, ¿Are u entering int value?")
else:
    print(f"You have chosen {int(number)}")
    
    
#   TXT FILE EXCEPTIONS
try:
    f = open("ignacio.txt", 'rb')
except OSError:
    print("Could not open/read file:", "ignacio.txt")
    sys.exit()
except:
    print("An unexpected value ocurred")
else:
    print("File sucessfuly opened")
