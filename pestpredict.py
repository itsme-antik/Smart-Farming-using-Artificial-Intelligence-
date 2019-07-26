# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:32:17 2019

@author: Antik
"""
import os
from twilio.rest import Client
from sklearn import tree
account_sid = "AC74c65f66f1de79c6a6b4f9314f161135"
auth_token = "04ca45f4d51b1c9e6dff55d9b786e3e8"

features = [[6,7,24,7.1,24,3,1,2,1],[6,7,24,7.1,24,3,1,2,2],[6,7,24,7.1,24,3,1,2,3],[5.8,6.8,29,12,30,1,2,3,1],
            [5.8,5.8,29,12,30,1,2,3,2],[5.8,5.8,29,12,30,1,2,3,3],[5.8,5.8,29,12,30,1,2,3,4],[5.8,6.8,24,5,20,1,2,3,5],[5,7,29,6,20,3,2,1,6],
            [5,7,29,6,20,3,2,1,7],[5,7,29,6,20,3,2,1,8],[5,7,29,6,20,3,2,1,1],[5.8,7,28,15,21,2,1,4,9],
            [5.8,7,28,15,21,2,1,4,10],[6,7,30,7.2,25,4,3,2,1],[6.3,7,25,5,25,3,2,1,3],[6.3,7,25,5,25,3,2,1,5],
            [6.3,7,25,5,25,3,2,1,5],[6.3,7,25,5,25,2,1,3,1],[6.5,7,24,10,27,2,1,3,1],[6.3,6.8,24,20,26,3,1,4,12]]
labels=['Aphids','Aphids','Aphids','Ballworms','Armyworms','Armyworms','Armyworms','Armyworms','Stem Borrers',
'Thrips','Thrips','Thrips','Thrips','Mealy bug','Mealy bug','Wevil','Mite','Mite','Mite','Scale Insect','Bean leaf bettle']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
a=int(input("Enter the maximum ph level of the soil: "))
b=int(input("Enter the minimum pg level of the soil: "))
c=int(input("Enter the temperature: "))
d=int(input("Enter the Pheromones content: "))
e=int(input("Enter the soil moisture percent: "))
N =int(input("Enter the Nitrogen content: "))
P =int(input("Enter the Phosphorous content: "))
K =int(input("Enter the Potassium content: "))
print("Enter the numbers from (1-12) for the corresponding crop: ")
print("1 --> Cotton")
print("2 --> Barley")
print("3 --> Wheat")
print("4 --> Corn")
print("5 --> Rice")
print("6 --> Tomato")
print("7 --> Onion")
print("8 --> Potatoes")
print("9 --> Sugarcane")
print("10 --> Papaya")
print("11 --> Rice")
print("12 --> Beans")
f=int(input("Enter your choice: "))
fr = clf.predict([[a,b,c,d,e,N,P,K,f]])[0]
                 
if (fr == 'Aphids'):
    pest = "You can use Neem oil or insecticidal soaps"
elif (fr =='Ballworms'):
    pest = "You can use Pyrethroids"
elif (fr =='Armyworms'):
    pest = "You can use pheromone traps"
elif (fr =='Stem Borrers'):
    pest = "You can use Phosalone, Acephate, Azadirachtin etc"
elif (fr == 'Thrips'):
    pest = "You can use horticultural oil, natural pyrethrins"
elif (fr =='Mealy bug'):
    pest = "You can use Neem oil or BotaniGard ES"
elif (fr == 'Wevil'):
    pest = "Take precautions"
elif (fr == 'Mite'):
    pest = "You can use acetamiprid, azadirachtin etc"
elif (fr == 'Scale insect'):
    pest = "Take precautions"
elif (fr == 'Bean leaf bettle'):
    pest = "Take precautions"

str1 = "Your field have chances to be attacked by "+fr
str2 = " "+pest
str3 = str1+str2
    
