from tkinter import * 
from PIL import Image, ImageTk
from tareaTablaHash import TabHash,Nodo
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
        
        self.btnAddOpt.grid(row=0,column=0,sticky=W,pady=2,padx=5)
        self.btnGenRand.grid(row=1,column=0,sticky=W,pady=2,padx=5)
        self.btnShowCont.grid(row=2,column=0,sticky=W,pady=2,padx=5)
        self.btnSearch.grid(row=3,column=0,sticky=W,pady=2,padx=5)
        self.btnExit.grid(row=4,column=0,sticky=W,pady=2,padx=5)
    def getFrame(self)->Frame:
        return self.frame    
class ScreenAddKey:
    def __init__(self,root,handleAdd) -> None:
        self.frame = Frame(root)
        #self.frame.grid(row=0,column=5,sticky=W,pady=2)
        #self.frame.pack(side=TOP)
        self.label = Label(self.frame,text = "Ingresa clave: ")
        self.entry = Entry(self.frame)
        self.button = Button(self.frame,text="Send value",command=handleAdd)
        self.button.config(cursor="hand2")
        self.label.grid(row=0,column=0,sticky=W,pady=2)
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
    def __init__(self,root) -> None:
        self.frame = Frame(root)
        self.label = Label(self.frame,text="Ingresa Clave a buscar: ")
        self.entry = Entry(self.frame)
        self.button = Button(self.frame,text="Aceptar")
        self.button.config(cursor="hand2")
        self.label.grid(row=0,column=0,sticky=W,pady=2)
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
        self.frame.config(bg="#5b5b5b")
    def getFrame(self)->Frame:
        return self.frame
    def showElements(self,table:TabHash)->None:
        photo = PhotoImage(file = "./arrow.png")
        for i,item in enumerate(table.getTable()) :
            if item != None:
                self.button = Button(self.frame,text=item.cve)
                self.button.config(width=10,cursor="hand2",bg="black",foreground="#4fff00")
                self.button.grid(row=i,column=0,sticky=W,pady=30)
                col = 11;    
                while item.sig != None:
                    #icon = Button(self.frame,text="-->")
                    button = Button(self.frame,text=item.sig.cve)
                    button.config(width=10,cursor="hand2",bg="black",foreground="#4fff00")
                    #icon.grid(row=i,column=col,sticky=W,pady=2 )
                    button.grid(row=i,column=col,sticky=E,pady=30)
                    col += 11
                    item = item.sig
class Screens:
    def __init__(self) -> None:
        self.startGui()
        self.tableHash = TabHash(100)
       
    def startGui(self)->None:
        self.root = Tk()
        self.root.geometry('600x300')
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
        self.tableHash.insert(self.screenAddKey.getValue())
        self.screenAddKey.setValue("")

    def displayGenRanKey(self)->None:
        pass
    def displayShowContent(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenShow = ScreenShow(self.root)
        self.screenShow.getFrame().pack(pady=2)
        self.screenShow.showElements(self.tableHash)
    def displaySearchKey(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenSearch = ScreenSearch(self.root)
        self.screenSearch.getFrame().pack(pady=2)
    def displayExit(self)->None:
        self.root.destroy()
obj = Screens()
obj.displayMenu()
obj.getRoot().mainloop()