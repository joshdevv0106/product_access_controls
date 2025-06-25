from odoo import models, fields, api

class ProductTemps(models.Model):
    _inherit = 'product.template'

    is_boolean = fields.Boolean(
        string="Boolean", compute="compute_is_boolean")

    def compute_is_boolean(self):
        if self.env.user.has_group('product_access_controls.inventory_admin_super'):
            self.is_boolean = True
        else:
            self.is_boolean = False

    # def _search_is_boolean(self, operator, value):
    #     results = []

    #     if value:
    #         if self.env.user.id in expense_sheet_id.user_ids.ids or any(item in self.env.user.groups_id.ids for item in expense_sheet_id.group_ids.ids) or self.env.user.has_group('hr_expense.group_hr_expense_manager'):
    #             results.append(expense_sheet_id.id)
    #     return [('id', 'in', results)]