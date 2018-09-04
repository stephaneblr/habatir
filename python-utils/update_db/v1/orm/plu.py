class Texte(db.Model):
    __tablename__='Texte'

    id_texte = db.Column('id_texte', db.Integer, primary_key=True)
    texte = db.Column('texte', db.String(1000))

class EntreeGraphique(db.Model):
    __tablename__='EntreeGraphique'

    id_entree_graphique = db.Column('id_entree_graphique', db.Integer, primary_key=True)
    label_entree_graphique = db.Column('label_entree_graphique', db.String(100))

class Zonage(db.Model):
    __tablename__='Zonage'

    id_zone = db.Column('id_zone', db.Integer, primary_key=True)
    id_parent_zone = db.Column('id_parent_zone', db.Integer)
    nom_zone = db.Column('nom_zone', db.String(20))

class Path(db.Model):
    __tablename__='Path'

    id_path = db.Column('id_path', db.Integer, primary_key=True)
    id_parent_path = db.Column('id_parent_path', db.Integer)
    reference_path = db.Column('reference_path', db.String(10))
    label_path = db.Column('label_path', db.String(50))

