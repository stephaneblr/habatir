from resources import resources_urbanisme

ns1 = Namespace('urbanisme', description='Ressources urbanisme')

ns1.add_resource(resources_urbanisme.SujetList, '/sujets')
ns1.add_resource(resources_urbanisme.SujetResource, '/sujets/<string:id_sujet>')

ns1.add_resource(resources_urbanisme.Destination2List, '/destinations_2')
ns1.add_resource(resources_urbanisme.Destination2Resource, '/destinations_2/<string:id_destination_2>')

ns1.add_resource(resources_urbanisme.Destination3List, '/destinations_3')
ns1.add_resource(resources_urbanisme.Destination3Resource, '/destinations_3/<string:id_destination_3>')

ns1.add_resource(resources_urbanisme.VariableList, '/variables')
ns1.add_resource(resources_urbanisme.VariableResource, '/variables/<string:id_variable>')

ns1.add_resource(resources_urbanisme.OutcomeEnumList, '/outcomes_enum')
ns1.add_resource(resources_urbanisme.OutcomeEnumResource, '/outcomes_enum/<string:id_outcome_enum>')

ns1.add_resource(resources_urbanisme.ValeurControleList, '/valeurs_controle')
ns1.add_resource(resources_urbanisme.ValeurControleResource, '/valeurs_controle/<string:id_valeur_controle>')

ns1.add_resource(resources_urbanisme.LoiList, '/lois')
ns1.add_resource(resources_urbanisme.LoiResource, '/lois/<string:id_loi>')

api.add_namespace(ns1)
