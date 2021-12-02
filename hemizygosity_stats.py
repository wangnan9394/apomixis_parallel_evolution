# -*- coding: utf-8 -*-
"""
Created on March 22 2021

@author: Nan
"""

import argparse

parser = argparse.ArgumentParser(description = 'None', add_help = False, usage = '\npython3 -g gff_file -v input.vcf -o out.results')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-v', '--vcf', metavar = '[input.vcf]', help = 'input', required = True)
required.add_argument('-g', '--gff', metavar = '[gff]', help = 'output', required = True)
required.add_argument('-o', '--output', metavar = '[output.file]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

out=open(args.output,'w')
with open(args.gff,'r') as f:
    list_gene=[]
    for line1 in f:
        #print(line)
        line=line1.replace("\n","").split("\t")
        if line[2]=='gene':
            gene=line[0]+'_'+line[1]+'_'+line[3]+'_'+line[4]
            list_gene.append(gene)
    for one in list_gene:
        chr=one.split('_')[0]
        start=int(one.split('_')[2])
        end=int(one.split('_')[3])
        #print(start,end)
        with open(args.vcf,'r') as fd:
            for each1 in fd:
                each=each1.replace("\n","").split("\t")
                #print(each)
                if each[0]==chr and 'DEL' in each[2]:
                    pred_start=int(each[1])
                    length=len(each[3])
                    pred_end=pred_start+length
                    if pred_end>start and pred_start<start and length > (end-start):
                        out.write('Gene:'+'\t'+one+'\n')
                        out.write('genesite:'+'\t'+str(start)+'\t'+str(end)+'\n')
                        out.write('SVsite:'+'\t'+str(pred_start)+'\t'+str(pred_end)+'\t'+str(length)+'\n')
                        out.write(each1)


