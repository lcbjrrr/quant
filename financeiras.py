def juros_simples(aporte,taxa,nper):
    total = aporte + aporte * taxa * nper
    return total
 

def juros_compostos(aporte,taxa,nper):
    total= aporte
    for i in range (0,nper,1):
        total = total * (1+taxa)
    return total

 


def valor_futuro(vp, pgto,n,i):
    vf = vp
    for j in range(0,n,1):
        vf = vf*(1+i) + pgto
    return vf

def vp(vf,n,i):
    presente = vf
    for j in range(0,n,1):
        presente = presente / (1+i) 
    return presente

 

def parcelas_presente(vf,n,i):
    soma=0
    for j in range(1,n+1,1):
        pp = vp(vf,j,i)
        soma = soma+pp
    return soma

erro_p = 0.005
inc = 0.0025
def taxa(vp,pgto,n):
    erro = vp*erro_p
    juros_base = ((n*pgto/vp)-1)/n
    juros = juros_base
    presente = parcelas_presente(pgto,n,juros)
    while(presente < vp-erro or presente > vp+erro ):
        juros = juros +inc
        presente = parcelas_presente(pgto,n,juros)
    print(presente)
    return juros

def raiz(a,b,c):
    delta = b**2 - 4*a*c
    r1 = (-b + delta**(1/2))/(2*a)
    r2 = (-b - delta**(1/2))/(2*a)
    return (r1,r2)


def rate(vp,pgto):
    i1,i2 = raiz(vp,(2*vp-pgto),(vp-2*pgto))
    if i1 > 0:
        return i1
    else:    
        return i2
    
    

from math import log

def nper(vf,vp,i):
    n = log(vf/vp) / log(1+ i)
    return n


def pgto(vp,i):
    p = (vp*i**2 +2*vp*i + vp)/(2+i)
    return p


def ipca_tri(ipca):
    tri=[]
    for i in range(0,4,1):
        base=1
        for j in range(0,3,1):
            base=base*(1+ipca[i+j]/100)
        tri.append((base-1)*100)
    return tri



def tri(des):
    tri=[]
    for i in range(0,4,1):
        base=0
        for j in range(0,3,1):
            base=base+des[i+j]
        tri.append(base/3)
    return tri


def max(nums):
    maior = 0
    for i in range(0,len(nums),1):
        if(nums[i]>maior):
            maior = nums[i]
    return maior

def maximo(covid):
    maxs = []
    for i in range(0,len(covid),7):
        mm = max(covid[i:i+7])
        maxs.append(mm)
    return maxs



def corrige_pib(pib, infs):
    real = pib
    for i in range(0,len(infs),1):
        real = real *(1+infs[i]/100)
    return real

def pib_real(pibs, infs):
    reais = [pibs[0]]
    for i in range(1,len(pibs),1):
        pib = corrige_pib(pibs[i], infs[:i])
        reais.append(pib)
    return reais



def raiz(a,b,c):
    delta = b**2 - 4*a*c
    r1 = (-b + delta**(1/2))/(2*a)
    r2 = (-b - delta**(1/2))/(2*a)
    return (r1,r2)


def tir(x,y,z):
    i1,i2 = raiz(x,(2*x-y),(x-y-z))
    if i1 > 0:
        return i1
    else:    
        return i2


