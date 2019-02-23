import xlrd
import xml.dom.minidom as md


def get_xls_data(filename):
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content=list()
     for i in range(sheet.nrows):
         content.append(sheet.row_values(i)[:])
     return content


def write_to_xml(xlscontent):

    xmlfile = md.Document() #创建新xml文件

    root = xmlfile.createElement('root')    #创建节点
    numbers = xmlfile.createElement('numbers')    #创建节点

    xmlfile.appendChild(root)    #在文件中添加root节点
    root.appendChild(numbers)    #在root下添加numbers节点

    comment = xmlfile.createComment('数字信息')    #创建评论
    numbers.appendChild(comment)    #在numbers标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))        #创建文本节点
    numbers.appendChild(xmlcontent)   #在numbers标签下添加文本内容

    with open('numbers.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8'))    #写入文件


write_to_xml(get_xls_data('numbers.xls'))