def RendueMonnaie(A):
    """input: nombre entier qu'il faut rendre (A)
    output: Liste des pièces à rendre (LF)"""
    L = [1,2,5,10,20,50,100,200]
    Lf = []
    i = len(L) - 1
    while A > 0:
        if A >= L[i]:
            A -= L[i]
            Lf.append(L[i])
        else:
            i -= 1

    return Lf

