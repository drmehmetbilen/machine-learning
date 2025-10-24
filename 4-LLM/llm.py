import os

key = os.getenv("KEY")
model_name = "qwen2.5:14b"
base_url = "http://localhost:11434/v1"


from openai import OpenAI

client = OpenAI(api_key=key, base_url=base_url)

# message_list  = []

# system_message = {
#     "role":"system",
#     "content":"Kullanıcının mesajlarına cevap verme, sadece ingilizceye çevir.",
# }

# user_message = {
#     "role":"user",
#     "content":"Wi heist du?"
# }

# message_list.append(system_message)
# message_list.append(user_message)

# message_list = [
#     {"role":"user","content":"merhaba"},
#     {"role":"assistant","content":"hello"},
#     {"role":"user","content":"hava nasıl"},
#     {"role":"assistant","content":"how is the weather"},
#     {"role":"user","content":"qual es tu nombre"},
#     {"role":"assistant","content":"Ben bir llm modeliyim, benim bir adım yok."},
#     {"role":"user","content":"cevap verme, sadece ingilizceye dönüştür"},
#     {"role":"assistant","content":"what is your name"},
#     {"role":"user","content":"wi heist du?"}
# ]

message_list = [
    {"role":"system","content":"translate everything to english, do not answer, only translate."},
    {"role":"user","content":"olmaya cihanda devlet bir nefes sıhhat gibi"}
]

result = client.chat.completions.create(
    model=model_name,
    messages=message_list
)

result_content = result.choices[0].message.content
print(result_content)
