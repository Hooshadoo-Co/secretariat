from odoo import models, fields, api
import jdatetime

class SecretariatDocument(models.Model):
    _name = 'secretariat.document'
    _description = 'Secretariat Document'
    _inherit = ['mail.thread']  # Add mail.thread to inherit from

    secretariat_date = fields.Date(string='Date of Issue')
    secretariat_date_jalali = fields.Char(string='تاریخ سند')
    secretariat_no = fields.Char(string='شماره سند')
    secretariat_flow = fields.Selection([
        ('incoming', 'ورودی'),
        ('outgoing', 'خروجی')
    ], string='مسیر سند')
    secretariat_contact = fields.Many2one('res.partner', string='فرد/سازمان مربوطه')
    secretariat_employee = fields.Many2one('hr.employee', string='کارمند مربوط')

    @api.onchange('secretariat_date')
    def _onchange_secretariat_date(self):
        if self.secretariat_date:
            gregorian_to_jalali_date = jdatetime.date.fromgregorian(date=self.secretariat_date)
            self.secretariat_date_jalali = gregorian_to_jalali_date.strftime('%Y/%m/%d')

    @api.onchange('secretariat_date_jalali')
    def _onchange_secretariat_date_jalali(self):
        if self.secretariat_date_jalali:
            try:
                jalali_to_gregorian_date = jdatetime.datetime.strptime(self.secretariat_date_jalali, '%Y/%m/%d').togregorian()
                self.secretariat_date = jalali_to_gregorian_date.date()
            except ValueError:
                self.secretariat_date_jalali = False
                return {
                    'warning': {
                        'title': "! فرمت تاریخ اشتباه است",
                        'message': ". وارید کنید YYYY/MM/DD لطفا تاریخ صحیح را با فرمت"
                    }
                }
