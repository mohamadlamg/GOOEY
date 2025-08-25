from tkinter import *
import random 
from tkinter import messagebox
import os

if not os.path.exists("bills"):
      os.mkdir("bills")

#definition des fonctions

def total ():
    global prix_savon,prix_coca,prix_deo,prix_dmq,prix_fanta,prix_huile,prix_Kapa,prix_lb,prix_malta,prix_mc,prix_pata,prix_yam,prix_sdo,prix_sdr,prix_rg,prix_parfum,prix_vimto,tva,TotalCos_prix,TotalEpi_prix,TotalSuc_prix

      #total des produits cosmetiques
    
    prix_savon = int(Entresavon.get())*500
    prix_parfum = int(Entreparfum.get())*4000
    prix_deo = int(Entredeo.get())*2500
    prix_rg = int(Entrerg.get())*500
    prix_lb = int(Entrelb.get())*1000
    prix_dmq = int(Entredmq.get())*800 

    TotalCos_prix = prix_savon+prix_parfum+prix_rg+prix_deo+prix_dmq+prix_lb
    EntreTotalCos.delete(0,END)
    EntreTotalCos.insert(0,f"{TotalCos_prix}  FCFA")

     #total prix des epiceries

    prix_sdr = int(Entresdr.get())*21000
    prix_huile = int(Entrehuile.get())*3500
    prix_sdo = int(Entresdo.get())*9000
    prix_pdt = int(Entrepdt.get())*8000
    prix_yam = int(Entreyam.get())*800
    prix_pata = int(Entrepata.get())*800

    TotalEpi_prix = prix_sdr+prix_sdo+prix_huile+prix_pdt+prix_yam+prix_pata
    EntreTotalEpi.delete(0,END)
    EntreTotalEpi.insert(0,f"{TotalEpi_prix}  FCFA")

   #total sucrerie

    prix_coca = int(Entrecoca.get())*500
    prix_fanta = int(Entrefanta.get())*500
    prix_Kapa = int(EntreKapa.get())*500
    prix_mc = int(Entremc.get())*500
    prix_malta = int(Entremalta.get())*500
    prix_vimto = int(Entrevimto.get())*500

    TotalSuc_prix = prix_coca+prix_Kapa+prix_malta+prix_fanta+prix_vimto+prix_mc
    EntreTotalSuc.delete(0,END)
    EntreTotalSuc.insert(0,f"{TotalSuc_prix}  FCFA")

    #calcul TVA 

    tva = (TotalCos_prix+TotalEpi_prix+TotalSuc_prix)*0.05
    Entretva.delete(0,END)
    Entretva.insert(0,f"{tva}  FCFA")

 #generation de facture

def save ():
      global numfac
      numfac = random.randint(1000,9999)
      result = YES

      messagebox.askyesno("Enregistrer","Voulez vous enregistrer cette facture ?")
      if result :
            contenu = zonetexte.get(1.0,END)
            dossier = open("bills/{numfac}.txt","w")
            dossier.write(contenu)
            dossier.close()
            messagebox.showinfo("Enregistrer","facture enregistré avec succès")

