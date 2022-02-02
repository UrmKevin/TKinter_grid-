from tkinter import *
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
multimeediaEP_1=Label(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da").grid(row=2,column=2,columnspan=2,sticky=N+S+W+E)
akenEP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,column=4,sticky=N+S+W+E)
progEP_1=Label(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1").grid(row=2,column=5,columnspan=3,sticky=N+S+W+E)
#EP 2 grupp
progEP_2=Label(aken,text="Programmeerimise alused",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1").grid(row=3,column=2,columnspan=3,sticky=N+S+W+E)
multimeediaEP_2=Label(aken,text="Multimeedia",font="Arial 16",borderwidth=1,relief="solid",bg="#33b9da").grid(row=3,column=5,columnspan=2,sticky=N+S+W+E)
akenEP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=3,column=7,sticky=N+S+W+E)
#EP
ruhm=Label(aken,text="Rühmaju\nhataja\ntund",font="Arial 16",borderwidth=1,relief="solid",bg="#92def1").grid(row=2,rowspan=2,column=8,sticky=N+S+W+E)

#TP 1 gupp
eng_1=Label(aken,text="Inglise keel",font="Arial 16",borderwidth=1,relief="solid",bg="#f7ffa6").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
estTP_1=Label(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#b780cc").grid(row=4,column=9,sticky=N+S+W+E)
#TP 2 grupp
eng_2=Label(aken,text="Inglise keel",font="Arial 16",borderwidth=1,relief="solid",bg="#de7ed8").grid(row=5,column=2,columnspan=2,sticky=N+S+W+E)
estTP_2=Label(aken,text="Eesti keel",font="Arial 16",borderwidth=1,relief="solid",bg="#a4a4a4").grid(row=5,column=9,sticky=N+S+W+E)
#TP
os=Label(aken,text="Operatsioonisüstee\nmide alused",font="Arial 16",borderwidth=1,relief="solid",bg="#ae72d8").grid(row=4,rowspan=2,column=4,columnspan=2,sticky=N+S+W+E)
akenTP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=6,sticky=N+S+W+E)
kk=Label(aken,text="Kehaline kasvatus",font="Arial 16",borderwidth=1,relief="solid",bg="#be5899").grid(row=4,rowspan=2,column=7,columnspan=2,sticky=N+S+W+E)
speekTP=Label(aken,text="Inimese\nõpetus\neesti\nkeeles",font="Arial 16",borderwidth=1,relief="solid",bg="#eee57a").grid(row=4,rowspan=2,column=10,sticky=N+S+W+E)










emptyEP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=1,sticky=N+S+W+E)
emptyTP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=1,sticky=N+S+W+E)
emptyKP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=6,rowspan=2,column=1,sticky=N+S+W+E)
emptyNP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=8,rowspan=2,column=1,sticky=N+S+W+E)
emptyRP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=10,rowspan=2,column=1,sticky=N+S+W+E)
emptyEP_1=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=9,sticky=N+S+W+E)
emptyEP_2=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=10,sticky=N+S+W+E)
emptyEP_3=Label(aken,text="",borderwidth=1,relief="solid").grid(row=2,rowspan=2,column=11,sticky=N+S+W+E)
emptyTP=Label(aken,text="",borderwidth=1,relief="solid").grid(row=4,rowspan=2,column=11,sticky=N+S+W+E)

aken.mainloop()
