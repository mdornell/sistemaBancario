def menu() :
    op = -1
    while op < 0 or op > 6:
        print("Sistema Bancário:")
        print("1-Inserir conta")
        print("2-Pesquisar por conta")
        print("3-Depositar")
        print("4-Maior saldo")
        print("5-Excluir conta")
        print("6-Listar")
        print("0-Sair")
        op = int(input("Escolha sua opção: "))
    return op
  
def inserir(contas,saldoConta):
    valConta = False
    conta = input("Insira o número da conta : ")
    while conta.isdigit() == False :
        print("Valor Invalido !!")
        conta = input("Insira o número da conta : ")
        if conta.isdigit() == True and int(conta) <= 0 :
            print("Número Invalido !!")
            conta = input("Insira o número da conta : ")

    conta = int(conta)
    for e in contas:
        if conta == e:
            print("Conta já existe !!")
            valConta = True
        
    if valConta == False:
        contas.append(int(conta))
        saldoConta.append(0)
        

    

def pesqConta(contas,pesq):
    for pos,e in enumerate(contas):
        if e == pesq :
            return pos
    return -1
    
def maiorSaldo(contas,saldoConta):
    maior = 0
    for pos,e in enumerate(contas):
        if saldoConta[pos] > maior :
            maior = saldoConta[pos]
            conta = e
    print("Conta: %d  Saldo: R$%.2f " %(conta,maior))

def lista(contas,saldos):
    print("CONTAS/SALDO")
    for pos,e in enumerate(contas):
        print("%d  /  R$%.2f" %(contas[pos],saldos[pos]))
        
        

###### PRINCIPAL ##########
#Variaveis Gerais
numConta = []
saldoConta = []

op = 1
while op != 0:
    op = menu()
    
    if op == 0:
        print("\n\nFim do programa!!!\n\n")
        
    elif op == 1:
        print("\n\nINSERIR CONTA\n\n")
        # Chamar a função para Inserir os dados nos vetores
        inserir(numConta,saldoConta)
        
        
    elif op == 2:
        print("\n\nPESQUISAR CONTA\n\n")
        # Ler a informação para pesquisar
        pesq = int(input("Insira o número da conta : "))
        # Chamar a função para pesquisar no vetor
        pos = pesqConta(numConta,pesq)
        # Imprimir os dados se encontrar
        if pos >= 0 :
            print("Conta: %d  Saldo: R$%.2f " %(numConta[pos],saldoConta[pos]))
        else:
            print("Nunhuma conta encontrada!!")



    elif op == 3:
        print("\n\nDEPOSITAR\n\n")
        # Ler a informação para pesquisar
        pesq = int(input("Insira o número da conta : "))
        deposito = float(input("Insira o valor a depositar :"))
        # Chamar a função para pesquisar no vetor
        pos = pesqConta(numConta,pesq)
        # Se encontrar, então soma o deposito no saldo.
        if pos >=0 :
            saldoConta[pos] += deposito
        else :
            print("Nunhuma conta encontrada!!")


    elif op == 4:
        print("\n\nMAIOR SALDO\n\n")
        # Chamar a função para pesquisar no vetor o maior elemento
        maiorSaldo(numConta,saldoConta)



    elif op == 5:
        print("\n\nEXCLUIR CONTA\n\n")
        # Ler a informação para pesquisar
        pesq = int(input("Insira o número da conta : "))
        # Chamar a função para pesquisar no vetor
        pos = pesqConta(numConta,pesq)
        # Excluir a posição pesquisada, se encontrar
        if pos >= 0 :
            del numConta[pos]
            del saldoConta[pos]
        else :
            print("Nenhuma conta encontrada!!")


    elif op == 6:
        print("\n\nLISTAR\n\n")
        # Listar todos os dados dos vetores
        lista(numConta,saldoConta)


    else:
        print("Opção inválida!")

    input("Pressione <enter> para continuar ...")
    




        