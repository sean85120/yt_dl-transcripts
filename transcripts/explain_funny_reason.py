import os

import openai
from dotenv import load_dotenv

load_dotenv()

from csv import DictWriter

openai_api_key = os.getenv("OPENAI_API_KEY")


prompt = "諸葛亮就是那種 前一秒你看到他臉書上面還是綠燈 結果你一瞧他 在嗎 不見 臭諸葛亮 到了第三次 到第三次三顧茅廬的時候 諸葛亮終於發現我不在家這個藉口 已經不能再用 所以他這次 諸葛亮看到劉備他們來 就像每個學生族群 看到老人上公車一樣 咳 咳 這麼美 咳 諸葛亮裝睡"
prompt = prompt.replace(',', '，')

def explain_funny_reason(prompt):
    
    # print('type in prompt:')
    # input_prompt = input()
    # print('you type in :', input_prompt)

    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":f"請解釋笑話為什麼好笑：\n {prompt}"}],
    )

    print(response)
    

    with open('./evaluations/funny_reason.txt', mode='a') as file:
        file.write('\n\n')
        file.write('content:\n')
        file.write(response['choices'][0]['message']['content'])
        file.write('\nusage:\n')
        file.write(str(response['usage']))


explain_funny_reason(prompt)
explain_funny_reason(prompt)