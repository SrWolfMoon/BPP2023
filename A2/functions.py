def getArea(x, y=-1):
    if(y != -1):
        return x*y
    return x*x

def getPerimeter(x, y="", a=-1, b=-1):  
    if(y == ""):
        return x * 4
    if(x <= 0 or y <= 0 or a <= 0 or b <= 0):
        return "No puede haber una figura con un lado negativo"

    return x + y + a + b

def sumAndParseToIntByStr(x, y):
    try:
        numberX = int(x)
        numberY = int(y)
        return numberX+numberY
    except:
        return "Ha ocurrido un error al parsear la cadena de texto"
    
def sumAndParseToFloatByStr(x, y):
    try:
        numberX = float(x)
        numberY = float(y)
        return numberX+numberY
    except:
        return "Ha ocurrido un error al parsear la cadena de texto"
    