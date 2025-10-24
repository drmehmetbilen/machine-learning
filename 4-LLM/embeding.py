key = "abcd"
model_name = "nomic-embed-text:latest"
base_url = "http://localhost:11434/v1"

input_message = "Merhaba"


from openai import OpenAI

client = OpenAI(api_key=key, base_url=base_url)

result = client.embeddings.create(
    model=model_name,
    input=input_message 
)
embedding_result = result.data[0].embedding
print(embedding_result)
