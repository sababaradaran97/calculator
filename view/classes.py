from tkinter import *

class LableWithEntry :

    def __init__ ( self , master , lable_text , x , y , data_taype = StringVar , distance = 60 ):
        Label( master , text = lable_text ).place( x = x , y = y )
        variable = data_taype()
        Entry( master , textvariable = variable ).place( x = x + distance , y = y )