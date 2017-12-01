#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, with_statement
import csv, os
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats

proj_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"

subjects = ['001', '002', '003', '004', '005', '006', '008', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027']

for subj in subjects:
    ss_path = os.path.join(proj_dir,'Raw_Behave',subj+'data.txt')
    with open(ss_path) as ss_data:
        reader = csv.reader(ss_data, delimiter="\t")
        ss_data = list(reader)
        ss_data = np.array(ss_data)

    # Setup correct vectors for all correct trials
    cor_mat=[] # all correct matching trials
    cor_cat=[] # all correct classification trials

    for row in xrange(len(ss_data)):
        answer = str(ss_data[row][16]) #feedback text
        phase = int(ss_data[row][2]) # 1 - matching, 2 - classification
        if answer == "Correct" or answer == "Correct. The correct category is 'A'." or answer == "Correct. The correct category is 'B'.":
            if phase == 1:
                cor_mat.append(1)
            else:
                cor_cat.append(1)
        elif answer == "Failed to respond" or answer == "Failed to respond. The correct category is 'A'." or answer == "Failed to respond. The correct category is 'B'.":
            if phase == 1:
                cor_mat.append(9) # NA
            else:
                cor_cat.append(9) # NA
        else:
            if phase == 1:
                cor_mat.append(0)
            else:
                cor_cat.append(0)

    # Now go through the classification correct vector and select only trials where more than 3 correct
    att_cor_cat=np.zeros((len(cor_cat),2))
    cor_mat_np=np.zeros((len(cor_mat),2))
    cor_mat_np[:,0]=cor_mat
    cor_mat_np[:,1]=cor_mat

    #Create a list of trial stimuli
    trial_stim=ss_data[np.where(ss_data[:,2]=="2"),7][0]
    labels=ss_data[np.where(ss_data[:,2]=="2"),16][0]
    labels=[labels[i][-3] for i in xrange(len(labels))]

    # set a function that selects what rules could be used for a specific choice
    def rule_select(trial,label):
        rset1=[4,3,2,1]
        rset2=[8,7,6,5]
        keep_rules=[]

        for j in xrange(len(trial)):
            if label == 'A': #the label is correct for RuleSwitch project, but can be incorrect for other.
                if trial[j] == '1':
                    keep_rules.append(rset1[j])
                else:
                    keep_rules.append(rset2[j])
            else:
                if trial[j] == '2':
                    keep_rules.append(rset1[j])
                else:
                    keep_rules.append(rset2[j])
        return keep_rules

    # loop through rows and select which correct to keep
    for row in range(3,len(cor_cat)):
        trial=trial_stim[row]
        prev_trial=trial_stim[row-1]
        label=labels[row]
        prev_label=labels[row-1]

        if cor_cat[row] == 1 and cor_cat[row-1] == 1 and cor_cat[row-2] == 1 and cor_cat[row-3] == 1:
            att_cor_cat[row]=[1,1]
            att_cor_cat[row-1]=[1,1]
            att_cor_cat[row-2]=[1,1]
            att_cor_cat[row-3]=[1,1]
            cur_rules = rule_select(trial,label)
            prev_rules = rule_select(prev_trial,prev_label)
            rules_keep = list(set(prev_rules) & set(cur_rules))
            if len(rules_keep)==0:
                att_cor_cat[row]=[0,0]

        elif cor_cat[row] == 0 and (att_cor_cat[row-1] == np.array([1.,1.])).all():
            cur_rules = rule_select(trial,label)
            prev_rules = rule_select(prev_trial,prev_label)
            rules_keep = list(set(prev_rules) & set(cur_rules))
            if len(rules_keep)>0:
                att_cor_cat[row]=[1,0]

        elif cor_cat[row] == 9:
            att_cor_cat[row]=[9,9]

    for row in xrange(3):
        if cor_cat[row] == 9:
            att_cor_cat[row]=[9,9]

    # Vstack the correct arrays
    all_cor="error"
    if int(ss_data[0][2]) == 1: #matching first
        all_cor=np.vstack((cor_mat_np,att_cor_cat))
    elif int(ss_data[0][2]) == 2: #classification first
        all_cor=np.vstack((att_cor_cat,cor_mat_np))

    #Now create EVs from the vectors
    for run in xrange(int(len(ss_data)/32)):
        ev1=[] #stimuli correct onsets
        ev2=[] #stimuli incorrect onsets
        ev3=[] #NAs stimuli
        ev4=[] #feedback correct onsets
        ev5=[] #feedback incorrect onsets
        ev6=[] #NAs feedback
        ev7=[] #cor modulator
        ev8=[] #incor modulator
        for row in xrange(len(ss_data)):
            if run == int(ss_data[row][30]):
                answer_ons = int(all_cor[row][0])
                answer_fdb = int(all_cor[row][1])
                if answer_ons == 1:
                    ev1.append(str(ss_data[row][17])+" 1 1")
                    ev7.append(str(ss_data[row][17])+" 1 "+str(ss_data[row][15]))
                if answer_ons == 0:
                    ev2.append(str(ss_data[row][17])+" 1 1")
                    ev8.append(str(ss_data[row][17])+" 1 "+str(ss_data[row][15]))
                if answer_ons == 9:
                    ev3.append(str(ss_data[row][17])+" 1 1")
                    ev6.append(str(ss_data[row][26])+" 1 1")
                if answer_fdb == 1:
                    ev4.append(str(ss_data[row][26])+" 1 1")
                if answer_fdb == 0:
                    ev5.append(str(ss_data[row][26])+" 1 1")


        #save the data
        if ev1==[]:
            ev1=['0 0 0']
        if ev2==[]:
            ev2=['0 0 0']
        if ev3==[]:
            ev3=['0 0 0']
        if ev4==[]:
            ev4=['0 0 0']
        if ev5==[]:
            ev5=['0 0 0']
        if ev6==[]:
            ev6=['0 0 0']
        if ev7==[]:
            ev7=['0 0 0']
        if ev8==[]:
            ev8=['0 0 0']

        write_path = "/mnt/net/LaCie/Dmitrii/repos/rules/univariate/univar1a_LearnApply_rt/behave/source_files/"

        for evar in ev1:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev1_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev2:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev2_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev3:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev3_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev4:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev4_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev5:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev5_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev6:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev6_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev7:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev7_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        for evar in ev8:
            data = str(evar)+'\n'
            data_file=open(write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev8_run"+str(run+1)+".txt",'a')
            data_file.write(data)
            data_file.close()

        #z-score modulators
        f_name = write_path+"Subject"+subj+"_univar1a_LearnApply_rt_ev7_run"+str(run+1)+".txt"
        df = pd.read_csv(f_name, sep=' ', header=None)
        df.columns = ['onset', 'duration', 'modulator']
        if df['modulator'][0] != 0:
            z_mod = stats.mstats.zscore(df['modulator'])
            df['modulator'] = z_mod
            df.to_csv(f_name, header=False, index=False, sep=' ', mode='w')

        f_name = write_path + "Subject" + subj + "_univar1a_LearnApply_rt_ev8_run" + str(run + 1) + ".txt"
        df = pd.read_csv(f_name, sep=' ', header=None)
        df.columns = ['onset', 'duration', 'modulator']
        if df['modulator'][0] != 0:
            z_mod = stats.mstats.zscore(df['modulator'])
            df['modulator'] = z_mod
            df.to_csv(f_name, header=False, index=False, sep=' ', mode='w')
