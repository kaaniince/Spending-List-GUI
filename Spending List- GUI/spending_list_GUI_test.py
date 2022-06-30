from expense_list_GUI import Harcamalar
from tkinter import*
def main():
    root = Tk() #root nesnesi yaratıldı
    app = Harcamalar(root,[]) #özniteliğe ulaşmak için yaratıldı
    root.mainloop()#widget ekranda kalsın

main()