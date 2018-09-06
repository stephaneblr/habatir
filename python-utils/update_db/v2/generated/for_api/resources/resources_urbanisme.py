from flask import jsonify
from flask_restplus import Resource
from server import models_urbanisme
from server import schemas_urbanisme

class SujetList(Resource):
    def get(self):
        all = models_urbanisme.Sujet.query.all()
        result = schemas_urbanisme.sujet_schema_many.dump(all)
        return jsonify(result.data)
class SujetResource(Resource):
    def get(self, id_sujet):
        one = models_urbanisme.Sujet.query.get(id_sujet)
        return schemas_urbanisme.sujet_schema.jsonify(one)


class Destination2List(Resource):
    def get(self):
        all = models_urbanisme.Destination2.query.all()
        result = schemas_urbanisme.destination_2_schema_many.dump(all)
        return jsonify(result.data)
class Destination2Resource(Resource):
    def get(self, id_destination_2):
        one = models_urbanisme.Destination2.query.get(id_destination_2)
        return schemas_urbanisme.destination_2_schema.jsonify(one)


class Destination3List(Resource):
    def get(self):
        all = models_urbanisme.Destination3.query.all()
        result = schemas_urbanisme.destination_3_schema_many.dump(all)
        return jsonify(result.data)
class Destination3Resource(Resource):
    def get(self, id_destination_3):
        one = models_urbanisme.Destination3.query.get(id_destination_3)
        return schemas_urbanisme.destination_3_schema.jsonify(one)


class VariableList(Resource):
    def get(self):
        all = models_urbanisme.Variable.query.all()
        result = schemas_urbanisme.variable_schema_many.dump(all)
        return jsonify(result.data)
class VariableResource(Resource):
    def get(self, id_variable):
        one = models_urbanisme.Variable.query.get(id_variable)
        return schemas_urbanisme.variable_schema.jsonify(one)


class OutcomeEnumList(Resource):
    def get(self):
        all = models_urbanisme.OutcomeEnum.query.all()
        result = schemas_urbanisme.outcome_enum_schema_many.dump(all)
        return jsonify(result.data)
class OutcomeEnumResource(Resource):
    def get(self, id_outcome_enum):
        one = models_urbanisme.OutcomeEnum.query.get(id_outcome_enum)
        return schemas_urbanisme.outcome_enum_schema.jsonify(one)


class ValeurControleList(Resource):
    def get(self):
        all = models_urbanisme.ValeurControle.query.all()
        result = schemas_urbanisme.valeur_controle_schema_many.dump(all)
        return jsonify(result.data)
class ValeurControleResource(Resource):
    def get(self, id_valeur_controle):
        one = models_urbanisme.ValeurControle.query.get(id_valeur_controle)
        return schemas_urbanisme.valeur_controle_schema.jsonify(one)


class LoiList(Resource):
    def get(self):
        all = models_urbanisme.Loi.query.all()
        result = schemas_urbanisme.loi_schema_many.dump(all)
        return jsonify(result.data)
class LoiResource(Resource):
    def get(self, id_loi):
        one = models_urbanisme.Loi.query.get(id_loi)
        return schemas_urbanisme.loi_schema.jsonify(one)


