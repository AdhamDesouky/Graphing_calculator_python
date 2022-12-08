from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Style
from math import *
def opencalc():
    import calculatorkareem 

root = Tk()
root.title('Graphical calculator')
# create all of the main containers
top_frame = Frame(root, bg='grey', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=450, height=450, padx=3, pady=3)
fonted=("Helvetica",9)
fonted2=("Helvetica",16)


# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_mid = Frame(center, bg='black', width=200, height=190, padx=2, pady=2)
ctr_right = Frame(center, bg='grey', width=150, height=190, padx=5, pady=3)


ctr_mid.grid(row=0, column=0, sticky="nsw")
ctr_right.grid(row=0,column=2, sticky="nse")

# create the widgets for the top frame
e = Entry(ctr_right, background="white")
width_label = Label(ctr_right, text='f(x):')

def drawing():
    #draw on current
    if var1.get()==False:
        canvas.delete("all")
        ondisplaylistbox.delete(0,END)
        main_canvas()
    texted=e.get()
    listbox_widget.insert(END, texted)
    ondisplaylistbox.insert(0,texted)
    i=0
    num_dict=('1','2','3','4','5','6','7','8','9','0')
    som=""
    somx=""
    while i<len(texted):
        if i+1>len(texted):
            break
        else:
            #numbers
            if texted[i] in num_dict :
                somx+=(texted[i])
                yx=(eval(somx)*25)        
                canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='black')
                i+=1
                yxa=centercanvas/eval(somx)
                #numbered sin(x)
                if texted[i] == 's' and texted[i+1]=='i' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 25*eval(somx)
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(sin(x * x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='green')
                    canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                    break
                #numbered cos(x)
                if texted[i] == 'c' and texted[i+1]=='o' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 25*eval(somx)
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(cos(x * x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='blue')
                    canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                    break
                #numbered tan
                if texted[i] == 't' and texted[i+1]=='a' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 25*eval(somx)
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(tan(x * -x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='red')
                    canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                    break
                #numbered x
                if texted[i]=='x':
                    i+=1
                    canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='black')
                    canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                    if texted[i]=='+':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            y=(eval(som)*25)
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                        canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='white')
                        canvas.create_line((centercanvas-yxa)-y/eval(somx), heightcanvas, (centercanvas+yxa)-y/eval(somx), 0,fill='black')
                        break
                    if texted[i]=='-':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            y=(eval(som)*25)
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                        canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='white')
                        canvas.create_line((centercanvas-yxa)+y/eval(somx), heightcanvas, (centercanvas+yxa)+y/eval(somx), 0,fill='black')
                        break
                    else: 
                        break
                
            #sinx
            if texted[i] == 's' and texted[i+1]=='i' :
                x_increment = 0.5
                # width stretch
                x_factor = 0.04035
                # height stretch
                y_amplitude = 26
                # create the coordinate list for the sin() curve, have to be integers
                xy1 = []
                for x in range(heightcanvas*2):
                    # x coordinates
                    xy1.append(x * x_increment)
                    # y coordinates
                    xy1.append(int(sin(x * x_factor) * y_amplitude) + centercanvas)
                canvas.create_line(xy1, fill='green')
                break
            #cosx
            if texted[i] == 'c' and texted[i+1]=='o' :
                x_increment = 0.5
                # width stretch
                x_factor = 0.04035
                # height stretch
                y_amplitude = 26
                # create the coordinate list for the sin() curve, have to be integers
                xy1 = []
                for x in range(heightcanvas*2):
                    # x coordinates
                    xy1.append(x * x_increment)
                    # y coordinates
                    xy1.append(int(cos(x * x_factor) * y_amplitude) + centercanvas)
                canvas.create_line(xy1, fill='blue')
                break
            #tanx
            if texted[i] == 't' and texted[i+1]=='a' :
                x_increment = 0.5
                # width stretch
                x_factor = 0.04035
                # height stretch
                y_amplitude = 26
                xy1 = []
                for x in range(heightcanvas*2):
                    # x coordinates
                    xy1.append(x * x_increment)
                    # y coordinates
                    xy1.append(int(tan(x * -x_factor) * y_amplitude) + centercanvas)
                canvas.create_line(xy1, fill='red')
                break
            #sqrtx
            if texted[i] == '√' and texted[i+1]=='x' :
                x_increment = 0.5
                # width stretch
                x_factor = 0.04035
                # height stretch
                y_amplitude = 18
                xy1 = []
                x=0
                xcord=centercanvas*2
                while x<heightcanvas:
                    # x coordinates
                    xy1.append(xcord * x_increment)
                    # y coordinates
                    xy1.append(int(-sqrt(x * x_factor) * y_amplitude) + centercanvas)
                    x+=1
                    xcord+=1
                canvas.create_line(xy1, fill='black')
                break
            #-sqrtx
            if texted[i] == '-' and texted[i+1]=='√' :
                x_increment = 0.5
                # width stretch
                x_factor = 0.04035
                # height stretch
                y_amplitude = 18
                xy1 = []
                x=0
                xcord=centercanvas*2
                while x<heightcanvas:
                    # x coordinates
                    xy1.append(xcord * x_increment)
                    # y coordinates
                    xy1.append(int(sqrt(x * x_factor) * y_amplitude) + centercanvas)
                    x+=1
                    xcord+=1
                canvas.create_line(xy1, fill='black')
                break
            
            #-numbered
            if texted[i]=='-':
                i+=1
                #-numbers
                if texted[i] in num_dict :
                    somx+=(texted[i])
                    yx=-(eval(somx)*25)        
                    canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='black')
                    i+=1
                    yxa=-(centercanvas/eval(somx))
                #-numbered sin(x)
                    if texted[i] == 's' and texted[i+1]=='i' :
                        x_increment = 0.5
                        # width stretch
                        x_factor = 0.04035
                        # height stretch
                        y_amplitude = 25*-eval(somx)
                        # create the coordinate list for the sin() curve, have to be integers
                        xy1 = []
                        for x in range(heightcanvas*2):
                            # x coordinates
                            xy1.append(x * x_increment)
                            # y coordinates
                            xy1.append(int(sin(x * x_factor) * y_amplitude) + centercanvas)
                        canvas.create_line(xy1, fill='green')
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                        break
                #-numbered cos(x)
                    if texted[i] == 'c' and texted[i+1]=='o' :
                        x_increment = 0.5
                        # width stretch
                        x_factor = 0.04035
                        # height stretch
                        y_amplitude = 25*-eval(somx)
                            # create the coordinate list for the sin() curve, have to be integers
                        xy1 = []
                        for x in range(heightcanvas*2):
                            # x coordinates
                            xy1.append(x * x_increment)
                            # y coordinates
                            xy1.append(int(cos(x * x_factor) * y_amplitude) + centercanvas)
                        canvas.create_line(xy1, fill='blue')
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                        break
                #-numbered tan     
                    if texted[i] == 't' and texted[i+1]=='a' :
                        x_increment = 0.5
                        # width stretch
                        x_factor = 0.04035
                        # height stretch
                        y_amplitude = 25*eval(somx)
                        # create the coordinate list for the sin() curve, have to be integers
                        xy1 = []
                        for x in range(heightcanvas*2):
                            # x coordinates
                            xy1.append(x * x_increment)
                                # y coordinates
                            xy1.append(int(tan(x * x_factor) * y_amplitude) + centercanvas)
                        canvas.create_line(xy1, fill='red')
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill='white')
                        break
                #-numbered x
                    if texted[i]=='x':
                        i+=1
                        canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='black')
                        canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                        if texted[i]=='+':
                            i+=1
                            while i<len(texted):
                                if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                    som+=(texted[i])
                                    i+=1
                                y=(eval(som)*25)
                            canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                            canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='white')
                            canvas.create_line((centercanvas-yxa)-y/eval(somx), heightcanvas, (centercanvas+yxa)-y/eval(somx), 0,fill='black')
                            break
                        if texted[i]=='-':
                            i+=1
                            while i<len(texted):
                                if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                    som+=(texted[i])
                                    i+=1
                            y=(eval(som)*25)
                            canvas.create_line(0, centercanvas-yx, heightcanvas, centercanvas-yx,fill="white")
                            canvas.create_line((centercanvas-yxa), heightcanvas, (centercanvas+yxa), 0,fill='white')
                            canvas.create_line((centercanvas-yxa)+y/eval(somx), heightcanvas, (centercanvas+yxa)+y/eval(somx), 0,fill='black')
                            break
                        else: 
                            break
                
                #-x
                elif texted[i]=='x':
                    i+=1
                    if texted[i]=='+':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            y=(eval(som)*25)
                        canvas.create_line(0+y, 0, heightcanvas+y, heightcanvas,fill='black')
                        i+=1
                        break
                    if texted[i]=='-':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            y=(eval(som)*25)
                        canvas.create_line(0-y, 0, heightcanvas-y, heightcanvas,fill='black')
                        i+=1
                        break
                #-|x|
                elif texted[i]=='|' and texted[i+1]=='x':
                    i+=2
                    if texted[i]=='+':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            elif texted[i]=='|':
                                i+=1
                                if texted[i]=='+':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)-y,(centercanvas)-f, heightcanvas-y, heightcanvas-f,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas)-f, 0-y, heightcanvas-f,fill='black')
                                    break
                                if texted[i]=='-':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)-y,(centercanvas)+f, heightcanvas-y, heightcanvas+f,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas)+f, 0-y, heightcanvas+f,fill='black')
                                    break
                                else:
                                    canvas.create_line((centercanvas)-y,(centercanvas), heightcanvas-y, heightcanvas,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas), 0-y, heightcanvas,fill='black')
                                    break
                            y=(eval(som)*25)
                        i+=1
                        break
                    if texted[i]=='-':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            elif texted[i]=='|':
                                i+=1
                                if texted[i]=='+':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)+y,(centercanvas)-f, heightcanvas+y, heightcanvas+f,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas)-f, 0+y, heightcanvas+f,fill='black')
                                    break
                                if texted[i]=='-':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)+y,(centercanvas)+f, heightcanvas+y, heightcanvas+f,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas)+f, 0+y, heightcanvas+f,fill='black')
                                    break
                                else:
                                    canvas.create_line((centercanvas)+y,(centercanvas), heightcanvas+y, heightcanvas,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas), 0+y, heightcanvas,fill='black')
                                    break
                            y=(eval(som)*25)
                        i+=1
                        break  
                #-sin(x)
                if texted[i] == 's' and texted[i+1]=='i' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 26
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(-sin(x * x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='green')
                    break
                #-cos(x)
                if texted[i] == 'c' and texted[i+1]=='o' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 26
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(-cos(x * x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='blue')
                    break
                #-tan(x)
                if texted[i] == 't' and texted[i+1]=='a' :
                    x_increment = 0.5
                    # width stretch
                    x_factor = 0.04035
                    # height stretch
                    y_amplitude = 26
                    # create the coordinate list for the sin() curve, have to be integers
                    xy1 = []
                    for x in range(heightcanvas*2):
                        # x coordinates
                        xy1.append(x * x_increment)
                        # y coordinates
                        xy1.append(int(tan(x * x_factor) * y_amplitude) + centercanvas)
                    canvas.create_line(xy1, fill='red')
                    break
                
                else:
                        canvas.create_line(0, 0, heightcanvas, heightcanvas,fill='black')
                        break
            #x
            elif texted[i]=='x' :
                i+=1
                if texted[i]=='+':
                    i+=1
                    while i<len(texted):
                        if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                            som+=(texted[i])
                            i+=1
                        y=(eval(som)*25)
                    canvas.create_line(0-y, heightcanvas, heightcanvas-y, 0,fill='black')
                    i+=1
                    break
                if texted[i]=='-':
                    i+=1
                    while i<len(texted):
                        if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                            som+=(texted[i])
                            i+=1
                        y=(eval(som)*25)
                    canvas.create_line(0+y, heightcanvas, heightcanvas+y, 0,fill='black')
                    i+=1
                    break
                else: 
                    canvas.create_line(0, heightcanvas, heightcanvas, 0,fill='black')
                    break
            #|x|
            if texted[i]=='|' and texted[i+1]=='x':
                    i+=2
                    if texted[i]=='+':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            elif texted[i]=='|':
                                i+=1
                                if texted[i]=='+':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)-y,(centercanvas)-f, heightcanvas-y, 0-f,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas)-f, 0-y, 0-f,fill='black')
                                    break
                                if texted[i]=='-':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)-y,(centercanvas)+f, heightcanvas-y, 0+f,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas)+f, 0-y, 0+f,fill='black')
                                    break
                                else:
                                    canvas.create_line((centercanvas)-y,(centercanvas), heightcanvas-y, 0,fill='black')
                                    canvas.create_line((centercanvas)-y,( centercanvas), 0-y, 0,fill='black')
                                    break
                            y=(eval(som)*25)
                        i+=1
                        break
                    if texted[i]=='-':
                        i+=1
                        while i<len(texted):
                            if texted[i] in num_dict or texted[i]=='.' or texted[i]==',':
                                som+=(texted[i])
                                i+=1
                            elif texted[i]=='|':
                                i+=1
                                if texted[i]=='+':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)+y,(centercanvas)-f, heightcanvas+y, 0-f,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas)-f, 0+y, 0-f,fill='black')
                                    break
                                if texted[i]=='-':
                                    i+=1
                                    somy=texted[i]
                                    f=(eval(somy)*25)
                                    canvas.create_line((centercanvas)+y,(centercanvas)+f, heightcanvas+y, 0+f,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas)+f, 0+y, 0+f,fill='black')
                                    break
                                else:
                                    canvas.create_line((centercanvas)+y,(centercanvas), heightcanvas+y, 0,fill='black')
                                    canvas.create_line((centercanvas)+y,( centercanvas), 0+y, 0,fill='black')
                                    break
                            y=(eval(som)*25)
                        i+=1
                        break          
            
