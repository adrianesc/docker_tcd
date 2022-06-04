# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Puntuacion(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'comentarios'
    _description = 'Modelo de la lista de comentarios'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="id"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    usuario = fields.Many2one("usuarios")
    pelicula = fields.Many2one("peliculas")
    comentario = fields.Char()
    #productos = fields.One2many("productos","cargamento")
