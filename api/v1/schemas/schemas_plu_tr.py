from server import ma

class RegleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_regle','regle_brute')
regle_schema = RegleSchema()
regle_schema_many = RegleSchema(many=True)

class RegleRunSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_regle','run_true','run_mb','run_except','run_alt')
regle_run_schema = RegleRunSchema()
regle_run_schema_many = RegleRunSchema(many=True)

class RegleAltSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_regle','id_option','niveau_alt')
regle_alt_schema = RegleAltSchema()
regle_alt_schema_many = RegleAltSchema(many=True)

class RegleTexteSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','id_texte')
regle_texte_schema = RegleTexteSchema()
regle_texte_schema_many = RegleTexteSchema(many=True)

class RegleDefSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','id_objet_def','option_def')
regle_def_schema = RegleDefSchema()
regle_def_schema_many = RegleDefSchema(many=True)

class RegleContexteSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','is_exception','is_exception_mb','id_zonage','id_sujet','id_is','id_from','id_to','descriptif_booleen','id_descriptif_quali')
regle_contexte_schema = RegleContexteSchema()
regle_contexte_schema_many = RegleContexteSchema(many=True)

class RegleConditionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_regle','condition_bool','id_condition_quali','id_condition_entree_graphique','condition_bande_constructible_min','condition_bande_constructible_max')
regle_condition_schema = RegleConditionSchema()
regle_condition_schema_many = RegleConditionSchema(many=True)

class RegleActionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','id_element_contraint','valeur_bool_true','valeur_bool_false','valeur_dis','valeur_reel','formule_dis','formule_reel','interdiction','autorisation','quali_information','quali_justification','quali_contrainte','package','id_free','is_opt','id_to_opt','opt_min','opt_max')
regle_action_schema = RegleActionSchema()
regle_action_schema_many = RegleActionSchema(many=True)

class ReglePackageSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','id_loi')
regle_package_schema = ReglePackageSchema()
regle_package_schema_many = ReglePackageSchema(many=True)

class VariableFormuleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle','lettre','id_variable')
variable_formule_schema = VariableFormuleSchema()
variable_formule_schema_many = VariableFormuleSchema(many=True)

class BooleenSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_booleen','formule_booleen')
booleen_schema = BooleenSchema()
booleen_schema_many = BooleenSchema(many=True)

class VariableBooleenSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_booleen','lettre','id_variable_bool')
variable_booleen_schema = VariableBooleenSchema()
variable_booleen_schema_many = VariableBooleenSchema(many=True)

