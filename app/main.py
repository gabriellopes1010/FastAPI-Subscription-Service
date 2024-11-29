from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId
from app.db import get_db, str_objectid  # Função para obter a conexão com o MongoDB e converter ObjectId para string

app = FastAPI()

# Modelo Pydantic para uma assinatura
class Subscription(BaseModel):
    username: str
    monthly_fee: float
    start_date: datetime

    class Config:
        orm_mode = True

@app.post("/new-subscription")
def new_subscription(subscription: Subscription):
    """Cria uma nova assinatura e salva no MongoDB"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]
    
    # Converte os dados da Subscription para um dicionário e insere no MongoDB
    subscription_dict = subscription.dict()
    result = subscriptions_collection.insert_one(subscription_dict)

    # Retorna o ID do documento inserido no banco
    return {"message": f"Subscription for {subscription.username} received and saved!", "id": str(result.inserted_id)}

@app.post("/webhooks/new-subscription")
async def webhook_new_subscription(subscription: Subscription):
    """Recebe uma requisição webhook para criar uma nova assinatura"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]
    
    # Converte os dados da Subscription para um dicionário e insere no MongoDB
    subscription_dict = subscription.dict()
    result = subscriptions_collection.insert_one(subscription_dict)
    
    # Retorna o ID do documento inserido no banco
    return {"message": f"Webhook: Subscription for {subscription.username} received and saved!", "id": str(result.inserted_id)}

@app.get("/subscription/{subscription_id}")
def get_subscription(subscription_id: str):
    """Busca uma assinatura pelo ID"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]

    # Verifica se o ID fornecido é um ObjectId válido
    try:
        object_id = ObjectId(subscription_id)  # Tentando converter a string para ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ObjectId: {e}")

    # Tenta encontrar a inscrição pelo ObjectId
    subscription = subscriptions_collection.find_one({"_id": object_id})

    if subscription:
        # Convertendo o _id de ObjectId para string
        subscription["_id"] = str_objectid(subscription["_id"])
        return subscription
    else:
        # Se não encontrar a inscrição, retorna um erro 404
        raise HTTPException(status_code=404, detail="Subscription not found")
    

@app.delete("/subscription/{subscription_id}")
def delete_subscription(subscription_id: str):
    """Deleta uma assinatura pelo ID e retorna o nome do usuário na mensagem de confirmação"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]

    # Verifica se o ID fornecido é um ObjectId válido
    try:
        object_id = ObjectId(subscription_id)  # Tentando converter a string para ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ObjectId: {e}")

    # Tenta encontrar a inscrição pelo ObjectId
    subscription = subscriptions_collection.find_one({"_id": object_id})

    if subscription:
        # Obtém o nome do usuário antes de excluir a assinatura
        username = subscription.get("username")

        # Exclui a assinatura
        result = subscriptions_collection.delete_one({"_id": object_id})

        if result.deleted_count == 1:
            # Retorna a mensagem com o nome do usuário
            return {"message": f"Subscription of {username} with the (ID {subscription_id}) has been deleted."}
        else:
            raise HTTPException(status_code=404, detail="Subscription not found")
    else:
        # Se não encontrar a inscrição, retorna um erro 404
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    
@app.put("/subscription/{subscription_id}")
def update_subscription(subscription_id: str, subscription: Subscription):
    """Atualiza as informações de uma assinatura pelo ID"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]

    # Verifica se o ID fornecido é um ObjectId válido
    try:
        object_id = ObjectId(subscription_id)  # Tentando converter a string para ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ObjectId: {e}")

    # Tenta encontrar a assinatura pelo ObjectId
    existing_subscription = subscriptions_collection.find_one({"_id": object_id})

    if existing_subscription:
        # Atualiza os dados da assinatura
        updated_subscription = subscription.dict()  # Converte os dados do Pydantic para um dicionário

        # Atualiza no banco de dados
        result = subscriptions_collection.update_one(
            {"_id": object_id}, 
            {"$set": updated_subscription}  # Atualiza os campos da assinatura
        )

        if result.modified_count == 1:
            return {"message": f"Subscription for {updated_subscription['username']} has been updated."}
        else:
            return {"message": "No changes made to the subscription."}
    else:
        # Se não encontrar a assinatura, retorna um erro 404
        raise HTTPException(status_code=404, detail="Subscription not found")
    

@app.get("/subscriptions", response_model=List[Subscription])
def list_subscriptions():
    """Listar todas as assinaturas no MongoDB"""
    db = get_db()  # Obtém a conexão com o MongoDB
    subscriptions_collection = db["subscriptions"]  # Coleção de assinaturas no MongoDB

    # Recupera todos os documentos da coleção
    subscriptions = subscriptions_collection.find()

    # Converte os resultados para um formato amigável para o Pydantic
    result = []
    for sub in subscriptions:
        sub["_id"] = str(sub["_id"])  # Converte o ObjectId para string para evitar erro
        result.append(sub)

    return result
