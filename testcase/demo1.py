import readExcel

class Demo1(object):
    oe = readExcel.OperateExcel("F:\dmpapi\data\es正则改写记录.xlsx", "Sheet1")
    oe1 = readExcel.OperateExcel("F:\dmpapi\data\es正则改写记录.xlsx", "Sheet3")
    start1 = 1
    end1 = oe.rows+1
    start2 = 1
    end2 = oe1.rows + 1


    while start1<=end1 and start2<=end2:
        if oe.table.cell(start1, 3).value=='pass':
            start1+=1
        else:
            oe.table.cell(start1, 1).value = oe1.table.cell(start2, 1).value
            oe.table.cell(start1, 2).value = oe1.table.cell(start2, 2).value
            oe.table.cell(start1, 3).value = oe1.table.cell(start2, 3).value
            start1+=1
            start2+=1
    oe.save("F:\dmpapi\data\es正则改写记录.xlsx")