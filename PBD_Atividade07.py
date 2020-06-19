from matplotlib import pyplot as plt
import random
from collections import Counter
import math

users = [
    {"id": 0, "name": "Hero","gender":"m","age":18, 'interest in': 'n'},    
    {"id": 1, "name": "Dunn","gender":"m","age":20, 'interest in': 'b'},    
    {"id": 2, "name": "Sue","gender":"f","age":14, 'interest in': 'm'},    
    {"id": 3, "name": "Chi","gender":"f","age":16, 'interest in': 'm'},      
    {"id": 4, "name": "Thor","gender":"m","age":18, 'interest in': 'f'},      
    {"id": 5, "name": "Clive","gender":"m","age":24, 'interest in': 'f'},
    {"id": 6, "name": "Hicks","gender":"m","age":22, 'interest in': 'f'},   
    {"id": 7, "name": "Devin","gender":"m","age":17, 'interest in': 'm'},       
    {"id": 8, "name": "Kate","gender":"f","age":19, 'interest in': 'm'},        
    {"id": 9, "name": "Klein","gender":"m","age":20, 'interest in': 'f'},
]

def quantidade_de_usuarios_na_rede():
    return len(users)

def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede): #Gera tuplas de conexoes
    conexoes = []
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                conexoes.append((u1, u2))
                break
    return [aux for aux in set(conexoes)]

def quantidade_de_amigos_por_sexo(amizades, sexo): # [qtd_pessoas:qtd_amigos]
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b  #quantos amigos tem cada id (id: qtd_amg) (1:3)

    total_amigos = []

    for key, value in tudo.items():
        if users[key]['gender'] == sexo:
            total_amigos.append(value)

    return Counter(x for x in total_amigos) 
 
def gera_histograma_contagem_amigos(qtde_amigos_f, qtde_amigos_m, qtde_usuarios_na_rede):
    xs = range(qtde_usuarios_na_rede)
    ys = [qtde_amigos_f[x] for x in xs]
    plt.bar(xs, ys)
    ys = [qtde_amigos_m[x] for x in xs]
    plt.bar(xs, ys, width=0.65, color="red")

    plt.yticks([i for i in range(qtde_usuarios_na_rede // 2)])
    plt.title("Histograma da Contagem de Amigos por sexo")
    plt.xlabel("# de amigos")
    plt.ylabel("# de pessoas")
    plt.show()

def exercicio1():
    qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades(10, qtde_usuarios_na_rede)
    
    qtde_amigos_f = quantidade_de_amigos_por_sexo(amizades, 'm')
    qtde_amigos_m = quantidade_de_amigos_por_sexo(amizades, 'f')

    gera_histograma_contagem_amigos(qtde_amigos_f, qtde_amigos_m, qtde_usuarios_na_rede)
#=================================================================================

def quantidade_de_amigos_por_idade(amizades):
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b 
    
    total_amigos_por_idade = {}

    for key, value in tudo.items():
        total_amigos_por_idade[users[key]['age']] = value

    return total_amigos_por_idade

def histograma_exercicio2(qtde_amigos, qtde_usuarios_na_rede):

    xs = qtde_amigos.keys()
    ys = qtde_amigos.values()
    plt.bar(xs, ys)
    plt.yticks([i for i in range(qtde_usuarios_na_rede // 2)])
    plt.xticks([i for i in qtde_amigos.keys()])
    plt.title("Histograma da Contagem de Amigos por idade")
    plt.xlabel("Idade")
    plt.ylabel("# de amigos")
    plt.show()

def exercicio2():
    qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades(10, qtde_usuarios_na_rede)
    
    qtde_amigos = quantidade_de_amigos_por_idade(amizades)
    histograma_exercicio2(qtde_amigos, qtde_usuarios_na_rede)

#=================================================================================
#Exercicio3:
def media(usuarios):
    auxSomaIdades = 0

    for user in usuarios:
        auxSomaIdades += user["age"]

    return auxSomaIdades / len(usuarios)

def retorna_masculino_superior_22anos():
    usuarios = []
    for user in users:
        if user['age'] >= 22 and user['gender'] == 'm':
            usuarios.append(user)
    return usuarios

def exercicio3():    
    usuarios = retorna_masculino_superior_22anos()
    med = media(usuarios)

    variancia = sum([(user['age']-med)**2 for user in usuarios]) / len(usuarios)
    print('Variância:', variancia)
    dp = variancia**(1/2)
    print('Desvio Padrão:', dp)
    
exercicio1()
exercicio2()
exercicio3()