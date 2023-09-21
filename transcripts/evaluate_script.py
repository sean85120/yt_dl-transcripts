import os

import openai
from dotenv import load_dotenv

load_dotenv()

from csv import DictWriter

openai_api_key = os.getenv("OPENAI_API_KEY")

field_name = ['script', 'neutral_sentiment', 'positive_sentiment', 'negative_sentiment']


prompt = "這個觸及率也太低了吧 這蛋糕 是你放的嗎 你發現旁邊就懸崖嗎 那些屍體是前男友嗎 我們所有跟他交往過的人 都走過這條男友之路 那其他男友都真的直上直下 直上直下 我超害怕的 我覺得這根本是一個好女婿測驗 真的好女婿測驗 但是他測驗的不是我的闊背肌 他測驗的是我誠不誠實 因為誠實是一段感情裡面 最重要的一環 他要看我遇到一些 不合理的要求的時候 我會不會表達出我的不滿 我誠不誠實 然後當天晚上呢 他爸爸就煮了一整桌的菜 然後他就深情款款的看著我說 博安啊 一個真男人 每次我煮的飯 都會想吃上個十萬 我一看那飯的顏色就覺得 他絕對是在考驗我誠不誠實 那個顏色怎麼可能 裡面還有頭髮 你剛在浴缸裡面住的嗎 所以我想說 哇這是我誠實的機會 這是我讓他知道 我是一個誠實好女婿的機會 就看著他 然後說 你呃 想買智慧電鍋嗎 謝謝大家"
prompt = prompt.replace(',', '，')

def evaluate_script(prompt):
    
    # print('type in prompt:')
    # input_prompt = input()
    # print('you type in :', input_prompt)

    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":f"rank the positive, neutral, negative sentiment of the stand up script in scale 0~1.0, just give me the number without other explanations:\n {prompt}"}],
    )

    print(response)
    

    obj = {
        'script': prompt,
        'neutral_sentiment': str(response['choices'][0]['message']['content']).split(': ')[2][0:3],
        'positive_sentiment': str(response['choices'][0]['message']['content']).split(': ')[1][0:3],
        'negative_sentiment': str(response['choices'][0]['message']['content']).split(': ')[3][0:3],
    }

    with open('./script_dataset.csv', mode='a') as file:
        dictwriter_object = DictWriter(file, fieldnames=field_name)
        file.write('')
        dictwriter_object.writerow(obj)

    with open('./evaluations/evaluation.txt', mode='a') as file:
        file.write('\n\n')
        file.write('content:\n')
        file.write(response['choices'][0]['message']['content'])
        file.write('\nusage:\n')
        file.write(str(response['usage']))


evaluate_script(prompt)





