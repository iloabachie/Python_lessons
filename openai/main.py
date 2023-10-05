import tkinter
import os
import openai
import dotenv

dotenv.load_dotenv(r"openai\.env")

openai.organization = "org-tqgq8VYlUXMUVnqhtf2s6isL"
openai.api_key = os.getenv("OPEN_AI_KEY")
openai.Model.list()#api_key=openai.api_key)



response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": 'write python code for factorial'}],
    temperature=0.8,
    max_tokens=256
)
print(response)

# def chat_with_gpt(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",  # You can use other engines as well
#         prompt=prompt,
#         max_tokens=50,  # Adjust max tokens as needed
#         temperature=0.7,  # Adjust temperature for creativity
#     )
#     # print(response)
#     # print()
#     # print(response.choices)
#     return response.choices[0].text


# user_input = "Translate the following English text to French: 'Hello, how are you?'"
# user_input = "write code in python for factorial"
# response = chat_with_gpt(user_input)
# print(response)


# def chat_with_gpt_turbo(prompt):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", 
#         messages=[{"role": "user", "content": prompt}]
#         )
#     return completion.choices[0].message.content


# question = "return an array of only the keywords from this passage 'Fine-tuning GPT models can make them better for specific applications, but it requires a careful investment of time and effort. We recommend first attempting to get good results with prompt engineering, prompt chaining (breaking complex tasks into multiple prompts), and function calling, with the key reasons being:'"
# completion = chat_with_gpt_turbo(question)


# print(completion)    