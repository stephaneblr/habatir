# Update DB

Executer main.py

Prend les données depuis GSheet --> Crée un fichier SQL et un modèle ORM pour chaque DB. 

#### Versionnage

- v1 : Pas encore la possibilité de préciser les FK

- v2 : Toujours pas bon pour les FK, mais permet de gérer les 4 bases de données, et crée 4 fichiers différents par DB. Le code est plus attomisé. ATTENTION : Il est nécessaire d'implémenter les __bind_key__ à la main dans chaque moèle ! A modifier. 


#### Pistes de développement

- Connecter directement le programme à l'API quand on en a une version plus stable. On devra être capable de préciser dans quelle version de l'API écrit le programme, et y accéder par un fichier update.py directement depuis l'API. 

- FK ! 