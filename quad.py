def abrir(nome):
    teste=open(nome,'r')
    final_arquivo = False
    string_vazia = ''
    m=0
    while not final_arquivo:
        linha = teste.readline()
        if linha == string_vazia:
            final_arquivo = True
        else:
            time = linha.split(' ')
            if m==0:
                p=int(time[0])
                n=[0]*(p**2)
                m+=1
            else:
                for i in range(p):
                    n[i+p*(m-1)]=time[i]
                m+=1
    teste.close()
    return n,p
def imprime(matriz,p):
    for k in range(p**2):
        print("",matriz[k],end = '')
def checar(matriz,p):
    soma=0
    n=0
    m=0
    for i in range(p):
        soma+=int(matriz[i])
    #linhas
    for i in range(p):
        for k in range(p):
            n+=int(matriz[k+p*i])
        if n==soma:
            n=0
        else:
            return False
    #diagonal esquerda > direita
    for i in range(p):
        n+=int(matriz[i+p])
    if n==soma:
        n=0
    else:
        return False
    #diagonal direita > esquerda
    for i in range(p-1,-1,-1):
        n+=int(matriz[i+p])
    if n==soma:
        n=0
    else:
        return False
    #colunas
    for i in range(p):
        for k in range(p):
            n+=int(matriz[(m+i)+(p*k)])
        if n==soma:
            n=0
        else:
            return False
    return True
def menu():
    print("ATENÇÃO VERIFIQUE SE A MATRIZ É APENAS SEPARADA POR 1 ESPAÇO (' ') SENÃO NÃO FUNCIONA")
    aa=str(input("nome do arquvo com .txt: "))
    n=abrir(aa)
    a=n[0]
    b=n[1]
    imprime(a,b)
    m=checar(a,b)
    if m == False:
        print('\n',"Não é quadrado magico")
    else:
        print('\n',"É um quadrado magico")
menu()
