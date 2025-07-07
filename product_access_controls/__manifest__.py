# -*- coding: utf-8 -*-
# Powered by Mindphin.
# © 2023 Mindphin. (<https://www.mindphin.com>).

{
    'name': "Product Access controls",
    "summary": """Product Access Control – Secure Product Fields in Odoo.
    Inventory | Inventory controls | Product customization | Product details.
    """,
    "description": """Restrict access to sensitive product fields like cost price and product type in Odoo. Ideal for finance, procurement, and inventory security.
    """,
    "category": "Point of Sale",
    "version": "17.0.1.0",
    'author': 'SageOre',
    'support': 'joshdevv0106@gmail.com',
    'depends': ['stock', 'product', 'sale'],
    'data': [
        'security/security.xml',
        'views/product.xml',
    ],
    'price': 8,
    'images': ['static/description/icon.png'],
    'currency': 'USD',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
