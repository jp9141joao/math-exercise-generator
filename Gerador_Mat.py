import time 
import random
import os
import math

def Soma(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0
    if Qntd <=0:
        print('Quantidade invalida!')
        return 

    if Dificuldade == 1: 
        for i in range(0,Qntd,1):
            X = random.randint(1,100)
            Y = random.randint(1,100)
            Perg = int(input(f'{i+1}) {X} + {Y} = '))
            while Perg != X+Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} + {Y} = '))
            
            print('Resposta Correta!')
        
        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(0,Qntd,1):
            X = random.randint(10,1000)
            Y = random.randint(10,100)
            Perg = int(input(f'{i+1}) {X} + {Y} = '))
            while Perg != X+Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} + {Y} = '))
            
            print('Resposta Correta!')
        
        print(f'Quantidade de Erros: {Tentativas}')

    elif Dificuldade == 3:
        for i in range(0,Qntd,1):
            X = random.randint(1000,10000)
            Y = random.randint(1000,10000)
            Perg = int(input(f'{i+1}) {X} + {Y} = '))
            while Perg != X+Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} + {Y} = '))
            
            print('Resposta Correta!')
        
        print(f'Quantidade de Erros: {Tentativas}')
    
    else:
        print('Dificuldade Invalida!')

    time.sleep(5)

