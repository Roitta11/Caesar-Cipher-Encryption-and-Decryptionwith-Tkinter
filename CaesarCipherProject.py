from tkinter import *
import tkinter.font as font
import tkinter as tk

# Caesar Cipher Encryption Algorithm
def encryption():

    cipherText.delete(0,'end')
 
    plainText= str(userMessage.get())
    keyValue = int(userKey.get())
    cipher=""

    for i in plainText:
        if i==' ':
            cipher = cipher + i
        elif i.isupper():
            cipher=cipher+chr((ord(i)+keyValue-65)%26+65)
        else:
            cipher=cipher+chr((ord(i)+keyValue-97)%26+97)

    finalOutput = cipher

    cipherText.insert(0,finalOutput)


# Caesar Cipher Decryption Algorithm
def decryption():
    userMessage2.delete(0,'end')

    toDecryptText= str(cipherText2.get())
    keyValueToDecrypt = int(userKey2.get())
    plainText2=""

    for i in toDecryptText:                                                                                 
        if i.isalpha()== True:
            x = ord(i) - 97
            x = x - keyValueToDecrypt
            x = x % 26
            plainText2+= chr(x + 97)
        else:
            plainText2 += i

    finalOutput2 = plainText2

    userMessage2.insert(0,plainText2)


root = Tk()
root.title('Caesar Cipher Machine')
FONT = font.Font(family ="Comic Sans MS", size ="9", weight ="bold")
root.geometry('500x300')

# Label for the Encryption Boxes
Label(root, text = "Caesar Cipher Encyption", font = FONT, bd=5, bg='#a60059', highlightbackground = '#a60059', fg='#FFFFCC').grid(row=1,column=1)
Label(root, font = FONT , fg= "#001a4d", text = "Plain Text ").grid(row=2, column = 0) 
Label(root, font = FONT , fg= "#001a4d", text = "Key ").grid(row=2, column = 2) 
Label(root, font = FONT , fg= "#001a4d", text = "Cipher Text ").grid(row=3, column = 0)

# Label for the Decryption Boxes
Label(root, text = "Caesar Cipher Decyption", font = FONT, bd=5, bg='#a60059', highlightbackground = '#a60059', fg='#FFFFCC').grid(row=5,column=1)
Label(root, font = FONT , fg= "#001a4d", text = "Cipher Text ").grid(row=6, column = 0) 
Label(root, font = FONT , fg= "#001a4d", text = "Key ").grid(row=6, column = 2) 
Label(root, font = FONT , fg= "#001a4d", text = "PLain Text ").grid(row=7, column = 0)


# Entry Boxes positioning for the Encyption 
userMessage = Entry(root) 
userKey = Entry(root) 
cipherText = Entry(root)

userMessage.grid(row=2, column=1) 
userKey.grid(row=2, column=3) 
cipherText.grid(row=3, column=1)

# Entry Boxes positioning for the Decryption 
cipherText2 = Entry(root) 
userKey2 = Entry(root) 
userMessage2  = Entry(root)

cipherText2.grid(row=6, column=1) 
userKey2.grid(row=6, column=3) 
userMessage2.grid(row=7, column=1)

# Button arrangement for Encyption and Decryption parts
Button(root, padx = 5, pady = 5, font=FONT, text='Encrypt', command=encryption).grid(row=4, column=1, sticky=W, pady=6)
Button(root, padx = 5, pady = 5, font=FONT, text='Quit', command=root.quit).grid(row=4, column=2, sticky=W, pady=6) 

Button(root, padx = 5, pady = 5, font=FONT, text='Decrypt', command=decryption).grid(row=8, column=1, sticky=W, pady=6)
Button(root, padx = 5, pady = 5, font=FONT, text='Quit', command=root.quit).grid(row=8, column=2, sticky=W, pady=6) 


# Run the window's mainloop
mainloop()