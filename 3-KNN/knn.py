#IMPORTS
import pandas as pd

def load_data(data_path="data/iris.csv", names = ["sl","sw","pl","pw","class"]):
    data = pd.read_csv(data_path, names=names)
    return data

def calculate_distance(ins1, ins2):
    sum = 0
    for index in range(len(ins1)):
        sum += (ins1[index] - ins2[index])**2
    sqr = sum**0.5
    return sqr

def predict_class(data,sample, K):
    distance_list = []
    for index, row in data.iterrows():
        data_sample = row.values[:-1]
        true_class = row.values[-1]
        distance = calculate_distance(data_sample, sample)
        distance_list.append([true_class, distance])
    
    sorted_distance_list = sorted(distance_list, key = lambda x: x[1])
    nearest_samples = sorted_distance_list[:K]
    class_names = [i[0] for i in sorted_distance_list]
    prediction = pd.Series(class_names).value_counts().idxmax()

    return prediction

def main():
    data = load_data()
    sample = [6.3,2.5,5.0,1.9]
    prediction = predict_class(data,sample,3)
    print(prediction)

if __name__ == "__main__":
    main()