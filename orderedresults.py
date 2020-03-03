import numpy as np
import csv
import operator
import matplotlib.pyplot as plt 
import math

p2=open("card2.csv", 'w',newline='') #More fixes for Windows
p3=open("card3.csv", 'w',newline='')
p4=open("card4.csv", 'w',newline='')
p5=open("card5.csv", 'w',newline='')
p6=open("card6.csv", 'w',newline='')
p7=open("card7.csv", 'w',newline='')
p8=open("card8.csv", 'w',newline='')
p9=open("card9.csv", 'w',newline='')
p10=open("card10.csv", 'w',newline='')
p11=open("card11.csv", 'w',newline='')
p12=open("card12.csv", 'w',newline='')
p13=open("card13.csv", 'w',newline='')
p14=open("card14.csv", 'w',newline='')
p15=open("card15.csv", 'w',newline='')
p16=open("card16.csv", 'w',newline='')
p17=open("card17.csv", 'w',newline='')
p18=open("card18.csv", 'w',newline='')
p19=open("card19.csv", 'w',newline='')
p20=open("card20.csv", 'w',newline='')
p21=open("card21.csv", 'w',newline='')
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


cntr_data = np.zeros((18,10))                                     # counter for landing in state
cntr_win = np.zeros((18,10))                                       # counter for actual wins
with open('actual_results.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        act_p_val = int(row[0])
        act_d_val = int(row[1])
        win = int(row[4])
        cntr_data[act_p_val-4][act_d_val-2] =  cntr_data[act_p_val-4][act_d_val-2] + 1
        if win == 1:
            cntr_win[act_p_val-4][act_d_val-2] =  cntr_win[act_p_val-4][act_d_val-2] + 1
        
cntr_win = np.multiply(cntr_win,1/cntr_data)
#print(win)
#print(winlist)
prob_max = np.zeros((18,10))                                           # 2D array for finding max of probabilities 
prob_mean = np.zeros((18,10))                                           # 2D array for finding mean of probabilites
hit_max = np.zeros((18,10))                                       # 2D array for storing 1-Hit and 0-Stand
hit_mean = np.zeros((18,10))                                     # 2D array to store hit or not hit based upon mean hitting
hit_cnt = np.zeros((18,10))                                          # 2D array hit counter
cntr = np.zeros((18,10))                                               # 2D array to keep count for mean computation
with open('predicted_results.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')

    for i, row in enumerate(csv_reader):
        val_player = float(row[1])
        val_dealer = float(row[2])
        val_soft = float(row[3])
        val_hit = float(row[4])
        probability = float(row[5])
        if val_player == 4.0:
            prob_mean[0][int(val_dealer)-2] =  prob_mean[0][int(val_dealer)-2] + probability 
            cntr[0][int(val_dealer)-2] = cntr[0][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[0][int(val_dealer)-2] = hit_cnt[0][int(val_dealer)-2] + 1
            
            if [val_player,val_dealer,val_soft,val_hit] not in play4:
                play4.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[0][int(val_dealer)-2]:
                    prob_max[0][int(val_dealer)-2] =  round(probability,2)
                    hit_max[0][int(val_dealer)-2] = val_hit
                    w4.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 5.0:
            prob_mean[1][int(val_dealer)-2] =  prob_mean[1][int(val_dealer)-2] + probability
            cntr[1][int(val_dealer)-2] = cntr[1][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[1][int(val_dealer)-2] = hit_cnt[1][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play5:
                play5.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[1][int(val_dealer)-2]:
                    prob_max[1][int(val_dealer)-2] =  round(probability,2)
                    hit_max[1][int(val_dealer)-2] = val_hit
                    if probability >= 0.52:
                        win_predicted = 1
                    else:
                        win_predicted = 0
                    w5.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 6.0:
            prob_mean[2][int(val_dealer)-2] =  prob_mean[2][int(val_dealer)-2] + probability
            cntr[2][int(val_dealer)-2] = cntr[2][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[2][int(val_dealer)-2] = hit_cnt[2][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play6:
                play6.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[2][int(val_dealer)-2]:
                    prob_max[2][int(val_dealer)-2] =  round(probability,2)
                    hit_max[2][int(val_dealer)-2] = val_hit
                    w6.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 7.0:
            prob_mean[3][int(val_dealer)-2] =  prob_mean[3][int(val_dealer)-2] + probability
            cntr[3][int(val_dealer)-2] = cntr[3][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[3][int(val_dealer)-2] = hit_cnt[3][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play7:
                play7.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[3][int(val_dealer)-2]:
                    prob_max[3][int(val_dealer)-2] =  round(probability,2)
                    hit_max[3][int(val_dealer)-2] = val_hit
                    w7.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 8.0:
            prob_mean[4][int(val_dealer)-2] =  prob_mean[4][int(val_dealer)-2] + probability
            cntr[4][int(val_dealer)-2] = cntr[4][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[4][int(val_dealer)-2] = hit_cnt[4][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play8:
                play8.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[4][int(val_dealer)-2]:
                    prob_max[4][int(val_dealer)-2] =  round(probability,2)
                    hit_max[4][int(val_dealer)-2] = val_hit
                    w8.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 9.0:
            prob_mean[5][int(val_dealer)-2] =  prob_mean[5][int(val_dealer)-2] + probability
            cntr[5][int(val_dealer)-2] = cntr[5][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[5][int(val_dealer)-2] = hit_cnt[5][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play9:
                play9.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[5][int(val_dealer)-2]:
                    prob_max[5][int(val_dealer)-2] =  round(probability,2)
                    hit_max[5][int(val_dealer)-2] = val_hit
                    w9.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 10.0:
            prob_mean[6][int(val_dealer)-2] =  prob_mean[6][int(val_dealer)-2] + probability
            cntr[6][int(val_dealer)-2] = cntr[6][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[6][int(val_dealer)-2] = hit_cnt[6][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play10:
                play10.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[6][int(val_dealer)-2]:
                    max10 = probability
                    prob_max[6][int(val_dealer)-2] =  round(probability,2)
                    hit_max[6][int(val_dealer)-2] = val_hit
                    w10.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 11.0:
            prob_mean[7][int(val_dealer)-2] =  prob_mean[7][int(val_dealer)-2] + probability
            cntr[7][int(val_dealer)-2] = cntr[7][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[7][int(val_dealer)-2] = hit_cnt[7][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play11:
                play11.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[7][int(val_dealer)-2]:
                    prob_max[7][int(val_dealer)-2] =  round(probability,2)
                    hit_max[7][int(val_dealer)-2] = val_hit
                    w11.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 12.0:
            prob_mean[8][int(val_dealer)-2] =  prob_mean[8][int(val_dealer)-2] + probability
            cntr[8][int(val_dealer)-2] = cntr[8][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[8][int(val_dealer)-2] = hit_cnt[8][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play12:
                play12.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[8][int(val_dealer)-2]:

                    prob_max[8][int(val_dealer)-2] =  round(probability,2)
                    hit_max[8][int(val_dealer)-2] = val_hit
                    w12.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 13.0:
            prob_mean[9][int(val_dealer)-2] =  prob_mean[9][int(val_dealer)-2] + probability
            cntr[9][int(val_dealer)-2] = cntr[9][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[9][int(val_dealer)-2] = hit_cnt[9][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play13:
                play13.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[9][int(val_dealer)-2]:
                    prob_max[9][int(val_dealer)-2] =  round(probability,2)
                    hit_max[9][int(val_dealer)-2] = val_hit
                    w13.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 14.0:
            prob_mean[10][int(val_dealer)-2] =  prob_mean[10][int(val_dealer)-2] + probability
            cntr[10][int(val_dealer)-2] = cntr[10][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[10][int(val_dealer)-2] = hit_cnt[10][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play14:
                play14.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[10][int(val_dealer)-2]:
                    prob_max[10][int(val_dealer)-2] =  round(probability,2)
                    hit_max[10][int(val_dealer)-2] = val_hit
                    w14.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 15.0:
            prob_mean[11][int(val_dealer)-2] =  prob_mean[11][int(val_dealer)-2] + probability
            cntr[11][int(val_dealer)-2] = cntr[11][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[11][int(val_dealer)-2] = hit_cnt[11][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play15:
                play15.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[11][int(val_dealer)-2]:
                    prob_max[11][int(val_dealer)-2] =  round(probability,2)
                    hit_max[11][int(val_dealer)-2] = val_hit
                    w15.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 16.0:
            prob_mean[12][int(val_dealer)-2] =  prob_mean[12][int(val_dealer)-2] + probability
            cntr[12][int(val_dealer)-2] = cntr[12][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[12][int(val_dealer)-2] = hit_cnt[12][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play16:
                play16.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[12][int(val_dealer)-2]:
                    prob_max[12][int(val_dealer)-2] =  round(probability,2)
                    hit_max[12][int(val_dealer)-2] = val_hit
                    w16.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 17.0:
            prob_mean[13][int(val_dealer)-2] =  prob_mean[13][int(val_dealer)-2] + probability
            cntr[13][int(val_dealer)-2] = cntr[13][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[13][int(val_dealer)-2] = hit_cnt[13][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play17:
                play17.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[13][int(val_dealer)-2]:
                    prob_max[13][int(val_dealer)-2] =  round(probability,2)
                    hit_max[13][int(val_dealer)-2] = val_hit
                    w17.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 18.0:
            prob_mean[14][int(val_dealer)-2] =  prob_mean[14][int(val_dealer)-2] + probability
            cntr[14][int(val_dealer)-2] = cntr[14][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[14][int(val_dealer)-2] = hit_cnt[14][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play18:
                play18.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[14][int(val_dealer)-2]:
                    prob_max[14][int(val_dealer)-2] =  round(probability,2)
                    hit_max[14][int(val_dealer)-2] = val_hit
                    w18.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 19.0:
            prob_mean[15][int(val_dealer)-2] =  prob_mean[15][int(val_dealer)-2] + probability
            cntr[15][int(val_dealer)-2] = cntr[15][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[15][int(val_dealer)-2] = hit_cnt[15][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play19:
                play19.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[15][int(val_dealer)-2]:
                    prob_max[15][int(val_dealer)-2] =  round(probability,2)
                    hit_max[15][int(val_dealer)-2] = val_hit
                    w19.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 20.0:
            prob_mean[16][int(val_dealer)-2] =  prob_mean[16][int(val_dealer)-2] + probability
            cntr[16][int(val_dealer)-2] = cntr[16][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[16][int(val_dealer)-2] = hit_cnt[16][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play20:
                play20.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[16][int(val_dealer)-2]:
                    prob_max[16][int(val_dealer)-2] =  round(probability,2)
                    hit_max[16][int(val_dealer)-2] = val_hit
                    w20.writerow([val_player,val_dealer,val_soft,val_hit,probability])
        elif val_player == 21.0:
            prob_mean[17][int(val_dealer)-2] =  prob_mean[17][int(val_dealer)-2] + probability
            cntr[17][int(val_dealer)-2] = cntr[17][int(val_dealer)-2] + 1
            if val_hit == 1:
                hit_cnt[17][int(val_dealer)-2] = hit_cnt[17][int(val_dealer)-2] + 1
                
            if [val_player,val_dealer,val_soft,val_hit] not in play21:
                play21.append([val_player,val_dealer,val_soft,val_hit])
                if probability > prob_max[17][int(val_dealer)-2]:
                    prob_max[17][int(val_dealer)-2] =  round(probability,2)
                    hit_max[17][int(val_dealer)-2] = val_hit
                    w21.writerow([val_player,val_dealer,val_soft,val_hit,probability])
                    
player_label = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
dealer_label = ["2","3","4","5","6","7","8","9","10","A"]

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        prob_mean[i][j] = round(prob_mean[i][j]/cntr[i][j],2)
        hitmean = hit_cnt[i][j]/cntr[i][j]
        #print(hitmean)
        if hitmean >= 0.50:
            
            hit_mean[i][j] = 1
        else:
            hit_mean[i][j] = 0
prob_std = np.zeros((18))
    
plt.figure(1)
fig1, ax1 = plt.subplots()
im1 = ax1.imshow(hit_max)
ax1.set_xticks(np.arange(len(dealer_label)))
ax1.set_yticks(np.arange(len(player_label)))
ax1.set_xticklabels(dealer_label)
ax1.set_yticklabels(player_label)
ax1.set_xlabel("Dealer's Card",fontsize=16)
ax1.set_ylabel("Player's Card Value",fontsize=16)

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax1.text(j, i, hit_max[i, j],
                       ha="center", va="center", color="w")       
ax1.set_title("MAX: 1-Hit, 0-Stand")

plt.figure(2)
fig, ax = plt.subplots()
im = ax.imshow(prob_max)

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
        text = ax.text(j, i, prob_max[i, j],
                       ha="center", va="center", color="w")                  
ax.set_title("MAX-Probability of Winning in Blackjack\n with Hit or Not Hit and Ace or No Ace")

plt.figure(3)
fig2, ax2 = plt.subplots()
im2 = ax2.imshow(prob_mean)
ax2.set_xticks(np.arange(len(dealer_label)))
ax2.set_yticks(np.arange(len(player_label)))
ax2.set_xticklabels(dealer_label)
ax2.set_yticklabels(player_label)
ax2.set_xlabel("Dealer's Card",fontsize=16)
ax2.set_ylabel("Player's Card Value",fontsize=16)

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax2.text(j, i, prob_mean[i, j],
                       ha="center", va="center", color="w")       
ax2.set_title("MEAN-Probability of Winning in Blackjack\n with Hit or Not Hit and Ace or No Ace")

plt.figure(4)
fig3, ax3 = plt.subplots()
im3 = ax3.imshow(hit_mean)
ax3.set_xticks(np.arange(len(dealer_label)))
ax3.set_yticks(np.arange(len(player_label)))
ax3.set_xticklabels(dealer_label)
ax3.set_yticklabels(player_label)
ax3.set_xlabel("Dealer's Card",fontsize=16)
ax3.set_ylabel("Player's Card Value",fontsize=16)

for i in range(len(player_label)):
    for j in range(len(dealer_label)):
        text = ax3.text(j, i, hit_mean[i, j],
                       ha="center", va="center", color="w")       
ax3.set_title("MEAN: 1-Hit, 0-Stand")

mean_p_hand=[]
mean_d_hand=[]
mean_p_hand_actual=[]
mean_d_hand_actual=[]
std_p_hand=[]
std_d_hand=[]
std_p_hand_actual=[]
std_d_hand_actual=[]
stdaccum = 0
stdaccum2 = 0
stdaccumd = 0
stdaccum2d = 0
for i in range(len(player_label)):
    mean_p_hand.append(sum(prob_mean[i][0:10])/len(prob_mean[i][0:10]))
    mean_p_hand_actual.append(sum(cntr_win[i][0:10])/len(cntr_win[i][0:10]))
    for j in range(len(dealer_label)):
        stdaccum = stdaccum + (prob_mean[i][j]-mean_p_hand[i])**2
        stdaccum2 = stdaccum2 + (cntr_win[i][j]-mean_p_hand_actual[i])**2
    std_p_hand.append(math.sqrt(stdaccum/10))
    std_p_hand_actual.append(math.sqrt(stdaccum2/10))

for j in range(len(dealer_label)): #  column
    mean_d_hand.append(sum(prob_mean[:,j])/len(prob_mean[:,j]))
    mean_d_hand_actual.append(sum(cntr_win[:,j])/len(cntr_win[:,j]))
    for i in range(len(player_label)): # row
        stdaccumd = stdaccumd + (prob_mean[i,j]-mean_d_hand[j])**2
        stdaccum2d = stdaccum2d + (cntr_win[i,j]-mean_d_hand_actual[j])**2
    std_d_hand.append(math.sqrt(stdaccumd/18))
    std_d_hand_actual.append(math.sqrt(stdaccum2d/18))
    
plt.figure(5)
fig4, ax4 = plt.subplots()
index = np.arange(18)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.4'}

rects1 = plt.bar(index, mean_p_hand, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_p_hand,
                 error_kw=error_config,
                 label='predicted')

rects2 = plt.bar(index + bar_width, mean_p_hand_actual, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=std_p_hand,
                 error_kw=error_config,
                 label='actual')

plt.xlabel('Player Initial Value',fontsize=16)
plt.ylabel('Probability of Tie or Win',fontsize=16)
plt.title('Mean and Standard Deviation \n for Initial Game Configuration ',fontsize=16)
plt.xticks(index + bar_width / 2, ('4', '5', '6', '7', '8','9','10','11','12','13','14','15','16','17','18','19','20','21'))
plt.legend()
plt.tight_layout()

plt.figure(6)
fig5, ax5 = plt.subplots()
index = np.arange(10)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.4'}

print(len(mean_d_hand))
print(len(std_d_hand))
rects1 = plt.bar(index, mean_d_hand, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='predicted')

rects2 = plt.bar(index + bar_width, mean_d_hand_actual, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='actual')

plt.xlabel('Dealer Initial Value',fontsize=16)
plt.ylabel('Probability of Tie or Win',fontsize=16)
plt.title('Mean for Initial Game Configuration ',fontsize=16)
plt.xticks(index + bar_width / 2, ('2', '3', '4', '5', '6','7','8','9','10','A'))
plt.legend()

plt.tight_layout()
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
