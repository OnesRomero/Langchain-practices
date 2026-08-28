# Usando api de LM Studio

# from dotenv import load_dotenv
# Cargar variables de archivo .env
# load_dotenv()

from langchain.chat_models import init_chat_model
from pprint import pprint


# Inicializar e invocar el modelo apuntando a LM Studio
model = init_chat_model(
    model="google/gemma-4-12b",
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    temperature=1.0,
    api_key="lm-studio"
)

response = model.invoke("¿Cuál es la capital de La Luna?")

response

print(response.content)


#pprint(response.response_metadata)