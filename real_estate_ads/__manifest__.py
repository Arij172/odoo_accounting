{
    'name':'Real Estate Ads',
    'description':"""
    Real Estate module to show available properties
    """,
    'version':'1.0',
    'category':"Sales",
    'depends':[],
    'data':[
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/menu_items.xml'
    ],

    'installable':True,
    'application':True,
    'license':'LGPL-3'
}