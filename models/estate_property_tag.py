from odoo import models, fields
class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')
    
    _sql_constraints = [('name_unique', 'UNIQUE(name)', ' A tag with this name already exists!')]