def Subtracao(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0
    if Qntd <= 0: 
        print('Quantidade invalida!')
        return

    if Dificuldade == 1:
        for i in range(0,Qntd,1):
            X = random.randint(1,100)
            Y = random.randint(1,100)
            if X > Y:
                Perg = int(input(f'{i+1}) {X} - {Y} = '))
                while Perg != X-Y:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {X} - {Y} = '))
            else:
                Perg = int(input(f'{i+1}) {Y} - {X} = '))
                while Perg != Y-X:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {Y} - {X} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(0,Qntd,1):
            X = random.randint(10,1000)
            Y = random.randint(10,1000)
            if X > Y:
                Perg = int(input(f'{i+1}) {X} - {Y} = '))
                while Perg != X-Y:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {X} - {Y} = '))
            else:
                Perg = int(input(f'{i+1}) {Y} - {X} = '))
                while Perg != Y-X:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {Y} - {X} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for i in range(0,Qntd,1):
            X = random.randint(1000,10000)
            Y = random.randint(1000,10000)
            if X > Y:
                Perg = int(input(f'{i+1}) {X} - {Y} = '))
                while Perg != X-Y:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {X} - {Y} = '))
            else:
                Perg = int(input(f'{i+1}) {Y} - {X} = '))
                while Perg != Y-X:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = int(input(f'{i+1}) {Y} - {X} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')

    else:
        print(f'Dificuldade Invalida!')

    time.sleep(5)
    
def Multiplicacao(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0
    if Qntd <= 0: 
        print('Quantidade invalida!')
        return

    if Dificuldade == 1:
        for i in range(0,Qntd,1):
            X = random.randint(1,50)
            Y = random.randint(1,50 )

            Perg = int(input(f'{i+1}) {X} X {Y} = '))
            while Perg != X*Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} X {Y} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')

    elif Dificuldade == 2:
        for i in range(0,Qntd,1):
            X = random.randint(10,100)
            Y = random.randint(10,100 )

            Perg = int(input(f'{i+1}) {X} X {Y} = '))
            while Perg != X*Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} X {Y} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')

    elif Dificuldade == 3:
        for i in range(0,Qntd,1):
            X = random.randint(100,1000)
            Y = random.randint(100,1000 )

            Perg = int(input(f'{i+1}) {X} X {Y} = '))
            while Perg != X*Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = int(input(f'{i+1}) {X} X {Y} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    else: 
        print(f'Dificuldade Invalida!')
    
    time.sleep(5)  
    
def Divisao(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return

    if Dificuldade == 1:

        for i in range(Qntd):
            X = random.randint(1,100)
            Y = random.randint(1,20)

            while X % Y != 0:
                X = random.randint(1,1000)
                Y = random.randint(1,100)

            Perg = float(input(f'{i+1}) {X} / {Y} = '))

            while Perg != X/Y:
                Tentativas += 1
                print('Resposta Incorreta!')
                Perg = float(input(f'{i+1}) {X} / {Y} = '))

            print('Resposta Correta!')
        
        print(f'Quantidade de Erros: {Tentativas}')

    elif Dificuldade == 2:

        for i in range(Qntd):
            X = random.randint(1,100)
            Y = random.randint(1,100)

            if X > Y:
                Perg = float(input(f'{i+1}) {X} / {Y} = '))

                while round(Perg,2) != round(X/Y):
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = float(input(f'{i+1}) {X} / {Y} = '))
            else:
                Perg = float(input(f'{i+1}) {Y} / {X} = '))

                while round(Perg,2) != round(Y/X,2):
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = float(input(f'{i+1}) {Y} / {X} = '))

            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')

    elif Dificuldade == 3:
        for i in range(Qntd):
            X = random.randint(100,1000)
            Y = random.randint(100,1000)

            if X > Y:
                Perg = float(input(f'{i+1}) {X} / {Y} = '))

                while round(Perg,2) != round(X/Y,2):
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = float(input(f'{i+1}) {X} / {Y} = '))
            
            else:
                Perg = float(input(f'{i+1}) {Y} / {X} = '))

                while round(Perg,2) != round(Y/X,2):
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Perg = float(input(f'{i+1}) {Y} / {X} = '))

            print('Resposta Correta!')
        
        print(f'Quantidade de Erros: {Tentativas}')

    else:
        print('Dificuldade Invalida!')

    time.sleep(5)  

def Matriz(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return

    Mat = []
    SomaL = []
    SomaC = []

    if Dificuldade == 1:
        for q in range(Qntd):
            for i in range(0,5,1):
                Mat.append([])
                for j in range(0,5,1):
                    Mat[i].append(random.randint(10,99))
                    print(f'{Mat[i][j]}',end=' ')
                print()

            print()

            for i in range(0,5,1):
                Soma = 0
                for j in range(0,5,1):
                    Soma += Mat[i][j]
                SomaL.append(Soma)
            
            for i in range(0,5,1):
                Soma = 0
                for j in range(0,5,1):
                    Soma += Mat[j][i]
                SomaC.append(Soma)

            for i in range(0,5,1):
                Resp = int(input(f'{i+1}) Digite a soma da {i+1}° linha: '))
                while Resp != SomaL[i]:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Resp = int(input(f'{i+1}) Digite a soma da {i+1}° linha: '))
                
                print('Resposta Correta!')

            for i in range(0,5,1):
                Resp = int(input(f'{i+1}) Digite a soma da {i+1}° coluna: '))
                while Resp != SomaC[i]:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Resp = int(input(f'{i+1}) Digite a soma da {i+1}° coluna: '))
                
                print('Resposta Correta!')

            print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for q in range(Qntd):
            for i in range(0,8,1):
                Mat.append([])
                for j in range(0,8,1):
                    Mat[i].append(random.randint(10,99))
                    print(f'{Mat[i][j]}',end=' ')
                print()
            print()

            for i in range(0,8,1):
                Soma = 0
                for j in range(0,8,1):
                    Soma += Mat[i][j]
                SomaL.append(Soma)
            
            for i in range(0,8,1):
                Soma = 0
                for j in range(0,8,1):
                    Soma += Mat[j][i]
                SomaC.append(Soma)

            for i in range(0,8,1):
                Resp = int(input(f'Digite a soma da {i+1}° coluna: '))
                while Resp != SomaL[i]:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Resp = int(input(f'Digite a soma da {i+1}° coluna: '))
                
                print('Resposta Correta!')

            print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for q in range(Qntd):
            for i in range(0,8,1):
                Mat.append([])
                for j in range(0,8,1):
                    Mat[i].append(random.randint(100,999))
                    print(f'{Mat[i][j]}',end=' ')
                print()
            print()

            for i in range(0,8,1):
                Soma = 0
                for j in range(0,8,1):
                    Soma += Mat[i][j]
                SomaL.append(Soma)
            
            for i in range(0,8,1):
                Soma = 0
                for j in range(0,8,1):
                    Soma += Mat[j][i]
                SomaC.append(Soma)

            for i in range(0,8,1):
                Resp = int(input(f'Digite a soma da {i+1}° coluna: '))
                while Resp != SomaL[i]:
                    Tentativas += 1
                    print('Resposta Incorreta!')
                    Resp = int(input(f'Digite a soma da {i+1}° coluna: '))
                
                print('Resposta Correta!')

            print(f'Quantidade de Erros: {Tentativas}')
    
    else:
        print('Dificuldade Invalida!')

    time.sleep(5)

def Raiz(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return

    
    if Dificuldade == 1:
        for i in range(Qntd):
            A = random.randint(1,50)
            while math.sqrt(A)%1 != 0:
                A = random.randint(1,50)
            
            Resp = int(input(f'{i+1}) √{A} = '))
            while Resp != math.sqrt(A):
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) √{A} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(Qntd):
            A = random.randint(10,200)
            while math.sqrt(A)%1 != 0:
                A = random.randint(10,200)    
            
            Resp = int(input(f'{i+1}) √{A} = '))
            while Resp != math.sqrt(A):
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) √{A} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for i in range(Qntd):
            A = random.randint(50,1000)
            while math.sqrt(A)%1 != 0:
                A = random.randint(50,1000)
            
            Resp = int(input(f'{i+1}) √{A} = '))
            while Resp != math.sqrt(A):
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) √{A} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')

    else: 
        print('Dificuldade Invalida!')
    
    time.sleep(5)

def Exponenciacao(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return

    
    if Dificuldade == 1:
        for i in range(Qntd):
            A = random.randint(1,50)
            B = random.randint(1,10)
            Resp = int(input(f'{i+1}) {A} elevado a {B} = '))

            while Resp != A**B:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A} elevado a {B} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(Qntd):
            A = random.randint(10,100)
            B = random.randint(5,20)
            Resp = int(input(f'{i+1}) {A} elevado a {B} = '))

            while Resp != A**B:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A} elevado a {B} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for i in range(Qntd):
            A = random.randint(10,500)
            B = random.randint(10,30)
            Resp = int(input(f'{i+1}) {A} elevado a {B} = '))

            while Resp != A**B:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A} elevado a {B} = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    else: 
        print('Dificuldade Invalida!')
    
    time.sleep(5)

def Fatoracao(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return
    
    if Dificuldade == 1:
        for i in range(Qntd):
            A = random.randint(1,10)
            Resp = int(input(f'{i+1}) {A}! = '))

            Result = A
            for i in range(1,A):
                Result = Result * i

            while Resp != Result:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A}! = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(Qntd):
            A = random.randint(5,12)
            Resp = int(input(f'{i+1}) {A}! = '))

            Result = A
            for i in range(1,A):
                Result = Result * i

            while Resp != Result:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A}! = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for i in range(Qntd):
            A = random.randint(8,15)
            Resp = int(input(f'{i+1}) {A}! = '))

            Result = A
            for i in range(1,A):
                Result = Result * i

            while Resp != Result:
                print('Resposta Incorreta!')
                Resp = int(input(f'{i+1}) {A}! = '))
                Tentativas += 1
        
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    else: 
        print('Dificuldade Invalida!')
    
    time.sleep(5)

