import seaborn as sns
import numpy as np
import csv
import operator
import matplotlib.pyplot as plt 

p2=open("card2.csv", 'w')
p3=open("card3.csv", 'w')
p4=open("card4.csv", 'w')
p5=open("card5.csv", 'w')
p6=open("card6.csv", 'w')
p7=open("card7.csv", 'w')
p8=open("card8.csv", 'w')
p9=open("card9.csv", 'w')
p10=open("card10.csv", 'w')
p11=open("card11.csv", 'w')
p12=open("card12.csv", 'w')
p13=open("card13.csv", 'w')
p14=open("card14.csv", 'w')
p15=open("card15.csv", 'w')
p16=open("card16.csv", 'w')
p17=open("card17.csv", 'w')
p18=open("card18.csv", 'w')
p19=open("card19.csv", 'w')
p20=open("card20.csv", 'w')
p21=open("card21.csv", 'w')
w2 = csv.writer(p2)
w3 = csv.writer(p3)
w4 = csv.writer(p4)
w5 = csv.writer(p5)
w6 = csv.writer(p6)
w7 = csv.writer(p7)
w8 = csv.writer(p8)
w9 = csv.writer(p9)
w10 = csv.writer(p10)
w11 = csv.writer(p11)
w12 = csv.writer(p12)
w13 = csv.writer(p13)
w14 = csv.writer(p14)
w15 = csv.writer(p15)
w16 = csv.writer(p16)
w17 = csv.writer(p17)
w18 = csv.writer(p18)
w19 = csv.writer(p19)
w20 = csv.writer(p20)
w21 = csv.writer(p21)

play4 = []
play5 = []
play6 = []
play7 = []
play8 = []
play9 = []
play10 = []
play11 =[]
play12 = []
play13 = []
play14 = []
play15 = []
play16 = []
play17 = []
play18 = []
play19 = []
play20 = []
play21 = []

winlist =[]

max4 = 0
max5 = 0
max6 = 0
max7 = 0
max8 = 0
max9 = 0
max10 = 0
max11 = 0
max12 = 0
max13 = 0
max14 = 0
max15 = 0
max16 = 0
max17 = 0
max18 = 0
max19 = 0
max20 = 0
max21 = 0

