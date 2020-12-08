import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=400)
canvas1.pack()

# input data for ivory
inputbox1 = tk.Entry(root)
canvas1.create_window(80, 50, window=inputbox1)
label1 = tk.Label(root, text='Enter number of Ivory Computers:')
label1.config(font=('helvetica', 10))
canvas1.create_window(110, 20, window=label1)

inputbox2 = tk.Entry(root)
canvas1.create_window(80, 120, window=inputbox2)
label2 = tk.Label(root, text='Enter number of Ivory Monitors:')
label2.config(font=('helvetica', 10))
canvas1.create_window(110, 90, window=label2)

inputbox3 = tk.Entry(root)
canvas1.create_window(80, 190, window=inputbox3)
label3 = tk.Label(root, text='Enter number of Ivory Monitors:')
label3.config(font=('helvetica', 10))
canvas1.create_window(110, 160, window=label3)

inputbox4 = tk.Entry(root)
canvas1.create_window(80, 250, window=inputbox4)
label4 = tk.Label(root, text='Enter number of Ivory Monitors:')
label4.config(font=('helvetica', 10))
canvas1.create_window(110, 220, window=label4)

# input data for ksp
inputbox5 = tk.Entry(root)
canvas1.create_window(450, 50, window=inputbox5)
label5 = tk.Label(root, text='Enter number of KSP Computers:')
label5.config(font=('helvetica', 10))
canvas1.create_window(480, 20, window=label5)

inputbox6 = tk.Entry(root)
canvas1.create_window(450, 120, window=inputbox6)
label6 = tk.Label(root, text='Enter number of KSP Monitors:')
label6.config(font=('helvetica', 10))
canvas1.create_window(480, 90, window=label6)

inputbox7 = tk.Entry(root)
canvas1.create_window(450, 190, window=inputbox7)
label7 = tk.Label(root, text='Enter number of KSP Monitors:')
label7.config(font=('helvetica', 10))
canvas1.create_window(480, 160, window=label7)

inputbox8 = tk.Entry(root)
canvas1.create_window(450, 250, window=inputbox8)
label8 = tk.Label(root, text='Enter number of KSP Monitors:')
label8.config(font=('helvetica', 10))
canvas1.create_window(480, 220, window=label8)

# ivory list price and input
ivorylist = ["computer", "monitor", "keyboard", "mouse"]
ivoryprice = [2200, 9000, 300, 700]

# ksp list price and input
ksplist = ["computer", "monitor", "keyboard", "mouse"]
kspprice = [2000, 4000, 500, 400]

# input prices for ivory
def getSquareRoot1():
    x1 = int(inputbox1.get()) * ivoryprice[0] + int(inputbox2.get()) * ivoryprice[1] + int(inputbox3.get()) * ivoryprice[2] + int(inputbox4.get()) * ivoryprice[3]

    label10 = tk.Label(root, text=int(x1))
    canvas1.create_window(80, 330, window=label10)

# input prices for ksp
def getSquareRoot2():
    x2 = int(inputbox5.get()) * kspprice[0] + int(inputbox6.get()) * kspprice[1] + int(inputbox7.get()) * kspprice[2] + int(inputbox8.get()) * kspprice[3]

    label2 = tk.Label(root, text=int(x2))
    canvas1.create_window(450, 330, window=label2)

# input for Frier
def getSquareRoot3():
    x3 = int(inputbox1.get()) * ivoryprice[0] + int(inputbox2.get()) * ivoryprice[1] + int(inputbox3.get()) * ivoryprice[2] + int(inputbox4.get()) * ivoryprice[3] + int(inputbox5.get()) * kspprice[0] + int(inputbox6.get()) * kspprice[1] + int(inputbox7.get()) * kspprice[2] + int(inputbox8.get()) * kspprice[3]

    label3 = tk.Label(root, text=int(x3))
    canvas1.create_window(280, 380, window=label3)

# button for Calculate Ivory Total Price
button1 = tk.Button(text='Calculate Ivory Total Price ', command=getSquareRoot1)
canvas1.create_window(100, 300, window=button1)

# button for Calculate KSP Total Price
button2 = tk.Button(text='Calculate KSP Total Price ', command=getSquareRoot2)
canvas1.create_window(460, 300, window=button2)

# button for Calculate Frier Total Price
button3 = tk.Button(text='Calculate Frier Total Price ', command=getSquareRoot3)
canvas1.create_window(280, 340, window=button3)

root.mainloop()