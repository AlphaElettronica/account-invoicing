# © 2016 Chafique DELLI @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.tools import float_compare


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    def _get_supplierinfo(self):
        """Given an invoice line, return the supplierinfo that matches
        with product and supplier, if exist"""
        self.ensure_one()
        supplierinfos = self.product_id.seller_ids.filtered(
            lambda seller: seller.name == self.invoice_id.supplier_partner_id)
        return supplierinfos and supplierinfos[0] or False

    @api.multi
    def _get_unit_price_in_purchase_uom(self):
        self.ensure_one()
        if not self.product_id:
            return self.price_unit
        uom = self.uom_id or self.product_id.uom_id
        return uom._compute_price(self.price_unit, self.product_id.uom_po_id)

    @api.multi
    def _is_correct_price(self, supplierinfo):
        """Return True if the partner information matche with line info
            Overload this function in custom module if extra fields
            are added in supplierinfo. (discount for exemple)
        """
        self.ensure_one()
        return (
            not self.uom_id or self.uom_id == supplierinfo.product_uom
        ) and not float_compare(
            self._get_unit_price_in_purchase_uom(),
            supplierinfo.price,
            precision_rounding=self.invoice_id.currency_id.rounding,
        )

    @api.multi
    def _prepare_supplier_wizard_line(self, supplierinfo):
        """Prepare the value that will proposed to user in the wizard
        to update supplierinfo"""
        self.ensure_one()
        price_unit = self._get_unit_price_in_purchase_uom()
        price_variation = False

        if supplierinfo:
            # Compute price variation
            if supplierinfo.price:
                price_variation = 100 *\
                    (price_unit - supplierinfo.price) / supplierinfo.price
            else:
                price_variation = False
        return {
            'product_id': self.product_id.id,
            'supplierinfo_id': supplierinfo and supplierinfo.id or False,
            'current_price': supplierinfo and supplierinfo.price or False,
            'new_price': self.price_unit,
            'current_uom_id': supplierinfo and supplierinfo.product_uom.id or False,
            'new_uom_id': self.uom_id.id,
            'current_min_quantity':
                supplierinfo and supplierinfo.min_qty or False,
            'new_min_quantity':
                supplierinfo and supplierinfo.min_qty or False,
            'price_variation': price_variation,
        }
