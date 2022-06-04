# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaPeliculas(http.Controller):
    
    '''
    Llamada web para obtener lista completa de cargamentos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/peliculas
    Y nos devolvera informacion sobre cada cargamento

    '''

    @http.route('/peliculas/', auth='public', cors='*', type='http')
    def obtenerDatosPeliculas(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "cargamento")
        peliculas = request.env['peliculas'].sudo().search([])

        #Generamos la lista de cargamentos
        '''lista_peliculas=[]

        for s in peliculas:
            lista_peliculas.append(s.read())
        json_result= http.Response(json.dumps(lista_peliculas, default=str)[1:-1].replace("], [",","),status=200,mimetype='application/json') 
        return json_result'''


        lista_peliculas=[]

        for s in peliculas:
        

            lista_peliculas.append({'id':s.id,'nombre':s.nombre,'director': s.director.nombre , 'dirID': s.director.id,

            'sinopsis':s.sinopsis,'genero':s.genero, 'genID':s.genero.id,'imagen':s.imagen,'trailer':s.trailer, 'puntuacion':s.puntuacion, 'visitas':s.visitas})
            



        json_result= http.Response(json.dumps(lista_peliculas, default=str)

        ,status=200,mimetype='application/json')

        return json_result