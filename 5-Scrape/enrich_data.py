from openai import OpenAI
import pandas as pd


def get_embedding(text):
    base_url = "http://localhost:11434/v1/"
    key = "ollama"
    client = OpenAI(base_url=base_url, api_key=key)

    result = client.embeddings.create(input=text, model="nomic-embed-text:latest")
    embedding_result = result.data[0].embedding
    return embedding_result

if __name__ == "__main__":
    embeddings = []
    df = pd.read_csv("data/maku_news.csv")
    for index,row in df.iterrows():
        print(f"Şu an {index}. haber işleniyor")
        text = row["title"]+" - "+row["content"]
        embedding = get_embedding(text)
        embeddings.append(embedding)

    df["embedding"] = embeddings
    df.to_csv("data/maku_news_emb.csv")
    
    