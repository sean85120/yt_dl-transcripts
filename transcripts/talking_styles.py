import os

import openai
from dotenv import load_dotenv

load_dotenv()

from csv import DictWriter

from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")


# prompt = "誰最會烤肉？老師，因為她考的都沒有教"
# prompt = prompt.replace(',', '，')

# def explain_funny_reason(prompt):
    
#     # print('type in prompt:')
#     # input_prompt = input()
#     # print('you type in :', input_prompt)

#     openai.api_key = openai_api_key

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role":"system",
#                 "content":"i want you to act as baby in chinese and without saying i'm a baby" 
             
#             },
#             {
#                 "role": "user", 
#                 "content":f"說了跟什麼有關的笑話",
#             }
#         ],
#         temperature=0.2,
#     )

#     print(response)
    

#     with open('./evaluations/funny_reason.txt', mode='a') as file:
#         file.write('\n\n')
#         file.write('content:\n')
#         file.write(response['choices'][0]['message']['content'])
#         file.write('\nusage:\n')
#         file.write(str(response['usage']))


# explain_funny_reason(prompt)



def talking_style():
    template = """問題: {question}

    答案: 讓我們一步一步分析."""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = OpenAI(
        openai_api_key=openai_api_key, 
        # model="gpt-3.5-turbo", 
        temperature=0.2,
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    question = "誰最會烤肉？老師，因為她考的都沒有教 請分析這個笑話"

    question2 = f"請你充當一個嬰兒並用繁體中文回答下列問題: {question}"

    response = llm_chain.run(question2)

    with open('./evaluations/talking_style_response.txt', mode='a') as f:
        f.write('\n\n')
        f.write('content:\n')
        f.write(response)

    print(response)


talking_style()
talking_style()