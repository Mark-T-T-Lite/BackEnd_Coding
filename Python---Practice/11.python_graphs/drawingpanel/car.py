from drawingpanel import *

panel = DrawingPanel(300,300)
panel.set_background('gray')
panel.canvas.create_rectangle(20,10,100,65,outline='white',fill='black')
panel.canvas.create_oval(30,70,70,40,fill='red')
#panel.canvas.create_oval(80,70,20,20,fill='red')
panel.canvas.create_rectangle(80,40,30,20,fill='cyan')

