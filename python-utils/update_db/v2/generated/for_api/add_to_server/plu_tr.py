from resources import resources_plu_tr

ns100 = Namespace('plu_tr', description='Ressources plu_tr')

ns100.add_resource(resources_plu_tr.RegleList, '/regles')
ns100.add_resource(resources_plu_tr.RegleResource, '/regles/<string:id_regle>')

ns100.add_resource(resources_plu_tr.RegleRunList, '/regles_run')
ns100.add_resource(resources_plu_tr.RegleRunResource, '/regles_run/<string:id_regle_run>')

ns100.add_resource(resources_plu_tr.RegleAltList, '/regles_alt')
ns100.add_resource(resources_plu_tr.RegleAltResource, '/regles_alt/<string:id_regle_alt>')

ns100.add_resource(resources_plu_tr.RegleTexteList, '/regles_texte')
ns100.add_resource(resources_plu_tr.RegleTexteResource, '/regles_texte/<string:id_regle_texte>')

ns100.add_resource(resources_plu_tr.RegleDefList, '/regles_def')
ns100.add_resource(resources_plu_tr.RegleDefResource, '/regles_def/<string:id_regle_def>')

ns100.add_resource(resources_plu_tr.RegleContexteList, '/regles_contexte')
ns100.add_resource(resources_plu_tr.RegleContexteResource, '/regles_contexte/<string:id_regle_contexte>')

ns100.add_resource(resources_plu_tr.RegleConditionList, '/regles_condition')
ns100.add_resource(resources_plu_tr.RegleConditionResource, '/regles_condition/<string:id_regle_condition>')

ns100.add_resource(resources_plu_tr.RegleActionList, '/regles_action')
ns100.add_resource(resources_plu_tr.RegleActionResource, '/regles_action/<string:id_regle_action>')

ns100.add_resource(resources_plu_tr.ReglePackageList, '/regles_package')
ns100.add_resource(resources_plu_tr.ReglePackageResource, '/regles_package/<string:id_regle_package>')

ns100.add_resource(resources_plu_tr.VariableFormuleList, '/variables_formule')
ns100.add_resource(resources_plu_tr.VariableFormuleResource, '/variables_formule/<string:id_variable_formule>')

ns100.add_resource(resources_plu_tr.BooleenList, '/booleens')
ns100.add_resource(resources_plu_tr.BooleenResource, '/booleens/<string:id_booleen>')

ns100.add_resource(resources_plu_tr.VariableBooleenList, '/variables_booleen')
ns100.add_resource(resources_plu_tr.VariableBooleenResource, '/variables_booleen/<string:id_variable_booleen>')

api.add_namespace(ns100)
