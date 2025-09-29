from tkinter import *
from classes import *

win = Tk()
win.title( "calculator" )
win.geometry( "300x390" )


Entry( win , name = "" , width = "40" , state = "readonly" ).place( x = "25" , y = "20" )

#first line

# master , lable_text , x , y , data_taype = StringVar , distance = 60

buttom_9 = LableWithEntry( win , "9" , "25" , "100" )

# buttom_9
buttom_9 = Button( win , text = "9" )
buttom_9.place( x = "25" , y = "100" , width = "50" , height = "40" )

# buttom_8
buttom_8 = Button( win , text = "8" )
buttom_8.place( x = "95" , y = "100" , width = "50" , height = "40" )

# buttom_7
buttom_7 = Button( win , text = "7" )
buttom_7.place( x = "165" , y = "100" , width = "50" , height = "40" )

# buttom_devide
buttom_devide = Button( win , text = "/" )
buttom_devide.place( x = "235" , y = "100" , width = "50" , height = "40" )

# second line

# buttom_6
buttom_6 = Button( win , text = "6" )
buttom_6.place( x = "25" , y = "160" , width = "50" , height = "40" )

# buttom_5
buttom_5 = Button( win , text = "5" )
buttom_5.place( x = "95" , y = "160" , width = "50" , height = "40" )

# buttom_4
buttom_4 = Button( win , text = "4" )
buttom_4.place( x = "165" , y = "160" , width = "50" , height = "40" )


# buttom_multipleation
buttom_multipleation = Button( win , text = "*" )
buttom_multipleation.place( x = "235" , y = "160" , width = "50" , height = "40" )

# third line

# buttom_3
buttom_3 = Button( win , text = "3" )
buttom_3.place( x = "25" , y = "220" , width = "50" , height = "40" )

# buttom_2
buttom_2 = Button( win , text = "2" )
buttom_2.place( x = "95" , y = "220" , width = "50" , height = "40" )

# buttom_1
buttom_1 = Button( win , text = "1" )
buttom_1.place( x = "165" , y = "220" , width = "50" , height = "40" )

# buttom_minez
buttom_minez = Button( win , text = "-" )
buttom_minez.place( x = "235" , y = "220" , width = "50" , height = "40" )

# fourth line

buttom_0 = Button( win , text = "0" )
buttom_0.place( x = "25" , y = "280" , width = "50" , height = "40" )

# buttom_equal
buttom_equal = Button( win , text = "=" )
buttom_equal.place( x = "165" , y = "280" , width = "50" , height = "40" )

# buttom_plus
buttom_plus = Button( win , text = "+" )
buttom_plus.place( x = "235" , y = "280" , width = "50" , height = "40" )

# dote
buttom_dote = Button( win , text = "." )
buttom_dote.place( x = "95" , y = "280" , width = "50" , height = "40" )


win.mainloop()