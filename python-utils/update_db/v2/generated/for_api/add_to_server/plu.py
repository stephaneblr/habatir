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