def Equacao1(Qntd,Dificuldade):
    os.system('cls')
    Tentativas = 0

    if Qntd <= 0:
        print('Quantidade invalida!')
        return
    
    if Dificuldade == 1:
        for i in range(Qntd):

            while True:
                A = random.randint(1,10)
                B = random.randint(1,20)
                if A%2==0 and B%2==0:
                    break

            Opcao = random.randint(1,2)

            if Opcao == 1:
                Resp = float(input(f'{i+1}) {A}X + {B}  = '))
                Result = (-B)/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}X + {B}  = '))
                    Tentativas += 1
            else:
                Resp = float(input(f'{i+1}) {A}X - {B} = '))
                Result = B/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}X - {B}  = '))
                    Tentativas += 1
            
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 2:
        for i in range(Qntd):

            while True:
                A = random.randint(1,10)
                B = random.randint(1,20)
                if A%2==0 and B%2==0:
                    break

            Opcao = random.randint(1,2)

            if Opcao == 1:
                Resp = float(input(f'{i+1}) {A}x + {B} ='))
                Result = (-B)/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}x + {B}  = '))
                    Tentativas += 1
            else:
                Resp = float(input(f'{i+1}) {A}x - {B} = '))
                Result = B/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}x - {B}  = '))
                    Tentativas += 1
            
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    elif Dificuldade == 3:
        for i in range(Qntd):

            while True:
                A = random.randint(1,10)
                B = random.randint(1,20)
                if A%2==0 and B%2==0:
                    break

            Opcao = random.randint(1,2)

            if Opcao == 1:
                Resp = float(input(f'{i+1}) {A}x + {B}  = '))
                Result = (-B)/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}x + {B}  = '))
                    Tentativas += 1
            else:
                Resp = float(input(f'{i+1}) {A}x - {B} = '))
                Result = B/A
                Result = round(Result,2)

                while Resp != Result:
                    print('Resposta Incorreta!')
                    Resp = float(input(f'{i+1}) {A}x - {B}  = '))
                    Tentativas += 1
            
            print('Resposta Correta!')

        print(f'Quantidade de Erros: {Tentativas}')
    
    else: 
        print('Dificuldade Invalida!')
    
    time.sleep(5)

