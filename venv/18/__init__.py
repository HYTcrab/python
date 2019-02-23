import xlrd
import xml.dom.minidom as md


def get_xls_data(filename):
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content = {}
     for i in range(sheet.nrows):
         content[i+1] = sheet.row_values(i)[1:]
     return content


def write_to_xml(xlscontent):

    xmlfile = md.Document() #创建新xml文件

    root = xmlfile.createElement('root')    #创建节点
    city = xmlfile.createElement('city')    #创建节点

    xmlfile.appendChild(root)    #在文件中添加root节点
    root.appendChild(city)    #在root下添加city节点

    comment = xmlfile.createComment('城市信息')    #创建评论
    city.appendChild(comment)    #在city标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))        #创建文本节点
    city.appendChild(xmlcontent)   #在city标签下添加文本内容

    with open('city.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8'))    #写入文件


write_to_xml(get_xls_data('city.xls'))