######################################################################################################################################
######################################################################################################################################
########################################### main canvas and buttons ################################################################## 
###################################################################################################################################### 
heightcanvas=701#########################################
centercanvas=heightcanvas/2##############################
#########################################################
canvas=Canvas(ctr_mid,bg="white",height=heightcanvas,width=heightcanvas)
canvas.pack()
def main_canvas():
    i=0 
    j=0
    #horizontal greys
    while i<heightcanvas:
        canvas.create_line(0, i, heightcanvas, i,fill="#E3E3E3")
        i+=25
    #vertical greys
    while j<heightcanvas:
        canvas.create_line(j, 0, j, heightcanvas,fill="#E3E3E3")
        j+=25
    #x and y axis
    canvas.create_line(0,(centercanvas), heightcanvas-1,(centercanvas))
    canvas.create_line((centercanvas), 0,(centercanvas), heightcanvas-1)
    #x axis numbering
    nx=14
    cx=-13
    while nx<heightcanvas:
        numx = Label(canvas, text=cx)
        numx.pack()
        canvas.create_window(nx, centercanvas+14, window=numx) 
        cx+=1
        nx+=25
    #y axis numbering
    ny=14
    cy=14
    while ny<heightcanvas:
        numy = Label(canvas, text=cy)
        numy.pack()
        canvas.create_window(centercanvas-14,ny, window=numy) 
        cy-=1
        ny+=25
