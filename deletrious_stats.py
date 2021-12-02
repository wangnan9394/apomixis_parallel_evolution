# -*- coding: utf-8 -*-
"""
Created on March 22 2021

@author: Nan
"""
import vcf
import argparse

parser = argparse.ArgumentParser(description = 'None', add_help = False, usage = '\npython3 -i [individuals.phased.vcf] -b [deleterious.bed] -o [output.file]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[individuals.phased.vcf]', help = 'input.phased.vcf', required = True)
required.add_argument('-b', '--bed_files', metavar = '[deleterious.bed]', help = 'deleterious.bed', required = True)
required.add_argument('-o', '--output', metavar = '[output.file]', help = 'output.stats', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()
summary_file=args.output

L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]
outfile=open(summary_file,'w')
in_file=args.input
name=args.input[:-8]####change depends on name
for wow in range(1,10):
    for pop in range(600):##change depends on length
        start=pop*100000
        end=(pop+1)*100000##100K_windows
        if start > L[wow-1]:##L[wow-1]
            break

        type1='SYNONYMOUS'
        type2='NONSYNONYMOUS'
        type3='FRAMESHIFT DELETION'
        type4='FRAMESHIFT INSERTION'
        type5='NONFRAMESHIFT DELETION'
        type6='NONFRAMESHIFT INSERTION'
        type7='START-LOST'
        type8='STOP-GAIN'
        type9='STOP-LOSS'
        type10='SUBSTITUTION'

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        list9=[]
        list10=[]
        chrrr='chr'+str(wow)
        chr_next='chr'+str(wow+1)
        info='Finished!'+'\t'+name+'\t'+chrrr+'\t'+str(start)+'\t'+str(end)
        print(info)
        with open(args.bed_files,'r') as f:
            for i in f:
                i=i.replace('\n','').split('\t')
                target=i[0]+'_'+i[1]           
                if i[0] ==chr_next:
                    break
                if i[0]==chrrr and int(i[1]) >start and int(i[1])<=end:
                    if i[-1]==type1:
                        list1.append(target)
                    if i[-1]==type2:
                        list2.append(target)
                    if i[-1]==type3:
                        list3.append(target)
                    if i[-1]==type4:
                        list4.append(target)
                    if i[-1]==type5:
                        list5.append(target)
                    if i[-1]==type6:
                        list6.append(target)
                    if i[-1]==type7:
                        list7.append(target)
                    if i[-1]==type8:
                        list8.append(target)
                    if i[-1]==type9:
                        list9.append(target)
                    if i[-1]==type10:
                        list10.append(target)
                        
        a1=0
        a2=0
        a3=0
        a4=0
        a5=0
        a6=0
        a7=0
        a8=0
        a9=0
        a10=0
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
        c7=0
        c8=0
        c9=0
        c10=0

        vcf_reader = vcf.Reader(open(in_file, 'r'))
        for record in vcf_reader:
            if record.CHROM == chr_next:
                break
            if record.CHROM==chrrr and record.POS >start and record.POS<=end:
                pred=record.CHROM+'_'+str(record.POS)
                gt=record.genotype(name)['GT']
                #print(pred)
                if gt =='0|0':
                    if pred in list1:
                        a1+=1
                    if pred in list2:
                        a2+=1
                    if pred in list3:
                        a3+=1
                    if pred in list4:
                        a4+=1
                    if pred in list5:
                        a5+=1
                    if pred in list6:
                        a6+=1
                    if pred in list7:
                        a7+=1
                    if pred in list8:
                        a8+=1
                    if pred in list9:
                        a9+=1
                    if pred in list10:
                        a10+=1
                if gt =='1|0' or gt=='0|1':
                    if pred in list1:
                        b1+=1
                    if pred in list2:
                        b2+=1
                    if pred in list3:
                        b3+=1
                    if pred in list4:
                        b4+=1
                    if pred in list5:
                        b5+=1
                    if pred in list6:
                        b6+=1
                    if pred in list7:
                        b7+=1
                    if pred in list8:
                        b8+=1
                    if pred in list9:
                        b9+=1
                    if pred in list10:
                        b10+=1
                if gt =='1|1':
                    if pred in list1:
                        c1+=1
                    if pred in list2:
                        c2+=1
                    if pred in list3:
                        c3+=1
                    if pred in list4:
                        c4+=1
                    if pred in list5:
                        #print(record)
                        c5+=1
                    if pred in list6:
                        c6+=1
                    if pred in list7:
                        c7+=1
                    if pred in list8:
                        c8+=1
                    if pred in list9:
                        c9+=1
                        #print(record)
                    if pred in list10:
                        c10+=1
            
        l1='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type1+'\t'+str(a1)+'\t'+str(b1)+'\t'+str(c1)+'\n'
        l2='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type2+'\t'+str(a2)+'\t'+str(b2)+'\t'+str(c2)+'\n'
        l3='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type3+'\t'+str(a3)+'\t'+str(b3)+'\t'+str(c3)+'\n'
        l4='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type4+'\t'+str(a4)+'\t'+str(b4)+'\t'+str(c4)+'\n'
        l5='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type5+'\t'+str(a5)+'\t'+str(b5)+'\t'+str(c5)+'\n'
        l6='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type6+'\t'+str(a6)+'\t'+str(b6)+'\t'+str(c6)+'\n'
        l7='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type7+'\t'+str(a7)+'\t'+str(b7)+'\t'+str(c7)+'\n'
        l8='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type8+'\t'+str(a8)+'\t'+str(b8)+'\t'+str(c8)+'\n'
        l9='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type9+'\t'+str(a9)+'\t'+str(b9)+'\t'+str(c9)+'\n'
        l10='region'+'_'+chrrr+'_'+str(start)+'_'+str(end)+'\t'+name+'\t'+type10+'\t'+str(a10)+'\t'+str(b10)+'\t'+str(c10)+'\n'

        outfile.write(l1)
        outfile.write(l2)
        outfile.write(l3)
        outfile.write(l4)
        outfile.write(l5)
        outfile.write(l6)
        outfile.write(l7)
        outfile.write(l8)
        outfile.write(l9)
        outfile.write(l10)
