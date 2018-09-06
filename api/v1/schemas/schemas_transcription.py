from server import ma

class FiliationUlL3Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle_ul','id_regle_l3')
filiation_ul_l_3_schema = FiliationUlL3Schema()
filiation_ul_l_3_schema_many = FiliationUlL3Schema(many=True)

class FiliationL3L2Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle_l3','id_regle_l2')
filiation_l_3_l_2_schema = FiliationL3L2Schema()
filiation_l_3_l_2_schema_many = FiliationL3L2Schema(many=True)

class FiliationL2L1Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_regle_l2','id_regle_l1')
filiation_l_2_l_1_schema = FiliationL2L1Schema()
filiation_l_2_l_1_schema_many = FiliationL2L1Schema(many=True)

class RegleAlternativeL3Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_option','regle','alternative')
regle_alternative_l_3_schema = RegleAlternativeL3Schema()
regle_alternative_l_3_schema_many = RegleAlternativeL3Schema(many=True)

class RegleAlternativeL2Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_option','regle','alternative')
regle_alternative_l_2_schema = RegleAlternativeL2Schema()
regle_alternative_l_2_schema_many = RegleAlternativeL2Schema(many=True)

class RegleAlternativeL1Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','id_option','regle','alternative')
regle_alternative_l_1_schema = RegleAlternativeL1Schema()
regle_alternative_l_1_schema_many = RegleAlternativeL1Schema(many=True)

