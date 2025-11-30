{
    'name': 'bienes y raices',
    'version': '18.0.1.0.2',
    'summary': 'Modulo que permite la administracion de bienes y raices',
    'author': 'Gerardo Ali Ferraro Schelijasch',
    'license': 'LGPL-3',
    'category': 'Other',
    'images': ['static/description/icon.png'],
    'depends': [
        'base',
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/real_estate_menus.xml"
        
        
    ],
    'application': True,
    
}