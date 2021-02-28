from flask import Flask, request
from flask_restful import Resource, Api,reqparse
import json,os
from lxml import etree
app = Flask(__name__)
api = Api(app)

def LeerDatos():
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    file_path = ROOT_PATH + "/" + "municipios.json"
    with open(file_path, encoding='utf-8') as fichero:
        datos=json.load(fichero)
    return datos


class ListarMunicipios(Resource):
    def get(self):
        datos=LeerDatos()
        return datos

class FiltrarMunicipios(Resource):
    def get(self,cadena):
        datos=LeerDatos()
        resultlist = [d for d in datos if d.get('NOMBRE', '').startswith(cadena.title())]
        resultlist = [{"CODIGO":d.get("CPRO")+d.get("CMUN"),"NOMBRE":d.get("NOMBRE")} for d in resultlist]
        return resultlist

class DevolverTemperatura(Resource):
    def get(self,codigo):
        try:
	        doc=etree.parse("http://www.aemet.es/xml/municipios/localidad_"+codigo+".xml")
        except:
            return({"error":"No puedo hacer la petición"})
        name=doc.find("nombre").text
        max=doc.find("prediccion/dia/temperatura").find("maxima").text
        min=doc.find("prediccion/dia/temperatura").find("minima").text
        return {"NOMBRE":name,"TMAX":max,"TMIN":min}

class Status(Resource):
    def get(self):
        return {"status":"ok"}


api.add_resource(ListarMunicipios, '/municipios')
api.add_resource(FiltrarMunicipios, '/municipios/<string:cadena>')
api.add_resource(DevolverTemperatura, '/temperatura/<string:codigo>')
api.add_resource(Status, '/status')

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
