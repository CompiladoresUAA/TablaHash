from tkinter import * 
from tareaTablaHash import TabHash,Nodo,alfaNum,checkString
from tareaTabHashBook import TabHash as Tbook
from tkinter import messagebox as mb
from screeninfo import get_monitors
# Creamos la raíz
#root = Tk()

# Comenzamos el bucle de aplicación, es como un while True

#frame = Frame(root)  

# Empaqueta el frame en la raíz
#frame.pack()

# Como no tenemos ningún elemento dentro del frame, 
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background
"""frame.config(bg="lightblue")     
root.grid() 
# Read the Image
img = Image.open("./arrow.png")
resize_image = img.resize((50, 30))
img = ImageTk.PhotoImage(resize_image)
# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(bg="lightblue")
frame.config(width=480,height=320)
#frame.grid(row=0, column=0,rowspan=1, columnspan=4, sticky="nsew")"""
"""label  = Label(frame)
label.config(width=500,height=100, image=img,bg="lightblue",border=0)
label.grid( row=5, column=5)
root.mainloop()  """
class ScreenOpts:
    def __init__(self,root,handleAdd,handleRand,handleShow,handleSearch,handleExit) -> None:
        self.frame = Frame(root)
        self.frame.config(bg="#5b5b5b")
        
        Label(self.frame,width=20,height=1,bg="#595959",foreground="white",text="Elige una opción").grid(row=0,column=0,pady=10,sticky=W)
        self.btnAddOpt = Button(self.frame,text="Agregar clave",command=handleAdd,activebackground="black",activeforeground="white")
        self.btnAddOpt.config(width=20,cursor="hand2",bg="black",foreground="#4fff00")
        self.btnGenRand = Button(self.frame,text="Generar clave aleatoria",command=handleRand,activebackground="black",activeforeground="white")
        self.btnGenRand.config(width=20,cursor="hand2",bg="black",foreground="#4fff00")
        self.btnShowCont = Button(self.frame,text="Mostrar contenido",command=handleShow,activebackground="black",activeforeground="white")
        self.btnShowCont.config(width=20,cursor="hand2",bg="black",foreground="#4fff00")
        self.btnSearch   = Button(self.frame,text="Buscar clave",command=handleSearch,activebackground="black",activeforeground="white")
        self.btnSearch.config(width=20,cursor="hand2",bg="black",foreground="#4fff00")
        self.btnExit     = Button(self.frame,text="Salir",command=handleExit,activebackground="black",activeforeground="white")
        self.btnExit.config(width=20,cursor="hand2",bg="black",foreground="#4fff00")
        
        self.btnAddOpt.grid(row=1,column=0,sticky=W,pady=2,padx=5)
        self.btnGenRand.grid(row=2,column=0,sticky=W,pady=2,padx=5)
        self.btnShowCont.grid(row=3,column=0,sticky=W,pady=2,padx=5)
        self.btnSearch.grid(row=4,column=0,sticky=W,pady=2,padx=5)
        self.btnExit.grid(row=5,column=0,sticky=W,pady=2,padx=5)
    def getFrame(self)->Frame:
        return self.frame    
class ScreenAddKey:
    def __init__(self,root,handleAdd) -> None:
        self.frame = Frame(root)
        self.frame.config(bg="#5b5b5b")
        #self.frame.grid(row=0,column=5,sticky=W,pady=2)
        #self.frame.pack(side=TOP)
        self.label = Label(self.frame,text = "Ingresa clave: ")
        self.label.config(bg="black",foreground="#4fff00")
        self.entry = Entry(self.frame)
        self.entry.config(bg="black",foreground="#4fff00",insertbackground="white")
        self.button = Button(self.frame,text="Send value",command=handleAdd,activebackground="black",activeforeground="white")
        self.button.config(cursor="hand2")
        self.button.config(bg="black",foreground="#4fff00")
        self.label.grid(row=0,column=0,sticky=W,pady=2,padx=4)
        self.entry.grid(row=0,column=1,sticky=W,pady=2)
        self.button.grid(row=1,column=1,sticky=E,pady=2)
    def getFrame(self)->Frame:
        return self.frame
    def setValue(self,value)->None:
        self.entry.delete(0,END)
    def getValue(self)->str:
        return self.entry.get()
    def handleAddKey(self)->None:
        print(self.getValue())
