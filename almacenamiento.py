def maximizar(As, D):
    As=sorted(As, key=lambda t: t[1])
    l=[]
    suma=0
    for i in range(len(As)):
        suma+=As[i][1]
        if(suma<=D):
            l+=[As[i]]
        else:
            break
    return l