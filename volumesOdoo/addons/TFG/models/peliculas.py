# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Peliculas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'peliculas'
    _description = 'Modelo de la lista de peliculas'

    _rec_name="nombre"
   
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
