from tkinter import *
from tkinter import messagebox
import math
import matplotlib

def click_action():


   
    blad = FALSE
    try: m = float (vmasa.get())
    except ValueError: blad = TRUE
    try: k = float (vopor_powietrza.get())
    except ValueError: blad = TRUE
    try: a = float (vkat_wystrzalu.get())
    except ValueError: blad = TRUE
    try: rad = float ((k/180)*math.pi)
    except ValueError: blad = TRUE
    try: v = float (vpredkosc_pocz.get())
    except ValueError: blad = TRUE
    
    if blad == FALSE:
     
    


        """OBLICZENIA"""
        k = float (b/m)
        Vox = float (v*math.cos(rad))
        g = float (9.81)
        Voy = float (v*math.sin(rad))
        x_t = float (0)
        y_t = float (0)
        t = int (0)
        
        while y_t >= 0:
            os_x1 = t
            os_y1 = x_t
            x_t = (Vox/k)*(1 - math.exp(-k*t))
            y_t = (((Voy/k)+(g/b))*(1 - math.exp(-k*t))) - ((g*t)/k)
            print(t)
            print(y_t)
            print(x_t)
            t = t + 1
            
            
            
        print("KONIEC !!")



        print(m)
        print(k)
        print(a)
        print(rad)
        print(v)
        print("Wow!")
        

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
        print("LOL!")




root = Tk()
root.title("MMM")
root.geometry("900x800")
text_label = Label(root, font=15, text="Wprowadź parametry")
masa = Label(root, font=40, text="Masa  [kg]")
opor_powietrza = Label(root, font=40, text="Opór powietrza [kg/s]")
kat_wystrzalu = Label(root, font=40, text="Kąt wystrzału [°]")
predkosc_pocz = Label(root, font=40, text="Prędkość początkowa [m/s]")
text_label.pack()

masa.place(x=0,y=50,height=50,width=150)
vmasa = Entry(root, width=10)
vmasa.insert(END, '0')
vmasa.place(x=10,y=100,height=25,width=130)

opor_powietrza.place(x=230,y=50,height=50,width=180)
vopor_powietrza = Entry(root,width=10) 
vopor_powietrza.insert(END, '0')
vopor_powietrza.place(x=240,y=100,height=25,width=130)

kat_wystrzalu.place(x=460,y=50,height=50,width=150)
vkat_wystrzalu = Entry(root,width=10)
vkat_wystrzalu.insert(END, '0')
vkat_wystrzalu.place(x=470,y=100,height=25,width=130)

predkosc_pocz.place(x=670,y=50,height=50,width=250)
vpredkosc_pocz = Entry(root,width=10)
vpredkosc_pocz.insert(END, '0')
vpredkosc_pocz.place(x=700,y=100,height=25,width=130)

Button(root, text="Zatwierdź", font=40, width=10, command=click_action).place(x=385,y=150,height=50,width=150)


root.mainloop()

'''
from tkinter import *
from tkinter import messagebox as msg
 
 
def gui2_init():
    gui2 = Tk()
    gui_settings(gui2)
    gui2.mainloop()
 
 
def stability_test(k, a, A, m, gui):
    if a > 0 and k * A * m > 0:
        print("stability")
        gui.destroy()
        gui2_init()
    else:
        msg.showerror(title="!!!", message="Układ jest niestabilny")
        return 0
 
 
def submit(k_entry, a_entry, A_entry, m_entry, gui):
    # get value
    try:
        k = float(k_entry.get())
        a = float(a_entry.get())
        A = float(A_entry.get())
        m = float(m_entry.get())
 
        if k < 0:
            msg.showerror(title="!!!", message="Wartość k musi być dodatnia")
 
        if A < 0:
            msg.showerror(title="!!!", message="Wartość k musi być dodatnia")
 
        if stability_test(k, a, A, m, gui) == 0:
            # RESET ENTRY
            k_entry.delete(0, END)
            a_entry.delete(0, END)
            A_entry.delete(0, END)
            m_entry.delete(0, END)
 
    except:
        msg.showerror(title="!!!", message="Wpisz wartości")
 
 
def gui_settings(gui):
    gui.configure(bg="lightgray")
    gui.title("MMM")
    gui.geometry("900x400")
 
 
def gui_init():
    # INIT tk
    gui = Tk()
    gui_settings(gui)
 
 
    Label(gui, text="Podaj wartość k:", font="Helvetica 10 bold", bg="lightgray").grid(row=1, column=0, padx=20,
                                                                                       pady=0)
    Label(gui, text="Podaj wartość a:", font="Helvetica 10 bold", bg="lightgray").grid(row=1, column=1, padx=20,
                                                                                       pady=0)
    Label(gui, text="Podaj wartość A:", font="Helvetica 10 bold", bg="lightgray").grid(row=1, column=2, padx=20,
                                                                                       pady=0)
    Label(gui, text="Podaj wartość m:", font="Helvetica 10 bold", bg="lightgray").grid(row=1, column=3, padx=20,
                                                                                       pady=0)
 
    k_entry = Entry(gui, width=30)
    k_entry.grid(row=2, column=0, padx=20, pady=0)
 
    a_entry = Entry(gui, width=30)
    a_entry.grid(row=2, column=1, padx=20, pady=0)
 
    A_entry = Entry(gui, width=30)
    A_entry.grid(row=2, column=2, padx=20, pady=0)
 
    m_entry = Entry(gui, width=30)
    m_entry.grid(row=2, column=3, padx=20, pady=0)
 
    button_submit = Button(gui, text="Submit", bg="gray", height=2, width=15,
                           command=lambda: submit(k_entry, a_entry, A_entry, m_entry, gui))
    button_submit.grid(row=3, column=0, padx=5, pady=10, columnspan=5)
 
    # START
    gui.mainloop()
 
 
if __name__ == '__main__':
    gui_init()

    '''
