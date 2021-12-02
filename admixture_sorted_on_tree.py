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

parser = argparse.ArgumentParser(description = 'For mandarin', add_help = False, usage = '\npython3 -i [admixture Q file] -t [tree_sort_list] -t [admixture_sort_list] ')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[admixture Q file]', help = 'admixture Q file', required = True)
required.add_argument('-t', '--tree', metavar = '[tree_sort_list]', help = 'pvalue', required = True)
required.add_argument('-a', '--admixture', metavar = '[admixture_sort_list]', help = 'admixture_sort_list', required = True)
required.add_argument('-o', '--output', metavar = '[output]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

tree_list=[]
with open(args.tree,'r') as f_tree:
    for each in f_tree:
        each=each.replace("\n","").split('\t')[0]
        tree_list.append(each)

admixture_list=[]
with open(args.admixture,'r') as f_admixture:
    for each in f_admixture:
        each=each.replace("\n","").split('\t')[0]
        admixture_list.append(each)

list=admixture_list
list_sort=tree_list

out_file=open(args.output,'w')
header="sample"+'\t'+"percentage"+'\t'+"component"+'\t'+'sort'+'\n'
out_file.write(header)
with open(args.input,'r') as f:
    count=0
    for line in f:
        line=line.replace("\n","").split(' ')
        len_K=len(line)
        name=list[count]
        sort=list_sort[count]
        for i in range(len_K):
            l0=name+'\t'+line[i]+'\t'+'C'+str(i)+'\t'+str(sort)+'\n'
            out_file.write(l0)
        count+=1