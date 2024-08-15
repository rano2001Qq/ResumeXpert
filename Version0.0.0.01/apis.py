# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

groq_key = "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"




def groq(input,key):
    chat = ChatGroq(
        temperature=0,
        model="llama3-70b-8192",
        api_key=key
    )
    
    return chat.invoke(input)

def final(Input):
    print("calling from groq")
    # return groq(Input,groq_keys[keys()[0]])
    return groq(Input,groq_key).content


