from server import ma

class TexteSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_texte','texte')
texte_schema = TexteSchema()
texte_schema_many = TexteSchema(many=True)

class EntreeGraphiqueSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_entree_graphique','label_entree_graphique')
entree_graphique_schema = EntreeGraphiqueSchema()
entree_graphique_schema_many = EntreeGraphiqueSchema(many=True)

class ZonageSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_zone','id_parent_zone','nom_zone')
zonage_schema = ZonageSchema()
zonage_schema_many = ZonageSchema(many=True)

class PathSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_path','id_parent_path','reference_path','label_path')
path_schema = PathSchema()
path_schema_many = PathSchema(many=True)

