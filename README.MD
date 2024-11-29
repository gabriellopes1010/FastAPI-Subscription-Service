# 🌟 FastAPI Subscription Service 🌟

**Este é um serviço de gerenciamento de assinaturas utilizando FastAPI e MongoDB.**  
Ele permite a criação, atualização, recuperação e exclusão de assinaturas. O projeto é uma API RESTful simples, onde os dados das assinaturas são armazenados em um banco de dados MongoDB.

---

## 🚀 Funcionalidades

- **Criar nova assinatura**  
  Método: `POST /new-subscription` e `POST /webhooks/new-subscription`
  
- **Obter detalhes de uma assinatura**  
  Método: `GET /subscription/{subscription_id}`
  
- **Excluir uma assinatura**  
  Método: `DELETE /subscription/{subscription_id}`
  
- **Atualizar uma assinatura**  
  Método: `PUT /subscription/{subscription_id}`
  
- **Listar todas as assinaturas**  
  Método: `GET /subscriptions`

---

## 🛠️ Tecnologias

- **FastAPI** - Framework moderno e de alto desempenho para APIs com Python 3.7+.
- **MongoDB** - Banco de dados NoSQL usado para armazenar as assinaturas.
- **Pydantic** - Para validação de dados e serialização/deserialização de modelos.
- **BSON** - Para manipulação do tipo `ObjectId` do MongoDB.

---

## 📋 Pré-requisitos

- Python 3.7 ou superior
- MongoDB (instale e configure o MongoDB em sua máquina local ou use uma instância na nuvem)

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/fastapi-subscription-service.git
cd fastapi-subscription-service
2. Crie um ambiente virtual (opcional, mas recomendado)
bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
3. Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4. Configure a conexão com o MongoDB
No arquivo app/db.py, configure a conexão com o banco de dados. Exemplo de configuração:

python
Copiar código
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # URL do MongoDB
    return client["subscription_db"]  # Nome do banco de dados
5. Execute o servidor FastAPI
bash
Copiar código
uvicorn main:app --reload
Agora, a API estará disponível em http://127.0.0.1:8000.
Você pode testar a documentação interativa da API acessando http://127.0.0.1:8000/docs.

📝 Endpoints
1. Criar uma nova assinatura
Método: POST /new-subscription
Descrição: Cria uma nova assinatura no MongoDB.
Exemplo de requisição:

]
🤝 Contribuindo
Se você gostaria de contribuir para este projeto, fique à vontade para abrir um pull request.

Faça um fork deste repositório.
Crie uma branch para sua nova funcionalidade:
git checkout -b minha-nova-funcionalidade
Realize as alterações desejadas.
Envie suas alterações para o seu repositório:
git push origin minha-nova-funcionalidade
Abra um pull request para este repositório.
📜 Licença
Este projeto está licenciado sob a MIT License.