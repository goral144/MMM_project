from cmath import sin
from re import I
from tkinter import *
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
from array import *

from numpy import size

def click_action():

    blad = FALSE
    try: m = float (vmasa.get())
    except ValueError: blad = TRUE
    try: k = float (vopor_powietrza.get())
    except ValueError: blad = TRUE
    try: a = float (vkat_wystrzalu.get())
    except ValueError: blad = TRUE
    try: v = float (vpredkosc_pocz.get())
    except ValueError: blad = TRUE

    if blad == FALSE:  
        '''krok obliczen'''  
        h = float(0.001) 
        '''parametry wpisywane przez uzytkownika'''
        m = float (vmasa.get())
        b = float (vopor_powietrza.get())
        a = float (vkat_wystrzalu.get())
        v = float (vpredkosc_pocz.get())
        t_tab = array('f',[])
        x_tab = array('f',[])
        y_tab = array('f',[])
        x_max = float(0)
        y_max =float(0)
        x_t = float (0)
        y_t = float (0)
        t = float (0)
        t_max_y = float (0)
        t_max = float (0)
        delta_x = float(0)
        delta_y = float(0)
        g = float(9.81)
        

        rad = float ((a/180)*math.pi)
        i = 1
        t_tab.insert(0,t)
        x_tab.insert(0,x_t)
        y_tab.insert(0,y_t)
        
        x_t = x_tab[0] + h*(v)*math.cos(rad) + h*h/2*(-b/m)*(v)*math.cos(rad) 
        y_t = y_tab[0] + h*(v)*math.sin(rad) + h*h/2*(-g-b/m*(v)*math.sin(rad))
        t = t + h

        t_tab.insert(i,t)
        x_tab.insert(i,x_t)
        y_tab.insert(i,y_t)
        delta_x = x_tab[1] - x_tab[0]
        delta_y = y_tab[1] - y_tab[0]


        while y_tab[i] > 0:
            i = i + 1
            x_t = x_tab[i-1] + h*(delta_x/h) + h*h/2*(-b/m)*(delta_x/h)
            y_t = y_tab[i-1] + h*(delta_y/h) + h*h/2*(-g-b/m*(delta_y/h))
            t = t_tab[i-1] + h
            t_tab.insert(i,t)
            x_tab.insert(i,x_t)
            y_tab.insert(i,y_t)
            delta_x = x_tab[i] - x_tab[i-1]
            delta_y = y_tab[i] - y_tab[i-1]
            t_max = t
            if y_t>y_max:
                y_max = y_tab[i]
                t_max_y = t_tab[i]
            elif  x_t>x_max:
                x_max = x_tab[i]

        print("Y max = ")
        print(y_max)
        print("Czas do osiągnięcia Y max =")
        print(t_max_y)
        print("X max = ")
        print(x_max)
        print("T max = ")
        print(t_max)
        

        plt.clf()
        plt.subplot(3,1,1)
        plt.plot(t_tab,x_tab,color='tab:red')
        plt.xlim([0,t_max])
        plt.ylim([0,x_max])
        plt.title('1.WYKRES x(t)  2.WYKRES y(t)  3.WYKRES y(x)')
        
        plt.subplot(3,1,2)
        plt.plot(t_tab,y_tab,color='tab:red')
        plt.xlim([0,t_max])
        plt.ylim([0,y_max])

        plt.subplot(3,1,3)
        plt.plot(x_tab,y_tab,color='tab:red')
        plt.xlim([0,x_max])
        plt.ylim([0,y_max])
        plt.title('\n')
        
        plt.tight_layout

        plt.show()


    else:
        vmasa.delete(0, END)
        vmasa.insert(END, '0')
        vopor_powietrza.delete(0, END)
        vopor_powietrza.insert(END, '0')
        vkat_wystrzalu.delete(0, END)
        vkat_wystrzalu.insert(END, '0')
        vpredkosc_pocz.delete(0, END)
        vpredkosc_pocz.insert(END, '0')
        messagebox.showerror('Informacja', 'Źle wprowadzone dane')
        print("KONIEC, ZŁE DANE!")

root = Tk()
root.title("MMM")
root.geometry("800x600")
text_label = Label(root, font=25, text="Wprowadź parametry")
masa = Label(root, font=40, text="Masa  \n[kg]")
opor_powietrza = Label(root, font=40, text="Opór powietrza \n[kg/s]")
kat_wystrzalu = Label(root, font=40, text="Kąt wystrzału \n[°]")
predkosc_pocz = Label(root, font=40, text="Prędkość początkowa \n[m/s]")
text_label.pack()

masa.place(x=0,y=50,height=50,width=200)
vmasa = Entry(root, width=10)
vmasa.insert(END, '0')
vmasa.place(x=10,y=110,height=25,width=180)

opor_powietrza.place(x=200,y=50,height=50,width=200)
vopor_powietrza = Entry(root,width=10) 
vopor_powietrza.insert(END, '0')
vopor_powietrza.place(x=210,y=110,height=25,width=180)

kat_wystrzalu.place(x=400,y=50,height=50,width=200)
vkat_wystrzalu = Entry(root,width=10)
vkat_wystrzalu.insert(END, '0')
vkat_wystrzalu.place(x=410,y=110,height=25,width=180)

predkosc_pocz.place(x=600,y=50,height=50,width=200)
vpredkosc_pocz = Entry(root,width=10)
vpredkosc_pocz.insert(END, '0')
vpredkosc_pocz.place(x=610,y=110,height=25,width=180)

Button(root, text="LOT POCISKU", font=40, width=10, command=click_action).place(x=325,y=150,height=50,width=150)

root.mainloop()