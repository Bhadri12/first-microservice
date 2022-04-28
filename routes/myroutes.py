import random
from config import app

@app.get('/message')
def greetnow():
    return "hi everyone how are you!!!"

@app.get('/number')
def fun():
    num =  random.randint(0,100) #Return a random integer inside the range 0 & 100
    return f"{num} is returned"