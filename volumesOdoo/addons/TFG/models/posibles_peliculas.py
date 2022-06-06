# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

#Definimos el modelo de datos
class PosiblesPeliculas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'posibles_peliculas'
    _description = 'Modelo de la lista de posibles peliculas'

    _rec_name="nombre"
   
    id = fields.Integer()
    nombre = fields.Char()
    director = fields.Char()
    sinopsis = fields.Char()
    genero = fields.Char()
    imagen = fields.Char()
    trailer = fields.Char()
    portada  = fields.Image(max_width=800, max_height=1200)

    #función la cual cuando se pulsa el botón "Aceptar", crea una copia del registro en la tabla películas
    @api.model
    def aceptar(self,values):
        #buscar el registro con el id introducido
        record = request.env['posibles_peliculas'].sudo().search([('id', '=', values[0])])
        #pasar los datos
        vals = {
            'nombre' : record.nombre ,
            'sinopsis' : record.sinopsis,
            'imagen' : record.imagen,
            'trailer' : record.trailer,
        }
        #crear el registro
        self.env['peliculas'].create(vals)