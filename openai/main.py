import os
import openai
import dotenv
import ConsolePrint

dotenv.load_dotenv(r"openai\.env")

openai.organization = "org-tqgq8VYlUXMUVnqhtf2s6isL"
openai.api_key = os.getenv("OPEN_AI_KEY")
models = openai.Model.list()

ConsolePrint.startConsoleSave(name=r"openai\Open AI Models.txt")
print(type(models))
print(models)
ConsolePrint.endConsoleSave()



def chat_with_gpt_turbo(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are an assistant that translates to french"}, 
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "I can help you with canadian French translations"} # Here make model provide answers in Canadian french.
            ],
        temperature=0.7, # Adjust temperature for creativity 0 - 1
        stream=False,  # mimic the webbased gpt iterative fluidity. makes answer a generator object
        # max_tokens=50  # Adjust max output tokens as needed
        )
    print(completion)
    return completion.choices[0].message.content


question = "'Fine-tuning GPT models can make them better for specific applications, but it requires a careful investment of time and effort. We recommend first attempting to get good results with prompt engineering, prompt chaining (breaking complex tasks into multiple prompts), and function calling, with the key reasons being:'"
# completion = chat_with_gpt_turbo(question)


# print(completion)    


