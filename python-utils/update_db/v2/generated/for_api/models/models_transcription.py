from server import db

class FiliationUlL3(db.Model):
    __tablename__='FiliationUlL3'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle_ul = db.Column('id_regle_ul', db.Integer)
    id_regle_l3 = db.Column('id_regle_l3', db.Integer)

class FiliationL3L2(db.Model):
    __tablename__='FiliationL3L2'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle_l3 = db.Column('id_regle_l3', db.Integer)
    id_regle_l2 = db.Column('id_regle_l2', db.Integer)

class FiliationL2L1(db.Model):
    __tablename__='FiliationL2L1'

    id = db.Column('id', db.Integer, primary_key=True)
    id_regle_l2 = db.Column('id_regle_l2', db.Integer)
    id_regle_l1 = db.Column('id_regle_l1', db.Integer)

class RegleAlternativeL3(db.Model):
    __tablename__='RegleAlternativeL3'

    id = db.Column('id', db.Integer, primary_key=True)
    id_option = db.Column('id_option', db.Integer)
    regle = db.Column('regle', db.Integer)
    alternative = db.Column('alternative', db.Integer)

class RegleAlternativeL2(db.Model):
    __tablename__='RegleAlternativeL2'

    id = db.Column('id', db.Integer, primary_key=True)
    id_option = db.Column('id_option', db.Integer)
    regle = db.Column('regle', db.Integer)
    alternative = db.Column('alternative', db.Integer)

class RegleAlternativeL1(db.Model):
    __tablename__='RegleAlternativeL1'

    id = db.Column('id', db.Integer, primary_key=True)
    id_option = db.Column('id_option', db.Integer)
    regle = db.Column('regle', db.Integer)
    alternative = db.Column('alternative', db.Integer)

