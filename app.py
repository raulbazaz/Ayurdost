import numpy as np
import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("./training.csv")
test = df.iloc[:,:132]
disease_name = df["prognosis"].to_list()
symptoms1= df.columns[:-1].to_list()

l2 = []
for i in range(0,len(symptoms1)):
    l2.append(0)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(df["prognosis"].to_list())
Diseases = le.transform(df["prognosis"].to_list())

df1=df.drop(["prognosis"],axis=1)
x = df1[symptoms1]
y = pd.Series(Diseases)

from sklearn import tree

model = tree.DecisionTreeClassifier() 
model = model.fit(x,y)

y_pred=model.predict(x)

df2 = pd.read_csv("./AyurvedaDataSet - Sheet1.csv")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/select")
def second():
    return render_template("./2nd.html")

@app.route("/symptoms")
def sympto():
    return render_template("./3rd.html")

@app.route("/treatment", methods=['GET', 'POST'])
def treate():
    symptoms = []
    if request.method == "POST":
        symptoms_str = request.form.get("symptoms", "")

        # If symptoms are passed as a single string, split them by comma and trim whitespaces
        if symptoms_str:
            symptoms = [symptom.strip() for symptom in symptoms_str.split(',')]

        
    
    for i in range(len(symptoms1)):
        if symptoms1[i] in symptoms :
            l2[i]=1
    l2
    len(l2)

    dict1= {}
    for i in range(len(symptoms1)):
        dict1[symptoms1[i]]= l2[i]
    print(dict1)
    test = pd.DataFrame(dict1,index=[0])

    y_text=model.predict(test)
    print(y_text)

    nameDisease = le.inverse_transform(y_text)[0]
    print(nameDisease)
    #print(le.inverse_transform(df["prognosis"].to_list()))
    
    df3 = df2["Diseases"]
    for i in range(len(df3)):
        if  str(nameDisease) in df3[i]:
            index = i 

    
    
    result = df2.iloc[index]
    Ayurved = result["Ayurvedic Formulations"]
    therapy = result["Therapy"]
    precautions = result["Precautions"]
    descrip = result["Details"]


    return render_template("./4th.html", symptoms=symptoms,nameDisease=nameDisease,Ayurved=Ayurved,therapy=therapy,precautions=precautions,descrip=descrip)


app.run(debug=True)



    
