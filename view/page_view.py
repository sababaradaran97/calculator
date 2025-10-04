from tkinter import *
from tkinter.messagebox import Message


one_3 = [ 1 , 2 , 3 ]
four_6 = [ 4 , 5 ,6 ]
seven_9 = [ 7 , 8 , 9 ]
action = [ "+" , "-" , "/" , "*" ]

window = Tk()
window.title( "calculator" )
window.geometry( "230x290" )


show_area = Label( window , text = "" , height = 2 , width = 26 , bg = "lightgray" , fg = "black" )
show_area.place( x = 20 , y = 20 )


def show ( i ):
    show_area.config( text = f"{ i }" + show_area.cget( "text" )  )


def actions ( i ) :
    the_action = action[ i ]
    show_area.config( text = f"{ the_action }" + show_area.cget( "text" ) )

def finall () :
    string = show_area.cget( "text" )
    answer = eval( f"{string}" )
    show_area.config( answer )

def dote () :
    string = show_area.cget( "text" )
    if "." in string :
        pass

    else :
        show_area.config( text = "." + show_area.cget( "text" ) )

y_position = 70
x_position = 20

for i in range( 9 , 0 , -1 ) :
    col =  ( ( i - 1 ) % 3 )
    row = 2 - ( ( i - 1 ) // 3 )
    
    button = Button( window, text=f"{i}", command=lambda i=i: show( i ) , width = 4 , height = 2 ).place( x = 40 * col + x_position , y = row * 50 + y_position )





for i in range( len( action ) ) :

    row = 2 - ( ( i - 1 ) // 3 )
    
    button = Button( window, text = f"{ action[ i ] }", command = lambda i = i : show( i ) , width = 4 , height = 2 ).place( x = 140 , y = row * 50 + y_position )


Button( window , text = "=" , command = finall , width = 4 , height = 2 ).place( x = 20 , y = 220 )

Button( window , text = "." , command = dote , width = 4 , height = 2 ).place( x = 60 , y = 220 )


mainloop = window.mainloop()

