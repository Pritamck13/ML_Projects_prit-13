
def shrt(x):

    count = 0
    shortest = 0
    for i in range(len(x)):
        length = 0
        while count <=3:
            if x[i] == "1":
                count = count + 1
            length = length +1
        if count == 3:
            shortest = min(shortest,length)
    return shortest
x = "01011010"
shrt(x)