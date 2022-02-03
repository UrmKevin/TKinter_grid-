from tkinter import *
from tkinter.messagebox import *

def failist_sonastikusse():
    tk={}
    file=open("tk.txt","r")
    for line in file:
        t, k=line.strip().split(":")
        tk[t.strip()]=k.strip()
    print(tk)
    file.close()
    return tk

def kirjeldus_aknasse(t:str,p:str):
    if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        alam_aken.title(p)
        alam_aken.geometry("650x670")
        lbl_kirjeldus=Label(alam_aken,text=tk[t]).pack()
        c=Canvas(alam_aken,height=1000,width=1000)
        file=PhotoImage(file=t)
        c.create_image(2,2,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
        showinfo("Vastus","Kui ei taha, siis ei taha!")
    #print(tk[t])



tk=failist_sonastikusse()
aken=Tk()
aken.title("Tunniplaan")
aken.state('zoomed')

paevad=["TARpv21","Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,12,2):
    p=Label(aken,text=paevad[j],font="Arial 18",width=10,relief="solid",pady=60).grid(row=i-1,column=0,rowspan=2,sticky=N+S+W+E)
    j+=1

kell=["07.40 - 08.25","08.30 - 09.15","09.20 - 10.05","10.10 - 10.55","11.00 - 11.45","11.50 - 12.35","12.40 - 13.25","13.30 - 14.15"
      ,"14.20 - 15.05","15.10 - 15.55","16.00 - 16.45"]
for i in range(11):
    tn="t"+str(i)
    tn=Label(aken,text=str(i)+"\n\n\n"+kell[i],font="Arial 12",width=8,relief="solid",pady=40,padx=11).grid(row=0,column=i+1,sticky=N+S+W+E)


#EP 1 grupp
multimeediaEP_1=Button(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=2,column=2,columnspan=2,sticky=N+S+W+E)
akenEP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,column=4,sticky=N+S+W+E)
progEP_1=Button(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1",command=lambda:kirjeldus_aknasse("py.png","Programmeerimise alused")).grid(row=2,column=5,columnspan=3,sticky=N+S+W+E)
#EP 2 grupp
progEP_2=Button(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1",command=lambda:kirjeldus_aknasse("py.png","Programmeerimise alused")).grid(row=3,column=2,columnspan=3,sticky=N+S+W+E)
multimeediaEP_2=Button(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=3,column=5,columnspan=2,sticky=N+S+W+E)
akenEP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=3,column=7,sticky=N+S+W+E)
#EP
ruhm=Button(aken,text="Rühmaju\nhataja\ntund",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1").grid(row=2,rowspan=2,column=8,sticky=N+S+W+E)

#TP 1 gupp
eng_1=Button(aken,text="Inglise keel",font="Arial 16",borderwidth=1,relief="solid",bg="#f7ffa6").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
estTP_1=Button(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#b780cc").grid(row=4,column=9,sticky=N+S+W+E)
#TP 2 grupp
eng_2=Button(aken,text="Inglise keel",font="Arial 16",borderwidth=1,relief="solid",bg="#de7ed8").grid(row=5,column=2,columnspan=2,sticky=N+S+W+E)
estTP_2=Button(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#a4a4a4").grid(row=5,column=9,sticky=N+S+W+E)
#TP
os=Button(aken,text="Operatsioonisüstee\nmide alused",font="Arial 16",borderwidth=1,relief="solid",bg="#ae72d8").grid(row=4,rowspan=2,column=4,columnspan=2,sticky=N+S+W+E)
akenTP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=6,sticky=N+S+W+E)
kk=Button(aken,text="Kehaline kasvatus",font="Arial 16",borderwidth=1,relief="solid",bg="#be5899").grid(row=4,rowspan=2,column=7,columnspan=2,sticky=N+S+W+E)
speekTP=Button(aken,text="Inimese\nõpetus\neesti\nkeeles",font="Arial 16",borderwidth=1,relief="solid",bg="#eee57a").grid(row=4,rowspan=2,column=10,sticky=N+S+W+E)

#KP 1 grupp
progKP_1=Button(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1",command=lambda:kirjeldus_aknasse("py.png","Programmeerimise alused")).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
multimeediaKP_1=Button(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
#KP 1 grupp
multimeediaKP_2=Button(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=7,column=2,columnspan=3,sticky=N+S+W+E)
progKP_2=Button(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1",command=lambda:kirjeldus_aknasse("py.png","Programmeerimise alused")).grid(row=7,column=6,columnspan=3,sticky=N+S+W+E)
#KP
akenKP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=6,rowspan=2,column=5,sticky=N+S+W+E)
kunstKP=Label(aken,text="Kunstianed",font="Arial 16",bg="#b82cb5",borderwidth=1,relief="solid").grid(row=6,rowspan=2,column=9,columnspan=2,sticky=N+S+W+E)

#TP 1 grupp
estTP_1=Button(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#b780cc").grid(row=8,column=8,sticky=N+S+W+E)
#TP 2 grupp
estTP_2=Button(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#a4a4a4").grid(row=9,column=8,sticky=N+S+W+E)
#TP
andme=Button(aken,text="Andmebaasisüstee\nmide alused",font="Arial 16",borderwidth=1,relief="solid",bg="#df3b6f").grid(row=8,rowspan=2,column=2,columnspan=5,sticky=N+S+W+E)
speekNP=Button(aken,text="Inimese\nõpetus\neesti\nkeeles",font="Arial 16",borderwidth=1,relief="solid",bg="#eee57a").grid(row=8,rowspan=2,column=7,sticky=N+S+W+E)

#RP
rus=Button(aken,text="Keel ja kirjandus",font="Arial 16",borderwidth=1,relief="solid",bg="#badf3b").grid(row=10,rowspan=2,column=3,columnspan=2,sticky=N+S+W+E)
akenRP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=10,rowspan=2,column=5,sticky=N+S+W+E)
math=Button(aken,text="Matemaatika",font="Arial 16",borderwidth=1,relief="solid",bg="#cb8bc7").grid(row=10,rowspan=2,column=6,columnspan=2,sticky=N+S+W+E)
suht=Button(aken,text="Suhtlemine ja\nklieenditeenindus",font="Arial 16",borderwidth=1,relief="solid",bg="#ca74ef").grid(row=10,rowspan=2,column=8,columnspan=2,sticky=N+S+W+E)
speekRP=Button(aken,text="Inimese\nõpetus\neesti\nkeeles",font="Arial 16",borderwidth=1,relief="solid",bg="#eee57a").grid(row=10,rowspan=2,column=10,sticky=N+S+W+E)




emptyEP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=1,sticky=N+S+W+E)
emptyTsP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=1,sticky=N+S+W+E)
emptyKP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=6,rowspan=2,column=1,sticky=N+S+W+E)
emptyNP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=8,rowspan=2,column=1,sticky=N+S+W+E)
emptyRP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=10,rowspan=2,column=1,sticky=N+S+W+E)
emptyEP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=9,sticky=N+S+W+E)
emptyEP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=10,sticky=N+S+W+E)
emptyEP_3=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=11,sticky=N+S+W+E)
emptyKP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=6,rowspan=2,column=11,sticky=N+S+W+E)
emptyTsP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=11,sticky=N+S+W+E)
emptyTP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=8,rowspan=2,column=9,sticky=N+S+W+E)
emptyTP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=8,rowspan=2,column=10,sticky=N+S+W+E)
emptyEP_3=Label(aken,text="",borderwidth=1,relief="solid").grid(row=8,rowspan=2,column=11,sticky=N+S+W+E)
emptyRP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=10,rowspan=2,column=2,sticky=N+S+W+E)
emptyRP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=10,rowspan=2,column=11,sticky=N+S+W+E)

aken.mainloop()
