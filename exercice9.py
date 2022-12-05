# La fonction de puissance
def puissance(X,n):
    power = 1
    for i in range(n):
        power *= X
    return power

# La fonction de la somme des elements
def sumOfElements(list):
    sum = 0
    for i in list:
     sum += i
       
# La fonction qui renoie une list triee
def bubbleSort(list):
    for i in range(len(list) -1):
        for j in range(len(list) -1):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list           

# La fonction qui renvoie la moyenne arithmetique
def moyenne(list):
    sum = 0
    for i in list:
     sum += i
    return sum / len(list)

# La fonction qui renvoie min ou max selon le choix de l'utilisateur
def max0rmin(liste,choix):
    if(choix == "min"):
        min = list[0]
        for i in range(1,len(list)):
            if(min > list[i]):
                min = list[i]
        return min
    elif(choix == "max"):
        max = list[0]
        for i in range(1,len(list)):
            if(max < list[i]):
                max = list[i]
        return max
    else:
        return "le choix n'est pas correcte" 

# La fonction qui renvoie qui renvoie la median d'une liste
def median(list):
    sort = bubbleSort(list)  

    if(len(list)%2 == 0):
        res1 = sort[len(sort)//2-1]
        res2 = sort[len(sort)//2]
        return (res1 + res2) / 2
    else:
        return sort[len(sort)//2]

# La fonction qui renvoie le mode d'une list
def mode(list):
    return max0rmin(list,"max")

# La fonction qui renvoie la variance d'une list
def variance(list):
    sum = 0
    for i in list: 
        sum += puissance(i,2)  
    return sum/len(list) - puissance(moyenne(list),2)                    