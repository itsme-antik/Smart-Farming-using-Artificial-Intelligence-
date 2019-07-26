import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import os
from twilio.rest import Client
account_sid = "AC74c65f66f1de79c6a6b4f9314f161135"
auth_token = "04ca45f4d51b1c9e6dff55d9b786e3e8"
client = Client(account_sid, auth_token)

dataset = pd.read_csv('C:\\Users\\Antik\\Desktop\\Tech-Master-5-master\\FinalFinal.csv')
#print(dataset.shape)
data2 = dataset[['msp','climate_conditions','rainfall','nitrogen','Season','soil_conditions']]
datalabels = dataset[['Type']]
dataset2 = pd.get_dummies(data2)
print(dataset2.iloc[:,:].head(5))
print(data2.head())
print(dataset2.shape)
pbset = pd.read_csv("C:\\Users\\Antik\\Desktop\\Tech-Master-5-master\\Finalpunjab.csv")
pb2 = pbset[['msp','climate_conditions','rainfall','nitrogen','Season','soil_conditions']]
pblabels = dataset[['Type']]
pbset2 = pd.get_dummies(pb2)
tmset = pd.read_csv("C:\\Users\\Antik\\Desktop\\Tech-Master-5-master\\Finaltamil.csv")
tm2 = tmset[['msp','climate_conditions','rainfall','nitrogen','Season','soil_conditions']]
tmlabels = dataset[['Type']]
tmset2 = pd.get_dummies(pb2)
print ("Enter 1 for Punjab and 2 for Tamil Nadu")
state = int(input("Enter the choice: "))
if (state == 1):
    X = pbset2.iloc[:,0:13].values
    Y = pblabels.iloc[:,:].values
    pb = pd.read_csv("C:\\Users\\Antik\\Desktop\\Tech-Master-5-master\\Finalpunjab.csv")
    X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train,Y_train)
    climate = int(input("Enter the average temperature in celcius: "))
    print ("Enter the soil type: ")
    print ("0 for Alluvial soil: ")
    print ("1 for Black soil: ")
    print ("2 for Laterite soil: ")
    print ("3 for Marshy soil: ")
    print ("4 for Red soil: ")
    soiltype = int(input(('Enter your option: ') ))
    rainfall = int(input("Enter the rainfall in mm in your region: "))
    nitrogen_nutri = int(input("Enter the nitrogen content in kg/ha: "))
    print("Enter the season: ")
    print("0 for kharif: ")
    print("1 for rabi: ")
    print("2 for year long: ")
    season = int(input("Enter your choice: "))
    if (season==0):
        if(soiltype==0):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,1,0,0,0,0,1]]))
        elif(soiltype==1):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,1,0,0,0,1]])) 
        elif(soiltype==2):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,1,0,0,1]]))
        elif(soiltype==3):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,0,1,0,1]]))
        elif(soiltype==4):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,0,0,1,1]]))
    else:
        if(soiltype==0):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,1,0,0,0,0,0]]))
        elif(soiltype==1):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,1,0,0,0,0]]))
        elif(soiltype==2):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,1,0,0,0]]))
        elif(soiltype==3):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,0,1,0,0]]))
        elif(soiltype==4):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,0,0,1,0]]))
    name = dataset['crop']
    if (name[crp[0]] == 'maize'):
        a = "According to your input the best crop to harvest would be maize or potatoes or tomatoes"
        print (a)
    
    elif (name[crp[0]] == 'cotton'):
        a = "According to your input the best crop to harvest would be cotton or sugarcane or jute"
        print (a)
    
    elif (name[crp[0]] == 'wheat'):
        a = "According to your input the best crop to harvest would be wheat or cotton"
        print (a)

    elif (name[crp[0]] == 'paddy'):
        a = "According to your input the best crop to harvest would be paddy or sugarcane or millet or groundnut or ragi"
        print (a)

    elif (name[crp[0]] == 'barley'):
        a = "According to your input the best crop to harvest would be barley or potato"
        print(a)
    elif (name[crp[0]] == 'finger millet'):
        a = "According to your input the best crop to harvest would be finger millet or ground nut or ragi"
        print (a)
    
    elif (name[crp[0]] == 'green gram'):
        a = "According to your input the best crop to harvest would be green gram or millet"
        print (a)

    elif (name[crp[0]] == 'tea'):
        a = "According to your input the best crop to harvest would be tea"
        print (a)
    
    elif (name[crp[0]] == 'chillies'):
        a = "According to your input the best crop to harvest would be chillies or rice or wheat or sugarcane"
        print (a)
    
    elif (name[crp[0]] == 'turmeric'):
        a = "According to your input the best crop to harvest would be turmeric"
        print (a)

    elif (name[crp[0]] == 'sugar cane'):
        a = "According to your input the best crop to harvest would be sugar cane or wheat or cotton or jute "
        print (a)

    elif (name[crp[0]] == 'jute'):
        a = "According to your input the best crop to harvest would be jute or wheat or cotton "
        print (a)

    elif (name[crp[0]] == 'sorghum'):
        a = "According to your input the best crop to harvest would be sorghum or cotton or pearl millet "
        print (a)
    
    elif (name[crp[0]] == 'bajra'):
        a = "According to your input the best crop to harvest would be bajra or wheat or sugarcane "
        print (a)
    
    elif (name[crp[0]] == 'red gram'):
        a = "According to your input the best crop to harvest would be red gram or Bengal gram "
        print (a)
    
    elif (name[crp[0]] == 'black gram'):
        a = "According to your input the best crop to harvest would be black gram or red gram or bengal gram "
        print (a)
    
    elif (name[crp[0]] == 'sesame'):
        a = "According to your input the best crop to harvest would be sesame or sunflower or soyabeans "
        print (a)

    elif (name[crp[0]] == 'sweet potato'):
        a = "According to your input the best crop to harvest would be sweet potato or beans or peas "
        print (a)

    elif (name[crp[0]] == 'mustard'):
        a = "According to your input the best crop to harvest would be mustard or wheat or barley "
        print (a)

    elif (name[crp[0]] == 'soyabean'):
        a = "According to your input the best crop to harvest would be soyabean or sunflower or sesame "
        print (a)

    elif (name[crp[0]] == 'lin seed'):
        a = "According to your input the best crop to harvest would be lin seed or wheat or rice"
        print (a)
    
    elif (name[crp[0]] == 'niger'):
        a = "According to your input the best crop to harvest would be niger "
        print (a)

    elif (name[crp[0]] == 'capsicum'):
        a = "According to your input the best crop to harvest would be capsicum "
        print (a)
    
    elif (name[crp[0]] == 'cucumber'):
        a = "According to your input the best crop to harvest would be cucumber "
        print (a)
       
    elif (name[crp[0]] == 'ridge gourd'):
        a = "According to your input the best crop to harvest would be ridge gourd "
        print (a)
       
    elif (name[crp[0]] == 'bottle gourd'):
        a = "According to your input the best crop to harvest would be bottle gourd "
        print (a)
       
    elif (name[crp[0]] == 'snake gourd'):
        a = "According to your input the best crop to harvest would be snake gourd "
        print (a)
   
    elif (name[crp[0]] == 'Water melon'):
        a = "According to your input the best crop to harvest would be Water melon "
        print (a)

    elif (name[crp[0]] == 'muskmelon'):
        a = "According to your input the best crop to harvest would be muskmelon "
        print (a)

    elif (name[crp[0]] == 'cauli flower'):
        a = "According to your input the best crop to harvest would be cauli flower"
        print (a)

    print ("According to your input the best crop to harvest would be: ", name[crp[0]])
    
