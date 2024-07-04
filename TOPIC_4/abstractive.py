from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=1.0,
    model="llama3-70b-8192",
    api_key="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"
)

system = "You are a helpful assistant."
human = "{text}"

prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

user_input = input("Enter your text: ")

chain = prompt | chat
response = chain.invoke({"text": user_input})

response_content = response.content
formatted_content = response_content.replace('\n\n', '\n').replace('\\', '')

print("AI Response:")
print(formatted_content)