from flask import jsonify
from flask_restplus import Resource
from server import models_plu_tr
from server import schemas_plu_tr

class RegleList(Resource):
    def get(self):
        all = models_plu_tr.Regle.query.all()
        result = schemas_plu_tr.regle_schema_many.dump(all)
        return jsonify(result.data)
class RegleResource(Resource):
    def get(self, id_regle):
        one = models_plu_tr.Regle.query.get(id_regle)
        return schemas_plu_tr.regle_schema.jsonify(one)


class RegleRunList(Resource):
    def get(self):
        all = models_plu_tr.RegleRun.query.all()
        result = schemas_plu_tr.regle_run_schema_many.dump(all)
        return jsonify(result.data)
class RegleRunResource(Resource):
    def get(self, id_regle_run):
        one = models_plu_tr.RegleRun.query.get(id_regle_run)
        return schemas_plu_tr.regle_run_schema.jsonify(one)


class RegleAltList(Resource):
    def get(self):
        all = models_plu_tr.RegleAlt.query.all()
        result = schemas_plu_tr.regle_alt_schema_many.dump(all)
        return jsonify(result.data)
class RegleAltResource(Resource):
    def get(self, id_regle_alt):
        one = models_plu_tr.RegleAlt.query.get(id_regle_alt)
        return schemas_plu_tr.regle_alt_schema.jsonify(one)


class RegleTexteList(Resource):
    def get(self):
        all = models_plu_tr.RegleTexte.query.all()
        result = schemas_plu_tr.regle_texte_schema_many.dump(all)
        return jsonify(result.data)
class RegleTexteResource(Resource):
    def get(self, id_regle_texte):
        one = models_plu_tr.RegleTexte.query.get(id_regle_texte)
        return schemas_plu_tr.regle_texte_schema.jsonify(one)


class RegleDefList(Resource):
    def get(self):
        all = models_plu_tr.RegleDef.query.all()
        result = schemas_plu_tr.regle_def_schema_many.dump(all)
        return jsonify(result.data)
class RegleDefResource(Resource):
    def get(self, id_regle_def):
        one = models_plu_tr.RegleDef.query.get(id_regle_def)
        return schemas_plu_tr.regle_def_schema.jsonify(one)


class RegleContexteList(Resource):
    def get(self):
        all = models_plu_tr.RegleContexte.query.all()
        result = schemas_plu_tr.regle_contexte_schema_many.dump(all)
        return jsonify(result.data)
class RegleContexteResource(Resource):
    def get(self, id_regle_contexte):
        one = models_plu_tr.RegleContexte.query.get(id_regle_contexte)
        return schemas_plu_tr.regle_contexte_schema.jsonify(one)


class RegleConditionList(Resource):
    def get(self):
        all = models_plu_tr.RegleCondition.query.all()
        result = schemas_plu_tr.regle_condition_schema_many.dump(all)
        return jsonify(result.data)
class RegleConditionResource(Resource):
    def get(self, id_regle_condition):
        one = models_plu_tr.RegleCondition.query.get(id_regle_condition)
        return schemas_plu_tr.regle_condition_schema.jsonify(one)


class RegleActionList(Resource):
    def get(self):
        all = models_plu_tr.RegleAction.query.all()
        result = schemas_plu_tr.regle_action_schema_many.dump(all)
        return jsonify(result.data)
class RegleActionResource(Resource):
    def get(self, id_regle_action):
        one = models_plu_tr.RegleAction.query.get(id_regle_action)
        return schemas_plu_tr.regle_action_schema.jsonify(one)


class ReglePackageList(Resource):
    def get(self):
        all = models_plu_tr.ReglePackage.query.all()
        result = schemas_plu_tr.regle_package_schema_many.dump(all)
        return jsonify(result.data)
class ReglePackageResource(Resource):
    def get(self, id_regle_package):
        one = models_plu_tr.ReglePackage.query.get(id_regle_package)
        return schemas_plu_tr.regle_package_schema.jsonify(one)


class VariableFormuleList(Resource):
    def get(self):
        all = models_plu_tr.VariableFormule.query.all()
        result = schemas_plu_tr.variable_formule_schema_many.dump(all)
        return jsonify(result.data)
class VariableFormuleResource(Resource):
    def get(self, id_variable_formule):
        one = models_plu_tr.VariableFormule.query.get(id_variable_formule)
        return schemas_plu_tr.variable_formule_schema.jsonify(one)


class BooleenList(Resource):
    def get(self):
        all = models_plu_tr.Booleen.query.all()
        result = schemas_plu_tr.booleen_schema_many.dump(all)
        return jsonify(result.data)
class BooleenResource(Resource):
    def get(self, id_booleen):
        one = models_plu_tr.Booleen.query.get(id_booleen)
        return schemas_plu_tr.booleen_schema.jsonify(one)


class VariableBooleenList(Resource):
    def get(self):
        all = models_plu_tr.VariableBooleen.query.all()
        result = schemas_plu_tr.variable_booleen_schema_many.dump(all)
        return jsonify(result.data)
class VariableBooleenResource(Resource):
    def get(self, id_variable_booleen):
        one = models_plu_tr.VariableBooleen.query.get(id_variable_booleen)
        return schemas_plu_tr.variable_booleen_schema.jsonify(one)


