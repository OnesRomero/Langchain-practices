# Usando api de openai

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pprint import pprint

# Cargar variables de archivo .env
load_dotenv()

# Inicializar e invocar el modelo
model = init_chat_model(model="gpt-5-nano")

response = model.invoke("What's the capital of the Moon?")

response

print(response.content)


pprint(response.response_metadata)