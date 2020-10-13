from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import PyPDF2
from fpdf import FPDF

import sqlite3

conn=sqlite3.connect('details.sqlite')
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Details(name TEXT,number VARCHAR(225),email VARCHAR(225) )")



def mainbook():
    window=Tk()

    window.title("Contack Book")
    window.geometry("600x600")
    color="#D3D3D3"
    btn_color="#A9A9A9"
    window.configure(bg=color)
    window.resizable(width=False,height=False)

    # variables


    #Frames

    first_frame=Frame(window,width=600,height=80,bg=color)
    first_frame.pack(side=TOP)

    second_frame=Frame(window,width=600,height=80,bg=color)
    second_frame.pack(side=TOP)

    third_frame=Frame(window,width=600,height=80,bg=color)
    third_frame.pack(side=TOP)

    forth_frame=Frame(window,width=600,height=80,bg=color)
    forth_frame.pack(side=TOP)

    fifth_frame=Frame(window,width=600,height=80,bg=color)
    fifth_frame.pack(side=TOP)

    sixth_frame=Frame(window,width=600,height=80,bg=color)
    sixth_frame.pack(side=TOP)

    seventh_frame= Frame(window,width=600,height=80,bg=color)
    seventh_frame.pack(side=TOP)

    eighth_frame= Frame(window,width=600,height=80,bg=color)
    eighth_frame.pack(side=TOP)

    #Functions
    def add():
        root=Tk()
        root.title("Insert")
        root.geometry("350x150")
        color = "#D3D3D3"
        btn_color = "#A9A9A9"
        root.configure(bg=color)
        root.resizable(width=False, height=False)

        b1=StringVar()
        b2=StringVar()
        b3=StringVar()

        a1 =Label(root,text="Name",bg=color)
        a1.place(x=35,y=10)
        e1 = Entry(root)
        e1.place(x=150,y=10)

        a2=Label(root,text="Phone Number",bg=color)
        a2.place(x=35,y=35)
        e2 = Entry(root)
        e2.place(x=150,y=35)

        a3=Label(root,text="Email",bg=color)
        a3.place(x=35,y=60)
        e3=Entry(root)
        e3.place(x=150,y=60)

        def savefile():
            cur.execute("INSERT INTO Details(name,number,email) VALUES (?,?,?)", (e1.get(), e2.get(),e3.get()))
            conn.commit()
            messagebox.showinfo('Message',"Successfully Saved !!")


        cancel=Button(root,text="Cancel",bg=btn_color,width=10,command=root.destroy).place(x=30,y=100)

        save=Button(root,text="Save",bg=btn_color,width=10,command=lambda :[savefile(),root.destroy()]).place(x=250,y=100)
        mainloop()


    def display():
        root1=Tk()
        root1.title("Contacts")
        root1.geometry("600x400")
        color="white"
        root1.configure(bg=color)
        root1.resizable(width=False, height=False)
        f1=Frame(root1,width=600,height=20,bg="red")
        f1.pack(side=BOTTOM)
        cur.execute("SELECT * FROM Details")
        try:
            data=cur.fetchone()[0]
            count=0
            l1 = Label(root1, text="Name", fg="black", bg=color).place(x=40, y=20)

            l2 = Label(root1, text="Phone Number", bg=color, fg="black").place(x=180, y=20)

            l3 = Label(root1, text="Email", fg="black", bg=color).place(x=380, y=20)
            for i in cur.execute("SELECT * FROM Details"):
                count=count+1
                Label(root1, text=count,fg="black",bg=color).place(x=10, y=40+(count*20))
                Label(root1, text=i[0],fg="black",bg=color).place(x=40, y=40+(count*20))
                Label(root1, text=i[1],fg="black",bg=color).place(x=180, y=40+(count*20))
                Label(root1, text=i[2],fg="black",bg=color).place(x=380, y=40+(count*20))
            Label(f1, text="Total Contacts : ", fg="black", bg=color).place(x=240)
            Label(f1, text=count, fg="black", bg=color).place(x=330)

        except:
            Label(root1,text="No Contacts Found !!",bg=color, fg="black").pack(side=TOP,pady=150)

        mainloop()

    def clear():
        cur.execute("DELETE FROM Details")
        messagebox.showinfo('Message', "All Contacts has been Successfully Removed !!")
        conn.commit()

    def find():
        root2 = Tk()
        root2.title("Contacts")
        root2.geometry("600x400")
        btn_color = "#A9A9A9"
        color="white"

        Label(root2,text="Enter Name").grid(column=0, row=5)
        q=Entry(root2)
        q.grid(column=1, row=5)

        def ff():
            cur.execute("SELECT * FROM Details WHERE name= ?",(q.get(),))

            try:
                data = cur.fetchone()[0]
                count = 0
                l1 = Label(root2, text="Name", fg="black", bg=color).place(x=40, y=40)

                l2 = Label(root2, text="Phone Number", bg=color, fg="black").place(x=180, y=40)

                l3 = Label(root2, text="Email", fg="black", bg=color).place(x=380, y=40)

                for i in cur.execute("SELECT * FROM Details WHERE name= ?",(q.get(),)):
                    count = count + 1
                    Label(root2, text=count, fg="black").place(x=10, y=60 + (count * 20))
                    Label(root2, text=i[0], fg="black").place(x=40, y=60 + (count * 20))
                    Label(root2, text=i[1], fg="black").place(x=180, y=60 + (count * 20))
                    Label(root2, text=i[2], fg="black").place(x=380, y=60 + (count * 20))
            except:
                if q.get() == "":
                    messagebox.showinfo('Error', "Field is Empty!!")
                else:
                    messagebox.showinfo('Message', "No Contacts Found !!")

        w=Button(root2, text="Find", bg=btn_color, width=8, command=lambda :[ff()]).grid(column=7, row=5)

        mainloop()

    def update():
        root3 = Tk()
        root3.title("Update")
        root3.geometry("350x150")
        color = "#D3D3D3"
        btn_color = "#A9A9A9"
        root3.configure(bg=color)
        root3.resizable(width=False, height=False)

        q=Label(root3,text="Enter Name",bg=color).place(x=60,y=50)
        w=Entry(root3)
        w.place(x=140,y=50)
        Button(root3,text="Go",bg=btn_color,width=8,command=lambda:[next(),root3.destroy()]).place(x=270,y=45)

        def next():
            name=w.get()
            try:
                cur.execute("SELECT * FROM Details WHERE name= ?", (name,))
                data=cur.fetchone()[0]
                root4 = Tk()
                root4.title("Insert")
                root4.geometry("350x150")
                color = "#D3D3D3"
                btn_color = "#A9A9A9"
                root4.configure(bg=color)
                root4.resizable(width=False, height=False)

                b1 = StringVar()
                b2 = StringVar()
                b3 = StringVar()

                a1 = Label(root4, text="Name", bg=color)
                a1.place(x=35, y=10)
                e1 = Entry(root4)
                e1.place(x=150, y=10)

                a2 = Label(root4, text="Phone Number", bg=color)
                a2.place(x=35, y=35)
                e2 = Entry(root4)
                e2.place(x=150, y=35)

                a3 = Label(root4, text="Email", bg=color)
                a3.place(x=35, y=60)
                e3 = Entry(root4)
                e3.place(x=150, y=60)
                def updatefile():
                    cur.execute("DELETE FROM Details WHERE name= ?", (name,))
                    cur.execute("INSERT INTO Details(name,number,email) VALUES (?,?,?)", (e1.get(), e2.get(), e3.get()))
                    conn.commit()
                    messagebox.showinfo('Message', "Successfully Updated !!")


                cancel = Button(root4, text="Cancel", bg=btn_color, width=10, command=root3.destroy).place(x=30, y=100)

                save = Button(root4, text="Update", bg=btn_color, width=10,
                              command=lambda: [updatefile(),root4.destroy()]).place(x=250, y=100)
            except:
                if w.get() == "":
                    messagebox.showinfo('Error', "Field is Empty!!")
                else:
                    messagebox.showinfo('Message', "No Contacts Found !!")

        mainloop()

    def generate():
            root5 = Tk()
            root5.title("Update")
            root5.geometry("350x150")
            color = "#D3D3D3"
            btn_color = "#A9A9A9"
            root5.configure(bg=color)
            root5.resizable(width=False, height=False)
            Label(root5, text="Save As:", bg=color).place(x=80, y=50)
            p = Entry(root5)
            p.place(x=140, y=50)
            def go():
                pdf1 = p.get() + ".pdf"
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=20)
                fh = open("eg.txt", "w")
                COUNT = 0
                for x in cur.execute("SELECT*FROM Details ORDER BY name ASC"):
                    COUNT = COUNT + 1
                    fh.write("Name :" + str(x[0]) + "\n")
                    fh.write("Phone_number :" + str(x[1]) + "\n")
                    fh.write("Email_address :" + str(x[2]) + "\n\n")
                fh.write("\nTotal contacts : " + str(COUNT))
                pdf.cell(200, 10, txt="Contact Details\n\n", ln=1, align='C')
                f = open("eg.txt", "r")
                pdf.set_font("Arial", size=15)
                fh.write("\n\n")
                fh.close()
                for q in f:
                    pdf.cell(200, 10, txt=q, ln=1, align='L')
                pdf.output(pdf1)


            Button(root5,text="Go",command=lambda :[go(),root5.destroy()],width=8,bg=btn_color).place(x=270,y=45)

            mainloop()

    def delc():
        root6 = Tk()
        root6.title("Update")
        root6.geometry("350x150")
        color = "#D3D3D3"
        btn_color = "#A9A9A9"
        root6.configure(bg=color)
        root6.resizable(width=False, height=False)

        q=Label(root6,text="Enter Name",bg=color).place(x=60,y=50)
        w=Entry(root6)
        w.place(x=140,y=50)
        name=w.get()
        def a():
            cur.execute("DELETE FROM Details WHERE name = ?", (w.get(),))
            conn.commit()
            messagebox.showinfo("Message","Contact deleted Successfully!!" )

        Button(root6,text="Delete",bg=btn_color,width=8,command=lambda:[a(),root6.destroy()]).place(x=270,y=45)


    #Buttons

    head=Label(first_frame,text="MENU",font=("Helvetica",26),bg=color,pady=40)
    head.pack(side=TOP)

    btn1=Button(second_frame,text="Insert Contact",bg=btn_color,width=40,command=add)
    btn1.pack(side=LEFT,pady=10)

    btn3=Button(third_frame,text="Update Contact",bg=btn_color,width=40,command=update)
    btn3.pack(side=LEFT,pady=10)

    btn4=Button(forth_frame,text="Search",bg=btn_color,width=40,command=find)
    btn4.pack(side=LEFT,pady=10)

    btn5=Button(fifth_frame,text="View Contacts",bg=btn_color,width=40,command=display)
    btn5.pack(side=LEFT,pady=10)

    btn6=Button(eighth_frame,text="Clear All",bg=btn_color,width=40,command=clear)
    btn6.pack(side=LEFT,pady=10)

    btn7=Button(seventh_frame,text="Generate Report",bg=btn_color,width=40,command=generate)
    btn7.pack(side=LEFT,pady=10)

    btn8=Button(sixth_frame,text="Delete",bg=btn_color,width=40,command=delc)
    btn8.pack(side=LEFT,pady=10)

    end=Label(window,text="Made By : Abhinav").pack(side=BOTTOM, ipadx=300)
    mainloop()
log=Tk()
log.title("Contack Book")
log.geometry("350x150")
color="#D3D3D3"
btn_color="#A9A9A9"
log.configure(bg=color)
log.resizable(width=False,height=False)

Label(log,text="Username ",bg=color).place(x=80,y=25)
e1=Entry(log)
e1.place(x=150,y=25)
Label(log,text="Password ",bg=color).place(x=80,y=60)
e2=Entry(log,show="*")
e2.place(x=150,y=60)


def ss():
    if e1.get()=="abhinav" and e2.get()=="123":
        log.destroy(),mainbook()
    else:
        messagebox.showinfo("Error","Wrong Password!!")

cancel = Button(log, text="Quit", bg=btn_color, width=10, command=log.destroy).place(x=30, y=100)

save = Button(log, text="Login", bg=btn_color, width=10,command=ss)
save.place(x=250,y=100)

mainloop()
