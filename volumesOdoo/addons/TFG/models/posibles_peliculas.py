# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

#Definimos el modelo de datos
class PosiblesPeliculas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'posibles_peliculas'
    _description = 'Modelo de la lista de posibles peliculas'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char()
    director = fields.Char()
    sinopsis = fields.Char()
    genero = fields.Char()
    imagen = fields.Char()
    trailer = fields.Char()
    portada  = fields.Image(max_width=800, max_height=1200)

    @api.model
    def aceptar(self,values):
        record = request.env['posibles_peliculas'].sudo().search([('id', '=', values[0])])
        vals = {
            'nombre' : record.nombre ,
            'sinopsis' : record.sinopsis,
            #'director' : 2
        }
        self.env['peliculas'].create(vals)