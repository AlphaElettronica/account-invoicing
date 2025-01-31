==================================
Stock Picking Return Refund Option
==================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:3786352c61f2558950c6363b8f0c52f820b5edd5f1849b64c644a0bf914673ce
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--invoicing-lightgray.png?logo=github
    :target: https://github.com/OCA/account-invoicing/tree/12.0/stock_picking_return_refund_option
    :alt: OCA/account-invoicing
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-invoicing-12-0/account-invoicing-12-0-stock_picking_return_refund_option
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-invoicing&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends the functionality of sales and purchase orders to support
modify stock move field to_refund after it has been confirmed.

**Table of contents**

.. contents::
   :local:

Installation
============

#. This module requires the additional installation of sale_stock or purchase
   modules for enabling the features it contains.

Usage
=====

To use this module, when some customer returns some refundable products to you
after you created an invoice, you need to:

For a sale order:

#. Go to *Sales > Sales Orders > Create*.
#. Choose a customer and add a product whose *Invoicing Policy* is *Delivered
   quantities*, and input some quantity to sell.
#. Confirm the sale.
#. Go to *Delivery > Validate > Apply*.
#. Return to the sale order.
#. Press *Create Invoice > Invoiceable lines > Create and View Invoices*.
#. The created invoice's amount is the same you sold.
#. Return to the sale order.
#. Go to *Delivery > Return*.
#. Set *Quantity* to a lower quantity than the sold one, and enable
   *To Refund*.
#. Press *Return > Validate > Apply*.
#. Return to the sale order.
#. Press *Create Invoice > Invoiceable lines (deduct down payments) >
   Create and View Invoices*.
#. A refund is created for the quantity you returned before.

For allowing to refund quantities after the picking has been confirmed if you
did not check 'to refund' in wizard, you can change the value
of 'Refund Options' field.

To use this module, when you return some refundable products to your supplier
after you created an invoice, you need to:

#. Go to *Purchase > Purchase Orders > Create*.
#. Choose a supplier and add a product whose *Invoicing Policy* is *Delivered
   quantities*, and input some quantity to buy.
#. Confirm the order.
#. Go to *Delivery > Validate > Apply*.
#. Return to the purchase order.
#. Press on smart button "Invoices" and create one.
#. The created invoice's amount is the same you sold.
#. Return to the purchase order.
#. Go to *Delivery > Return*.
#. Set *Quantity* to a lower quantity than you bought, and enable
   *To Refund*.
#. Press *Return > Validate > Apply*.
#. Return to the purchase order.

For allowing to refund quantities after the picking has been confirmed if you
did not check 'to refund' in wizard, you can change the value
of 'Refund Options' field.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-invoicing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-invoicing/issues/new?body=module:%20stock_picking_return_refund_option%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* Sergio Teruel <sergio.teruel@tecnativa.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-sergio-teruel| image:: https://github.com/sergio-teruel.png?size=40px
    :target: https://github.com/sergio-teruel
    :alt: sergio-teruel

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-sergio-teruel| 

This module is part of the `OCA/account-invoicing <https://github.com/OCA/account-invoicing/tree/12.0/stock_picking_return_refund_option>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
