# -*- coding: utf-8 -*-
"""Metode K Nearest Neighbors (KNN)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A_WVQMA_k1ZJ6orHn-L0mXE-2T79zkWN
"""

# -*- coding: utf-8 -*-
"""Metode K. Nearest Neighbors (KNN).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YMux9eFISyxOQ9v-OtQVlSPqbh47cuR0
"""

from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# x = Data, Y = Target
x = [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1], [3,0], [3,1], [4,0], [4,1]]
y = [0,0,0,1,0,0,1,0,0,1]

# Training and Classify
clf = NearestCentroid()
clf.fit(x,y)

# Prediksi
print ("Logika AND Metode K. Nearest Neighbors (KNN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("2 0 = ", clf.predict([[2,0]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("3 0 = ", clf.predict([[3,0]]))
print ("3 1 = ", clf.predict([[3,1]]))
print ("4 0 = ", clf.predict([[4,0]]))
print ("4 1 = ", clf.predict([[4,1]]))