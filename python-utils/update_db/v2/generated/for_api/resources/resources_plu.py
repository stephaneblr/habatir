from flask import jsonify
from flask_restplus import Resource
from server import models_plu
from server import schemas_plu

class TexteList(Resource):
    def get(self):
        all = models_plu.Texte.query.all()
        result = schemas_plu.texte_schema_many.dump(all)
        return jsonify(result.data)
class TexteResource(Resource):
    def get(self, id_texte):
        one = models_plu.Texte.query.get(id_texte)
        return schemas_plu.texte_schema.jsonify(one)


class EntreeGraphiqueList(Resource):
    def get(self):
        all = models_plu.EntreeGraphique.query.all()
        result = schemas_plu.entree_graphique_schema_many.dump(all)
        return jsonify(result.data)
class EntreeGraphiqueResource(Resource):
    def get(self, id_entree_graphique):
        one = models_plu.EntreeGraphique.query.get(id_entree_graphique)
        return schemas_plu.entree_graphique_schema.jsonify(one)


class ZonageList(Resource):
    def get(self):
        all = models_plu.Zonage.query.all()
        result = schemas_plu.zonage_schema_many.dump(all)
        return jsonify(result.data)
class ZonageResource(Resource):
    def get(self, id_zonage):
        one = models_plu.Zonage.query.get(id_zonage)
        return schemas_plu.zonage_schema.jsonify(one)


class PathList(Resource):
    def get(self):
        all = models_plu.Path.query.all()
        result = schemas_plu.path_schema_many.dump(all)
        return jsonify(result.data)
class PathResource(Resource):
    def get(self, id_path):
        one = models_plu.Path.query.get(id_path)
        return schemas_plu.path_schema.jsonify(one)


