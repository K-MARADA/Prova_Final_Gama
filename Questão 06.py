import os
from os import getenv
from pymongo import MongoClient

os.system("cls")
print("••• Q U E S T Ã O   0 6 •••\n")

HOST = getenv('MONGO_HOST')
PASSWORD = getenv('MONGO_PASSWORD')
USERNAME = getenv('MONGO_USERNAME')
DATABASE = getenv('MONGO_DATABASE')

connection_string = f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}/?retryWrites=true&w=majority"

def obter_colecao_mongodb(url_conexao, colecao):
    mongoclient = MongoClient(url_conexao)
    database = mongoclient[DATABASE]
    return database[colecao]

def ajustar_estoque(sku, estoque):
    colecao_produtos = obter_colecao_mongodb(connection_string, 'produtos')
    query = { "sku": sku }
    inc = { "$inc": { "estoque": estoque }}

    colecao_produtos.update_one(query, inc)

colecao_produtos = obter_colecao_mongodb(connection_string, 'produtos')

primeiro_produto = colecao_produtos.find_one()
print(primeiro_produto)
ajustar_estoque(1, -5)

primeiro_produto = colecao_produtos.find_one()
print(primeiro_produto)
ajustar_estoque(1, 10)

primeiro_produto = colecao_produtos.find_one()
print(primeiro_produto)