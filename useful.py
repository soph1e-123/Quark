def sameHeight(obj1, obj2):
    overlap = max([0, -max([obj1.getPosition()[1]-obj1.getSize()[1], obj2.getPosition()[1]-obj2.getSize()[1]])+min([obj1.getPosition()[1], obj2.getPosition()[1]])])
    return overlap >= 0.5*obj1.getSize()[1]
    
    #return (obj1.getPosition()[1] >= obj2.getPosition()[1] and obj1.getPosition()[1]-obj1.getSize()[1] <= obj2.getPosition()[1]
           # or obj2.getPosition()[1] >= obj1.getPosition()[1] and obj2.getPosition()[1]-obj2.getSize()[1] <= obj1.getPosition()[1])


def findOverlap(a1, a2, b1, b2):
    overlap = max([0, -max([a1,b1])+min([a2,b2])])
    return overlap