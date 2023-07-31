
def arithmetic_arranger(list, want_res = False):

    if len(list) > 5:
        print("Error: Too many problems.")
        return 
    
    line1 = []
    line2 = []
    operator = []
    dashes = []
    sumi = []

    for item in list:
        tonum = item.split(" ")
        line1.append(tonum[0])
        operator.append(tonum[1])
        line2.append(tonum[2])

    for item in operator:
        if item != '+' and item != '-':
            print("Error: Operator must be '+' or '-'.")
            return
        
    j = 0
    while j < len(line1):
        if operator[j] == '+':
            s = int(line1[j]) + int(line2[j])
            sumi.append(str(s))

        if operator[j] == '-':
            s = int(line1[j]) - int(line2[j])
            sumi.append(str(s))
        j = j + 1

    i = 0
    while i < len(line1):
        digits1 = len(line1[i])
        digits2 = len(line2[i])
        digits3 = len(sumi[i])

        if line1[i].isdigit() == False or line2[i].isdigit() == False:
            print("Error: Numbers must only contain digits.")
            return  

        if digits1 > 4 or digits2 > 4:
            print("Error: Numbers cannot be more than four digits.")
            return
        
        if digits1 > digits2:
            higher = digits1
            spaces1 = ' ' * 2
            spaces2 = ' ' * (digits1 - digits2 + 1)
            line1[i] = f"{spaces1}{line1[i]}"
            line2[i] = f"{spaces2}{line2[i]}"
            dashes.append("-" * (digits1 + 2))
        else:
            higher = digits2
            spaces1 = ' ' * (digits2 + 2 - digits1)
            spaces2 = ' '
            line1[i] = f"{spaces1}{line1[i]}"
            line2[i] = f"{spaces2}{line2[i]}"
            dashes.append("-" * (digits2 + 2))

        line2[i] = f"{operator[i]}{line2[i]}"

        if digits3 > higher:
            spaces3 = " "
            sumi[i] = f"{spaces3}{sumi[i]}"
        else:         
            spaces3 = " " * (higher - digits3 + 2 )
            sumi[i] = f"{spaces3}{sumi[i]}"
        i = i + 1 
    
    a = "    ".join(line1)
    b = "    ".join(line2)
    c = "    ".join(dashes)
    
    print(a)
    print(b)
    print(c)
    if want_res == True:
        d = "    ".join(sumi)
        print(d)

    return


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)




