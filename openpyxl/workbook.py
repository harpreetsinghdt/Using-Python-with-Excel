from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = Workbook()
ws = wb.active

ws1 = wb.create_sheet("Employees")
ws2 = wb.create_sheet("Departments", 0)

ws.title = "Harp Infotech"

#print(wb.sheetnames)

wb2 = load_workbook('../regions.xlsx')
new_sheet = wb2.create_sheet('NewSheet')
active_sheet = wb2.active
cell = active_sheet['A1']
#print(cell.value)

active_sheet['A1'] = 'County'
wb2.save('modified.xlsx')
