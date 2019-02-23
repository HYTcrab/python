import xlwt
with open('city','r',encoding='utf-8') as file:
    data=file.read()
    _city=eval(data)
    city=list()
    for i in range(1,4):
        info=_city[str(i)]
        city.append(i)
        city.append(info)

def horz_left(x,y,data):
    algnt=xlwt.Alignment()
    algnt.horz=xlwt.Alignment.HORZ_LEFT
    style=xlwt.XFStyle()
    style.alignment=algnt
    table.write(x,y,data,style)

xls=xlwt.Workbook()
table=xls.add_sheet('city')
for i in range(len(city)):
    horz_left(i//2,i%2,city[i])

xls.save('city.xls')

