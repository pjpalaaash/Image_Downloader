
from tkinter import *

from tkinter import ttk
from tkinter import filedialog

import requests

Folder = ''

def openLocation():
    global Folder

    Folder = filedialog.askdirectory()

    if (len(Folder)> 1):

        locationError.config(text=Folder,fg='green')

    else:

        locationError.config(text="Please Choose the File Location",fg='red')     


def Download():

    url = urlentry.get()

    filename = url.split('/')[-1]

    fold = Folder

    if (len(url)>1):
        urlerror.config(text="")

        with requests.get(url, stream=True) as r:

            # print("DOWNLOADING IMAGE....!!!")

            with open(fold+'/'+filename,"wb") as f:

                # print('Processing...')
                for ch in r.iter_content(chunk_size=1024):
                    f.write(ch)

        f.close()
        urlerror.config(text="Download Completed!!")

    else:

        urlerror.config(text="Please Enter the Url")

root = Tk()

root.title('Image Downloader')

root.geometry('350x400')

root.columnconfigure(0,weight=1)

urllab = Label(root, text="Enter the Url")

urllab.grid()

urlentryVar = StringVar()

urlentry = Entry(root,width=50, textvariable=urlentryVar)

urlentry.grid()


urlerror = Label(root, text="Error", fg='red')
urlerror.grid()

saveLabel = Label(root, text="Save the Image File")

saveLabel.grid()

saveEntry = Button(root,width=10,fg='green',bg='white',text='Choose Path',command=openLocation)
saveEntry.grid()


locationError = Label(root, text="Error",fg='red')

locationError.grid()


Downloadbt = Button(root,text='Download',width=15,command=Download)

Downloadbt.grid()



root.mainloop()




