"""Inherited HR Employee Model"""

from odoo import api, models, _


class HrEmployeeDocument(models.Model):
    """
    HR Employee Document Inherited Model.
    """
    _inherit = 'hr.employee.document'

    # pylint: disable=no-member
    @api.constrains('expiry_date')
    def check_expr_date(self):
        """
        Override to fix if expire date not choosen
        """
        emp_doc_ids = self.env['hr.employee.document']
        for each in self:
            if each.expiry_date:
                emp_doc_ids |= each
        return super(HrEmployeeDocument, emp_doc_ids).check_expr_date()
        

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def document_view(self):
            self.ensure_one()
            domain = [
                ('employee_ref', '=', self.id)]
            return {
                'name': _('Documents'),
                'domain': domain,
                'res_model': 'hr.employee.document',
                'type': 'ir.actions.act_window',
                'view_id': False,
                'view_mode': 'tree,form',
                'view_type': 'form',
                'help': _('''<p class="oe_view_nocontent_create">
                               Click to Create for New Documents
                            </p>'''),
                'limit': 80,
                'context': {
                    'default_employee_ref': self.id,
                }
                }