def facture ():
    if NomEntre.get() == '' or NumEntre.get() == '':
          messagebox.showerror("Erreur","Informations sur l'acheteur(se) réquises")

    elif EntreTotalCos.get()=='' and EntreTotalEpi.get()=='' and EntreTotalSuc.get()=='' :
          messagebox.showerror("Erreur","Aucun achat effectué")

    elif EntreTotalCos.get()=="0  FCFA" and EntreTotalEpi.get()=="0  FCFA" and EntreTotalSuc.get()=="0  FCFA" :
         messagebox.showerror("Erreur","Aucun achat effectué")

    else:
          
         zonetexte.insert(END,"\t\tANGE-SERVICES\n")
         zonetexte.insert(END,f"--------------------------------------------")
         numfac = random.randint(1000,9999)
         zonetexte.insert(END,f"\nNº de facture :  {numfac}\n")
         zonetexte.insert(END,f"Client(e) : {NomEntre.get()}\n")
         zonetexte.insert(END,f"Nº du Client(e) : {NumEntre.get()}\n")
         zonetexte.insert(END,f"--------------------------------------------\n")
         zonetexte.insert(END,"Produits\t\tQuantité\t\tPrix\n")
         zonetexte.insert(END,f"--------------------------------------------\n")
        #afficher les marchandises et les prix
         if Entresavon.get() !=  "0" :
                zonetexte.insert(END,f"Savon LUX\t\t{Entresavon.get()}\t\t{prix_savon} FCFA\n")
         if Entreparfum.get() != "0":
                zonetexte.insert(END,f"Parfum LV\t\t{Entreparfum.get()}\t\t{prix_parfum} FCFA\n")
         if Entrerg.get() != "0":
                zonetexte.insert(END,f"Rouges à lèvres\t\t{Entrerg.get()}\t\t{prix_rg} FCFA\n")
         if Entredeo.get() != "0" :
                zonetexte.insert(END,f"Déodorant\t\t{Entredeo.get()}\t\t{prix_deo} FCFA\n")
         if Entrelb.get() != "0" :
                zonetexte.insert(END,f"Lubrifiant\t\t{Entrelb.get()}\t\t{prix_lb} FCFA\n")
         if Entredmq.get() != "0" :
                zonetexte.insert(END,f"Démaquillant\t\t{Entredmq.get()}\t\t{prix_dmq} FCFA\n")
         if Entresdr.get() != "0" :
                zonetexte.insert(END,f"Sac de riz\t\t{Entresdr.get()}\t\t{prix_sdr} FCFA\n")
         if Entrehuile.get() != "0" :
                zonetexte.insert(END,f"Huile\t\t{Entrehuile.get()}\t\t{prix_huile} FCFA\n")
         if Entresdo.get() != "0" :
                zonetexte.insert(END,f"Sac d'oignons\t\t{Entresdo.get()}\t\t{prix_sdo} FCFA\n")
         if Entreyam.get() != "0":
                zonetexte.insert(END,f"Ignames(par Kg)\t\t{Entreyam.get()}\t\t{prix_yam} FCFA\n")
         if Entrepata.get() != "0" :
                zonetexte.insert(END,f"Patates(par Kg)\t\t{Entrepata.get()}\t\t{prix_pata} FCFA\n")
         if Entrecoca.get() != "0":
                zonetexte.insert(END,f"Coca cola\t\t{Entrecoca.get()}\t\t{prix_coca} FCFA\n")
         if Entrefanta.get() != "0" :
                zonetexte.insert(END,f"Fanta\t\t{Entrefanta.get()}\t\t{prix_fanta} FCFA\n")
         if EntreKapa.get() != "0" :
                zonetexte.insert(END,f"Kapa\t\t{EntreKapa.get()}\t\t{prix_Kapa} FCFA\n")
         if Entremc.get() != "0" :
                zonetexte.insert(END,f"Moka café\t\t{Entremc.get()}\t\t{prix_mc} FCFA\n")
         if Entremalta.get() != "0" :
                zonetexte.insert(END,f"Malta\t\t{Entremalta.get()}\t\t{prix_malta} FCFA\n")
         if Entrevimto.get() != "0" :
                zonetexte.insert(END,f"Vimto\t\t{Entrevimto.get()}\t\t{prix_vimto} FCFA\n")
         zonetexte.insert(END,f"--------------------------------------------")
         #ajouter la tva
         zonetexte.insert(END,f"TVA\t\t\t\t{tva}\n")
         zonetexte.insert(END,f"--------------------------------------------")
         #donner le prix total
         Total_G = TotalSuc_prix+TotalCos_prix+TotalEpi_prix+tva
         zonetexte.insert(END,f"TOTAL\t\t\t\t{Total_G}\n")
         zonetexte.insert(END,f"\n\t Merci et à Bientôt !")
         

        
        

         
         










#Creation de l'interface
ft = Tk()
ft.title("Facture des Achats")

GrandTitre = Label(ft,text="Facture des Achats",font=("sans serif",40,"bold"),bg="skyblue",fg="ivory2",border=14,relief=RIDGE)
GrandTitre.pack(fill=X)

DetailsClient = LabelFrame(ft,text="Coordonnés du client",font=("sans serif",18,"bold"),fg="ivory2",bd=10,relief=GROOVE,bg="skyblue")
DetailsClient.pack(fill=X,pady=3)

