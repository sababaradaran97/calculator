from tkinter import *

win = Tk()
win.title( "calculator" )
win.geometry( "300x390" )


def entry ( master , text_name , text_width , text_x , text_y ) :
    Entry( master , name = text_name , width = text_width , state = "readonly" ).place( x = text_x , y = text_y )

name = "caculator"
width = "42"
x = "25"
y = "40"

entry( win , name , width , x , y )

def show_result_9 () :
    buttom_9.get()

def show_result_8 () :
    buttom_8.get()

def show_result_7 () :
    buttom_7.get()

def show_result_6 () :
    buttom_6.get()

def show_result_5 () :
    buttom_5.get()

def show_result_4 () :
    buttom_4.get()

def show_result_3 () :
    buttom_3.get()

def show_result_2 () :
    buttom_2.get()

def show_result_1 () :
    buttom_1.get()

def show_result_0 () :
    buttom_0.get()

def show_result_minez () :
    buttom_minez.get()

def show_result_plus () :
    buttom_plus.get()

def show_result_equal () :
    buttom_equal.get()

def show_result_devide () :
    buttom_devide.get()

def show_result_multiplation () :
    buttom_multipleation.get()

def show_result_dote () :
    buttom_dote.get()





#first line

# buttom_9
buttom_9 = StringVar
buttom_9 = Button( win , text = "9" , command = show_result_9 )
buttom_9.place( x = "25" , y = "100" , width = "50" , height = "40" )

# buttom_8
buttom_8 = StringVar
buttom_8 = Button( win , text = "8" , command = show_result_8 )
buttom_8.place( x = "95" , y = "100" , width = "50" , height = "40" )

# buttom_7
buttom_7 = StringVar
buttom_7 = Button( win , text = "7" , command = show_result_7 )
buttom_7.place( x = "165" , y = "100" , width = "50" , height = "40" )

# buttom_devide
buttom_devide = StringVar
buttom_devide = Button( win , text = "/" , command = show_result_devide )
buttom_devide.place( x = "235" , y = "100" , width = "50" , height = "40" )

# second line

# buttom_6
buttom_6 = StringVar
buttom_6 = Button( win , text = "6" , command = show_result_6 )
buttom_6.place( x = "25" , y = "160" , width = "50" , height = "40" )

# buttom_5
buttom_5 = StringVar
buttom_5 = Button( win , text = "5" , command = show_result_5 )
buttom_5.place( x = "95" , y = "160" , width = "50" , height = "40" )

# buttom_4
buttom_4 = StringVar
buttom_4 = Button( win , text = "4" , command = show_result_4 )
buttom_4.place( x = "165" , y = "160" , width = "50" , height = "40" )


# buttom_multipleation
buttom_multipleation = StringVar
buttom_multipleation = Button( win , text = "*" , command = show_result_multiplation )
buttom_multipleation.place( x = "235" , y = "160" , width = "50" , height = "40" )

# third line

# buttom_3
buttom_3 = StringVar
buttom_3 = Button( win , text = "3" , command = show_result_3 )
buttom_3.place( x = "25" , y = "220" , width = "50" , height = "40" )

# buttom_2
buttom_2 = StringVar
buttom_2 = Button( win , text = "2" , command = show_result_2 )
buttom_2.place( x = "95" , y = "220" , width = "50" , height = "40" )

# buttom_1
buttom_1 = StringVar
buttom_1 = Button( win , text = "1" , command = show_result_1 )
buttom_1.place( x = "165" , y = "220" , width = "50" , height = "40" )

# buttom_minez
buttom_minez = StringVar
buttom_minez = Button( win , text = "-" , command = show_result_minez )
buttom_minez.place( x = "235" , y = "220" , width = "50" , height = "40" )

# fourth line

buttom_0 = StringVar
buttom_0 = Button( win , text = "0" , command = show_result_0 )
buttom_0.place( x = "25" , y = "280" , width = "50" , height = "40" )

# buttom_equal
buttom_equal = StringVar
buttom_equal = Button( win , text = "=" , command = show_result_equal )
buttom_equal.place( x = "165" , y = "280" , width = "50" , height = "40" )

# buttom_plus
buttom_plus = StringVar
buttom_plus = Button( win , text = "+" , command = show_result_plus )
buttom_plus.place( x = "235" , y = "280" , width = "50" , height = "40" )

# dote
buttom_dote = StringVar
buttom_dote = Button( win , text = "." , command = show_result_dote )
buttom_dote.place( x = "95" , y = "280" , width = "50" , height = "40" )


win.mainloop()
