# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 02:31:06 2019

@author: Antik
"""

N = int(input("Enter the Nitrogen content: "))
P = int(input("Enter the Phosphorous content: "))
K = int(input("Enter the Potassium content: "))
if ((N<=46)and(P<=10)and(K<=15)):
    print("Less Phosphorous and Potassium, Add Urea")

elif ((N<=34)and(P<=12)and(K<=14)):
    print("Less Phosphorous and Potassium, Add Ammonium Nitrate")

elif ((N<=34)and(P<=7)and(K<=11)):
    print("Less Phosphorous and Potassium, Add Ammonium Sulphate Urea")

elif ((N<=21)and(P<=13)and(K<=11)):
    print("Less Phosphorous and Potassium, Add Ammonium Sulphate")

elif ((N<=82)and(P<=10)and(K<=10)):
    print("Less Phosphorous and Potassium High Nitrogen, Add Anhydrous Sulphate")
    
elif ((N<=28)and(P<=9)and(K<=11)):
    print("Less Phosphorous and Potassium, Add Urea-Ammonium Nitrate")
elif ((N<=12)and(P<=51)and(K<=10)):
    print("Less Nitrogen and Potassium, Add Mono-Ammonium Phosphate")
    
elif ((N<=10)and(P<=34)and(K<=12)):
    print("Less Nitrogen and Potassium, Add Ammonium Polyphosphate Solution")

elif ((N<=16)and(P<=20)and(K<=15)):
    print("Less Nitrogen and Potassium, Add Ammonium phosphate Sulphate")

elif ((N<=27)and(P<14)and(K<=13)):
    print("Less Phosphorous and Potassium, Add Ammonium Nitrate Phosphate")
    
elif ((N<=34)and(P<=17)and(K<=15)):
    print("Less Phosphorous and Potassium, Add Urea Ammonium Phosphate")
    
elif ((N<=10)and(P<=15)and(K<=60)):
    print("Less Nitrogen and Phosphorous, HIGH Potassium, Add Potash Chloride")
    
elif ((N<=12)and(P<=11)and(K<=52)):
    print("Less Nitrogen and Phosphorous, HIGH Potassium, Add Potassium Sulphate")
    
elif ((N<=20)and(P<=10)and(K<=15)):
    print("Less  Phosphorous and Potassium, Add Ammonium Sulphate")
    
elif ((N<=10)and(P<=12)and(K<=11)):
    print("Less Nitrogen and Potassium, Add Gypsum")
    
elif ((N<=14)and(P<=15)and(K<=10)):
    print("Less Nitrogen and Potasium, Add Elemental Sulphur")

elif ((N<=12)and(P<=10)and(K<=15)):
    print("Less Nitrogen and Potassium, Add Ammonium Thiosulphate Solution")




        