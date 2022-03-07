# -*- coding: utf-8 -*-
{
    'name': "Laporan DJBC",

    'summary': """
        Modul add on IT Inventory """,

    'description': """
        Modul ini merupakan prototype untuk pengajuan fasilitas kawasan industri berikat, 
        bisa digunakan untuk memulai pengembangan lebih lanjut.
    """,
    'license':"LGPL-3",
    'author': "Harist",
    'mailto': "manharist@gmail.com",
    'category': 'Inventory',
    'version': '0.1',

    'depends': ['base','stock'],
    'data': [
        'security/djbc_app_security.xml',
        'security/ir.model.access.csv',
        'views/djbc_views.xml',
        'views/exim_views.xml',
        'views/templates.xml',
    ],
    "images": ['static/description/icon.png', 'static/images/banner.png'],
    
}
