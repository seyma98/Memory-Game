from tkinter import *
from  random import *
root=Tk()
root.title("THE HARDEST MEMORY GAME")
root.geometry("900x900")

liste=[]
size=5
x=0
i=0


def last_value():
 etiket['text']=""


def rand_value():
 global size
 global liste
 global i
 if(i<size):
  a=randint(1,100)
  liste.append(a)
  locx=randint(50,850)
  locy=randint(50,850)
  etiket['text']=str(a)
 
  etiket.place(relx=locx/900,rely=locy/900)
  i=i+1
  root.after(1000,rand_value)
 else:
  last_value()

def validate(value):
 try: 
  if value:
   return int(value)
 except:
  return None

def Takeinput():
 global i
 global x
 global liste
 global size
  
 value=e.get() 
 valid_value=validate(value)
 e.delete(0,"end")
 
 if(valid_value!=liste[x]):
  error=Label(root,text=str(x+1)+". number is not correct. Try again!")
  error.pack()
  error.after(1000,error.destroy)
 else:
  error2=Label(root,text="Congratulations!")
  error2.pack()
  error2.after(1000,error2.destroy)
  x=x+1
  if(x==size):
   x=0 
   i=0
   liste.clear()
   size=size+1

   rand_value()
etiket=Label(root)
e=Entry(root)
e.pack()
rand_value()

b=Button(root,height=1,width=10,text="click",command=Takeinput).pack()


root.mainloop()








