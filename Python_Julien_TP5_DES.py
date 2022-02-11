IP = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]
IP_Inverse = [40,8,48,16,56,24,64,32,
              39,7,47,15,55,23,63,31,
              38,6,46,14,54,22,62,30,
              37,5,45,13,53,21,61,29,
              36,4,44,12,52,20,60,28,
              35,3,43,11,51,19,59,27,
              34,2,42,10,50,18,58,26,
              33,1,41,9,49,17,57,25]


PC_1 = [57,49,41,33,25,17,9,
        1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,
        19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,
        7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,
        21,13,5,28,20,12,4]
PC_2 = [14,17,11,24,1,5,
        3,28,15,6,21,10,
        23,19,12,4,26,8,
        16,7,27,20,13,2,
        41,52,31,37,47,55,
        30,40,51,45,33,48,
        44,49,39,56,34,53,
        46,42,50,36,29,32]

E = [32,1,2,3,4,5,
     4,5,6,7,8,9,
     8,9,10,11,12,13,
     12,13,14,15,16,17,
     16,17,18,19,20,21,
     20,21,22,23,24,25,
     24,25,26,27,28,29,
     28,29,30,31,32,1]
P = [16,7,20,21,
     29,12,28,17,
     1,15,23,26,
     5,18,31,10,
     2,8,24,14,
     32,27,3,9,
     19,13,30,6,
     22,11,4,25]

