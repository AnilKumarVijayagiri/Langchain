from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-3")

result=llm.invoke("Which planet has the most number of moons")
print(result.content)