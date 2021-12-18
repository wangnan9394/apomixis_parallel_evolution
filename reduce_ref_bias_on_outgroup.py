# -*- coding: utf-8 -*-
"""
Created on March 12 2021

@author: Nan
"""

import vcf
import argparse

parser = argparse.ArgumentParser(description = 'For mandarin', add_help = False, usage = '\npython3 -i [input.vcf] -g [outgroup_list] -o [output.vcf]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input_vcf]', help = 'input_vcf', required = True)
required.add_argument('-g', '--group', metavar = '[outgroup_list]', help = 'outgroup_list', required = True)
required.add_argument('-o', '--output', metavar = '[output]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')
args = parser.parse_args()
vcf_reader = vcf.Reader(open(args.input, 'r'))

def rever_SNP(gt):
    if gt=='0/0':
        new_gt='1/1'
    if gt=='0/1':
        new_gt='0/1'
    if gt=='1/1':
        new_gt='0/0'
    if gt =='./.':
        new_gt='./.'
    if gt =='./1':
        new_gt='./0'
    if gt =='./0':
        new_gt='./1'
    if gt =='0/.':
        new_gt='1/.'
    if gt =='1/.':
        new_gt='0/.'
    return new_gt

outGrooup_file=[]
with open(args.group,'r') as outgroup_name:
    for each in outgroup_name:
        each=each.replace("\n","").split('\t')[0]
        outGrooup_file.append(each)

out_vcf=open(args.output,'w')
with open(args.input,'r') as f:#set3.234.deepvariants.vcf
    for line in f:
        if line.startswith('#'):
            out_vcf.write(line)
        else:
            break

for record in vcf_reader:
    #print(record)
    chr=record.CHROM
    pos=record.POS
    id=record.ID
    ref=record.REF
    alt=record.ALT[0]
    qual=record.QUAL
    filter='.'
    info='.'
    format=record.FORMAT
    out_group_freq=0
    for i in outGrooup_file:
        gt=record.genotype(i)['GT'].split('/')
        if '1' in gt:
            out_group_freq+=1
    if out_group_freq >0:
        list=[]
        for i in record.samples:
                index=i['GT']
                new_index=rever_SNP(index)
                list.append(new_index)
        l2=''
        for each in list:
            l2+=each+'\t'
    else:
        list=[]
        for i in record.samples:
            index=i['GT']
            list.append(index)
        l2=''
        for each in list:
            l2+=each+'\t'
    ll=chr+'\t'+str(pos)+'\t'+id+'\t'+ref+'\t'+str(alt)+'\t'+str(qual)+'\t'+filter+'\t'+info+'\t'+format+'\t'+l2+'\n'
    out_vcf.write(ll)
  


