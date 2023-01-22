import pytest
import functions

def test_sumAndParseInt_Ok():
    x = "1"
    y = "2"
    expected = 3
    
    assert functions.sumAndParseToIntByStr(x,y) == expected

def test_sumAndParseFloat_Ok():
    x = "1.5"
    y = "2.25"
    expected = 3.75
    
    assert functions.sumAndParseToFloatByStr(x,y) == expected
    
def test_sumAndParseFloat_KO():
    x = "1.5"
    y = "2,25"
    expected = "Ha ocurrido un error al parsear la cadena de texto"
    
    assert functions.sumAndParseToFloatByStr(x,y) == expected
    
def test_sumAndParseInt_KO():
    x = "1.5"
    y = "2.25"
    expected = "Ha ocurrido un error al parsear la cadena de texto"
    
    assert functions.sumAndParseToIntByStr(x,y) == expected
    
def test_getArea_OK():
    x = 10
    expected = 100
    
    assert functions.getArea(x) == expected