#coding=utf-8
import xlrd
import xlwt
book = xlrd.open_workbook("D:/PythonProject/WordsExtraction/wordlist.xls")
print(book.nsheets)
print(book.sheet_names())
first_sheet=book.sheet_by_index(0)
print(first_sheet.row_values(0))
print(first_sheet.cell(1,1))