main_canvas()
####################################################################################################################################### 
###########################################################buttons##################################################################### 
####################################################################################################################################### 
btncalc=Button(top_frame, text = "Calculator",font=fonted,height=2,width=8,command=opencalc)
btncalc.place(x=855,y=0)
# btncalc=Button(top_frame, text = "About us",font=fonted,height=2,width=8,command=aboutus)
# btncalc.place(x=855,y=0)
button = Button(ctr_right, text = "Enter",font=fonted,height=1,width=5,command=drawing)
button.grid(row=1,column=4)

def writex():
    e.delete(0,END)
    e.insert(0,"x")
    return
btnx = Button(ctr_right,text= 'x', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writex)
btnx.place(x=0, y=60)

def write_x():
    e.delete(0,END)
    e.insert(0,"-x")
    return
btn_x = Button(ctr_right,text= '-x', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write_x)
btn_x.place(x=50, y=60)

def writeabsx():
    e.delete(0,END)
    e.insert(0,"|x|")
    return
btnabsx = Button(ctr_right,text= '|x|', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writeabsx)
btnabsx.place(x=100, y=60)

def writenegabsx():
    e.delete(0,END)
    e.insert(0,"-|x|")
    return
btnnegabsx = Button(ctr_right,text= '-|x|', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writenegabsx)
btnnegabsx.place(x=150, y=60)

