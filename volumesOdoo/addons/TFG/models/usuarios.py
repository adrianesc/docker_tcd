# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Usuarios(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'usuarios'
    _description = 'Modelo de la lista de usuarios'

    _rec_name="nombre"

    id = fields.Integer()
    nombre = fields.Char()
    contrasenya = fields.Char()
