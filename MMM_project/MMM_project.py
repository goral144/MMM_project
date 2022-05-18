from re import I
from tkinter import *
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
from array import *

def click_action():
    if vmasa.get().isnumeric() == TRUE and vopor_powietrza.get().isnumeric() == TRUE and vkat_wystrzalu.get().isnumeric() == TRUE and vpredkosc_pocz.get().isnumeric() == TRUE :
        m = float (vmasa.get())
        b = float (vopor_powietrza.get())
        a = float (vkat_wystrzalu.get())
        v = float (vpredkosc_pocz.get())
        t_tab = array('f',[0,0.1])
        x_tab = array('f',[0,0.1])
        y_tab = array('f',[0,0.1])
        x_max = float(0)
        y_max =float(0)
        x_t = float (0)
        y_t = float (0)
        t = float (0)
        t_max_y = float (0)
        t_max = float (0)

        """OBLICZENIA"""
        
        rad = float ((a/180)*math.pi)
        k = float (b/m)
        Vox = float (v*math.cos(rad))
        g = float (9.81)
        Voy = float (v*math.sin(rad))        
        
        while y_t >= 0:
            x_t = (Vox/k)*(1 - math.exp(-k*t))
            y_t = (((Voy/k)+(g/b))*(1 - math.exp(-k*t))) - ((g*t)/k)
            i = int(t*100)
            t_tab.insert(i,t)
            x_tab.insert(i,x_t)
            y_tab.insert(i,y_t)
            if y_t>y_max:
                y_max = y_t
                t_max_y = t
            elif  x_t>x_max:
                x_max = x_t
            t_max = t
            t = t + 0.01

        i = int(t*100) 
        x_tab.insert(i,x_max)
        y_tab.insert(i,0)

        print("Y max = ")
        print(y_max)
        print("Czas do osiągnięcia Y max =")
        print(t_max_y)
        print("X max = ")
        print(x_max)
        print("T max = ")
        print(t_max)
        plt.plot(x_tab,y_tab,color='tab:red')
        plt.xlim([0,x_t+0.01])
        plt.ylim([0,y_max+0.01])
        plt.title('WYKRES y(x)')
        plt.show()

        print("KONIEC LOT!!")
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
    
def click_action1():
    if vmasa.get().isnumeric() == TRUE and vopor_powietrza.get().isnumeric() == TRUE and vkat_wystrzalu.get().isnumeric() == TRUE and vpredkosc_pocz.get().isnumeric() == TRUE :
        m = float (vmasa.get())
        b = float (vopor_powietrza.get())
        a = float (vkat_wystrzalu.get())
        v = float (vpredkosc_pocz.get())
        t_tab = array('f',[0,0.1])
        x_tab = array('f',[0,0.1])
        y_tab = array('f',[0,0.1])
        x_max = float(0)
        y_max =float(0)
        x_t = float (0)
        y_t = float (0)
        t = float (0)

        """OBLICZENIA"""
        
        rad = float ((a/180)*math.pi)
        k = float (b/m)
        Vox = float (v*math.cos(rad))
        g = float (9.81)
        Voy = float (v*math.sin(rad))        
        
        while y_t >= 0:
            x_t = (Vox/k)*(1 - math.exp(-k*t))
            y_t = (((Voy/k)+(g/b))*(1 - math.exp(-k*t))) - ((g*t)/k)
            i = int(t*100)
            t_tab.insert(i,t)
            x_tab.insert(i,x_t)
            y_tab.insert(i,y_t)
            if y_t>y_max:
                y_max = y_t
            elif  x_t>x_max:
                x_max = x_t
            t = t + 0.01

        i = int(t*100) 
        x_tab.insert(i,x_max)
        t_tab.insert(i,t)       
        plt1.plot(t_tab,x_tab,color='tab:red')
        plt1.xlim([0,t+0.01])
        plt1.ylim([0,x_max+0.01])
        plt1.title('WYKRES x(t)')
        plt1.show()

        print("KONIEC x(t)!")
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
        print("KONIEC ZŁE DANE!")

def click_action2():
    if vmasa.get().isnumeric() == TRUE and vopor_powietrza.get().isnumeric() == TRUE and vkat_wystrzalu.get().isnumeric() == TRUE and vpredkosc_pocz.get().isnumeric() == TRUE :
        m = float (vmasa.get())
        b = float (vopor_powietrza.get())
        a = float (vkat_wystrzalu.get())
        v = float (vpredkosc_pocz.get())
        t_tab = array('f',[0,0.1])
        x_tab = array('f',[0,0.1])
        y_tab = array('f',[0,0.1])
        x_max = float(0)
        y_max =float(0)
        x_t = float (0)
        y_t = float (0)
        t = float (0)

        """OBLICZENIA"""
        
        rad = float ((a/180)*math.pi)
        k = float (b/m)
        Vox = float (v*math.cos(rad))
        g = float (9.81)
        Voy = float (v*math.sin(rad))    
        
        while y_t >= 0:
            x_t = (Vox/k)*(1 - math.exp(-k*t))
            y_t = (((Voy/k)+(g/b))*(1 - math.exp(-k*t))) - ((g*t)/k)
            i = int(t*100)
            t_tab.insert(i,t)
            x_tab.insert(i,x_t)
            y_tab.insert(i,y_t)
            if y_t>y_max:
                y_max = y_t
            elif  x_t>x_max:
                x_max = x_t
            t = t + 0.01

        i = int(t*100) 
        y_tab.insert(i,0)
        t_tab.insert(i,t)
        plt2.plot(t_tab,y_tab,color='tab:red')
        plt2.xlim([0,t+0.01])
        plt2.ylim([0,y_max+0.01])
        plt2.title('WYKRES y(t)')
        plt2.show()

        print("KONIEC y(t)!")
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
        print("KONIEC ZŁE DANE!")


root = Tk()
root.title("MMM")
root.geometry("800x600")
text_label = Label(root, font=15, text="Wprowadź parametry")
masa = Label(root, font=40, text="Masa  [kg]")
opor_powietrza = Label(root, font=40, text="Opór powietrza [kg/s]")
kat_wystrzalu = Label(root, font=40, text="Kąt wystrzału [°]")
predkosc_pocz = Label(root, font=40, text="Prędkość początkowa [m/s]")
text_label.pack()

masa.place(x=0,y=50,height=50,width=200)
vmasa = Entry(root, width=10)
vmasa.insert(END, '0')
vmasa.place(x=10,y=100,height=25,width=180)

opor_powietrza.place(x=200,y=50,height=50,width=200)
vopor_powietrza = Entry(root,width=10) 
vopor_powietrza.insert(END, '0')
vopor_powietrza.place(x=210,y=100,height=25,width=180)

kat_wystrzalu.place(x=400,y=50,height=50,width=200)
vkat_wystrzalu = Entry(root,width=10)
vkat_wystrzalu.insert(END, '0')
vkat_wystrzalu.place(x=410,y=100,height=25,width=180)

predkosc_pocz.place(x=600,y=50,height=50,width=200)
vpredkosc_pocz = Entry(root,width=10)
vpredkosc_pocz.insert(END, '0')
vpredkosc_pocz.place(x=610,y=100,height=25,width=180)

Button(root, text="LOT POCISKU", font=40, width=10, command=click_action).place(x=325,y=150,height=50,width=150)
Button(root, text="RZUT OŚ X", font=40, width=10, command=click_action1).place(x=150,y=150,height=50,width=150)
Button(root, text="RZUT OŚ Y", font=40, width=10, command=click_action2).place(x=500,y=150,height=50,width=150)



root.mainloop()
