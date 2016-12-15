import xlwt
workbook=xlwt.Workbook(encoding="utf-8")
sheet1=workbook.add_sheet("Python Sheet1")
sheet2=workbook.add_sheet("Python Sheet2")
sheet3=workbook.add_sheet("Python Sheet3")

sheet1.write(0,0,"This is Sheet 1")
sheet1.write(0,1,"好")
sheet1.write(0,2,3)
sheet2.write(0,0,"This is Sheet 2")
sheet3.write(0,0,"This is Sheet 3")

workbook.save("PythonSepreadSheet.xls")
print("workbook created")