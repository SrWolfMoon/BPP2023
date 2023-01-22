import pdb
pdb.set_trace()


exampleList = [[1,24,213,23],[2,4,0,245,3,4],[7,13,27,22]]

# EX 1
def getMaxInList(list):
    returnList = []
    #Se procede a marcar el número máximo con un **, se intenta poner en negrita
    #Pero mi máquina linux no lo registra (Se intenta hasta con librerias termcolor)
    maxN = max(list)
     
    [returnList.append(f"*{n}*") if n == maxN 
               else returnList.append(n) for n in list]
            
    return returnList

# EX 2
def getPrimeList(list):
    returnList = filter(lambda n: isPrime(n), list)
    return returnList

def isPrime(number):
    # Se programa de tal forma que en cuanto pase por la regla retorna 0
    # esto nos permite ganar ms en tiempo de ejecución, que en definitiva
    # es la base de optimización del código
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            return False
        
    return True

#MAIN
print("---------------MAX IN A ROW (marked with *)----------------")
for example in exampleList:
    print(getMaxInList(example))
    
print("---------------PRIMES----------------")
for example in exampleList:
    print(list(getPrimeList(example)))