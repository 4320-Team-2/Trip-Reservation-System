
def createConfirmationNum(firstName, it4320String):


    it4320List = list(it4320String)
    name = list(firstName)

    confirmationNumber = ""
    len1 = len(name)
    len2 = len(it4320List)
    i = 0

    while i in range(len1) or i in range(len2):
        if(i < len1):
            confirmationNumber += name[i]
        if(i < len2):
            confirmationNumber += it4320List[i]
        i += 1

    return confirmationNumber
