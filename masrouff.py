from pickle import load, dump
from datetime import datetime
from numpy import array
# Function load tableau
def loadt(t):
    try:
        with open("ficherfix.dat", "rb") as ft:
            n = 0
            while True:
                x = load(ft)
                t[n] = x  # Remplacer la ligne par un simple assignement
                n += 1
    except EOFError:
        print(t)
        return n
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
        return 0
# Function to search for a specific date
def recherche(t):
    with open("ficherfix.dat", "rb") as ft:
        n=0
        while True:
            try:
                x = load(ft)
                t[n]["tot"]=x["tot"]
                t[n]["day"]=x["day"]
                t[n]["mas"]=x["mas"]
                t[n]["mnt"]=x["mnt"]
                t[n]["des"]=x["des"]
                t[n]["dat"]=x["dat"]
                t[n]["cos"]=x["cos"]
                t[n]["rest"]=x["float"]
                n=n+1
            except EOFError:
                break

    # Find specific date
    i=0
    x=input("donner la date")
    while(i>n or t[i]["cos"]!=x):
        i=i+1
    if t[i]["cos"]==x:
        choices = ["DAY :"+str(t[i]["day"]), "MASROUF :"+str(t[i]["mas"]), "9ADECH :"+str(t[i]["mnt"]), "DESCRIPTION :"+str(t[i]["des"]), "DATE EXACT :"+str(t[i]["dat"])]
        for i, choice in enumerate(choices):
            print(f" {choice}")
        return
    else:
        print("n'existe pas")
        traitmentdenombre()
# Function to view file contents
def vuefich(filename, mode):
    print("-----------------")
    with open(filename, mode) as q:
        for line in q:
            if line.find("-")==-1:
                print(line, end='')
            else:
                print(line, end='')
                print("-----------------")
    c = int(input("retourner à la liste (1 ou 0): "))
    if c == 0:
        print("**")
    else:
        traitmentdenombre()
# Function to delete files
def fichsupp():
    c = input("si supprimer fichfix taper 2, si supprimer fichtxt taper 1: ")
    while not c.isdecimal():
        c = input("Erreur, si supprimer fichfix taper 1, si supprimer fichtxt taper 2: ")
    
    if c == "1":
        open("ficherjdid.txt", "w").close()
    elif c == "2":
        open("ficherfix.dat", "wb").close()
    
    print("Suppression avec succès")
    traitmentdenombre()
# Function to insert new entries
def Newinsert(t,i):
    with open("ficherjdid.txt", "a") as f:
            date_obj = datetime.now()
            day = date_obj.strftime("%A")
            a = input(" tu veux chnanger le a 1=nouvelle mois else 0")
            while not(a.isdecimal() and (0<=int(a)<3)):
                a = input("Erreur, tu veux chnanger le a 1=nouvelle mois else 0")
            if int(a)==1:
                tot= float(input("donner le montant de mois: ")),
            #tot=total(f)
            x ={
                    "tot":tot,
                    "day": day,
                    "mas": input("chnwa srafet ===> "),
                    "dat": str(date_obj),
                    "mnt": float(input("9adech ====> ")),
                    "des": input("tfatheelll ====> "),
                    "cos": f"{date_obj.day}-{date_obj.month}-{date_obj.year}"
                    }
            x={"rest":0,}
            t[i]["day"]=x["day"]
            t[i]["mas"]=x["mas"]
            t[i]["mnt"]=x["mnt"]
            t[i]["des"]=x["des"]
            t[i]["dat"]=x["dat"]
            t[i]["cos"]=x["cos"]
            t[i]["rest"]=x["rest"]
            i=i+1
            last_day = t[i-1]["day"]
            if last_day!= day:
                x['day']="*"
            else:
                x['day']=day
            f.write("\n".join([f"{x['day']}:\nchnwa chrit=> {x['mas']}\n9adech srafet=> {x['mnt']}DT\nkifech=> {x['des']}\ndate=> {x['dat']}\n{x['cos']}", ""]))
            print("saved")
    f.close()
    if input("t3awed t3abi (true/false): ").lower() != "false":
            Newinsert(t,i)
    if input("enregistrer 0 ou non 1: ") == "0":
            print("fichtxt saved")
            fichierfix(t,i)
    else:
            traitmentdenombre()
# Function to save data to fixed file
def fichierfix(t,n):
    with open("ficherfix.dat", "ab") as ft:
        for i in range(n):
            dump(t[i], ft)
    print("fichfix saved succsfuly")
# Function to manage main choices
def traitmentdenombre():
    print("Votre choix : ")
    choices = ["REMPLISSAGE JDID", "VUE FIXE", "FICHER SUPRIM", "RECHERCHE DATE EXACT", "Quitter"]
    for i, choice in enumerate(choices):
        print(f"Choix {i + 1} pour ==> {choice}")
    n = input("Donner un nombre: ")
    while not n.isdecimal() or not (1 <= int(n) <= len(choices)):
        n = input("Erreur, donner un nombre entre 1 et 5: ")
    n = int(n)
    if n == 1:
        qq = input("si le tableau est n'existe pas taper entre : ")
        if qq:
            i=loadt(t)
            Newinsert(t,i)
        else:
            i=0
            Newinsert(t,i)
    elif n == 2:
        g = int(input("vue fich txt (1) ou fix (0): "))
        vuefich("ficherjdid.txt" if g == 1 else "ficherfix.dat", "rb" if g == 0 else "r")
    elif n == 3:
        fichsupp()
    elif n == 4:
        recherche(t)
    else:
        print("Au revoir!")
# Main program entry
dict={
                    "tot":float(),
                    "day":str ,
                    "mas":str ,
                    "mnt":float(), 
                    "des":str,
                    "dat":str,
                    "cos":str,
                    "rest":float,
                }
t=array([dict]*2)
traitmentdenombre()
