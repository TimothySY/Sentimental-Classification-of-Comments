#coding=utf-8
import jieba
import _csv
import xlwt
import xlrd
import pandas as pd

def judge(sentence):
    book = xlrd.open_workbook("D:/PythonProject/WordsExtraction/Pythonexcel.xls")
    sheet=book.sheet_by_index(0)
    nrows=sheet.nrows
    ncols=sheet.ncols
    row_list=[]
    row_firstcolomn=[]
    for i in range(0,nrows):
        row_data=sheet.row_values(i)
        row_datafirst=sheet.cell_value(i,0)
        row_list.append(row_data)
        row_firstcolomn.append(row_datafirst)


    sent= list(jieba.cut(sentence, cut_all=False))

    filename1="meidi_jd_pos_1.2.txt"
    myfilename1=open(filename1,'rb')
    filename2="meidi_jd_neg_1.2.txt"
    myfilename2=open(filename2,'rb')
    pos=[]
    posdoc=len(myfilename1.readlines())
    neg=[]
    negdoc=len(myfilename2.readlines())
    prior1=posdoc/(posdoc+negdoc)
    prior2=1-prior1
    prior1=0.8788
    prior2=1-0.8788
    for word in sent:
        if(row_firstcolomn.__contains__(word)):
            ind=row_firstcolomn.index(word)
            content=row_list[ind]
            print(content)
            temp_pos=((1+content[1])/(2+posdoc))
            temp_neg=((1+content[2])/(2+negdoc))
            pos.append(temp_pos)
            neg.append(temp_neg)

    posprop=1
    negprop=1

    for i in range(len(pos)):
        posprop=posprop*pos.__getitem__(i)
        negprop=negprop*neg.__getitem__(i)

    finalresult=0.5
    if(prior1*posprop+prior2*negprop!=0):
     finalresult=(prior1*posprop)/(prior1*posprop+prior2*negprop)


    return  finalresult


l=list(jieba.cut("出水速度很快，很耐用"))
print(l)
print(judge("出水速度很快，很耐用"))
# correct=0
# total=0
# f=open("postest.txt")
# line=f.readline()
# while line:
#     total=total+1
#     if(judge(line)>0.5):
#         correct=correct+1
#     line=f.readline()
#     print(correct)
#     print(total)
# f.close()
# print(correct/total)

