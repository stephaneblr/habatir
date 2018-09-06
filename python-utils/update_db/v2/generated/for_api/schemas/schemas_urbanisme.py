from server import ma

class SujetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_sujet','id_parent_sujet','nom_sujet')
sujet_schema = SujetSchema()
sujet_schema_many = SujetSchema(many=True)

class Destination2Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_destination','id_parent_destination','nom_destination')
destination_2_schema = Destination2Schema()
destination_2_schema_many = Destination2Schema(many=True)

class Destination3Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_destination','id_parent_destination','nom_destination')
destination_3_schema = Destination3Schema()
destination_3_schema_many = Destination3Schema(many=True)

class VariableSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_variable','id_parent_variable','id_sujet','id_destination','nom_variable','est_noeud','est_caracteristique','est_variable_reelle','est_variable_booleenne','est_variable_dqr','est_variable_enumeration','est_mimao')
variable_schema = VariableSchema()
variable_schema_many = VariableSchema(many=True)

class OutcomeEnumSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_variable','id_outcome','nom_outcome')
outcome_enum_schema = OutcomeEnumSchema()
outcome_enum_schema_many = OutcomeEnumSchema(many=True)

class ValeurControleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_valeur_controle','id_variable','nom_valeur_controle','est_minimum','est_identite','est_maximum','est_autorisation','est_obligation','est_autre')
valeur_controle_schema = ValeurControleSchema()
valeur_controle_schema_many = ValeurControleSchema(many=True)

class LoiSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_loi','reference_article','branche','sujet_loi','lien')
loi_schema = LoiSchema()
loi_schema_many = LoiSchema(many=True)

