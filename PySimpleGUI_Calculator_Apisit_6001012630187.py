
# coding: utf-8

# # PySimpleGUI Calculator

# # By Apisit Khomcharoen 6001012630187

# #  Blog Me ---> https://apisit13411.blogspot.com/

# #  Ref ---> https://pysimplegui.readthedocs.io/en/latest/cookbook/

# In[7]:


# Calculator by PySimpleGUI
# Credit Thankyou "   https://pysimplegui.readthedocs.io/en/latest/cookbook/    "

from Class_Button import *
import PySimpleGUI as sg    


# Creat GUI       # Call Class from Class_Button.py
layout = [[sg.Txt(''  * 10)],                      
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='input')],
          [sg.Txt(''  * 10)],
          [Button('(',('black','orange')).Create(), Button(')',('black','orange')).Create(), Button('c',('black','orange')).Create(), Button('«',('black','orange')).Create()],
          [Button('7',('black','yellow')).Create(), Button('8',('black','yellow')).Create(), Button('9',('black','yellow')).Create(), Button('÷',('black','orange')).Create()],
          [Button('4',('black','yellow')).Create(), Button('5',('black','yellow')).Create(), Button('6',('black','yellow')).Create(), Button('x',('black','orange')).Create()],
          [Button('1',('black','yellow')).Create(), Button('2',('black','yellow')).Create(), Button('3',('black','yellow')).Create(), Button('-',('black','orange')).Create()],
          [Button('.',('black','orange')).Create(), Button('0',('black','yellow')).Create(), Button('=',('black','orange')).Create(), Button('+',('black','orange')).Create()],
          ]


# Set PySimpleGUI
form = sg.FlexForm('13411_CALCULATOR', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Set Process
Equal = ''
List_Op_Error =  ['+','-','*','/','(']

# Loop
while True:
    button, value = form.Read()                            # call GUI
    
    # Press Button
    if button is 'c':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button is '«':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-().':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button is 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button is '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    
   # Process Conditional
    elif button is '=':
        # Error Case
        for i in List_Op_Error :  
            if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   # Check Error Case
                print(0)
                Answer = "Error Operation" 
                break
            elif Equal == '6001012630187':
                Answer = 'Apisit.Khomcharoen'
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error Operation" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error Operation" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error Operation" 
                    break
    # Calculate Case    
        else :
            Answer = str("%0.2f" %(eval(Equal)))                         # eval(Equal)  
            if '.0' in Answer:
                Answer = str(int(float(Answer)))                         # convert float to int
        form.FindElement('input').Update(Answer)                         # Update to GUI
        Equal = Answer

    elif button is 'Quit'  or button is None:                            # QUIT Program
        break
        
#---------------------------------------------------------------------
        
"""

Example Test Cal

5*6 = 30
(   = Error Operation
8*(6+4) = 80
6* = Error Operation
6*/2 = Error Operation
7 // 3 = 2
3 ** 3 = 27
27 ** (1/3) = 3
6001012630187 = Apisit.Khomcharoen
59) = Error Operation 
                    
"""

