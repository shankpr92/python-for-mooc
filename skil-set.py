import pdb
import xlrd
from xlwt import Workbook

#File location of responce.xlsx
file_location = "E://Summer 2018//Social Network Analysis//Project//Project.xlsx"
workbook = xlrd.open_workbook(file_location)

#Spreadsheet to write the results
workbook_write = Workbook()
sheet1 = workbook_write.add_sheet('ID by skills')

#Sheet 1 of input spreadsheet
sheet = workbook.sheet_by_index(0)
col = 12

#row and col of output
row_op = 1
#Header of output file
sheet1.write(0,0,'exp')
sheet1.write(0,1,'courses')

#pdb.set_trace()
for row in range(1,sheet.nrows):
    #gender = sheet.cell(row,25)
    name = sheet.cell(row,2)
    skills = sheet.cell_value(row,12)
    exp = sheet.cell_value(row,30)
    id = row
    skill = skills.split(",")
    for s1 in skill:
        print(name,id,s1,exp)
        sheet1.write(row_op,0,exp)
        sheet1.write(row_op,1,s1)
        row_op += 1

workbook_write.save('output file_courses_by_exp.xls')
