from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from PIL import ImageTk, Image
import pyttsx3



def speak():
    engine=pyttsx3.init()
    engine.setProperty('rate',130)
    engine.say(destination_txt.get(1.0,END),)
    engine.runAndWait()


def change(text="type",src="english",dest="hindi"):
        text1=text
        src1=src
        dest1=dest
        trans1=Translator().translate(text=text1,src=src1,dest=dest1)
        return trans1.text
def data():
    s=comb_sor.get()
    d=comb_destination.get()
    msg=source_txt.get(1.0,END)
    textget=change(text = msg,src = s,dest = d)
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textget)
    
    
root =Tk()
root.title("Text Translator")
root.geometry("1000x600")
root.resizable(False,False)


image_0=Image.open("D:\\MCA_FILES\\AI\\Text Translator Project\\background.jpg")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)



# root.config(bg='lightblue')
# label_name=Label(root,text="Translator",font=('Times New Roman',20))
# label_name.place(x=500,y=130,height=50,width=300)


frame= Frame(root).pack(side=BOTTOM)

label_source_txt=Label(root,text="Source Text",font=('Times New Roman',20))
label_source_txt.place(x=570,y=183,height=20,width=160)
source_txt=Text(frame,font=('Times New Roman',20),wrap=WORD)
source_txt.place(x=420,y=220,height=50,width=450)


list_text=list(LANGUAGES.values())
comb_sor=ttk.Combobox(frame,values=list_text)
comb_sor.place(x=420,y=280,height=40,width=100)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=lambda: [data(), speak()])
button_change.place(x=590,y=280,height=40,width=100)

comb_destination=ttk.Combobox(frame,values=list_text)
comb_destination.place(x=770,y=280,height=40,width=100)
comb_destination.set("english")


label_destination_txt=Label(root,text="Translated Text",font=('Times New Roman',20))
label_destination_txt.place(x=550,y=340,height=20,width=200)
destination_txt=Text(frame,font=('Times New Roman',20),wrap=WORD)
destination_txt.place(x=420,y=380,height=100,width=450)

# button_speak=Button(frame,text="Speak",relief=RAISED,command=speak)
# button_speak.place(x=10,y=400,height=40,width=100)

root.mainloop()