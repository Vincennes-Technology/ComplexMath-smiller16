#!/usr/bin/python
#Smiller
#complex beginnings
def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer, imagAnswer)
print complexAdd((1,2),(3,1))
def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer,imagAnswer)
print complexSubtract((2,2),(1,1))

def complexMultiply(a, b):
    realAnswer = a[0] * b[0]
    imagAnswer = a[1] * b[1]
    return (realAnswer, imagAnswer)
print complexMultiply((2,3),(2,3))

def complexDivide(a,b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[1] / b[1]
    return (realAnswer, imagAnswer)
print complexDivide((6,6),(2,3))
