#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:37:01 2018

@author: stephaneblondellarougery
"""

from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app, 
    title='API Urbanis',
    version='0.6',
    description='Version de developpement',
         )

api.namespaces.clear()

from models import models_urbanisme, models_plu, models_plu_tr, models_transcription
from schemas import schemas_urbanisme, schemas_plu, schemas_plu_tr, schemas_transcription

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

from resources import resources_plu

ns10 = Namespace('plu', description='Ressources plu')

ns10.add_resource(resources_plu.TexteList, '/textes')
ns10.add_resource(resources_plu.TexteResource, '/textes/<string:id_texte>')

ns10.add_resource(resources_plu.EntreeGraphiqueList, '/entrees_graphique')
ns10.add_resource(resources_plu.EntreeGraphiqueResource, '/entrees_graphique/<string:id_entree_graphique>')

ns10.add_resource(resources_plu.ZonageList, '/zonages')
ns10.add_resource(resources_plu.ZonageResource, '/zonages/<string:id_zonage>')

ns10.add_resource(resources_plu.PathList, '/paths')
ns10.add_resource(resources_plu.PathResource, '/paths/<string:id_path>')

api.add_namespace(ns10)

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
    


if __name__ == '__main__':
    app.run(debug=True)