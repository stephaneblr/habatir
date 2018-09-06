from resources import resources_transcription

ns1000 = Namespace('transcription', description='Ressources transcription')

ns1000.add_resource(resources_transcription.FiliationUlL3List, '/filiations_ul_l_3')
ns1000.add_resource(resources_transcription.FiliationUlL3Resource, '/filiations_ul_l_3/<string:id_filiation_ul_l_3>')

ns1000.add_resource(resources_transcription.FiliationL3L2List, '/filiations_l_3_l_2')
ns1000.add_resource(resources_transcription.FiliationL3L2Resource, '/filiations_l_3_l_2/<string:id_filiation_l_3_l_2>')

ns1000.add_resource(resources_transcription.FiliationL2L1List, '/filiations_l_2_l_1')
ns1000.add_resource(resources_transcription.FiliationL2L1Resource, '/filiations_l_2_l_1/<string:id_filiation_l_2_l_1>')

ns1000.add_resource(resources_transcription.RegleAlternativeL3List, '/regles_alternative_l_3')
ns1000.add_resource(resources_transcription.RegleAlternativeL3Resource, '/regles_alternative_l_3/<string:id_regle_alternative_l_3>')

ns1000.add_resource(resources_transcription.RegleAlternativeL2List, '/regles_alternative_l_2')
ns1000.add_resource(resources_transcription.RegleAlternativeL2Resource, '/regles_alternative_l_2/<string:id_regle_alternative_l_2>')

ns1000.add_resource(resources_transcription.RegleAlternativeL1List, '/regles_alternative_l_1')
ns1000.add_resource(resources_transcription.RegleAlternativeL1Resource, '/regles_alternative_l_1/<string:id_regle_alternative_l_1>')

api.add_namespace(ns1000)
