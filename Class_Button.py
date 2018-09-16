# Use with PySimpleGUI_Calculator_Apisit_6001012630187.py
 
import PySimpleGUI as sg    

class Button():
    
    def __init__ (self,text,color=None,border=None):            # Setting Variable
        self.text = text
        self.color = color
        self.border = border
    
    def Create (self):                                          # Create Button
        return sg.ReadFormButton(self.text,button_color=self.color,border_width=self.border)

