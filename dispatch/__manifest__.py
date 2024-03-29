{
    'name': "Transport Management System",
    'version': '1.0',
    'depends': ['base','fleet','stock_picking_batch','web_gantt','stock'],
    'author': "Hritik Kumar",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        "security/ir.model.access.csv",
        "views/fleet_vehicle_model_inherit_views.xml",
        "views/stock_picking_inherit_views.xml",
        "views/stock_picking_batch_inherit.xml",
    ],
    "application": True,
    "installable":True,
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}