"""
Part 1:
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Input: 273025-767253
"""

def partOne():
    """
    """
    start = [2,7,3,0,2,5]
    end = 767253
    

    l = []

    def checkDecrease(start):
        """
        """
        for i in range(5):
            if start[i] > start[i + 1]:
                start[i + 1] = start[i]
                
        #print(start)
        return start.copy()
    
    def checkAjacent(start):
        """
        """
        for i, j in enumerate(range(1, 6)):
            if start[i] == start[j]:
                return True
        
        return False

    l.append(checkDecrease(start))

    while int(''.join(map(str, start))) <= end:

        for i in range(5, 0, -1):

            if i < 5:
                if start[i] < start[i + 1]:
                    for j in range((i + 1), 6):
                        start[j] = start[i]
                    #print(start)
                    if checkAjacent(start):
                        l.append(start.copy())
                    break
                #print(start)
                if checkAjacent(start):
                    l.append(start.copy())

            if start[i] < 9:
                start[i] += 1
                #print(start)
                if checkAjacent(start):
                    l.append(start.copy())
                break
            
            if start[i] == 9:
                start[i - 1] += 1

        if start[1] == 9:
            for j in range(1, 6):
                start[j] = start[0]
            if checkAjacent(start):
                if int(''.join(map(str, start))) <= end:
                    #print(start)
                    l.append(start.copy())

    return l


def partTwo(possiblePasswords):
    """
    """
    psw = possiblePasswords.copy()
    counter = 0
    
    for elm in possiblePasswords:
        tflag = False
        ind0 = 0
        ind1 = 0
        for i, j, k in zip(range(0, 4), range(1, 5), range(2, 6)):
            #print(f"elm i: {elm[i]}")
            #print(f"elm j: {elm[j]}")
            #print(f"elm k: {elm[k]}")
            if elm[i] == elm[j]:
                if elm[j] == elm[k]:
                    # tripple
                    tflag = True

                    # if i == 0 we still have to check the last three
                    if i == 0:
                        ind0 = k

                    # if i == 1 we still have to check the last two
                    if i == 1:
                        ind1 = k

                    # if i == 2 there is only one left and it cant be a pair - break and dump this element
                    if i == 2:
                        print(f"removing element : {elm}")
                        psw.remove(elm)
                        counter += 1
                        break
                elif not tflag:
                    # we have identified a double. this string is good no matter what
                    break
            elif tflag and i == ind0:
                if elm[i] == elm[j] and elm[j] == elm[k]:
                    #the last three match therefore we need to throw this out
                    print(f"removing element : {elm}")
                    psw.remove(elm)
                    counter += 1
                    break
            elif tflag and i == ind1:
                if elm[j] == elm[k]:
                    #this string will be good no matter what
                    pass
                else:
                    #string is garbage remove it
                    print(f"removing element : {elm}")
                    psw.remove(elm)
                    counter += 1
                    break
    
    # remove tripple tripples
    print('')
    print('removing tripple elements')
    print('')
    pswc = psw.copy()
    for elm in psw:
        if (elm[0] == elm[1] and elm[1] == elm[2]) and (elm[3] == elm[4] and elm[4] == elm[5]):
            print(f"removing element : {elm}")
            pswc.remove(elm)

        # tripple at the back
        if (elm[0] != elm[1] and elm[1] != elm[2]) and (elm[3] == elm[4] and elm[4] == elm[5]):
            print(f"removing element : {elm}")
            pswc.remove(elm)

        # tripple at the front
        if (elm[0] == elm[1] and elm[1] == elm[2]) and (elm[3] != elm[4] and elm[4] != elm[5]):
            print(f"removing element : {elm}")
            pswc.remove(elm)
    
    #print(counter)
    print(len(pswc))
    return pswc
            
            



password = partOne()
print(*password, sep="\n")
print(len(password))
print('')
print('')
updatedpass = partTwo(password)
# print(*updatedpass, sep="\n")

