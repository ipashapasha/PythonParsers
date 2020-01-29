import tkinter
from tkinter import *

app = Tk()
app.title("Парсер из строки")

class Controls:
    
    def __init__(self,master):
        
        #Ввод
        self.title = Label(master, text="Введите вашу строку:", font=('bold', 14), padx=5, pady=5)
        self.title.grid(row=0, column=0)
        self.inputText = Entry(master, width=50)
        self.inputText.grid(row=0, column=1)
        self.inputButton = Button(master, width=15, command=self.parsingText, bg="#D23320", text="Распарсить")
        self.inputButton.grid(row=0, column=2)
        
        #Вывод
        self.title1 = Label(master, text="Тут будет результат:", font=('bold', 14), padx=5, pady=5)
        self.title1.grid(row=2, column=0)
        self.exportLabel = Label(master, width=50)
        self.exportLabel.grid(row=2, column=1)

        #Вспомогательные кнопки
        self.copyButton = Button(master,width=15, command=self.copyingClypboard, text="В буфер")
        self.copyButton.grid(row=2, column=2)
        self.closeButton = Button(master, width=15, command=self.closingProgram, text="Закрыть")
        self.closeButton.grid(row=3, column=2)

    def parsingText(self):
        p1 = self.inputText.get()
        p1 = p1.split(',')
        self.exportLabel['text'] = '\n'.join(p1)

    def copyingClypboard(self):
        app.clipboard_clear()
        app.clipboard_append(self.exportLabel['text'])

    def closingProgram(self):
        app.destroy()

firstBlock = Controls(app)

app.mainloop()