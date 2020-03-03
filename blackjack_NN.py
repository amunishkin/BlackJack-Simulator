import csv
import numpy as np
import matplotlib.pyplot as plt 
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout
valuelist = []
winlist = []
with open('input_features.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        
        valuelist.append([float(row[0]),float(row[1]),int(row[2]),int(row[3])])

with open('actual_results.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        winlist.append([int(row[4])])
    
game_results = []
train_X = np.asarray(valuelist)
#print(train_X)
train_Y = np.asarray(winlist, dtype=np.int).reshape(-1,1)
#print (train_Y)
model = Sequential()
model.add(Dense(128))
model.add(Dense(64))
model.add(Dense(32))
model.add(Dense(16))
model.add(Dense(8))
model.add(Dense(4))
model.add(Dense(2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd')
model.fit(train_X, train_Y, epochs=30, batch_size=256, verbose=1)

pred_Y_train = model.predict(train_X)   

actuals = train_Y[:,-1]
f = open('predicted_results.csv','w',newline='') #Windows fix for python3
w = csv.writer(f)
for i in range(0,len(pred_Y_train)):
    #game_results.append([valuelist[i][0],valuelist[i][1],valuelist[i][2],valuelist[i][3],pred_Y_train[i][0]])
    w.writerow([valuelist[i][0]+valuelist[i][1],valuelist[i][0],valuelist[i][1],valuelist[i][2],valuelist[i][3],pred_Y_train[i][0]])
f.close()
#x = np.arange(1,len(actuals)+1)
#plt.plot(x,actuals) 
#plt.show()
