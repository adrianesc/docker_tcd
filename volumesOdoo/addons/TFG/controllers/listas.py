# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaListas(http.Controller):
    


    @http.route('/<modelo>', auth='public', cors='*', type='http')
    def obtenerDatosListas(self, modelo, **kw):
        cargamentos = request.env[modelo].sudo().search([])

        lista_cargamentos=[]
        for s in cargamentos:
            lista_cargamentos.append(s.read())
        json_result= http.Response(json.dumps(lista_cargamentos, default=str)[1:-1].replace("], [",","),status=200,mimetype='application/json') 
        return json_result
