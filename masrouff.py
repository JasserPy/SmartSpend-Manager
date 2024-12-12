from pickle import load, dump
from datetime import datetime

# Chemins des fichiers
TEXT_FILE = "expenses_log.txt"
DATA_FILE = "expenses.dat"

# Fonction pour afficher le contenu d'un fichier texte
def vue_fichier(filename):
    try:
        print("\n--- Contenu du fichier ---")
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Fichier introuvable.")
    except Exception as e:
        print("Erreur lors de la lecture :", e)

# Fonction pour supprimer les fichiers
def supprimer_fichier():
    try:
        print("Choisissez le fichier à supprimer :")
        print("1. Fichier texte (expenses_log.txt)")
        print("2. Fichier binaire (expenses.dat)")
        choix = input("Votre choix : ")

        if choix == "1":
            open(TEXT_FILE, "w").close()
            print("Fichier texte supprimé avec succès.")
        elif choix == "2":
            open(DATA_FILE, "wb").close()
            print("Fichier binaire supprimé avec succès.")
        else:
            print("Choix invalide.")
    except Exception as e:
        print("Erreur lors de la suppression :", e)

# Fonction pour insérer de nouvelles données directement dans le fichier texte
def nouvelle_insertion():
    try:
        now = datetime.now()
        jour = now.strftime("%A")
        montant_total = float(input("Montant du mois (DT) : ")) if input("Nouveau mois ? (1 pour oui, autre pour non) : ") == "1" else 0

        nouveau_record = {
            "tot": montant_total,
            "day": jour,
            "mas": input("Qu'avez-vous dépensé ? : "),
            "mnt": float(input("Montant (DT) : ")),
            "des": input("Description : "),
            "dat": now.strftime("%Y-%m-%d %H:%M:%S"),
            "cos": now.strftime("%d-%m-%Y"),
        }

        with open(TEXT_FILE, "a") as file:
            file.write(f"{jour} :\n")
            file.write(f"  Qu'avez-vous dépensé ? {nouveau_record['mas']}\n")
            file.write(f"  Montant : {nouveau_record['mnt']} DT\n")
            file.write(f"  Description : {nouveau_record['des']}\n")
            file.write(f"  Date : {nouveau_record['dat']}\n")
            file.write(f"  Date clé : {nouveau_record['cos']}\n\n")

        print("Dépense enregistrée avec succès.")

        if input("Ajouter une autre dépense ? (true/false) : ").lower() != "false":
            nouvelle_insertion()
    except ValueError:
        print("Veuillez entrer un montant valide.")
    except Exception as e:
        print("Erreur lors de l'insertion :", e)

# Fonction pour sauvegarder les données du fichier texte vers le fichier binaire si le jour change
def sauvegarder_dans_fichier_binaire():
    try:
        with open(TEXT_FILE, "r") as file:
            lignes = file.readlines()

        records = []
        record = {}
        for ligne in lignes:
            if " :" in ligne:
                if record:
                    records.append(record)
                record = {"day": ligne.split(" :")[0].strip()}
            elif "Qu'avez-vous dépensé ?" in ligne:
                record["mas"] = ligne.split("?")[1].strip()
            elif "Montant :" in ligne:
                record["mnt"] = float(ligne.split(":")[1].strip().replace(" DT", ""))
            elif "Description :" in ligne:
                record["des"] = ligne.split(":")[1].strip()
            elif "Date :" in ligne:
                record["dat"] = ligne.split(":")[1].strip()
            elif "Date clé :" in ligne:
                record["cos"] = ligne.split(":")[1].strip()

        if record:
            records.append(record)

        with open(DATA_FILE, "ab") as bin_file:
            for record in records:
                dump(record, bin_file)

        open(TEXT_FILE, "w").close()
        print("Données sauvegardées dans le fichier binaire et fichier texte réinitialisé.")

    except FileNotFoundError:
        print("Fichier texte introuvable.")
    except Exception as e:
        print("Erreur lors de la sauvegarde :", e)

# Fonction pour rechercher une date dans le fichier texte
def recherche_date():
    try:
        date_recherchee = input("Donner la date (format JJ-MM-AAAA) : ")
        trouve = False

        with open(TEXT_FILE, "r") as file:
            print("\n--- Résultats de la recherche ---")
            for line in file:
                if date_recherchee in line:
                    trouve = True
                    print(line.strip())
                    for _ in range(4):
                        print(file.readline().strip())

        if not trouve:
            print("Aucune correspondance trouvée pour cette date.")
    except FileNotFoundError:
        print("Fichier introuvable.")
    except Exception as e:
        print("Erreur lors de la recherche :", e)

# Fonction principale pour gérer les choix
def menu_principal():
    while True:
        print("\n=== Gestion des Dépenses ===")
        print("1. Ajouter une nouvelle dépense")
        print("2. Voir le contenu du fichier texte")
        print("3. Sauvegarder les données dans le fichier binaire")
        print("4. Supprimer un fichier")
        print("5. Rechercher une dépense par date")
        print("6. Quitter")

        choix = input("Choisissez une option (1-6) : ")
        if choix == "1":
            nouvelle_insertion()
        elif choix == "2":
            vue_fichier(TEXT_FILE)
        elif choix == "3":
            sauvegarder_dans_fichier_binaire()
        elif choix == "4":
            supprimer_fichier()
        elif choix == "5":
            recherche_date()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme principal
if __name__ == "__main__":
    menu_principal()