with open('correct_action.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        winlist.append(int(row[0]))

#print(winlist)
prob1 = np.zeros((18,10))                                           # 2D array for finding max of probabilities 
prob2 = np.zeros((18,10))                                           # 2D array for finding mean of probabilites
hit = np.zeros((18,10))                                                 # 2D array for storing 1-Hit and 0-Stand
cntr = np.zeros((18,10))                                               # 2D array to keep count for mean computation
with open('results.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    
    for i, row in enumerate(csv_reader):
        val_player = float(row[1])
        val_dealer = float(row[2])
        val_soft = float(row[3])
        val_hit = float(row[4])
        probability = float(row[5])
        if val_player == 4.0:
            prob2[0][int(val_dealer)-2] =  prob2[0][int(val_dealer)-2] + probability 
            cntr[0][int(val_dealer)-2] = cntr[0][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play4:
                play4.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[0][int(val_dealer)-2]:
                    prob1[0][int(val_dealer)-2] =  round(probability,2)
                    hit[0][int(val_dealer)-2] = val_hit
                    w4.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 5.0:
            prob2[1][int(val_dealer)-2] =  prob2[1][int(val_dealer)-2] + probability
            cntr[1][int(val_dealer)-2] = cntr[1][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play5:
                play5.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[1][int(val_dealer)-2]:
                    prob1[1][int(val_dealer)-2] =  round(probability,2)
                    hit[1][int(val_dealer)-2] = val_hit
                    w5.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 6.0:
            prob2[2][int(val_dealer)-2] =  prob2[2][int(val_dealer)-2] + probability
            cntr[2][int(val_dealer)-2] = cntr[2][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play6:
                play6.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[2][int(val_dealer)-2]:
                    prob1[2][int(val_dealer)-2] =  round(probability,2)
                    hit[2][int(val_dealer)-2] = val_hit
                    w6.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 7.0:
            prob2[3][int(val_dealer)-2] =  prob2[3][int(val_dealer)-2] + probability
            cntr[3][int(val_dealer)-2] = cntr[3][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play7:
                play7.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[3][int(val_dealer)-2]:
                    prob1[3][int(val_dealer)-2] =  round(probability,2)
                    hit[3][int(val_dealer)-2] = val_hit
                    w7.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 8.0:
            prob2[4][int(val_dealer)-2] =  prob2[4][int(val_dealer)-2] + probability
            cntr[4][int(val_dealer)-2] = cntr[4][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play8:
                play8.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[4][int(val_dealer)-2]:
                    prob1[4][int(val_dealer)-2] =  round(probability,2)
                    hit[4][int(val_dealer)-2] = val_hit
                    w8.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 9.0:
            prob2[5][int(val_dealer)-2] =  prob2[5][int(val_dealer)-2] + probability
            cntr[5][int(val_dealer)-2] = cntr[5][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play9:
                play9.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[5][int(val_dealer)-2]:
                    prob1[5][int(val_dealer)-2] =  round(probability,2)
                    hit[5][int(val_dealer)-2] = val_hit
                    w9.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 10.0:
            prob2[6][int(val_dealer)-2] =  prob2[6][int(val_dealer)-2] + probability
            cntr[6][int(val_dealer)-2] = cntr[6][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play10:
                play10.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[6][int(val_dealer)-2]:
                    max10 = probability
                    prob1[6][int(val_dealer)-2] =  round(probability,2)
                    hit[6][int(val_dealer)-2] = val_hit
                    w10.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 11.0:
            prob2[7][int(val_dealer)-2] =  prob2[7][int(val_dealer)-2] + probability
            cntr[7][int(val_dealer)-2] = cntr[7][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play11:
                play11.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[7][int(val_dealer)-2]:
                    prob1[7][int(val_dealer)-2] =  round(probability,2)
                    hit[7][int(val_dealer)-2] = val_hit
                    w11.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 12.0:
            prob2[8][int(val_dealer)-2] =  prob2[8][int(val_dealer)-2] + probability
            cntr[8][int(val_dealer)-2] = cntr[8][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play12:
                play12.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[8][int(val_dealer)-2]:
                    #print(val_dealer)
                    #print(probability)
                    prob1[8][int(val_dealer)-2] =  round(probability,2)
                    hit[8][int(val_dealer)-2] = val_hit
                    w12.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 13.0:
            prob2[9][int(val_dealer)-2] =  prob2[9][int(val_dealer)-2] + probability
            cntr[9][int(val_dealer)-2] = cntr[9][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play13:
                play13.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[9][int(val_dealer)-2]:
                    prob1[9][int(val_dealer)-2] =  round(probability,2)
                    hit[9][int(val_dealer)-2] = val_hit
                    w13.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 14.0:
            prob2[10][int(val_dealer)-2] =  prob2[10][int(val_dealer)-2] + probability
            cntr[10][int(val_dealer)-2] = cntr[10][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play14:
                play14.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[10][int(val_dealer)-2]:
                    prob1[10][int(val_dealer)-2] =  round(probability,2)
                    hit[10][int(val_dealer)-2] = val_hit
                    w14.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 15.0:
            prob2[11][int(val_dealer)-2] =  prob2[11][int(val_dealer)-2] + probability
            cntr[11][int(val_dealer)-2] = cntr[11][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play15:
                play15.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[11][int(val_dealer)-2]:
                    prob1[11][int(val_dealer)-2] =  round(probability,2)
                    hit[11][int(val_dealer)-2] = val_hit
                    w15.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 16.0:
            prob2[12][int(val_dealer)-2] =  prob2[12][int(val_dealer)-2] + probability
            cntr[12][int(val_dealer)-2] = cntr[12][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play16:
                play16.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[12][int(val_dealer)-2]:
                    prob1[12][int(val_dealer)-2] =  round(probability,2)
                    hit[12][int(val_dealer)-2] = val_hit
                    w16.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 17.0:
            prob2[13][int(val_dealer)-2] =  prob2[13][int(val_dealer)-2] + probability
            cntr[13][int(val_dealer)-2] = cntr[13][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play17:
                play17.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[13][int(val_dealer)-2]:
                    prob1[13][int(val_dealer)-2] =  round(probability,2)
                    hit[13][int(val_dealer)-2] = val_hit
                    w17.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 18.0:
            prob2[14][int(val_dealer)-2] =  prob2[14][int(val_dealer)-2] + probability
            cntr[14][int(val_dealer)-2] = cntr[14][int(val_dealer)-2] + 1
        
            if [val_player,val_dealer,val_soft,val_hit] not in play18:
                play18.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[14][int(val_dealer)-2]:
                    prob1[14][int(val_dealer)-2] =  round(probability,2)
                    hit[14][int(val_dealer)-2] = val_hit
                    w18.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 19.0:
            prob2[15][int(val_dealer)-2] =  prob2[15][int(val_dealer)-2] + probability
            cntr[15][int(val_dealer)-2] = cntr[15][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play19:
                play19.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[15][int(val_dealer)-2]:
                    prob1[15][int(val_dealer)-2] =  round(probability,2)
                    hit[15][int(val_dealer)-2] = val_hit
                    w19.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 20.0:
            prob2[16][int(val_dealer)-2] =  prob2[16][int(val_dealer)-2] + probability
            cntr[16][int(val_dealer)-2] = cntr[16][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play20:
                play20.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[16][int(val_dealer)-2]:
                    prob1[16][int(val_dealer)-2] =  round(probability,2)
                    hit[16][int(val_dealer)-2] = val_hit
                    w20.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
        elif val_player == 21.0:
            prob2[17][int(val_dealer)-2] =  prob2[17][int(val_dealer)-2] + probability
            cntr[17][int(val_dealer)-2] = cntr[17][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play21:
                play21.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob1[17][int(val_dealer)-2]:
                    prob1[17][int(val_dealer)-2] =  round(probability,2)
                    hit[17][int(val_dealer)-2] = val_hit
                    w21.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i]])
                    
player_label = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
dealer_label = ["2","3","4","5","6","7","8","9","10","A"]

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        prob2[i][j] = round(prob2[i][j]/cntr[i][j],2)
        print(str(prob2[i][j]) + " ", end =" ")
    print("")

plt.figure(1)
fig1, ax1 = plt.subplots()
im1 = ax1.imshow(hit)
ax1.set_xticks(np.arange(len(dealer_label)))
ax1.set_yticks(np.arange(len(player_label)))
ax1.set_xticklabels(dealer_label)
ax1.set_yticklabels(player_label)
ax1.set_xlabel("Dealer's Card",fontsize=16)
ax1.set_ylabel("Player's Card Value",fontsize=16)

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax1.text(j, i, hit[i, j],
                       ha="center", va="center", color="w")       
ax1.set_title("1-Hit, 0-Stand")

plt.figure(2)
fig, ax = plt.subplots()
im = ax.imshow(prob1)

# We want to show all ticks...
ax.set_xticks(np.arange(len(dealer_label)))
ax.set_yticks(np.arange(len(player_label)))
# ... and label them with the respective list entries
ax.set_xticklabels(dealer_label)
ax.set_yticklabels(player_label)
ax.set_xlabel("Dealer's Card",fontsize=16)
ax.set_ylabel("Player's Card Value",fontsize=16)
# Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")
         
# Loop over data dimensions and create text annotations.
for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax.text(j, i, prob1[i, j],
                       ha="center", va="center", color="w")                  
ax.set_title("MAX-Probability of Winning in Blackjack\n with Hit or Not Hit and Ace or No Ace")

plt.figure(3)
fig2, ax2 = plt.subplots()
im2 = ax2.imshow(prob2)
ax2.set_xticks(np.arange(len(dealer_label)))
ax2.set_yticks(np.arange(len(player_label)))
ax2.set_xticklabels(dealer_label)
ax2.set_yticklabels(player_label)
ax2.set_xlabel("Dealer's Card",fontsize=16)
ax2.set_ylabel("Player's Card Value",fontsize=16)

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax2.text(j, i, prob2[i, j],
                       ha="center", va="center", color="w")       
ax2.set_title("MEAN-Probability of Winning in Blackjack\n with Hit or Not Hit and Ace or No Ace")

plt.show()
p2.close()
p3.close()
p4.close()
p5.close()
p6.close()
p7.close()
p8.close()
p9.close()
p10.close()
p11.close()
p12.close()
p13.close()
p14.close()
p15.close()
p16.close()
p17.close()
p18.close()
p19.close()
p20.close()
p21.close()