# import matplotlib.pyplot as plt


# gun = [1,2,3,4,5,6,7,8,9]
# vaka = [1,3,20,37,68,95,188,294,419]

# plt.figure(figsize=(10,8))
# plt.subplot(2,2,1) #1.Grafik
# plt.plot(gun,vaka)
# plt.xlabel('Gün')
# plt.ylabel('Vaka Sayısı')
# plt.title('Türkiye Korona Viris Grafiği')

# plt.subplot(2,2,2) #2.Grafik

# olum = [0,0,0,0,1,4,9,21,33]
# plt.plot(vaka,olum)


# plt.xlabel('Vaka')
# plt.ylabel('Olum Sayısı')
# plt.title('Türkiye Korona Ölüm Grafiği')
#plt.show()



#BU KISIM EXCELDE VERİ OKUMA DOSYAYI CEKTİK VE MATPLOTLİB İLE GÖRSELLEŞTİRDİK
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os



# Dosyanın adı ve uzantısı
data = pd.read_excel('/Users/fatihsaritas/Desktop/VS Code/sorularVeCözümleri.py/Pythonda Projeler/corona.xlsx')


#print(data.head())


plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.title('Türkiye Korona Viris Grafiği')
plt.xlabel('Gün')
plt.ylabel('Vaka')
plt.plot(data.Tr,data.Vaka)





plt.subplot(2,2,2) #2.Grafik

olum = [0,0,0,0,1,4,9,21,33]
plt.plot(data.Tr,data.Ölüm)


plt.show()
