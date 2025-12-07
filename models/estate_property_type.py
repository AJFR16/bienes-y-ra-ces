from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'sequence'
    
    name = fields.Char(required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id')
    
    _sql_constraints = [('name_unique', 'UNIQUE(name)', ' A type wiht this name already exists!')]
    
    sequence = fields.Integer(default=1, help="Order of property types.Lower apperars first.")
    name = fields.Char(required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id')
    