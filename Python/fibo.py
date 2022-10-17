""" Fibo Function
# {int} n0: 1er élément parcouru
# {int} n1: 2ème élément parcouru
# {int} c: compteur, qui nous permettre de nous arrêter
"""
def fibo(n0, n1, c, stop):
    if(n0 < 1): print(str(n0), end=",")
    if(c < stop):
        print(str(n1), end=",")
        return(fibo(n1, n0+n1, c+1, stop))


#fibo(0,1,0, stop = 2)

def fiboWithWhile():
    n0 = 0; n1 = 1; nInter = 0
    c = 0
    print(str(n0), end=",")
    while c < 8:
        print(str(n1), end=",")
        nInter = n0;
        n0 = n1;
        n1 = nInter+n1;
        c += 1;

fiboWithWhile()