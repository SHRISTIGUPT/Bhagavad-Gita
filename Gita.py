# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:39:09 2023
@author: Shristi Gupta
"""

import PySimpleGUI as sg
import pandas as pd
idx_num = 0
info1 = """–––––––––––––––––––––––––––––––––––
गीता में कुल १८ अध्याय और ७०० श्लोक हैं. 
इस में दोहे प्रो.सी.बी.श्रीवास्तव "विदग्ध",(मण्डला म.प्र.)की रचनाएं हैं.
01 - अर्जुन विषाद योग (47)
02 - सांख्य योग (72)
03 - कर्म योग (43)
04 - ज्ञान कर्म संन्यास योग (42)
05 - कर्म संन्यास योग (29)
06 - ध्यान योग (47)
07 - ज्ञान विज्ञान योग (30)
08 - अक्षर ब्रह्म योग (28)
09 - राज विद्या राज गुह्य योग (34)
10 - विभूति योग (42)
11 - विश्वरूप दर्शन योग (55)
12 - भक्ति योग (20)
13 - क्षेत्र क्षेत्रज्ञ विभाग योग (34)
14 - गुण त्रय विभाग योग (27)
15 - पुरुषोत्तम योग (20)
16 - दैवसुर संपाद विभाग योग (24)
17 - श्रद्धा त्रय विभाग योग (28)
18 - मोक्ष संन्यास योग (78)
–––––––––––––––––––––––––––––––––––
Program by - Shristi Gupta
"""
# =============================================================================
def get_line(idx_num,msg):
    val_chp = gt.loc[idx_num].values[0]
    val_shl = gt.loc[idx_num].values[1]
    val_san = gt.loc[idx_num].values[2] 
    val_eng = gt.loc[idx_num].values[3] 
    val_hin = gt.loc[idx_num].values[4] 
    val_doh = gt.loc[idx_num].values[5] + "\n" + gt.loc[idx_num].values[6]            
    val_des = gt.loc[idx_num].values[7] 

    val_san = val_san.replace(' |',' |\n')
    val_hin = val_hin.replace('।','।\n')
    val_eng = val_eng.replace('.','.\n')

    window["-chapter_combo-"].update(val_chp)
    window["-shlok-"].update(val_shl)
    window["-msg-"].update(msg)

    window["-sanskrit-"].update(val_san)
    window["-hindi-"].update(val_hin)
    window["-english-"].update(val_eng)
    window["-doha-"].update(val_doh)
    window["-ch_name-"].update(val_des)

def info():
    sg.popup(info1,title='Information', icon="favicon.ico")
# =============================================================================
chapter = [i for i in range(1, 19)]

sg.theme('Light Brown 3')

# Left & right column in window
input_col = [[sg.Text('Select Chapter', size=(11, 1)), 
             sg.Combo(chapter, default_value=1,key='-chapter_combo-'),
             sg.Text('   ') ,                           
             sg.Text('Select Shlok', size=(11, 1)), 
             sg.Input(size=(5, 1),default_text=1, key='-shlok-')
             ]]
button_col = [[sg.Submit(button_text="Show",button_color="green",size=(10,1)),
              sg.Cancel(button_text="Close",button_color="blue",size=(10,1)),
              sg.Button(button_text="Info",button_color="orange",size=(10,1))]]

layout = [
           [sg.Column(input_col, element_justification='l'), sg.VSeperator(),
            sg.Column(button_col, element_justification='c')],

            [ sg.Text(" "*15),
              sg.Button(button_text="< Previous",button_color="brown",size=(10,1),bind_return_key=True),
              sg.Text(" "*10),
              sg.Button(button_text="Next >",button_color="brown",size=(10,1),focus=True) ],
           
            [sg.Text("",key="-msg-",text_color="red",font=("Arial Unicode MS",14,"bold"))],
           [sg.Text("–" * 100)],

           [[sg.Text('संस्कृत श्लोक   '),sg.Text('',size=(35,1),key='-ch_name-',text_color="red"),sg.Text('     हिंदी दोहा')],
            [sg.Multiline('',text_color="blue",font=('Sanskrit Text',14), size=(33, 3), key="-sanskrit-"),
            sg.Multiline('',text_color="Green",font=('Aparajita',14), size=(38, 4), key="-doha-")],
            [sg.Text('हिंदी अर्थ')], 
            [sg.Multiline('',text_color="red",font=('Utsaah',18), size=(70, 4), key="-hindi-")],
            [sg.Text('English Meaning')], 
            [sg.Multiline('',text_color="purple",font=('Courier New',13), size=(70, 4), key="-english-")],
           [sg.Text("–" * 100)]]
         ]
# ---------------------------------------------------------------------------------

gt = pd.read_csv("gitaF.csv")
msg = ''

window = sg.Window('Gita Text', layout, icon="favicon.ico")
while True:
    try:
        event, values = window.read()
        if (event == sg.WINDOW_CLOSED) or (event == "Close"):
            window.close()
            break
          
        if event == "Info":
            info()
            
        if event == "Show":
            msg=""
            sel_chapter = values['-chapter_combo-']
            if values["-shlok-"].isnumeric():
                sel_shlok = int(values["-shlok-"])
            else:
                sel_shlok = 1
                msg = "Invalid value. Showing first Shlok."
                pass
            
            idx_num = gt.loc[(gt['Chapter'] == sel_chapter) & (gt['Shlok'] == sel_shlok)].index[0]
            get_line(idx_num,msg)

            # --------------------- for Next - previous button --------------
        if event == "< Previous":
            msg=""
            if idx_num == 0:
                idx_num = 1
                msg = "You have reached at first Shlok"
            idx_num = idx_num - 1
            # idx_num = gt.loc[index_num].index[0]
            get_line(idx_num,msg)
            
        if event == "Next >":
            msg=""
            idx_num = idx_num + 1
            if idx_num == 701:
                idx_num = 700
                msg = "You have reached at last Shlok"
            # idx_num = gt.loc[index_num].index[0]
            get_line(idx_num,msg)
            # --------------------- for Next - previous button --------------
    
    except:
        import sys
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # print(f"Error ID: {exc_type.__name__}")
        window["-msg-"].update(f"Error Value: {exc_value}")

