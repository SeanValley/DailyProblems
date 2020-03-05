#main() contains tests for car() and cdr()
#car() returns the first element of the pair in cons
#cdr() returns the second element of the pair in cons
#This was a weird problem and taught me some stuff I didn't know could be done in python.
#I'm not sure this is the right way to do it, but it seems to make sense.

def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#First Element
def car(construct):
    return construct(getValues)[0]
    
#Second Element
def cdr(construct):
    return construct(getValues)[1]

def getValues(a, b):
    return [a, b]

main()
