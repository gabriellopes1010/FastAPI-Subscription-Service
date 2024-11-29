from fastapi import APIRouter
from app.models.subscription import Subscription
from app.db import get_collection

router = APIRouter()

@router.post("/new-subscription")
async def new_subscription(subscription: Subscription):
    """Quando um novo usuário se inscreve, salva no MongoDB"""
    
    # Conectar ao MongoDB e inserir a nova assinatura
    collection = get_collection()
    subscription_dict = subscription.dict()  # Converte o modelo Pydantic para dicionário
    result = collection.insert_one(subscription_dict)
    
    # Retorna o ID gerado pelo MongoDB junto com os dados
    return {"message": "Assinatura processada com sucesso", "subscription_id": str(result.inserted_id)}