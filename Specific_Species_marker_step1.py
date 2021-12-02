# -*- coding: utf-8 -*-
"""
Created on March 22 2021

@author: Nan
"""
import re
import vcf
import argparse

parser = argparse.ArgumentParser(description = 'For citrus', add_help = False, usage = '\npython3 -s [sample name in vcf file] -v [input.vcf] -b [bed files] -o [output.file]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-s', '--sample', metavar = '[sample name in vcf file]', help = 'input', required = True)
required.add_argument('-v', '--vcf', metavar = '[input.vcf]', help = 'input', required = True)
required.add_argument('-b', '--bed', metavar = '[bed files]', help = 'bed files,chr/t pos/t variations', required = True)
required.add_argument('-o', '--output', metavar = '[output.file]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

def step1(vcffile,bedfile,outfile,samplename):
    vcf_reader = vcf.Reader(open(vcffile, 'r'))
    count=[]
    name_list=[samplename]
    out=open(outfile,'w')
    for record in vcf_reader:
        GT=record.genotype(samplename)['GT']##修改ID
        pred='chr'+record.CHROM+'_'+str(record.POS)
        if GT=='0/0':
            with open(bedfile) as f:
                for line in f:
                    line=line.replace("\n","").split("\t")
                    target=line[0]+'_'+line[1]
                    if target==pred:
                        target_sjg=line[2]
                        target_Jg=line[3]
                        #print(target)
            geno=record.REF
            if geno==target_sjg:
                final_type='pure'
            if geno==target_Jg:
                final_type='out'
            ll=pred+'\t'+final_type+'\n'
            out.write(ll)
            #print(final_type)
        elif GT=='1/1':
            with open(bedfile) as f:
                for line in f:
                    line=line.replace("\n","").split("\t")
                    target=line[0]+'_'+line[1]
                    if target==pred:
                        target_sjg=line[2]
                        target_Jg=line[3]
                        #print(target_sjg)
            geno=record.ALT[0]
            if geno==target_sjg:
                final_type='pure'
            if geno==target_Jg:
                final_type='out'
            ll=pred+'\t'+final_type+'\n'
            out.write(ll)
            #print(final_type)
        elif GT=='0/1':
            final_type='mix'
            ll=pred+'\t'+final_type+'\n'
            out.write(ll)
            #print(final_type)
        else:
            final_type='None'
            ll=pred+'\t'+final_type+'\n'
step1(args.vcf,args.bed,args.output,args.sample)