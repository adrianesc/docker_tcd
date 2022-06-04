# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class Listaputuacion(http.Controller):
    
    '''
    Llamada web para obtener lista completa de cargamentos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/peliculas
    Y nos devolvera informacion sobre cada cargamento

    '''

    @http.route('/borrar/putuacion', auth='public', cors='*', type='http')
    def borrarputuacion(self, **kw):

        record = request.env['puntuacion'].sudo().search([('id','=','13')])

        record.unlink()

        return http.Response(
        json.dumps(       
        record[0].read(), #Lectura del registro
        default=str),
        status=200, # Respuesta de la aplicación al navegador
        mimetype='application/json'
        )       


