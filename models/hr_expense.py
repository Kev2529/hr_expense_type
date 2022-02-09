from odoo import fields, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    expense_type = fields.Selection([
        ('regular', 'Regular')
    ], required=True, default="regular")
