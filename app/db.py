from bson import ObjectId
from pymongo import MongoClient
import os

# Variáveis de ambiente ou configuração direta da URL de conexão
MONGO_URI = "mongodb+srv://gabriellopes1010:1065@cluster0.osi1l.mongodb.net/"

def str_objectid(object_id: ObjectId) -> str:
    """Converte ObjectId para string"""
    return str(object_id)

client = MongoClient(MONGO_URI)
db = client["webhook"]  # Nome do banco de dados



# Função para retornar a conexão com o MongoDB
def get_db():
    return db