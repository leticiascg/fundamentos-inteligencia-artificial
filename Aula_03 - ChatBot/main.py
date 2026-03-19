import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import LangChainException

env_path = find_dotenv()

if not env_path:
    print("Aviso: Arquivo .env não foi encontrado automaticamente pelo find_dotenv().")
else:
    load_dotenv(env_path)

if not os.getenv("GROQ_API_KEY"):
    print(f"DEBUG: Caminho do arquivo .env tentado: '{env_path}'")
    print("Erro: A variável de ambiente GROQ_API_KEY não foi definida.")
    print("Verifique se o arquivo .env existe e não está nomeado como .env.txt.")
    exit()

chat = ChatGroq(model="llama-3.3-70b-versatile")

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um confeiteiro renomado e prestativo."),
    ("user", "Ensine a receita de {doce} com o seguinte detalhe: {detalhe}")
])

output_parser = StrOutputParser()

chain = template | chat | output_parser

try:
    resposta = chain.invoke({
        "doce": "Bolo de Chocolate",
        "detalhe": "sem lactose"
    })

    print(resposta)
except LangChainException as e:
    print(f"Ocorreu um erro ao invocar a chain: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")