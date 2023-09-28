from tkinter import * 
from PIL import Image, ImageTk
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
        self.btnAddOpt = Button(self.frame,text="Agregar clave",command=handleAdd)
        self.btnAddOpt.config(cursor="hand2")
        self.btnGenRand = Button(self.frame,text="Generar clave aleatoria",command=handleRand)
        self.btnGenRand.config(cursor="hand2")
        self.btnShowCont = Button(self.frame,text="Mostrar contenido",command=handleShow)
        self.btnShowCont.config(cursor="hand2")
        self.btnSearch   = Button(self.frame,text="Buscar clave",command=handleSearch)
        self.btnSearch.config(cursor="hand2")
        self.btnExit     = Button(self.frame,text="Salir",command=handleExit)
        self.btnExit.config(cursor="hand2")
        
        self.btnAddOpt.grid(row=0,column=0,sticky=W,pady=2,padx=5)
        self.btnGenRand.grid(row=0,column=1,sticky=W,pady=2,padx=5)
        self.btnShowCont.grid(row=0,column=2,sticky=W,pady=2,padx=5)
        self.btnSearch.grid(row=0,column=3,sticky=W,pady=2,padx=5)
        self.btnExit.grid(row=0,column=4,sticky=W,pady=2,padx=5)
    def getFrame(self)->Frame:
        return self.frame    
class ScreenAddKey:
    def __init__(self,root) -> None:
        self.frame = Frame(root)
        #self.frame.grid(row=0,column=5,sticky=W,pady=2)
        #self.frame.pack(side=TOP)
        self.label = Label(self.frame,text = "Ingresa clave: ")
        self.entry = Entry(self.frame)
        self.button = Button(self.frame,text="Send value",command=self.handleAddKey)
        self.button.config(cursor="hand2")
        self.label.grid(row=0,column=0,sticky=W,pady=2)
        self.entry.grid(row=0,column=1,sticky=W,pady=2)
        self.button.grid(row=1,column=1,sticky=E,pady=2)
    def getFrame(self)->Frame:
        return self.frame
    def getValue(self)->str:
        return self.entry.get()
    def handleAddKey(self)->None:
        print(self.getValue())
class Screens:
    def __init__(self) -> None:
        self.startGui()
       
    def startGui(self)->None:
        self.root = Tk()
        self.root.geometry('600x300')
        self.root.config(bg="lightblue")
        
    def getRoot(self)->Tk:
        return self.root
    def displayMenu(self)->None:
        self.screenMenu = ScreenOpts(self.root,self.displayAddKey,self.displayGenRanKey,self.displayShowContent,self.displaySearchKey,self.displayExit)
        self.screenMenu.getFrame().pack()
    def displayAddKey(self)->None:
        self.root.destroy()
        self.startGui()
        self.screenAddKey = ScreenAddKey(self.root)
        self.screenAddKey.getFrame().pack(pady=2)
        
        
    
    def displayGenRanKey(self)->None:
        pass
    def displayShowContent(self)->None:
        pass
    def displaySearchKey(self)->None:
        pass
    def displayExit(self)->None:
        pass
obj = Screens()
obj.displayMenu()
obj.getRoot().mainloop()