S_1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
       [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
       [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
       [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

S_2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
       [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
       [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
       [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

S_3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
       [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
       [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
       [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

S_4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
       [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
       [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
       [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

S_5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
       [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
       [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
       [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

S_6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
       [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
       [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
       [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

S_7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
       [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
       [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
       [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

S_8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
       [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
       [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
       [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

S_Boxes = [S_1,S_2,S_3,S_4,S_5,S_6,S_7,S_8]

Rotations = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def splitList(a_list): #sépare une liste paire en deux elmts de même taille
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

'''def addXor(a,b):#addition Xor pour hexadecimal
        s = []
    for i in range(0,len(A)):
        s.append
    
    return (hex(b ^ a)) '''

def addXor(A, B): #XOR entre deux elements
    s = []
    for i in range(0,len(A)):
        s.append(A[i] ^ B[i])
    return s

'''def perm (bloc,table):#permute un bloc en fonction d'une table
    a=[]
    for x in table:
        a.append(bloc[x-1])
    return(a)'''

def perm (bloc,table):#permute un bloc en fonction d'une table
    l = [None] * len(table)
    j=0
    for x in table:
        #print(x)
        l[j]=bloc[x-1]
        j+=1
    return(l)

def revDict(oldDict): #renverse l'ordre d'un dico plein à partir du zéro jusqu'à n
    m={}
    taille=len(oldDict)
    j=0
    for x in oldDict:
        m[taille-j]=oldDict[j]
        j+=1
    return m

def binRot(liste): #rotation binaire pour cle 1 sur la gauche
    b=[]
    
    for i in range(0,len(liste)-1):
        b.append(liste[i+1])
    b.append(liste[0])
    return b

def binRot2Bits(liste): #rotation binaire pour cle 2 sur la gauche
    b=[]
    
    for i in range(0,len(liste)-2):
        b.append(liste[i+2])
    b.append(liste[0])
    b.append(liste[1])
    return b

def DES (message,key): #progr DES
    K_apres_perm=perm(key,PC_1)
    M_apres_perm=perm(message,IP)#IP au message
    L={}#dicos
    R={}
    L[0],R[0]=splitList(M_apres_perm)#message séparé
    LK={}
    RK={}
    LK[0],RK[0]=splitList(K_apres_perm)
    SubKey={}
    #encryption------------------------------------------------
    j=1
    for i in range (0,15):#ie i=0..14
        #Binary rotation
        if i in [0,1,8]:
            LK[i+1]=binRot(LK[i])
            RK[i+1]=binRot(RK[i])
        else:
            LK[i+1]=binRot2Bits(LK[i])
            RK[i+1]=binRot2Bits(RK[i])    
            
        SubKey[i+1]=perm(LK[i+1]+RK[i+1],PC_2) 
        
        L[i+1]=R[i]
        R[i+1]=addXor(L[i],Cipher(R[i],SubKey[i+1]))
        
    #pour la decryption------------------------------------------     
    '''    for i in range (0,15):#ie i=0..14
        #Binary rotation
        if i in [0,1,8]:
            LK[i+1]=binRot(LK[i])
            RK[i+1]=binRot(RK[i])
        else:
            LK[i+1]=binRot2Bits(LK[i])
            RK[i+1]=binRot2Bits(RK[i])    
            
        SubKey[i+1]=perm(LK[i+1]+RK[i+1],PC_2) 
        
    LK[16]=binRot(LK[15])
    RK[16]=binRot(RK[15])    
    SubKey[16]=perm(LK[16]+RK[16],PC_2)    
    
    
    for i in range (0,15):
        
        L[i+1]=R[i]
        R[i+1]=addXor(L[i],Cipher(R[i],SubKey[16-i]))
        
    L[16]=addXor(L[15],Cipher(R[15],SubKey[1]))
    R[16]=R[15] '''   
    #--------------------------------------------------------------
    #16ème étape
    #print("R15",R[15])
    #print("L15",L[15])
    
    #print("Cipher resul",Cipher(L[15],SubKey[15]))
    
    #On sépare la dernière opération de la boucle car différente
    LK[16]=binRot(LK[15])
    RK[16]=binRot(RK[15])    
    SubKey[16]=perm(LK[16]+RK[16],PC_2)

    L[16]=addXor(L[15],Cipher(R[15],SubKey[16]))
    R[16]=R[15]
    
    #final permutation
    return perm(L[16]+R[16],IP_Inverse)

#------------------------------------------------

def splitListIn8(a_list): #sépare une liste de 48 elmts en 8 listes
    return a_list[0:6], a_list[6:12],a_list[12:18],a_list[18:24],a_list[24:30],a_list[30:36],a_list[36:42],a_list[42:48]


def Cipher(RH,SubKey):#Cipher
    #1)
    #print("ceci est RH", RH)
    a=[None] * len(RH)
    a=perm(RH,E)
    
    #2)
    c=addXor(a,SubKey)
    
    #3)
    b={}
    b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]=splitListIn8(c)
    ligne={}
    col={}
    valBin=[]
    d={}
    e={}
    t={}
    s={}
    
    for i in range(1,9):#ie i=1..8      
        d[i]=[]
        d[i].append(b[i][0%6])#en fait pas forcement besoin du modulo..
        d[i].append(b[i][5%6])
        ligne[i]=int(''.join(map(str, d[i])),2) #transfo bin en entier
        
        e[i]=[]
        e[i].append(b[i][1%6])
        e[i].append(b[i][2%6])
        e[i].append(b[i][3%6])
        e[i].append(b[i][4%6])
        col[i]=int(''.join(map(str, e[i])),2)
        
        t[i]= S_Boxes[i-1][ligne[i]][col[i]] #va chercher val ds S_box
        
        s[i]= '{:04b}'.format(t[i]) #transfo binaire à 4 caract.
        
        valBin.append(s[i])#toutes nos val bin
    #print(ligne)
    #print("t est",t)
    #print(s)
    #print(valBin)
    
    resultBin=''.join(map(str, valBin))
    
    w=[]
    for x in resultBin: 
        w.append(x)
        
    for i in range(0, len(w)): # trick pour passer de '011100' à [0,1,1,1,0,0]
        w[i] = int(w[i]) 
        
    #print("resultbin",resultBin)
    #print("P est",P)
    #print(w)
    return perm(w,P)


message_test = list(map(int,list(format(0x0011223344556677, '0>64b'))))
cle_test = list(map(int,list(format(0x0123456789ABCDEF, '0>64b'))))

ResultFin=DES(message_test,cle_test)

#print(ResultFin)

cipher_lisible = hex(int("".join(str(x) for x in ResultFin),2))

print(cipher_lisible)

if cipher_lisible == "0xcadb6782ee2b4823":
    print("gagne")
else:
    print("perdu")
