def insert(myFrob, newFrob):
    a = myFrob
    if myFrob.getAfter() == None and myFrob.getBefore() == None:
        if newFrob.myName() > myFrob.myName():
            myFrob.setAfter(newFrob)
            newFrob.setBefore(myFrob)
            return
        else:
            myFrob.setBefore(newFrob)
            newFrob.setAfter(myFrob)
            return
    if newFrob.getAfter() != None or newFrob.getBefore() != None:
        return
    a = myFrob
    if newFrob.myName() > a.myName():
        while newFrob.myName() > a.myName() and a.getAfter() != None:
            a = a.getAfter()
    else:
        while newFrob.myName() < a.myName() and a.getBefore() != None:
            a = a.getBefore()
    try:
        if newFrob.myName() > a.myName():
            newFrob.setAfter(a.getAfter())
            a.getAfter().setBefore(newFrob)
            a.setAfter(newFrob)
            newFrob.setBefore(a)
            return
    except AttributeError:
        a.setAfter(newFrob)
        newFrob.setBefore(a)
        return
    try:
        if newFrob.myName() < a.myName():
            newFrob.setBefore(a.getBefore())
            a.getBefore().setAfter(newFrob)
            a.setBefore(newFrob)
            newFrob.setAfter(a)
            return
    except AttributeError:
        a.setBefore(newFrob)
        newFrob.setAfter(a)
        return
    try:
        if newFrob.myName() == a.myName():
            newFrob.setBefore(a)
            newFrob.setAfter(a.getAfter())
            a.getAfter().setBefore(newFrob)
            a.setAfter(newFrob)
            return
    except AttributeError:
        newFrob.setBefore(a)
        a.setAfter(newFrob)
        return
      
      
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() != None:
        return findFront(start.getBefore())
    else:
        return start

