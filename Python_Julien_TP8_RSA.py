import random
import math
#PYTHON JULIEN

#generateur de nb premiers
def primeGen(n):
    a = random.randint(2, n - 1) #genere nb aleatoire
    #print(a)
    b=a**(n-1)%n
    #print(b)
    if b != 1:#a pas premier
        #print("n pas premier")
        return 0
    else: 
        #print("n semble premier")
        return 1
    
#fonction exponentiation rapide
def fastExp(base,puiss,nbmod): #dans notre exemple, base=3,puiss=42,nbmod=25
    puiss = bin(puiss)[2:]
    temp = 1
    for i in range(len(puiss)-1,-1,-1):
        temp=(temp*base **int(puiss[i])) % nbmod
        base = (base ** 2) % nbmod
    return temp

#alg d'Euclide etendu
def etenduEuc(a,b):
    if b == 0:
        return a, 1, 0

    a1,b1,c1 = etenduEuc(b, a % b)
    a2 = a1
    b2 = c1
    c2 = b1 - math.floor(a/b) * c1
    return a2, b2, c2

#obtenir un nombre premier presque surement
def getAPseudoPrime():
    temp3=0
    while (temp3 == 0):
        n = random.randint(10**6, 10**7)#on peut changer ces valeurs selon la taille du premier souhaité
        #print(n)

        for k in range(1,100):
            j = random.randint(1,n-1)
            if (fastExp(j,n-1,n) != 1):#si pas un nombre premier, on arrête la boucle
                #print("stop pour j=",j)
                break
            else:#on a trouvé un nombre premier
                #print("premier trouvé :",n)
                temp3=1
                return n
                break
                
#calcule un nombre premier avec m
def getAPseudoPrimeWithm(m):
    temp3=0
    while (temp3 == 0):
        n = random.randint(2, m-1)#fonction de ci dussur adaptée à cette ligne pour avoir un nombre premier avec m
        #print(n)

        for k in range(1,100):
            j = random.randint(1,n-1)
            if (fastExp(j,n-1,n) != 1):
                break
            else:
                temp3=1
                return n
                break
                
#Thm des restes chinois
def thmRestesChin(a,b,p,q):
    temp=(a*q*(fastExp(q,p-2,p)) + b*p*(fastExp(p,p-2,q)))%(p*q) #mod p*q car toutes les solutions sont congrues à p*q
    return temp
                
#fonction le le 4ème bullet point de l'enoncé                
def pointQuatre():
    p=getAPseudoPrime()
    q=getAPseudoPrime()
    n=p*q
    phi_n = (p-1)*(q-1)
    e=getAPseudoPrimeWithm(phi_n)
    d=(etenduEuc(phi_n,e)[2]) % phi_n #TO CHECK
    return p,q,n,phi_n,e,d

#encryption du message
def encryption(n,e,message):
    cipher=fastExp(message,e,n)
    return cipher

#def decryption(atilda,btilda,p,q):
#    temp4=thmRestesChin(atilda,btilda,p,q)
#    return temp4


#REMARQUE: pour la decryption, je n'ai pas réussi à y faire fonctionner avec 
# le thm des restes chinois directement, mais voici une méthode similaire

#decryption du message
def decryption(p,q,c,d):
    atilda=fastExp(c,(d % (p-1)),p)
    btilda=fastExp(c,(d % (q-1)),q)
    h=fastExp(atilda-btilda,p-2,p)%p
    mess=btilda + h*q
    return mess
    
    
w=pointQuatre()
#print(w)
p=w[0]
q=w[1]
n=w[2]
phi_n=w[3]
e=w[4]
d=w[5]

message=123456
print("le message encrypté est :",message)
c = encryption(n,e,message)
print("le cipher est",c)

mess=decryption(p,q,c,d)
print("le message décrypté est :",mess)