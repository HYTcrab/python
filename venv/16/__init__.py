import xlwt
with open('numbers','r') as file:
    str=eval(file.read())
    print(str)
def horz_left(x,y,data):
    algnt=xlwt.Alignment()
    algnt.horz=xlwt.Alignment.HORZ_RIGHT
    style=xlwt.XFStyle()
    style.alignment=algnt
    table.write(x,y,data,style)

xls=xlwt.Workbook()
table=xls.add_sheet('numbers')
for i in range(3):
    for j in range(3):
        horz_left(i,j,str[i][j])
xls.save('numbers.xls')