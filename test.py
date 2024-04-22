def mintoHours(min):
    minsLeft = min%60
    hours = min//60
    return (hours, minsLeft)

print(mintoHours(125))