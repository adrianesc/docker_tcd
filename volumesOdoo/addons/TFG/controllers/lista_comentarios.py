# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaComentarios(http.Controller):
    
    '''
    Llamada web para obtener lista completa de comentarios.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/comentarios
    Y nos devolvera informacion sobre cada comentario

    '''

    @http.route('/gestion/comentarios/', auth='public', cors='*', type='http')
    def obtenerDatosComentarios(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "comentarios")
        comentarios = request.env['comentarios'].sudo().search([])

        #Generamos la lista de comentarios

        lista_comentarios=[]

        for s in comentarios:
        
        #Obtenemos los campos que nos iteresan del registro

            lista_comentarios.append({'id':s.id,'usuario':s.usuario.nombre,'pelicula': s.pelicula.nombre, 'comentario':s.comentario})
            



        json_result= http.Response(json.dumps(lista_comentarios, default=str)

        ,status=200,mimetype='application/json')

        #Devolvemos el registro formateado

        return json_result