def cleartxtbox():
    e.delete(0,END)
    return
btncleartxt = Button(ctr_right,text= 'C', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =cleartxtbox)
btncleartxt.place(x=150, y=260)

def clearcanvas():
    ondisplaylistbox.delete(0,END)
    canvas.delete("all")
    main_canvas()
    return
btnclearcanvas = Button(ctr_right,text= 'CC', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =clearcanvas)
btnclearcanvas.place(x=50, y=260)


def writesqrtx():
    e.delete(0,END)
    e.insert(0,"√x")
    return
btnsqrtx = Button(ctr_right,text= '√x', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writesqrtx)
btnsqrtx.place(x=0, y=110)

def write1():
    e.insert(END,"1")
    return
btn1 = Button(ctr_right,text= '1', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write1)
btn1.place(x=50, y=110)

def write2():
    e.insert(END,"2")
    return
btn2 = Button(ctr_right,text= '2', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write2)
btn2.place(x=100, y=110)

def write3():
    e.insert(END,"3")
    return
btn3 = Button(ctr_right,text= '3', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write3)
btn3.place(x=150, y=110)

def write4():
    e.insert(END,"4")
    return
btn4 = Button(ctr_right,text= '4', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write4)
btn4.place(x=50, y=160)

def write5():
    e.insert(END,"5")
    return
