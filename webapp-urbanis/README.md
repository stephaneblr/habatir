# WebApp Urbanis


## LANCER LE PROJET

- Ouvrir un terminal et se déplacer dans le projet
```
    cd chemin/du/projet
```

- ensuite executer les commandes suivantes pour construire les conteneurs(installation des dépendances etc..):
```
    docker build -t webdb ./db
    docker build -t webback ./back
    docker build -t webfront ./front
```

- Ensuite lancer le projet avec cette commande:
```
    docker-compose up
```

- Une fois la compilation terminé, se rendre sur http://localhost:4200

- pour arreter l'app
```
    docker-compose stop

```

## Update la base de données

- supprimer tout les fichiers et dossiers dans ./db/data/ (toujours a la racine du projet)
```
    rm -rf ./db/data/*
```
- remplacer les fichiers csv dans ./db

- reconstruire le conteneur
```
    docker build -t webdb ./db
```
- relancer le projet 
```
    docker-compose up
```


### GET /sujets
Réponse:
```
 [
   {
     "id_sujet": 1, 
     "nom": "construction"
   }
 ]
```

### GET /variables
Réponse:
```
 [
   {
     "id_variable": 101, 
     "nom": "terrain"
   },
 ]
```


### POST /search

Body:
```
{
	"c1": 1,
	"c2": [{
		"id": 137,
		"option": 2
	}]
}
```
Réponse:
```
[
    {
        "description_loi": null,
        "id_loi": null,
        "id_txt": 1,
        "lien": null,
        "txt": "<div class=\"txt\">Le présent Plan Local d’Urbanisme s'applique à l'ensemble du territoire communal de Sèvres.<br/><br/></div>"
    }
]
```


###ALGO DE RECHERCHE PSEUDO CODE
Pour la requête, on rechercher la présence de l’id_sujet correspondant au mot clé dans la table “Regle”: 
colonne “contrainte” si l’utilisateur choisit l’option 1
colonne “change_def” si l’utilisateur choisit l’option 3
Si l’utilisateur choisit l’option 2, la requête va utiliser la table de jointure “ContientVariable”, selon le même principe. (id_regle, id_variable)

###BASE
SELECT txt.id_txt, txt.txt, lois.id_loi, lois.description as description_loi, lois.lien FROM webapp.txt
    LEFT JOIN webapp.lois ON webapp.lois.id_loi = txt.loi
    LEFT JOIN webapp.regle ON webapp.regle.txt=webapp.txt.id_txt


###C2
TRIER PAR OPTION

####OPTION 2:
LEFT JOIN contientvariable ON contientvariable.id_regle = regle.id_regle WHERE contientvariable.id_variable= 1 && 2 && 3 && 4

####OPTION 1:
if OPTION 2 EST NULL
    WHERE
else
    AND
    regle.contrainte == 1 || 2 || 3 ...

####OPTION 3:
if OPTION 1 EST NULL && OPTION 2 EST NULL
    WHERE
else
    AND
    regle.change_def == 1 || 2 || 3 ...  

###C1
IF C2 IS NULL
    WHERE
ELSE
    AND
webapp.regle.sujet=' + str(c1) + ';'