NomClient = Label(DetailsClient,text="NOM ET PRENOM(S)",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2")
NomClient.grid(row=0,column=0,padx=12,pady=4)

NomEntre = Entry(DetailsClient,font=("arial",12),border=4,width=18)
NomEntre.grid(row=0,column=1,padx=8,pady=4)

NumClient = Label(DetailsClient,text="Nº de Téléphone",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2")
NumClient.grid(row=0,column=2,padx=12,pady=4)

NumEntre = Entry(DetailsClient,font=("arial",12),border=4,width=22)
NumEntre.grid(row=0,column=3,padx=10,pady=4)

NumFacture = Label(DetailsClient,text="Nº de Facture",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2")
NumFacture.grid(row=0,column=4,padx=12,pady=4)

FactureEntre = Entry(DetailsClient,font=("arial",12),border=4,width=22)
FactureEntre.grid(row=0,column=5,padx=20,pady=4)

Search = Button(DetailsClient,text="Rechercher",font=("sans serif",10,"bold"),bg="white",fg="black",bd=4)
Search.grid(row=0,column=6,pady=4)

Produits = Frame(ft)
Produits.pack(fill=X)

Cosmetiques = LabelFrame(Produits,text="Cosmétques & Beauté",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2",relief=GROOVE,bd=4)
Cosmetiques.grid(row=0,column=0,padx=3)

savon = Label(Cosmetiques,text="Savon LUX",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
savon.grid(row=0,column=0,padx=10)
Entresavon = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entresavon.grid(row=0,column=1,padx=6)
Entresavon.insert(0,0)

parfum = Label(Cosmetiques,text="Parfum LV",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
parfum.grid(row=1,column=0,padx=10,pady=11)
Entreparfum = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entreparfum.grid(row=1,column=1,pady=8,padx=6)
Entreparfum.insert(0,0)


deo = Label(Cosmetiques,text="Déodorant",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
deo.grid(row=2,column=0,padx=10,pady=11)
Entredeo = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entredeo.grid(row=2,column=1,pady=8,padx=6)
Entredeo.insert(0,0)


rg = Label(Cosmetiques,text="Rouge à lèvres",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
rg.grid(row=3,column=0,padx=10,pady=11)
Entrerg = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entrerg.grid(row=3,column=1,pady=8,padx=6)
Entrerg.insert(0,0)


lb = Label(Cosmetiques,text="Lubrifiant",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
lb.grid(row=4,column=0,padx=10,pady=11)
Entrelb = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entrelb.grid(row=4,column=1,pady=8,padx=6)
Entrelb.insert(0,0)


dmq = Label(Cosmetiques,text="Démaquillant",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
dmq.grid(row=5,column=0,padx=10,pady=11)
Entredmq = Entry(Cosmetiques,bd=4,relief=GROOVE)
Entredmq.grid(row=5,column=1,pady=8,padx=6)
Entredmq.insert(0,0)


Epicerie = LabelFrame(Produits,text="Épicerie",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2",relief=GROOVE,bd=4)
Epicerie.grid(row=0,column=1,padx=3)

sdr = Label(Epicerie,text="Sac de riz",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
sdr.grid(row=0,column=0,padx=10)
Entresdr = Entry(Epicerie,bd=4,relief=GROOVE)
Entresdr.grid(row=0,column=1,padx=6)
Entresdr.insert(0,0)


huile = Label(Epicerie,text="Huile",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
huile.grid(row=1,column=0,padx=10)
Entrehuile = Entry(Epicerie,bd=4,relief=GROOVE)
Entrehuile.grid(row=1,column=1,pady=8,padx=6)
Entrehuile.insert(0,0)


pdt = Label(Epicerie,text="Pomme de terre",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
pdt.grid(row=2,column=0,padx=10)
Entrepdt = Entry(Epicerie,bd=4,relief=GROOVE)
Entrepdt.grid(row=2,column=1,pady=8,padx=6)
Entrepdt.insert(0,0)


sdo = Label(Epicerie,text="Sac d'oignons",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
sdo.grid(row=3,column=0,padx=10)
Entresdo = Entry(Epicerie,bd=4,relief=GROOVE)
Entresdo.grid(row=3,column=1,pady=8,padx=6)
Entresdo.insert(0,0)


yam = Label(Epicerie,text="Ignames",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
yam.grid(row=4,column=0,padx=10)
Entreyam = Entry(Epicerie,bd=4,relief=GROOVE)
Entreyam.grid(row=4,column=1,pady=8,padx=6)
Entreyam.insert(0,0)


pata = Label(Epicerie,text="Patates",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
pata.grid(row=5,column=0,padx=10)
Entrepata = Entry(Epicerie,bd=4,relief=GROOVE)
Entrepata.grid(row=5,column=1,pady=8,padx=6)
Entrepata.insert(0,0)


Sucrerie = LabelFrame(Produits,text="Sucrerie",font=("sans serif",10,"bold"),bg="skyblue",fg="ivory2",relief=GROOVE,bd=4)
Sucrerie.grid(row=0,column=2,padx=3)

coca = Label(Sucrerie,text="Coca Cola",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
coca.grid(row=0,column=0,padx=10)
Entrecoca = Entry(Sucrerie,bd=4,relief=GROOVE)
Entrecoca.grid(row=0,column=1)
Entrecoca.insert(0,0)


fanta = Label(Sucrerie,text="Fanta",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
fanta.grid(row=1,column=0,padx=10)
Entrefanta = Entry(Sucrerie,bd=4,relief=GROOVE)
Entrefanta.grid(row=1,column=1,pady=8,padx=6)
Entrefanta.insert(0,0)


Kapa = Label(Sucrerie,text="Kapa",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
Kapa.grid(row=2,column=0,padx=10)
EntreKapa = Entry(Sucrerie,bd=4,relief=GROOVE)
EntreKapa.grid(row=2,column=1,pady=8,padx=6)
EntreKapa.insert(0,0)


mc = Label(Sucrerie,text="Moca café",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
mc.grid(row=3,column=0,padx=10)
Entremc = Entry(Sucrerie,bd=4,relief=GROOVE)
Entremc.grid(row=3,column=1,pady=8,padx=6)
Entremc.insert(0,0)


vimto = Label(Sucrerie,text="Vimto",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
vimto.grid(row=4,column=0,padx=10)
Entrevimto = Entry(Sucrerie,bd=4,relief=GROOVE)
Entrevimto.grid(row=4,column=1,pady=8,padx=6)
Entrevimto.insert(0,0)


malta = Label(Sucrerie,text="Malta",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
malta.grid(row=5,column=0,padx=10)
Entremalta = Entry(Sucrerie,bd=4,relief=GROOVE)
Entremalta.grid(row=5,column=1,pady=8,padx=6)
Entremalta.insert(0,0)


coinfacture = Frame(Produits,bd=5,relief=GROOVE)
coinfacture.grid(row=0,column=3)

titre = Label(coinfacture,text="Facture",font=("sans serif",9,"bold"),fg="deepskyblue3",bd=4,relief=GROOVE)
titre.pack(fill=X)

zonetexte = Text(coinfacture,height=10,width=44,bg="light cyan",fg="black")
zonetexte.pack()

scroll = Scrollbar(coinfacture,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=zonetexte.yview)

menufacture = LabelFrame(ft,text="Menu de Facture",font=("sans serif",13,"bold"),bg="skyblue",fg="ivory2")
menufacture.pack(fill=X,pady=5)

TotalCos = Label(menufacture,text="Total Cosmétques & Beauté",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
TotalCos.grid(row=0,column=0,padx=10)
EntreTotalCos = Entry(menufacture,bd=4,relief=GROOVE)
EntreTotalCos.grid(row=0,column=1,padx=6)

TotalEpi = Label(menufacture,text="Total Épicerie",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
TotalEpi.grid(row=1,column=0,padx=10)
EntreTotalEpi = Entry(menufacture,bd=4,relief=GROOVE)
EntreTotalEpi.grid(row=1,column=1,pady=3,padx=6)

TotalSuc = Label(menufacture,text="Total Sucrérie",font=("sans serif",9,"bold"),bg="skyblue",fg="ivory2")
TotalSuc.grid(row=2,column=0,padx=10)
EntreTotalSuc = Entry(menufacture,bd=4,relief=GROOVE)
EntreTotalSuc.grid(row=2,column=1,pady=3,padx=6,sticky=W)

tva = Label(menufacture,text="TVA",font=("sans serif",15,"bold"),bg="skyblue",fg="ivory2")
tva.grid(row=1,column=2,padx=10)
Entretva = Entry(menufacture,bd=4,relief=GROOVE)
Entretva.grid(row=1,column=3,pady=3,padx=20)

boutons = Frame(menufacture,bd=4,relief=GROOVE )
boutons.grid(row=0,column=4,rowspan=3)

totalbouton = Button(boutons,text="TOTAL",font=("sans serif",15,"bold"),command=total)
totalbouton.grid(row=1,column=0,padx=6,pady=12)

facturebouton = Button(boutons,text="FACTURE",font=("sans serif",15,"bold"),command=facture)
facturebouton.grid(row=1,column=1,padx=6,pady=12)

mailbouton = Button(boutons,text="EMAIL",font=("sans serif",15,"bold"))
mailbouton.grid(row=1,column=2,padx=6,pady=12)

printbouton = Button(boutons,text="ENREGISTRER",font=("sans serif",15,"bold"))
printbouton.grid(row=1,column=3,pady=12,padx=6)

clearbouton = Button(boutons,text="EFFACER",font=("sans serif",15,"bold"))
clearbouton.grid(row=1,column=4,pady=12)



ft.mainloop()