class ScreenSearch:
    def __init__(self,root,handleSearch) -> None:
        self.frame = Frame(root)
        self.frame.config(bg="#5b5b5b")
        self.label = Label(self.frame,text="Ingresa Clave a buscar: ")
        self.entry = Entry(self.frame)
        self.entry.config(bg="black",foreground="#4fff00",insertbackground="white")
        self.button = Button(self.frame,text="Aceptar")
        self.button.config(bg="black",foreground="#4fff00")
        self.button.config(cursor="hand2",activebackground="black",command=handleSearch,activeforeground="white")
        self.label.config(bg="black",foreground="#4fff00")
        self.label.grid(row=0,column=0,sticky=W,pady=2,padx=4)
        self.entry.grid(row=0,column=1,sticky=W,pady=2)
        self.button.grid(row=1,column=1,sticky=E,pady=2)
    def getFrame(self)->Frame:
        return self.frame
    def getValue(self)->str:
        try:
            val = self.entry.get()
            return val
        except:
            return ""
class ScreenShow:
    def __init__(self,root) -> None:
        self.frame = Frame(root)
        self.frame.config(bg="#5b5b5b",pady=30)
    def getFrame(self)->Frame:
        return self.frame
    def showElements(self,table:TabHash)->None:
       
        j = 0
        for i,item in enumerate(table.getTable()) :
            if item != None:
                createButton(self.frame,"Indice").grid(row=0,column=0,sticky=W,pady=2)
                createButton(self.frame,"Cve").grid(row=0,column=11,sticky=W,pady=2)
                createButton(self.frame,str(i)).grid(row=j+1,column=0,sticky=W,pady=2)
                createButton(self.frame,item.cve).grid(row=j+1,column=11,sticky=W,pady=2)
                
                col = 22;    
                while item.sig != None:
                    createButton(self.frame,item.sig.cve).grid(row=j+1,column=col,sticky=E,pady=2)
                    
                    col += 11
                    item = item.sig
                j = j+1
def createButton(frame:Frame,text:str)->Button:    
    button = Button(frame,text=text)
    button.config(width=10,bg="black",foreground="#4fff00")
    return button
                
class Screens:
    def __init__(self,TableType) -> None:
        if TableType == 1 : 
            self.tableHash = Tbook(100)
        else:
            self.tableHash = TabHash(100)
        self.startGui()
       
    def startGui(self)->None:
        self.root = Tk()
        primary_screen = get_monitors()[0]
        w_width = primary_screen.width
        w_height = primary_screen.height
        self.root.geometry(f'{w_width}x{w_height}')
        self.root.config(bg="#595959")
        ret = Button(self.root,text="<-")
        ret.config(cursor="hand2",command=self.displayMenu,bg="black",foreground="#4fff00")
        ret.pack(side=LEFT,anchor=NW)
        
    def getRoot(self)->Tk:
        return self.root
    def displayMenu(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenMenu = ScreenOpts(self.root,self.displayAddKey,self.displayGenRanKey,self.displayShowContent,self.displaySearchKey,self.displayExit)
        self.screenMenu.getFrame().pack()
    def displayAddKey(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenAddKey = ScreenAddKey(self.root,self.handleAdd)
        self.screenAddKey.getFrame().pack(pady=2)
    def handleAdd(self)->None:    
        if checkString(self.screenAddKey.getValue()):
            self.tableHash.insert(self.screenAddKey.getValue())
            self.screenAddKey.setValue("")
        else:
            mb.showinfo("Value Incorrect","The value expected was an alphanumeric.")
#https://python-course.eu/tkinter/dialogs-in-tkinter.php
    def displayGenRanKey(self)->None:
        self.tableHash.insert(alfaNum())
        mb.showinfo('Success', 'Key added successfully')
    def displayShowContent(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenShow = ScreenShow(self.root)
        self.screenShow.getFrame().pack(side=LEFT,pady=2)
        self.screenShow.showElements(self.tableHash)
    def displaySearchKey(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenSearch = ScreenSearch(self.root,self.handleSearch)
        self.screenSearch.getFrame().pack(pady=2)
    def handleSearch(self)->None:
        if self.tableHash.buscar( self.screenSearch.getValue() ) :
            mb.showinfo('Success', 'The value was found')
        else:
            mb.showerror('The value doesn´t exist', 'The value specified isn´t in the table.')
    def displayExit(self)->None:
        self.root.destroy()
def genScreen(root:Tk,op:int)->None:
    root.destroy()
    obj = Screens(op) 
    obj.displayMenu()   
    obj.getRoot().mainloop()    
    
if __name__ == '__main__':
    init = Tk()
    init.geometry("450x380")
    init.config(bg="#595959")
    Label(init,width=30,height=1,bg="#595959",foreground="white",text="Elige una opción").pack(pady=10)
    opt1 = createButton(init,"Con función hash modulo.")
    opt2 = createButton(init,"Con función hash alfanumerica.")
    opt1.config(width=30,cursor="hand2",command=lambda: genScreen(init,1))
    opt2.config(width=30,cursor="hand2",command=lambda: genScreen(init,2))
    opt1.pack()
    opt2.pack()
    
    init.mainloop()
