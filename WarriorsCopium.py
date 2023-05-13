import math

### FUNCTIONS ###

def round(n):
    if(n % 1 >= 0.5):
        return math.trunc(n +1)
    else:
        return math.trunc(n)

def calledEven(n, per):
    return round(n * (per / 100))

def actualScore(s, ft, ac):
    return s - ft + ac

def result(w, l):
    if(w == l):
        print("The Warriors and Lakers would have needed overtime to decide this game.", w, "-", l)
    elif(w < l):
        print("The Lakers would have won this game.", l, "-", w)
    else:
        print("The Warriors would have won this game.", w, "-", l)
    return 0

### STAGE 1 VARIABLES ###

game1Fouls = calledEven(6, 86.2)
game2Fouls = calledEven(16, 58.8)
game3Fouls = calledEven(17, 75.7)
game4Fouls = calledEven(12, 100.0)
game5Fouls = calledEven(15, 80.0)
game6Fouls = calledEven(14, 73.8)

### STAGE 2 VARIABLES ###

game1 = actualScore(117, 25, game1Fouls)
game2 = actualScore(100, 10, game2Fouls)
game3 = actualScore(127, 28, game3Fouls)
game4 = actualScore(104, 20, game4Fouls)
game5 = actualScore(106, 12, game5Fouls)
game6 = actualScore(122, 31, game6Fouls)

### RESULTS ###

result(112, game1)
result(127, game2)
result(97, game3)
result(101, game4)
result(121, game5)
result(101, game6)
