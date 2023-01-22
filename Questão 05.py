import os
from os import getenv
from pymongo import MongoClient

os.system("cls")
print("••• Q U E S T Ã O   0 5 •••\n")

HOST = getenv("MONGO_HOST")
PASSWORD = getenv("MONGO_PASSWORD")
USERNAME = getenv("MONGO_USERNAME")
DATABASE = getenv("MONGO_DATABASE")

connection_string = F"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}/?retryWrites=true&w=majority"

def obter_colecao_mongodb(url_conexao, colecao):
    mongoclient = MongoClient(url_conexao)
    database = mongoclient[DATABASE]
    return database[colecao]

colecao_produtos = obter_colecao_mongodb(connection_string, "produtos")
primeiro_produto = colecao_produtos.find_one()

print("Registro de teste lido da coleção:") 
print(F"\033[93m{primeiro_produto}\033[m")
print("")