btn5 = Button(ctr_right,text= '5', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write5)
btn5.place(x=100, y=160)

def write6():
    e.insert(END,"6")
    return
btn6 = Button(ctr_right,text= '6', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write6)
btn6.place(x=150, y=160)

def write7():
    e.insert(END,"7")
    return
btn7 = Button(ctr_right,text= '7', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write7)
btn7.place(x=50, y=210)

def write8():
    e.insert(END,"8")
    return
btn8 = Button(ctr_right,text= '8', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write8)
btn8.place(x=100, y=210)

def write9():
    e.insert(END,"9")
    return
btn9 = Button(ctr_right,text= '9', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write9)
btn9.place(x=150, y=210)

def write0():
    e.insert(END,"0")
    return
btn0 = Button(ctr_right,text= '0', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write0)
btn0.place(x=100, y=260)

def writeplus():
    e.insert(END,"+")
    return
btnplus = Button(ctr_right,text= '+', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writeplus)
btnplus.place(x=0, y=210)

def writeminus():
    e.insert(END,"-")
    return
btnminus = Button(ctr_right,text= '-', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =writeminus)
btnminus.place(x=0, y=260)
def writesinx():
    e.delete(0,END)
    e.insert(0,"sin(x)")
    return
btnsinx = Button(ctr_right,text= 'sin(x)', bd = '1',relief=GROOVE,height=2,width=8,font=fonted, command =writesinx)
btnsinx.place(x=0, y=310)
def writecosx():
    e.delete(0,END)
    e.insert(0,"cos(x)")
    return
