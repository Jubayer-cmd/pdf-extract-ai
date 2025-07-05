import os
import getpass
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_google_api_key():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        api_key = getpass.getpass("Enter API key for Google Gemini: ")
        os.environ["GOOGLE_API_KEY"] = api_key
    return api_key

def main():
    get_google_api_key()
    chat_model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

    prompt = ChatPromptTemplate.from_template("So you are a funny guy you answer everything humour and funny like fantasy and not real info {topic}")

    chain = prompt | chat_model | StrOutputParser()

    # print(chain.invoke({"topic": "Barmuda Triangle"}))
    # for s in chain.stream({"topic": "Barmuda Triangle"}):
    #     print(s, end="", flush=True)
    results = chain.batch([{"topic": "Barmuda Triangle"}, {"topic": "Titanic"}])
    for s in results:
        print(s, end="", flush=True)
if __name__ == "__main__":
    main()