import pathlib
import PySimpleGUI as sg
import PySimpleGUI as psg
import itertools
import xml.etree.ElementTree as ET

sg.ChangeLookAndFeel('BrownBlue')

xmlfile = sg.popup_get_file('Enter the xml file that represent knowledge')
sg.popup('You file dictionary', xmlfile)

tree = ET.parse(xmlfile)
root = tree.getroot()

xmlstr = ET.tostring(root, encoding='utf8', method='xml')

XMLexample_stored_in_a_string = xmlstr

root = ET.fromstring(XMLexample_stored_in_a_string)
n = []
for child in root:
    for x in child:
        print(x.attrib.values())
        z = list(x.attrib.values())
        vvvv = list(x.attrib.keys())
        vvvv = dict(zip(vvvv, z))
        for i in range(len(vvvv)):
            print(list(vvvv.values()))
            n.append(list(vvvv.values()))
            print(n)
            
            
p = list(n for n,_ in itertools.groupby(n))

newnew = []
convertedList = []
xx = []
mmm = list(x.attrib.values())
kkk = list(x.attrib.keys())
for oo in range (len(p[0])):
    print("==========")
    for jj in range (len(p)):
#         print(p[jj][oo])
        xx.append(p[jj][oo])
        print(xx)
#define layout
    layout=[[psg.Text(f'Choose attribute of {kkk[oo]}',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(xx,key='board')],
            [sg.Input(size=(50,1), key='newval')],
            
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
    win =psg.Window('Choose your attribute of each Concept',layout)
#Read  values entered by user
    e,v=win.read()
#close first window
    win.close()
#access the selected value in the list box and add them to a string
        
#display string in a popup         
    psg.popup('Options Chosen', 'Your Choise of '+f'{kkk[oo]} is :'+ v['board']
            + ' and your update in '+ f'{kkk[oo]} is :'+ v['newval'])
    
    convertedList.append(v['board'])
    newnew.append(v['newval'])
    xx.clear()
    
# for b in range(len(x.attrib.values())):
#     convertedList.append(values[b][0])
g = ' '.join(str(e) for e in convertedList)

concept_list = g.split(" ")

for zzz in concept_list: 
    for child in root:
        for x in child:
            z = x.attrib.values()
            if (sorted(z) == sorted(concept_list)):
                print(child.attrib.values())
                sg.popup('The Rule: ', child.attrib.values())
                for po in range(len(concept_list)):
                    concept_list[po] = newnew[po]
                    print(concept_list[po])
                    print("pppppppp")
                    print(newnew[po])
                sg.popup(f'Your old attributes {g} \n your new attributes {newnew}')
            else:
                sg.popup('Unkonow Rule')
#         break
    break
