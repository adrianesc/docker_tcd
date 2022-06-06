# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Puntuacion(models.Model):
    _name = 'comentarios'
    _description = 'Modelo de la lista de comentarios'
    _rec_name="id"

    id = fields.Integer()
    usuario = fields.Many2one("usuarios")
    pelicula = fields.Many2one("peliculas")
    comentario = fields.Char()
