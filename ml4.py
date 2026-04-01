import pandas as pd
def find_s_algorithm(file_path):
    data = pd.read_csv(file_path)
    print("Training data:\n")
    print(data)

    attributes = data.columns[:-1]
    class_label = data.columns[-1]

    hypothesis = [None] * len(attributes)
    
for index, row in data.iterrows():
        if row[class_label].lower() == "yes":
            row_values = row[attributes].tolist()
            if None in hypothesis:
                hypothesis = row_values.copy()
            else:
                for i in range(len(attributes)):
                    if hypothesis[i] != row_values[i]:
                        hypothesis[i] = '?'   
    return hypothesis

file_path = 'training_data.csv'
hypothesis = find_s_algorithm(file_path)
print("Final hypothesis :", hypothesis)