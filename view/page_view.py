from tkinter import *
from tkinter.messagebox import Message


one_3 = [ 1 , 2 , 3 ]
four_6 = [ 4 , 5 ,6 ]
seven_9 = [ 7 , 8 , 9 ]
action = [ "+" , "-" , "/" , "*" , "." , "=" ]

window = Tk()
window.title( "calculator" )
window.geometry( "230x290" )

string = ""


show_area = Label( window , text = "" , height = 2 , width = 26 , bg = "lightgray" , fg = "black" )
show_area.place( x = 20 , y = 20 )


def show ( i ):
    show_area.config( text = f"{ i }" + show_area.cget( "text" ) )

y_position = 70
x_position = 20

for i in range( 9 , 0 , -1 ) :
    col =  ( ( i - 1 ) % 3 )
    row = 2 - ( ( i - 1 ) // 3 )
    
    button = Button( window, text=f"{i}", command=lambda i=i: show( i ) , width = 4 , height = 2 ).place( x = 40 * col + x_position , y = row * 50 + y_position )



"""
for i in range( 10 ):

    if i in [ 9 , 8 , 7 ] :

        if i == 9 :
            button = Button( window, text=f"{i}", command = lambda i=i: show( i ) , width = 4 , height = 2 ).place( x = 20 , y = 70 )

        if i == 8 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 70 , y = 70 )

        if i == 7 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 120 , y = 70 )

    elif i in [ 6 , 5 , 4 ] :

        if i == 6 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 20 , y = 120 )

        if i == 5 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 70 , y = 120 )

        if i == 4 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 120 , y = 120 )
        

    elif i in [ 3 , 2 , 1 ] :
        if i == 3 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 20 , y = 170 )

        if i == 2 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 70 , y = 170 )

        if i == 1 :
            button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 120 , y = 170 )


    else :
        button = Button( window, text=f"{i}", command=lambda i=i: hello( i ) , width = 4 , height = 2 ).place( x = 20 , y = 220 )


   
for i in range( len( action ) ):

    if action[ i ] == "+":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 170 , y = 70 )

    if action[ i ] == "-":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 170 , y = 120 )

    if action[ i ] == "/":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 170 , y = 170 )

    if action[ i ] == "*":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 170 , y = 220 )

    if action[ i ] == ".":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 70 , y = 220 )

    if action[ i ] == "=":
        button = Button( window, text=f"{action[ i ]}", command=lambda act=action[ i ]: hello( act ) , width = 4 , height = 2 ).place( x = 120 , y = 220 )

    

"""


mainloop = window.mainloop()

