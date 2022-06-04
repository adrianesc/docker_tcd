# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web

class EditarPelicula(http.Controller):
    
    '''
    Llamada web para obtener lista completa de cargamentos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/peliculas
    Y nos devolvera informacion sobre cada cargamento

    '''

    @http.route('/editar/pelicula/<id>/<tipo>/<dato>', auth='public', cors='*', type='http')
    def editarPelicula(self, id, tipo, dato,**kw):
        record = request.env['peliculas'].sudo().search([('id','=', id)])
        if (tipo == 'p'):
            record.write({"puntuacion":dato})
        elif (tipo == 'v'):
            record.write({"visitas":dato})
            #Devolvemos el registro creado, siguiendo este esquema
        return http.Response(
        json.dumps(
        
            record.read(), #Lectura del registro
            default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
            ),
            status=200, # Respuesta de la aplicación al navegador
            mimetype='application/json'
        )    