while True:
    os.system('cls')
    Opcao = int(input('*Menu de Opção*\n1- Treinar Soma\n2- Treinar Subtração\n3- Treinar Multiplicação\n4- Treinar Divisão\n5- Treinar a soma dos elementos de uma Matriz\n6- Treinar Raiz Quadrada\n7- Treinar Exponenciação\n8- Treinar Fatoração\n9- Treinar Equação de 1° grau\n10- Imprimir Lista de Exercicio\n11- Sair\nR: '))

    if Opcao == 11:
        print('Progrma Encerrado!')
        break
    elif Opcao > 11 or Opcao <= 0:
        os.system('cls')
        print('Opcao Invalida!')
        time.sleep(2)
        continue
    
    os.system('cls')
    Qntd = int(input('Quantos exercicios deseja fazer: '))
    os.system('cls')
    Dificuldade = int(input('Qual a dificuldade dos exercicios:\n1- Facil\n2- Medio\n3- Dificil\nR: '))

    if Opcao == 1:
        Soma(Qntd,Dificuldade)
    elif Opcao == 2:
        Subtracao(Qntd,Dificuldade)
    elif Opcao == 3:
        Multiplicacao(Qntd,Dificuldade)
    elif Opcao == 4:
        Divisao(Qntd,Dificuldade)
    elif Opcao == 5:
        Matriz(Qntd,Dificuldade)
    elif Opcao == 6:
        Raiz(Qntd,Dificuldade)
    elif Opcao == 7:
        Exponenciacao(Qntd,Dificuldade)
    elif Opcao == 8:
        Fatoracao(Qntd,Dificuldade)
    elif Opcao == 9:
        Equacao1(Qntd,Dificuldade)
    elif Opcao == 10:
        Lista(Qntd,Dificuldade)
    