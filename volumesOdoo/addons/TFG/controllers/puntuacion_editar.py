# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web

class EditarPutuacion(http.Controller):
    
    '''
    Llamada web para obtener modificar la puntuación.
    
    '''

    @http.route('/editar/putuacion/<pelicula>/<usuario>', auth='public', cors='*', type='http')
    def editarputuacion(self,pelicula, usuario,**kw):

        record = request.env['puntuacion'].sudo().search([('pelicula','=',pelicula),('usuario','=',usuario)])

        record.write({"puntuacion":"2"})
            #Devolvemos el registro creado, siguiendo este esquema
        return http.Response(
        json.dumps(
        
            record.read(), #Lectura del registro
            default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
            ),
            status=200, # Respuesta de la aplicación al navegador
            mimetype='application/json'
        )    


