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
required.add_argument('-i', '--input', metavar = '[input file from step2]', help = 'input file from step2', required = True)
required.add_argument('-l', '--list', metavar = '[sample list]', help = 'sample list', required = True)
required.add_argument('-o', '--output', metavar = '[output.file]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

def step3(inputfile,outfile):
    L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]
    file_name=inputfile

    out_file_name=outfile
    out=open(out_file_name,"w")

    for ind in range(1,10):
        pred_chr='chr'+str(ind)
        list_pos=[]
        list_pos.append(0)
        with open(file_name,"r")as fd:
            dict={}
            for line in fd:
                line=line.replace("\n","").split("\t")
                #print(line)
                chr=line[0]
                if chr==pred_chr:
                    start=int(line[1])
                    end=int(line[2])
                    list_pos.append(start)
                    list_pos.append(end)
                    dict[end]=line[3]

            list_pos.append(L[ind-1])
        #print(list_pos)
        for s in range(len(list_pos)-1):##mix&noraml
            l1=list_pos[s:s+2]
            a=(l1[0]+sum(L[:ind-1])+3000000*(ind-1))*0.0001
            b=(l1[-1]-1+sum(L[:ind-1])+3000000*(ind-1))*0.0001
            if (s % 2) == 0:
                l1='chr'+str(ind)+'\t'+str(a)+'\t'+str(b)+'\t'+'noraml'+'\n'
            else:
                l1='chr'+str(ind)+'\t'+str(a)+'\t'+str(b)+'\t'+dict[l1[1]]+'\n'
            out.write(l1)

test=[]
with open(args.list,'r') as f_tree:
    for each in f_tree:
        each=each.replace("\n","").split('\t')[0]
        test.append(each)

for i in test:
    step2(i,i+".zuotu.txt")