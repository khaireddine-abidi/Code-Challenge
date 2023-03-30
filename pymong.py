from pymongo import MongoClient
from datetime import date , datetime
import json


# Ouvrir une connexion à la base de données
""" def collection(uri):

    client = MongoClient(uri) 
    

    db=client["rhobs"]
    collection1 =db["people"]

    return collection1 
""" 
client = MongoClient ("mongodb://localhost:27017/")
db = client["rhobs"]
collection = db["people"]


# Insérer les données dans la collection "people"
def load(uri="mongodb://localhost:27017/", datapath="data.json"):

    coll = collection(uri-uri)

    with open(datapath, "r") as fp:

       data = json.load(fp)

       for person in data: coll.insert_one(person)




# Compter le nombre de femmes / d'hommes.
print("le nombre de femmes ",collection.count_documents({"sex": "F"}))
print("le nombre d'hommes",collection.count_documents({"sex": "M"}))




# Écrire une fonction qui renvoie les entreprises de plus de N personnes
def entreprises_plus_de_n_personnes(n):
    return collection.distinct("company", {"$where": f"this.company.length > {n}"})



    

# Écrire une fonction qui prend en paramètre un métier et qui renvoie la pyramide des âges pour ce métier
def pyramide_ages_metier(metier):
     
    clients = collection.find({"job": metier})
    pyramide = {}
      # creation de la pyramide des âges
    for i in range(18, 100, 10):
        pyramide[str(i) + "-" + str(i+9)] = 0

     # calcul de la pyramide des âges
    for client in clients:
        date_naissance = client["birthdate"]
        date_naissance1 = datetime.strptime(date_naissance, "%Y-%m-%d")
        age = (datetime.now() - date_naissance1).days // 365
        for i in range(18, 100, 10):
            if age >= i and age <= i+9:
                pyramide[str(i) + "-" + str(i+9)] += 1

    # Affichage de la pyramide des âges
    print("Pyramide des âges pour le métier", metier + ":")
    for tranche in pyramide:
        print(tranche + " ans :", "*" * pyramide[tranche])
    

# Exemple d'utilisation
metier = "ingénieur télécoms et réseaux"
pyramide_ages_metier(metier)
print(entreprises_plus_de_n_personnes(29))git

