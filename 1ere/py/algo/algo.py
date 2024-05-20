def recherche_min(l):
    min = l[0]
    for i in range(1, len(l)):
        if min > l[i]:
            min = l[i]
    l.remove(min)
    return min

def tri_naif(l):
    l_triee = [[recherche_min(l)]for i in range(len(l))]
    return l_triee

xA =float(input("xA"))
yA =float(input("yA"))
xB =float(input("xB"))
yB =float(input("yB"))
xC =float(input("xC"))
yC =float(input("yC"))
xD =float(input("xD"))
yD =float(input("yD"))


def colinéaires (xA,yA,xB,yB):
    if (xA*xB)-(yB*yA)==0:
        print("les vecteurs A et B sont colinéaires")
    else:
        print("les vecteurs A et B ne sont pas colinéaires")

def colinéaires (xC,yC,xD,yD):
    if (xC*xD)-(yD*yC)==0:
        print("les vecteurs C et D sont colinéaires")
    else:
        print("les vecteurs C et D ne sont pas colinéaires")

