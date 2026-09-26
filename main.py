import random
from conta import Pessoa
import time

accounts = []

def menu():
    print("1 - criar conta")
    print("2 - depositar")
    print("3 - sacar")
    print("4 - Consultar saldo")
    print("5 - listar contas")
    print("6 - transferir")
    print("7 - sair")
    

def new_account():
    number_account = ""
    
    for i in range(6):
        number_account += str(random.randint(0, 9))
    
    print("Enter your name: ")
    name = input("> ")

    conta = Pessoa(name, number_account, 0)
    
    accounts.append(conta)
    
    print("Conta criada com sucesso!!")
    print(f"numero: {number_account}" )
    print(f"saldo: {conta.saldo}")
    

def deposit():
    print("Numero da conta: ")
    n = str(input("> "))
    
    print("Quanto deseja depositar: ")
    d = float(input("> "))
    
    for a in accounts:
        print("Conta encontrada na lista:", a.numero)
        
    encontrou = False

    for a in accounts:
        if n == a.numero:
          a.depositar(d)
          print(f"Saldo atual: {a.saldo}")
          encontrou = True

    if not encontrou:
        print("Conta inexistente!")
        
def saque():
        print("Digite o numero da conta: ")
        n = str(input("> "))
        
        print("Quanto deseja sacar: ")
        s = float(input("> "))
        
        print("Procurando...")
        time.sleep(1.5)
        
        encontrada = False
        for a in accounts:
            if n == a.numero: 
                print("Conta encontrada!!")
                print("Titular: " + a.titular)
                time.sleep(1)
                print("sacando...")
                time.sleep
                if s > a.saldo or s < 0 :
                    print("Erro ao sacar saldo insuficiente!")
                print("Saque concluido com sucesso!")
                a.sacar(s)
                print(f"saldo atual: {a.saldo}" )
                encontrada = True

def show_accounts():
    print("=============ACCOUNTS============")
    for a in accounts:
        print(f"Titular: {a.titular}")
        print(f"N° da conta: {a.numero}")
        print(f"saldo: {a.saldo}")
        

def consultar_saldo():
    print("Digite o numero da conta: ")
    n = str(input("> "))
    
    print("Procurando...")
    time.sleep(1.5)
    encontrada = False
    for a in accounts:
        if n == a.numero:
            print("Encontrado!!")
            time.sleep(1)
            
            print("titular: " + a.titular)
            print("saldo: " + str(a.consultar_saldo()))            
            encontrada = True
        else:
            print("Conta inexitente!")
            
            
def transferir():
    print("Digite a conta de origem: ")
    conta_origem = str(input("> "))
    print("Digite a conta de destino: ")
    conta_destino = str(input("> "))
    print("Digite o valor da transferencia: ")
    quantidade_dinheiro = float(input("> "))
    
    encontrado_origem = False
    encontrado_destino = False
    
    print("Procurando contas...")
    time.sleep(2)
    
    for a in accounts:
        if conta_origem == a.numero: 
            print("Encontrado conta de origem!")
            a.saldo -= quantidade_dinheiro
            encontrado_origem = True

        if not encontrado_origem:
           print("Conta inexistente")
           
        if conta_destino == a.numero:
            print("Encontrado conta destino")
            encontrado_destino = True
            print("Transferindo....")
            time.sleep(1.5)
            a.saldo += quantidade_dinheiro
        if not encontrado_destino:
            print("Conta inexistente")
        


while True:
    menu()
    r = int(input("> "))
    
    match r:
        case 1:
            new_account()
        case 2:
            deposit()
        case 3:
            saque()
        case 4:
            consultar_saldo()
        case 5:
            show_accounts()           
        case 6:
            transferir()
        case 7:
            exit 
        case _:
            print("erro")
        
            
            
            
            
            
            
            