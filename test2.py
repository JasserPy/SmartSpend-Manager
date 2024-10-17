from pickle import load, dump
from datetime import datetime
from numpy import array
# Function load tableau
def loadt(t):
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
                n=n+1
            except EOFError:
                traitmentdenombre()
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
                n=n+1
            except EOFError:
                break

    # Find specific date
    for i, entry in enumerate(t):
        p=entry["dat"]
        p=p[:p.find(" ")]
        x=input("donner la date")
        if p == x:
            choices = ["DAY :"+str(entry["day"]), "MASROUF :"+str(entry["mas"]), "9ADECH :"+str(entry["mnt"]), "DESCRIPTION :"+str(entry["des"]), "DATE EXACT :"+str(entry["dat"])]
            for i, choice in enumerate(choices):
                print(f" {choice}")
            return
    print("n'existe pas")

# Function to view file contents
def vuefich(filename, mode):
    with open(filename, mode) as q:
        for line in q:
            print(line, end='')

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
        open("ficherfix.txt", "w").close()
    
    print("Suppression avec succès")
    traitmentdenombre()
# Function to insert new entries
def Newinsert(t):
    with open("ficherjdid.txt", "a") as f:
            last_day = t[-1]["day"] if t else None  # Get the last saved day if exists
            while True:
                date_input = input("Entrer une date (format YYYY-MM-DD) ou appuyer sur Entrée pour aujourd'hui: ")
                if date_input:
                    try:
                        date_obj = datetime.strptime(date_input, "%Y-%m-%d")
                        day = date_obj.strftime("%A")  # Get day from entered date
                    except ValueError:
                        print("Format de date invalide. Veuillez réessayer.")
                        continue
                else:
                    date_obj = datetime.now()
                    day = date_obj.strftime("%A")

                if last_day == day:
                    print("Vous ne pouvez pas entrer le même jour. Veuillez entrer un jour différent.")
                    continue

                x = {
                    "tot": float(input("donner le montant de mois: ")),
                    "day": day,
                    "mas": input("chnwa srafet ===> "),
                    "mnt": float(input("9adech ====> ")),
                    "des": input("tfatheelll ====> "),
                    "dat": str(date_obj),
                    "cos": f"{date_obj.day}-{date_obj.month}-{date_obj.year}"
                }
                t.append(x)
                f.write("\n".join([f"{x['day']}:\nchnwa chrit=> {x['mas']}\n9adech srafet=> {x['mnt']}DT\nkifech=> {x['des']}\ndate=> {x['dat']}\n{x['cos']}", ""]))
                if input("t3awed t3abi (true/false): ").lower() != "true":
                    break

            if input("enregistrer 1 ou non 0: ") == "0":
                print("fichtxt saved")
            else:
                fichierfix(t)
# Function to save data to fixed file
def fichierfix(t):
    with open("ficherfix.dat", "ab") as ft:
        for entry in t:
            dump(entry, ft)
    print("fichfix saved")
    recherche(t)

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
            loadt(t)
        else:
            Newinsert(t)
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
                }
t=[dict]
traitmentdenombre()