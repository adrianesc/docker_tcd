# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Peliculas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'directores'
    _description = 'Modelo de la lista de directores'
    _rec_name="nombre"


    id = fields.Integer()
    nombre = fields.Char()
