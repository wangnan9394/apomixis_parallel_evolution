# -*- coding: utf-8 -*-
"""
Created on March 22 2021

@author: Nan
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.sandbox.stats.multicomp import multipletests
import argparse

parser = argparse.ArgumentParser(description = 'For mandarin', add_help = False, usage = '\npython3 -i [input.txt] -a [adjust pvalue] -p [pvalue]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[exp_table]', help = 'exp_table', required = True)
required.add_argument('-p', '--pvalue', metavar = '[pvalue]', help = 'pvalue', required = True)
required.add_argument('-a', '--adjust', metavar = '[adjust pvalue]', help = 'adjust pvalue', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()
def fdr(p_vals):
    from scipy.stats import rankdata
    ranked_p_values = rankdata(p_vals)
    fdr = p_vals * len(p_vals) / ranked_p_values
    fdr[fdr > 1] = 1
    return fdr

out=open(args.pvalue,'w')
out_p_adjust2=open(args.adjust,'w')
with open(args.input,"r") as f:
    fd=f.readlines()
    fd=fd[1:]
    count=0
    list_p=[]
    l0=''
    for line1 in fd:
        count+=1
        line=line1.replace("\n","").split("\t")
        #print(line)
        list1=line[1:4]
        list2=line[7:10]
        list1=np.array([float(i) for i in list1])
        list2=np.array([float(i) for i in list2])
        #print(list1)
        #print(list2)
        t_out=stats.ttest_ind(list1,list2,equal_var=False)
        p=t_out[1]
        #print(p)
        list_p.append(p)
        l0=str(p)+'\n'
        out.write(l0)
    p_value=np.array(list_p)
    #p_adjust1=fdr(p_value)#####方法一
    p_adjust2 = multipletests(p_value, alpha=0.05,method='fdr_bh')#####方法二
    l1=''
    l2=''
    #for each in p_adjust1:
    #    l1=str(each)+'\n'
    #    out_p_adjust1.write(l1)
    for each in p_adjust2[0]:
        l2=str(each)+'\n'
        out_p_adjust2.write(l2)