# Update DB

Ce module permet de transformer les spreadsheets DB (urbanisme, plu, plu_tr, etc.) en : 
- Fichiers SQL, pour update de la cloudDB OVH
- Fichiers Python de modèles pour ORM (SQLAlchemy)



main.py utilise orm_methods.py et sql_methods.py pour écrire respectivement dans les dossiers orm et sql. 


#### Versionnage : 

La V1 ne prend pas pas en compte les clés étrangères. 
