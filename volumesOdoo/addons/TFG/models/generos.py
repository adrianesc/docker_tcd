# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Generos(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'generos'
    _description = 'Modelo de la lista de generos'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

   
    id = fields.Integer()
    nombre = fields.Char()
