from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_anthropic import ChatAnthropic
#from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage
load_dotenv()

messages=[
    SystemMessage(content="You are an Astrophysics expert."),
    HumanMessage(content="Which planet has the most number of moons?"),
    #HumanMessage(content="What is the square root of 81?"),
]
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result=model.invoke(messages)
print(result.content)