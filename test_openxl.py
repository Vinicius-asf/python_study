from openpyxl import Workbook
wb = Workbook()

ws = wb.active

for i in range(1,11):
  ws.cell(i,1,i)

wb.save('testOpenxl.xlsx')