# This is a small GUI program that encrypts user input with the given offset value using a caeser cypher method of encryption
#todo input validation and blank space triming


from tkinter import *
import string
import collections

def caesar(pText, offset):
   upper = collections.deque(string.ascii_uppercase)
   lower = collections.deque(string.ascii_lowercase)

   upper.rotate(offset)
   lower.rotate(offset)

   upper =''.join(list(upper))
   lower =''.join(list(lower))

   return pText.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase,lower))

def myClick():
    errorLB = Label(root, text="")
    errorLB.grid(row=5, column=0)
    errorLB2 = Label(root, text="")
    errorLB2.grid(row=6, column=0)

    plainText=ptxtBox.get()
    offsetNM=int(offsetBox.get())
    if plainText.replace(" ", "").isalpha() is False:
        errorLB= Label(root,text="Only letters are allowed!")
        errorLB.grid(row=5,column=0)
    if offsetNM >= 0 and offsetNM <= 25:
        cypherT=caesar(plainText.replace(" ", ""),offsetNM)
        etxt = Label(root, text=cypherT)
        cyphLB= Label(root, text="Cypher Text:")
        cyphLB.grid(row=4,column=0)
        etxt.grid(row=4,column=1)
    else:
        errorLB2 = Label(root, text="Only 0-25 can be used for offset values!")
        errorLB2.grid(row=6, column=0)


#build GUI
root =Tk()
mylabel = Label(root, text="Caesar Cypher")
plainTxtLb=Label(root,text="Plain Text:")
ptxtBox = Entry(root)
offsetLb = Label(root, text="Offset of Letter:")
offsetBox = Entry(root)


encryptBTN = Button(root, text="encrypt", command=myClick)
mylabel.grid(row=0,column=0)
plainTxtLb.grid(row=1,column=0)
ptxtBox.grid(row=1,column=1)
offsetLb.grid(row=2,column=0)
offsetBox.grid(row=2,column=1)
encryptBTN.grid(row=3,column=1)


root.mainloop()




