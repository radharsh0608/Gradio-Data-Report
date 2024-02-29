import json
import requests
from openai import OpenAI

stream = False
def responseFromModel(model,prompt,inputFromUser,temperature,maxTokens,topP,repitionPenalty):
    if "chatNBX" in model:
        model=model.split("- ")
        model=model[1]
        print(model)
        url = "https://chat.tune.app/api/chat/completions"
        headers = {
            "Authorization": "tune-2268bafc-b05c-4183-8592-faae30f21a4a1708968076",
            "Content-Type": "application/json"
        }
        data = {
            "temperature": temperature,
            "messages": [
            {
              "role": "system",
              "content": prompt
            },
            {
              "role": "user",
              "content": inputFromUser
            }
          ],
            "model": model,
            "stream": stream,
            "max_tokens": maxTokens
        }
        response = requests.post(url, headers=headers, json=data)
        data=[]
        if stream:
            for line in response.iter_lines():
                if line:
                    l = line[6:]
                    if l != b'[DONE]':
                      print("Error")
                      data.append(json.loads(l))
        else:
          data=response.json()
          print(data["choices"][0]["message"]["content"])
          return data["choices"][0]["message"]["content"]

    elif "OpenRouter" in model:
        model = model.split("- ")
        model = model[1]
        print(model)
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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"
        )

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",
                 "content": prompt,
                 },
                {
                    "role": "user",
                    "content": inputFromUser
                },

            ],
            max_tokens=maxTokens,
            top_p=topP,
            temperature=temperature,

        )
        return completion.choices[0].message.content

