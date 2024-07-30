# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
import json

class ProductController(http.Controller):
    @http.route('/get/products', type='http', auth='public', csrf=False)
    def get_products(self, **kw):
        # Cek metode HTTP yang digunakan
        if request.httprequest.method != 'GET':
            return request.make_response(
                json.dumps({
                    'status': 405,
                    'message': 'Method Not Allowed'
                }),
                headers={'Content-Type': 'application/json'},
                status=405
            )

        # Mengambil data produk dari model produk
        products = request.env['product.template'].sudo().search([])

        # Menyiapkan data respons
        product_data = []
        for product in products:
            product_data.append({
                'nama_produk': product.name,
                'kategori': product.categ_id.name,
                'internal_reference': product.default_code,
                'sales_price': product.list_price,
                'cost_price': product.standard_price
            })

        response = {
            'status': 200,
            'message': 'success',
            'data': product_data
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(response),
            headers={'Content-Type': 'application/json'}
        )
