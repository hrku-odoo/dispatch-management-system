{
    'name': "Transport Management System",
    'version': '1.0',
    'depends': ['base','fleet','stock_picking_batch'],
    'author': "Hritik Kumar",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        "security/ir.model.access.csv",
        "views/transport_management_system_views.xml",
        'views/my_module_views.xml',
        "views/inventory_batch_views.xml",
    ],
    "application": True,
    "installable":True,
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}