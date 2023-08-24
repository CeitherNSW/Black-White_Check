import random

def pixsum(width, height):
    sumP = (width - 20) * height
    return sumP

def getPixels(width, height):
    sumpix = pixsum(width, height)
    cordinates = []
    for i in range(sumpix):
        row = random.randint(0, height - 1)
        col = random.randint(0, width - 21)
        cordinates.append((row, col))
    return cordinates
