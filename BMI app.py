import customtkinter as ctk
#imort settings file
from settings import *
#responsible about window
try:
    from ctypes import windll,byref,sizeof,c_int
except:
    pass
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)
        self.title('')
        self.iconbitmap('images/empty.ico')
        self.geometry('400x400')
        #to prevent window resize
        self.resizable(False,False)
        #method
        self.change_title_bar_color()

        #layout
        self.columnconfigure(0,weight=1)
        #4 rows
        self.rowconfigure((0,1,2,3),weight=1,uniform='a')

        #widgets
        ResultText(self)
        WeightInput(self)






        self.mainloop()

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(
                HWND,
                DWMWA_ATTRIBUTE,
                byref(c_int(COLOR)),
                sizeof(c_int))
        except:
            pass

#inherit from ctk.CTkLabel
class ResultText(ctk.CTkLabel):
    def __init__(self,parent):
        font = ctk.CTkFont(family=FONT,size=MAIN_TEXT_SIZE,weight='bold')
        #use parent .CTkLabel
        super().__init__(master=parent,text=22.5,font=font,text_color=WHITE)
        self.grid(column=0,row=0,rowspan=2,sticky='nsew')

class WeightInput(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=WHITE)
        self.grid(column=0,row=2,sticky='nsew',padx=10,pady=10)

        #LAYOUT
        self.rowconfigure(0,weight=1,uniform='b')
        self.columnconfigure(0,weight=2,uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        



#to run this file only
if __name__== '__main__':
    App()

