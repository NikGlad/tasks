import docx
# from pyautocad import *


# doc = docx.Document()

# TODO expert
doc1 = docx.Document("экспертиза1.docx")

all_paras = doc1
for para in all_paras:
    print(para.text)

doc.save('exp.docx')
#
# acad = Autocad("C:/Program Files/Autodesk/AutoCAD 2021/UserDataCache")
# acad.prompt("Hello, Autocad from Python\n")
# print (acad.doc.Name)

# for text in all_paras:
#     print(acad)


# p1 = APoint(0, 0)
# p2 = APoint(50, 25)
# for i in range(5):
#     text = acad.model.AddText()
#     acad.model.AddLine(p1, p2)
#     acad.model.AddCircle(p1, 10)
#     p1.y += 10
#
# dp = APoint(10, 0)
# for text in acad.iter_objects('Text'):
#     print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
#     text.InsertionPoint = APoint(text.InsertionPoint) + dp
#
# for obj in acad.iter_objects(['Circle', 'Line']):
#     print(obj.ObjectName)
