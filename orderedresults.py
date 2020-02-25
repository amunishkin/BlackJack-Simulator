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
prob = np.zeros((18,10))
hit = np.zeros((18,10))
with open('results.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    
    for i, row in enumerate(csv_reader):
        val_player = float(row[1])
        val_dealer = float(row[2])
        val_soft = float(row[3])
        val_hit = float(row[4])
        probability = float(row[5])
        #print(float(row[1]))
        if val_player == 4.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play4:
                play4.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[0][int(val_dealer)-2]:
                    prob[0][int(val_dealer)-2] =  round(probability,2)
                    hit[0][int(val_dealer)-2] = val_hit
                    w4.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w4.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 5.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play5:
                play5.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[1][int(val_dealer)-2]:
                    prob[1][int(val_dealer)-2] =  round(probability,2)
                    hit[1][int(val_dealer)-2] = val_hit
                    w5.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w5.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 6.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play6:
                play6.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[2][int(val_dealer)-2]:
                    prob[2][int(val_dealer)-2] =  round(probability,2)
                    hit[2][int(val_dealer)-2] = val_hit
                    w6.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w6.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 7.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play7:
                play7.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[3][int(val_dealer)-2]:
                    prob[3][int(val_dealer)-2] =  round(probability,2)
                    hit[3][int(val_dealer)-2] = val_hit
                    w7.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w7.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 8.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play8:
                play8.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[4][int(val_dealer)-2]:
                    prob[4][int(val_dealer)-2] =  round(probability,2)
                    hit[4][int(val_dealer)-2] = val_hit
                    w8.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w8.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 9.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play9:
                play9.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[5][int(val_dealer)-2]:
                    prob[5][int(val_dealer)-2] =  round(probability,2)
                    hit[5][int(val_dealer)-2] = val_hit
                    w9.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w9.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 10.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play10:
                play10.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[6][int(val_dealer)-2]:
                    max10 = probability
                    prob[6][int(val_dealer)-2] =  round(probability,2)
                    hit[6][int(val_dealer)-2] = val_hit
                    w10.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w10.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 11.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play11:
                play11.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[7][int(val_dealer)-2]:
                    prob[7][int(val_dealer)-2] =  round(probability,2)
                    hit[7][int(val_dealer)-2] = val_hit
                    w11.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w11.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 12.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play12:
                play12.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[8][int(val_dealer)-2]:
                    #print(val_dealer)
                    #print(probability)
                    prob[8][int(val_dealer)-2] =  round(probability,2)
                    hit[8][int(val_dealer)-2] = val_hit
                    w12.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w12.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 13.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play13:
                play13.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[9][int(val_dealer)-2]:
                    prob[9][int(val_dealer)-2] =  round(probability,2)
                    hit[9][int(val_dealer)-2] = val_hit
                    w13.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w13.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 14.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play14:
                play14.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[10][int(val_dealer)-2]:
                    prob[10][int(val_dealer)-2] =  round(probability,2)
                    hit[10][int(val_dealer)-2] = val_hit
                    w14.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w14.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 15.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play15:
                play15.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[11][int(val_dealer)-2]:
                    prob[11][int(val_dealer)-2] =  round(probability,2)
                    hit[11][int(val_dealer)-2] = val_hit
                    w15.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w15.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 16.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play16:
                play16.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[12][int(val_dealer)-2]:
                    prob[12][int(val_dealer)-2] =  round(probability,2)
                    hit[12][int(val_dealer)-2] = val_hit
                    w16.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w16.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 17.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play17:
                play17.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[13][int(val_dealer)-2]:
                    prob[13][int(val_dealer)-2] =  round(probability,2)
                    hit[13][int(val_dealer)-2] = val_hit
                    w17.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w17.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 18.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play18:
                play18.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[14][int(val_dealer)-2]:
                    prob[14][int(val_dealer)-2] =  round(probability,2)
                    hit[14][int(val_dealer)-2] = val_hit
                    w18.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w18.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 19.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play19:
                play19.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[15][int(val_dealer)-2]:
                    prob[15][int(val_dealer)-2] =  round(probability,2)
                    hit[15][int(val_dealer)-2] = val_hit
                    w19.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w19.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 20.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play20:
                play20.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[16][int(val_dealer)-2]:
                    prob[16][int(val_dealer)-2] =  round(probability,2)
                    hit[16][int(val_dealer)-2] = val_hit
                    w20.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w20.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
        elif val_player == 21.0:
            if [val_player,val_dealer,val_soft,val_hit] not in play21:
                play21.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob[17][int(val_dealer)-2]:
                    prob[17][int(val_dealer)-2] =  round(probability,2)
                    hit[17][int(val_dealer)-2] = val_hit
                    w21.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"I"])
                else:
                    w21.writerow([val_player,val_dealer,val_soft,val_hit,probability,winlist[i],"O"])
player_label = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
dealer_label = ["2","3","4","5","6","7","8","9","10","A"]

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

plt.figure(2)
fig, ax = plt.subplots()
im = ax.imshow(prob)

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
        text = ax.text(j, i, prob[i, j],
                       ha="center", va="center", color="w")                  

ax.set_title("Probability of Winning in Blackjack with Hit or Not Hit and Ace or No Ace")
#fig.tight_layout()
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