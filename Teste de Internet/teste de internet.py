#importe o TKinter
from tkinter import*

#importando o pillow
from PIL import Image, ImageTk


# cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue

#criando janela

janela = Tk ()
janela.title("")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(width=False, height=FALSE)

#dividindo a janela em d2 freme 
Frame_logo = Frame(janela, width=350, height=60, bg=co1)
Frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_corpo = Frame(janela, width=350, height=140, bg=co1)
Frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurado o frame_logo
imagem = Image.open('speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)


l_logo_imagem = Label(Frame_logo, height=60,image=imagem, compound=LEFT, padx=10, anchor='nw', font=("Ivy 16 bold"),bg=co1,fg=co3)
l_logo_imagem.place(x=20, y=0)
l_logo_nome = Label(Frame_logo, text='Internet speed test', padx=10, anchor=NE, font=("Ivy 20"),bg=co1,fg=co4)
l_logo_nome.place(x=75, y=10)

#linha do titulo
l_logo_linha = Label(Frame_logo, width=350, anchor=NW, font=("Ivy 1"),bg=co2)
l_logo_linha.place(x=0, y=57)


janela.mainloop()

