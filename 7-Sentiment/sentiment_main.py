from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from transformers import MarianMTModel, MarianTokenizer

import numpy as np
from scipy.special import softmax
from transformers import pipeline

def sentiment_analysis(text):

    # MODEL LOADING
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    # PREDICTION
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)

    # SCORE PARSING
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    predicted_class = config.id2label[ranking[0]]
    predicted_score = scores[ranking[0]]

    print(f"Metin içerisindeki duygu :{predicted_class}")
    print(f"Duygunun Derecesi :{predicted_score}")

    return predicted_class, predicted_score

def translate(text):

    src_text = [
       text
    ]

    model_name = "ckartal/turkish-to-english-finetuned-model"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))


    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    print("Çeviri : ",translated_text)
    return translated_text

def detect_language(input_text):

    text = [
        input_text
    ]

    model_ckpt = "papluca/xlm-roberta-base-language-detection"
    pipe = pipeline("text-classification", model=model_ckpt)
    detection = pipe(text, top_k=1, truncation=True)
    language = detection[0][0]["label"]
    print("Tespit edilen dil : ",language)
    return language

def main(text):
    lang = detect_language(text)
    if lang not in ["tr","en"]:
        print("Bu dil ile duygu analizi yapılamıyor! Dil :",lang)
        return
    if lang=="tr":
        text = translate(text)
        
    emotion, score = sentiment_analysis(text)

text = "Ich habe keine ahnung!"
main(text)

# ODEV : 
# Test seneryolarının oluşturulması - pytest
# Workflow'un başka dilleri de kapsayacak şekilde geliştirilmesi.
# Opsiyonel : API'ye dönüştürüp, daha da opsiyonel : bir web sayfası içerisine yerleştirilmesi


