# 구글 제미나이 API
from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일로드
gen_key = os.getenv("GEMINI_API_KEY")

def gai(que):
    client = genai.Client(api_key = gen_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents = que + '300자 이내로 답변하되 중학생에게 설명하듯이 쉽고 친근한 말투로 해라.')
    print(response.text)

if __name__=="__main__":
    for n in range(5):
        gai(input("질문하세요: >>"))