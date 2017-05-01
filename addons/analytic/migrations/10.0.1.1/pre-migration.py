# -*- coding: utf-8 -*-
# © 2017 Therp BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

@openupgrade.migrate(use_env=False)
def migrate(cr, version):
    import pudb
    pudb.set_trace()
    openupgrade.copy_columns( cr, {
        'account.analytic.account' : [('account_type', None, None)]
    })


