#coding=utf-8
import jieba
import _csv
import xlwt
import xlrd
import pandas as pd
import xlrd
inputfile1 ='D:/PythonProject/WordsExtraction/meidi_jd_neg.txt'
inputfile2 ='D:/PythonProject/WordsExtraction/meidi_jd_pos.txt'
outputfile='D:/PythonProject/WordsExtraction/wordlist.txt'
data1 = pd.read_csv(inputfile1, encoding = 'utf-8', sep='delimiter',header = None,engine='python')
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', sep='delimiter',header = None,engine='python')
m={}
for i in data1[0]:
    temp_row=list(jieba.cut(i))

    for j in range(len(temp_row)):
        if (m.__contains__(temp_row[j])):
            m[temp_row[j]][1] += 1
        else:
            m[temp_row[j]] = [0, 1]

for i in data2[0]:
    temp_row=list(jieba.cut(i))

    for j in range(len(temp_row)):
        if (m.__contains__(temp_row[j])):
            m[temp_row[j]][0] += 1
        else:
            m[temp_row[j]] = [1,0]


workbook=xlwt.Workbook(encoding="utf-8")
sheet1=workbook.add_sheet("Python Sheet1")
row=0
for x in m.keys():
    print(x+' ')
    print(m[x][0])
    print(m[x][1])
    sheet1.write(row,0,x)
    sheet1.write(row,1,m[x][0])
    sheet1.write(row,2,m[x][1])
    row=row+1


workbook.save("Pythonexcell.xls")
print("successfully")


