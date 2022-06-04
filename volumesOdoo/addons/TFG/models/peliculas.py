# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Peliculas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'peliculas'
    _description = 'Modelo de la lista de peliculas'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char()
    director = fields.Many2one("directores")
    sinopsis = fields.Text()
    genero = fields.Many2one("generos")
    imagen = fields.Char()
    trailer = fields.Char()
    portada  = fields.Image(max_width=800, max_height=1200)
    puntuacion = fields.Float()
    visitas = fields.Integer()
    #productos = fields.One2many("productos","cargamento")
