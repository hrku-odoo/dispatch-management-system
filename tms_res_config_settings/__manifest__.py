{
    'name': "Res Config Settings Inherited",
    'version': '1.0',
    'depends': ['base','stock'],
    'author': "Hritik Kumar",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        "views/res_config_inherited_views.xml",
    ],
    "application": True,
    "installable":True,
    "auto_install":True,
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}