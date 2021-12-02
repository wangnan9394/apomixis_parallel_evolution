# -*- coding: utf-8 -*-
"""
Created on March 22 2021

@author: Nan
"""
import re
import vcf
import argparse

parser = argparse.ArgumentParser(description = 'For citrus', add_help = False, usage = '\npython3 -i [input file from step1] -l [sample list] -o [output.file]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input file from step1]', help = 'input file from step1', required = True)
required.add_argument('-l', '--list', metavar = '[sample list]', help = 'sample list', required = True)
required.add_argument('-o', '--output', metavar = '[output.file]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

def step2(inputfile,outfile):
    out=open(outfile,"w")
    L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]
    for i in range(1,10):
        list=[]
        with open(inputfile,'r') as f:
            fd=f.readlines()
            first_line=fd[0]
            order=first_line.replace("\n",'').split()[1]##primary_statement
            pos='chr'+str(i)+'_1'
            one=[pos,order]
            list.append(one)
        with open(inputfile,'r') as f:    
            for line in f:
                line=line.replace("\n",'').split()
                if 'chr'+str(i) in line[0]:
                    list.append(line)
                    last_order=line[1]
            last_pos='chr'+str(i)+'_'+str(L[i-1])
            last=[last_pos,last_order]
            list.append(last)

        list_type=[]
        order=list[0][1]
        for num,i in enumerate(list):
            if i[1]==order:
                list_type.append(i)
            else:
                if len(list_type)>0:
                    #print(list_type[0],list_type[-1])
                    ll=list_type[0][0].split('_')[0]+'\t'+list_type[0][0].split('_')[1]+'\t'+list_type[-1][0].split('_')[1]+'\t'+list_type[-1][1]+'\n'
                    #print(ll)
                    out.write(ll)
                order=i[1]
                list_type=[]
                list_type.append(i)
        ll2=list_type[0][0].split('_')[0]+'\t'+list[-2][0].split('_')[1]+'\t'+last[0].split('_')[1]+'\t'+last[1]+'\n'
        out.write(ll2)

test=[]
with open(args.list,'r') as f_tree:
    for each in f_tree:
        each=each.replace("\n","").split('\t')[0]
        test.append(each)

for i in test:
    step2(i,i+".out.R.txt")


