import requests
import json 

link = "https://reconview-1410a-default-rtdb.firebaseio.com/"
#Cadastrar Dados:
#dados = {'nome':'joao','email': 'joao@gmail.com','senha':'123'}
#criar = requests.post(f'{link}/users/.json', data=json.dumps(dados))
#print(criar)
#print(criar.text)


#Editar Dados:
#dados = {'nome':'joao vyctor'}
#editar = requests.patch(f'{link}/users/-NgHFQRYff858q9oPZm8/.json', data=json.dumps(dados))

#Consultar Dados:
consulta = requests.get(f'{link}/users/.json')
dic_user = consulta.json()
print(consulta)
id_user= None
for id in dic_user:
    user = dic_user[id]['nome'] 
    if user == "joao":
        id_user = id 

        print(id_user)

#Deletar Dados:
delete = requests.delete(f'{link}/users/{id}/.json')
                         