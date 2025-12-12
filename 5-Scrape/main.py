from openai import OpenAI
from rag import get_similar_records

base_url = "http://localhost:11434/v1/"
key = "ollama"
model_name = "qwen2.5:14b"
client = OpenAI(base_url=base_url, api_key=key)

message_list = [
    {"role":"system","content":"You are a helpful assistant."}
]

while True:
    user_message = input("USER : ")
    enriched_user_message = get_similar_records(user_message,3)
    message_list.append(
        {"role":"user","content":enriched_user_message}
    )
    result = client.chat.completions.create(
        model=model_name,
        messages=message_list
    )
    ai_response = result.choices[0].message.content
    message_list.append({"role":"assistant","content":ai_response})
    print("AI : ",ai_response)
    