btncosx = Button(ctr_right,text= 'cos(x)', bd = '1',relief=GROOVE,height=2,width=8,font=fonted, command =writecosx)
btncosx.place(x=71, y=310)
def writetanx():
    e.delete(0,END)
    e.insert(0,"tan(x)")
    return
btntanx = Button(ctr_right,text= 'tan(x)', bd = '1',relief=GROOVE,height=2,width=6,font=fonted, command =writetanx)
btntanx.place(x=142, y=310)
def write_sqrtx():
    e.delete(0,END)
    e.insert(0,"-√x")
    return
btn_sqrtx = Button(ctr_right,text= '-√x', bd = '1',relief=GROOVE,height=2,width=5,font=fonted, command =write_sqrtx)
btn_sqrtx.place(x=0, y=160)

def applyhistory():
    e.delete(0,END)
    e.insert(END, listbox_widget.get(ANCHOR))
    drawing()
    return
btnapplyhistory = Button(ctr_right,text= 'Apply', bd = '1',relief=GROOVE,height=2,width=8, command =applyhistory)
btnapplyhistory.place(x=130, y=360)
def deletehistory():
    listbox_widget.delete(ANCHOR)
    return
btndeletehistory = Button(ctr_right,text= 'Delete', bd = '1',relief=GROOVE,height=2,width=8, command =deletehistory)
btndeletehistory.place(x=130, y=410)
def clearhistory():
    listbox_widget.delete(0,END)
    return
btnclearhistory = Button(ctr_right,text= 'Clear', bd = '1',height=2,width=8,relief=GROOVE, command =clearhistory)
btnclearhistory.place(x=130, y=460)

var1 = IntVar()
c1 = Checkbutton(ctr_right, text='Add to existing function',variable=var1, onvalue=1, offvalue=0)
c1.place(x=0, y=30)
#i want to make an apply button to reapply the item in history
#i want to make alist for items on screen with colors
labelframe_widget = LabelFrame(ctr_right,text="History")
labelframe_widget.place(x=0,y=360)
listbox_widget = Listbox(labelframe_widget,height=8)
listbox_widget.pack()
labelcord=Label(ctr_right,text="Coordinates (hover over canvas to change value)",font=fonted2)
labelcord.place(x=10,y=660)

ondisplaylabelframe = LabelFrame(ctr_right,text="On display")
ondisplaylabelframe.place(x=0,y=515)
ondisplaylistbox = Listbox(ondisplaylabelframe,height=5,width=31)
ondisplaylistbox.pack()
############################################################################################################################ 
###########################################################buttons########################################################## 
############################################################################################################################ 
############################################################################################################################ 
# layout the widgets
width_label.grid(row=1, column=0)
e.grid(row=1, column=3)

#########################################################
def motion(event):
    x, y = event.x, event.y
    xx=round((x/25-15)+1,1)
    yy=round(-(y/25-13)+1,1)
    labelcord.config(text= ("x="+str(xx)+ " y="+str(yy)))
canvas.bind('<Motion>', motion)

def click(event):
    x, y = event.x, event.y
    xx=round((x/25-15)+1,1)
    yy=round(-(y/25-13)+1,1)
    canvas.create_oval(x, y,x+1, y+1, width = 2, fill = 'black')
    canvas.create_text(x+11, y+9,text="x="+str(xx)+" y="+str(yy),font=fonted)
    ondisplaylistbox.insert(0,("x="+str(xx)+" y="+str(yy)))
canvas.bind('<Button-1>', click)

root.resizable(False, False) 
root.eval('tk::PlaceWindow . center')
root.geometry("930x770")
root.mainloop()