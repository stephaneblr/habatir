from server import db

class Sujet(db.Model):
    __tablename__='Sujet'

    id_sujet = db.Column('id_sujet', db.Integer, primary_key=True)
    id_parent_sujet = db.Column('id_parent_sujet', db.Integer)
    nom_sujet = db.Column('nom_sujet', db.String(50))

class Destination2(db.Model):
    __tablename__='Destination2'

    id_destination = db.Column('id_destination', db.Integer, primary_key=True)
    id_parent_destination = db.Column('id_parent_destination', db.Integer)
    nom_destination = db.Column('nom_destination', db.String(50))

class Destination3(db.Model):
    __tablename__='Destination3'

    id_destination = db.Column('id_destination', db.Integer, primary_key=True)
    id_parent_destination = db.Column('id_parent_destination', db.Integer)
    nom_destination = db.Column('nom_destination', db.String(50))

class Variable(db.Model):
    __tablename__='Variable'

    id_variable = db.Column('id_variable', db.Integer, primary_key=True)
    id_parent_variable = db.Column('id_parent_variable', db.Integer)
    id_sujet = db.Column('id_sujet', db.Integer)
    id_destination = db.Column('id_destination', db.Integer)
    nom_variable = db.Column('nom_variable', db.String(100))
    est_noeud = db.Column('est_noeud', db.Boolean)
    est_caracteristique = db.Column('est_caracteristique', db.Boolean)
    est_variable_reelle = db.Column('est_variable_reelle', db.Boolean)
    est_variable_booleenne = db.Column('est_variable_booleenne', db.Boolean)
    est_variable_dqr = db.Column('est_variable_dqr', db.Boolean)
    est_variable_enumeration = db.Column('est_variable_enumeration', db.Boolean)
    est_mimao = db.Column('est_mimao', db.Boolean)

class OutcomeEnum(db.Model):
    __tablename__='OutcomeEnum'

    id = db.Column('id', db.Integer, primary_key=True)
    id_variable = db.Column('id_variable', db.Integer)
    id_outcome = db.Column('id_outcome', db.Integer)
    nom_outcome = db.Column('nom_outcome', db.String(100))

class ValeurControle(db.Model):
    __tablename__='ValeurControle'

    id_valeur_controle = db.Column('id_valeur_controle', db.Integer, primary_key=True)
    id_variable = db.Column('id_variable', db.Integer)
    nom_valeur_controle = db.Column('nom_valeur_controle', db.String(150))
    est_minimum = db.Column('est_minimum', db.Boolean)
    est_identite = db.Column('est_identite', db.Boolean)
    est_maximum = db.Column('est_maximum', db.Boolean)
    est_autorisation = db.Column('est_autorisation', db.Boolean)
    est_obligation = db.Column('est_obligation', db.Boolean)
    est_autre = db.Column('est_autre', db.Boolean)

class Loi(db.Model):
    __tablename__='Loi'

    id_loi = db.Column('id_loi', db.Integer, primary_key=True)
    reference_article = db.Column('reference_article', db.String(50))
    branche = db.Column('branche', db.String(50))
    sujet_loi = db.Column('sujet_loi', db.String(150))
    lien = db.Column('lien', db.String(150))

