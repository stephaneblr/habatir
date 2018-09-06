from server import db

class Regle(db.Model):
    __tablename__='Regle'

    id_regle = db.Column('id_regle', db.Integer, primary_key=True)
    regle_brute = db.Column('regle_brute', db.String(200))

class RegleRun(db.Model):
    __tablename__='RegleRun'

    id_regle = db.Column('id_regle', db.Integer, primary_key=True)
    run_true = db.Column('run_true', db.Boolean)
    run_mb = db.Column('run_mb', db.Boolean)
    run_except = db.Column('run_except', db.Boolean)
    run_alt = db.Column('run_alt', db.Boolean)

class RegleAlt(db.Model):
    __tablename__='RegleAlt'

    id_regle = db.Column('id_regle', db.Integer, primary_key=True)
    id_option = db.Column('id_option', db.Integer)
    niveau_alt = db.Column('niveau_alt', db.Integer)

class RegleTexte(db.Model):
    __tablename__='RegleTexte'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    id_texte = db.Column('id_texte', db.Integer)

class RegleDef(db.Model):
    __tablename__='RegleDef'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    id_objet_def = db.Column('id_objet_def', db.Integer)
    option_def = db.Column('option_def', db.Integer)

class RegleContexte(db.Model):
    __tablename__='RegleContexte'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    is_exception = db.Column('is_exception', db.Boolean)
    is_exception_mb = db.Column('is_exception_mb', db.Boolean)
    id_zonage = db.Column('id_zonage', db.Integer)
    id_sujet = db.Column('id_sujet', db.Integer)
    id_is = db.Column('id_is', db.Integer)
    id_from = db.Column('id_from', db.Integer)
    id_to = db.Column('id_to', db.Integer)
    descriptif_booleen = db.Column('descriptif_booleen', db.String(50))
    id_descriptif_quali = db.Column('id_descriptif_quali', db.Integer)

class RegleCondition(db.Model):
    __tablename__='RegleCondition'

    id_regle = db.Column('id_regle', db.Integer, primary_key=True)
    condition_bool = db.Column('condition_bool', db.String(50))
    id_condition_quali = db.Column('id_condition_quali', db.Integer)
    id_condition_entree_graphique = db.Column('id_condition_entree_graphique', db.Integer)
    condition_bande_constructible_min = db.Column('condition_bande_constructible_min', db.String(10))
    condition_bande_constructible_max = db.Column('condition_bande_constructible_max', db.String(10))

class RegleAction(db.Model):
    __tablename__='RegleAction'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    id_element_contraint = db.Column('id_element_contraint', db.Integer)
    valeur_bool_true = db.Column('valeur_bool_true', db.Boolean)
    valeur_bool_false = db.Column('valeur_bool_false', db.Boolean)
    valeur_dis = db.Column('valeur_dis', db.String(10))
    valeur_reel = db.Column('valeur_reel', db.String(10))
    formule_dis = db.Column('formule_dis', db.String(50))
    formule_reel = db.Column('formule_reel', db.String(50))
    interdiction = db.Column('interdiction', db.Boolean)
    autorisation = db.Column('autorisation', db.Boolean)
    quali_information = db.Column('quali_information', db.Boolean)
    quali_justification = db.Column('quali_justification', db.Boolean)
    quali_contrainte = db.Column('quali_contrainte', db.Boolean)
    package = db.Column('package', db.Boolean)
    id_free = db.Column('id_free', db.Integer)
    is_opt = db.Column('is_opt', db.Boolean)
    id_to_opt = db.Column('id_to_opt', db.Integer)
    opt_min = db.Column('opt_min', db.Boolean)
    opt_max = db.Column('opt_max', db.Boolean)

class ReglePackage(db.Model):
    __tablename__='ReglePackage'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    id_loi = db.Column('id_loi', db.Integer)

class VariableFormule(db.Model):
    __tablename__='VariableFormule'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle = db.Column('id_regle', db.Integer)
    lettre = db.Column('lettre', db.String(1))
    id_variable = db.Column('id_variable', db.Integer)

class Booleen(db.Model):
    __tablename__='Booleen'

    id_booleen = db.Column('id_booleen', db.Integer, primary_key=True)
    formule_booleen = db.Column('formule_booleen', db.String(50))

class VariableBooleen(db.Model):
    __tablename__='VariableBooleen'

    id = db.Column('id', db.Integer, primary_key=True)
    id_booleen = db.Column('id_booleen', db.Integer)
    lettre = db.Column('lettre', db.String(1))
    id_variable_bool = db.Column('id_variable_bool', db.Integer)

