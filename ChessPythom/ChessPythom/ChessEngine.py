
def horseMove(x,y):
    posiblemoves=[]
 
    posiblemoves = [[x + 1,y + 2],
    [x + 1,y - 2],
    [x + 2,y + 1],
    [x + 2,y - 1],
    [x - 1,y - 2],
    [x - 1,y - 1],
    [x - 2,y + 1],
    [x - 2,y + 2]]
    print(posiblemoves)
    posiblemoves = outofrangeelemts(posiblemoves)

    return posiblemoves

def bishopMove(x,y):
    posiblemoves = []
    xi = x
    yi = y


    x = xi
    y = yi
    while x <= 7 and y <= 7:
        x += 1
        y += 1
        posiblemoves.append([x,y])  

    x = xi
    y = yi
    while x >= 0 and y <= 7:
        x -= 1
        y += 1
        posiblemoves.append([x,y])

    x = xi
    y = yi
    while x <= 7 and y >= 0:
        x += 1
        y -= 1
        posiblemoves.append([x,y])

    x = xi
    y = yi
    while x >= 0 and y >= 0:
        x -= 1
        y -= 1
        posiblemoves.append([x,y])
    posiblemoves = outofrangeelemts(posiblemoves)
    return(posiblemoves)
        
def rookMove(x,y):
    posiblemoves = []
    for i in range(8):
        posiblemoves.append([x,i])
        posiblemoves.append([i,y])
    posiblemoves.remove([x,y])
    return posiblemoves

def blackpawnMove(x,y):
    posiblemoves = []
    posiblemoves = [[x+1,y]]
    return posiblemoves

def whitepawnMove(x,y):
    posiblemoves = []
    posiblemoves = [[x-1,y]]
    return posiblemoves

def queenMove(x,y):#tengo que arreglar cuando junto las dos listas de la torre y el alfil
    posiblemoves = []
    posiblemoves = bishopMove(x,y)
    appendThis = rookMove(x,y)
    posiblemoves.append(appendThis)
    return posiblemoves

def kingMove(x,y):
    posiblemoves = []
    posiblemoves = [[x+1,y+1],[x+1,y],[x+1,y-1],
                    [x,y+1],[x,y-1],
                    [x-1,y+1],[x-1,y],[x-1,y-1]]
    posiblemoves = outofrangeelemts(posiblemoves)
    return posiblemoves


    

#posiciones[element[1]][element[2]]
def outofrangeelemts(posiblemoves):
    elementstoremove = []
    for element in posiblemoves:
      if element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7:
            elementstoremove.append(element)
    for element in elementstoremove:
        posiblemoves.remove(element)
    return posiblemoves