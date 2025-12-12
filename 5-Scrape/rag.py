import pandas as pd
from openai import OpenAI


def get_embedding(text):
    base_url = "http://localhost:11434/v1/"
    key = "ollama"
    client = OpenAI(base_url=base_url, api_key=key)

    result = client.embeddings.create(input=text, model="nomic-embed-text:latest")
    embedding_result = result.data[0].embedding
    return embedding_result

def load_data():
    df = pd.read_csv("data/maku_news_emb.csv")
    df["embedding"] = df["embedding"].apply(eval)
    return df

def get_distance(embed1, embed2):
    n = len(embed1)
    sum = 0
    for i in range(n):
        sum+=(embed1[i]-embed2[i])*(embed1[i]-embed2[i])
    return sum ** 0.5

def get_full_text(df):
    full_text = ""
    for index, row in df.iterrows():
        full_text+=f'{row["title"]}\n{row["content"]}\nKaynak:{row["link"]}\n\n'    
    return full_text

def get_similar_records(text,n_record_count):
    #+1. kullanıcının text'inin embedding'ini al
    #+2. embeddinge - listedeki her bir embeddingin uzaklığını bulmamız lazım
    #2.1 uzaklık / benzerlik dönüşümü
    #3. Listeyi sıralatabiliriz.
    #4. n_record_count adet kaydı geri döndür.
    
    text_embedding = get_embedding(text)
    
    df = load_data()
    df["distance"] = df["embedding"].apply(lambda x:get_distance(x,text_embedding))
    #df["similarity"] = 1 - df["distance"]
    full_text = get_full_text(df.sort_values("distance").head(n_record_count))
    
    enriched_user_message = f"""
    User Question : {text}
    Here are the data in our DB. Use this data to respond user question : 
    {full_text}
    """
    
    return enriched_user_message
    

if __name__ == "__main__":
    result = get_similar_records("akademik takvim",3)
    for index, row in result.iterrows():
        print(row["distance"],":",row["title"])
    
    ft = get_full_text(result)
    pass