else:
    X_1 = pbset2.iloc[:,0:13].values
    Y_1 = pblabels.iloc[:,:].values
    tm = pd.read_csv("C:\\Users\\Antik\\Desktop\\Tech-Master-5-master\\Finaltamil.csv")
    X_train_1,X_test_1,Y_train_1,Y_test_1= train_test_split(X_1,Y_1,test_size=0)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train_1,Y_train_1)
    climate = int(input("Enter the average temperature in celcius: "))
    print ("Enter the soil type: ")
    print ("0 for Alluvial soil: ")
    print ("1 for Black soil: ")
    print ("2 for Laterite soil: ")
    print ("3 for Marshy soil: ")
    print ("4 for Red soil: ")
    soiltype = int(input(('Enter your option: ') ))
    rainfall = int(input("Enter the rainfall in mm in your region: "))
    nitrogen_nutri = int(input("Enter the nitrogen content in kg/ha: "))
    print("Enter the season: ")
    print("0 for kharif: ")
    print("1 for rabi: ")
    print("2 for year long: ")
    season = int(input("Enter your choice: "))
    if (season==0):
        if(soiltype==0):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,1,0,0,0,0,1]]))
        elif(soiltype==1):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,1,0,0,0,1]])) 
        elif(soiltype==2):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,1,0,0,1]]))
        elif(soiltype==3):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,0,1,0,1]]))
        elif(soiltype==4):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,1,0,0,0,0,0,1,1]]))
    else:
        if(soiltype==0):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,1,0,0,0,0,0]]))
        elif(soiltype==1):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,1,0,0,0,0]]))
        elif(soiltype==2):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,1,0,0,0]]))
        elif(soiltype==3):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,0,1,0,0]]))
        elif(soiltype==4):
                crp = (clf.predict([[climate,rainfall,nitrogen_nutri,0,1,0,0,0,0,1,0]]))
    name = dataset['crop']
    if (name[crp[0]] == 'maize'):
        a = "According to your input the best crop to harvest would be maize or potatoes or tomatoes"
        print (a)
    
    elif (name[crp[0]] == 'cotton'):
        a = "According to your input the best crop to harvest would be cotton or sugarcane or jute"
        print (a)
    
    elif (name[crp[0]] == 'wheat'):
        a = "According to your input the best crop to harvest would be wheat or cotton"
        print (a)

    elif (name[crp[0]] == 'paddy'):
        a = "According to your input the best crop to harvest would be paddy or sugarcane or millet or groundnut or ragi"
        print (a)

    elif (name[crp[0]] == 'barley'):
        a = "According to your input the best crop to harvest would be barley or potato"
        print(a)
    elif (name[crp[0]] == 'finger millet'):
        a = "According to your input the best crop to harvest would be finger millet or ground nut or ragi"
        print (a)
    
    elif (name[crp[0]] == 'green gram'):
        a = "According to your input the best crop to harvest would be green gram or millet"
        print (a)

    elif (name[crp[0]] == 'tea'):
        a = "According to your input the best crop to harvest would be tea"
        print (a)
    
    elif (name[crp[0]] == 'chillies'):
        a = "According to your input the best crop to harvest would be chillies or rice or wheat or sugarcane"
        print (a)
    
    elif (name[crp[0]] == 'turmeric'):
        a = "According to your input the best crop to harvest would be turmeric"
        print (a)

    elif (name[crp[0]] == 'sugar cane'):
        a = "According to your input the best crop to harvest would be sugar cane or wheat or cotton or jute "
        print (a)

    elif (name[crp[0]] == 'jute'):
        a = "According to your input the best crop to harvest would be jute or wheat or cotton "
        print (a)

    elif (name[crp[0]] == 'sorghum'):
        a = "According to your input the best crop to harvest would be sorghum or cotton or pearl millet "
        print (a)
    
    elif (name[crp[0]] == 'bajra'):
        a = "According to your input the best crop to harvest would be bajra or wheat or sugarcane "
        print (a)
    
    elif (name[crp[0]] == 'red gram'):
        a = "According to your input the best crop to harvest would be red gram or Bengal gram "
        print (a)
    
    elif (name[crp[0]] == 'black gram'):
        a = "According to your input the best crop to harvest would be black gram or red gram or bengal gram "
        print (a)
    
    elif (name[crp[0]] == 'sesame'):
        a = "According to your input the best crop to harvest would be sesame or sunflower or soyabeans "
        print (a)

    elif (name[crp[0]] == 'sweet potato'):
        a = "According to your input the best crop to harvest would be sweet potato or beans or peas "
        print (a)

    elif (name[crp[0]] == 'mustard'):
        a = "According to your input the best crop to harvest would be mustard or wheat or barley "
        print (a)

    elif (name[crp[0]] == 'soyabean'):
        a = "According to your input the best crop to harvest would be soyabean or sunflower or sesame "
        print (a)

    elif (name[crp[0]] == 'lin seed'):
        a = "According to your input the best crop to harvest would be lin seed or wheat or rice"
        print (a)
    
    elif (name[crp[0]] == 'niger'):
        a = "According to your input the best crop to harvest would be niger "
        print (a)

    elif (name[crp[0]] == 'capsicum'):
        a = "According to your input the best crop to harvest would be capsicum "
        print (a)
    
    elif (name[crp[0]] == 'cucumber'):
        a = "According to your input the best crop to harvest would be cucumber "
        print (a)
       
    elif (name[crp[0]] == 'ridge gourd'):
        a = "According to your input the best crop to harvest would be ridge gourd "
        print (a)
       
    elif (name[crp[0]] == 'bottle gourd'):
        a = "According to your input the best crop to harvest would be bottle gourd "
        print (a)
       
    elif (name[crp[0]] == 'snake gourd'):
        a = "According to your input the best crop to harvest would be snake gourd "
        print (a)
   
    elif (name[crp[0]] == 'Water melon'):
        a = "According to your input the best crop to harvest would be Water melon "
        print (a)

    elif (name[crp[0]] == 'muskmelon'):
        a = "According to your input the best crop to harvest would be muskmelon "
        print (a)

    elif (name[crp[0]] == 'cauli flower'):
        a = "According to your input the best crop to harvest would be cauli flower"
        print (a)

    print ("According to your input the best crop to harvest would be: ", name[crp[0]])
    
'''message = client.messages.create (
        body=a,
        from_ = "+14797633931",
        to = "+919007488686"
        )
print(message.sid)'''
