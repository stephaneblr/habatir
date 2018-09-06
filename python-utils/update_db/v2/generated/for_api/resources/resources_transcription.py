from flask import jsonify
from flask_restplus import Resource
from server import models_transcription
from server import schemas_transcription

class FiliationUlL3List(Resource):
    def get(self):
        all = models_transcription.FiliationUlL3.query.all()
        result = schemas_transcription.filiation_ul_l_3_schema_many.dump(all)
        return jsonify(result.data)
class FiliationUlL3Resource(Resource):
    def get(self, id_filiation_ul_l_3):
        one = models_transcription.FiliationUlL3.query.get(id_filiation_ul_l_3)
        return schemas_transcription.filiation_ul_l_3_schema.jsonify(one)


class FiliationL3L2List(Resource):
    def get(self):
        all = models_transcription.FiliationL3L2.query.all()
        result = schemas_transcription.filiation_l_3_l_2_schema_many.dump(all)
        return jsonify(result.data)
class FiliationL3L2Resource(Resource):
    def get(self, id_filiation_l_3_l_2):
        one = models_transcription.FiliationL3L2.query.get(id_filiation_l_3_l_2)
        return schemas_transcription.filiation_l_3_l_2_schema.jsonify(one)


class FiliationL2L1List(Resource):
    def get(self):
        all = models_transcription.FiliationL2L1.query.all()
        result = schemas_transcription.filiation_l_2_l_1_schema_many.dump(all)
        return jsonify(result.data)
class FiliationL2L1Resource(Resource):
    def get(self, id_filiation_l_2_l_1):
        one = models_transcription.FiliationL2L1.query.get(id_filiation_l_2_l_1)
        return schemas_transcription.filiation_l_2_l_1_schema.jsonify(one)


class RegleAlternativeL3List(Resource):
    def get(self):
        all = models_transcription.RegleAlternativeL3.query.all()
        result = schemas_transcription.regle_alternative_l_3_schema_many.dump(all)
        return jsonify(result.data)
class RegleAlternativeL3Resource(Resource):
    def get(self, id_regle_alternative_l_3):
        one = models_transcription.RegleAlternativeL3.query.get(id_regle_alternative_l_3)
        return schemas_transcription.regle_alternative_l_3_schema.jsonify(one)


class RegleAlternativeL2List(Resource):
    def get(self):
        all = models_transcription.RegleAlternativeL2.query.all()
        result = schemas_transcription.regle_alternative_l_2_schema_many.dump(all)
        return jsonify(result.data)
class RegleAlternativeL2Resource(Resource):
    def get(self, id_regle_alternative_l_2):
        one = models_transcription.RegleAlternativeL2.query.get(id_regle_alternative_l_2)
        return schemas_transcription.regle_alternative_l_2_schema.jsonify(one)


class RegleAlternativeL1List(Resource):
    def get(self):
        all = models_transcription.RegleAlternativeL1.query.all()
        result = schemas_transcription.regle_alternative_l_1_schema_many.dump(all)
        return jsonify(result.data)
class RegleAlternativeL1Resource(Resource):
    def get(self, id_regle_alternative_l_1):
        one = models_transcription.RegleAlternativeL1.query.get(id_regle_alternative_l_1)
        return schemas_transcription.regle_alternative_l_1_schema.jsonify(one)


