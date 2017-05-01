# -*- coding: utf-8 -*-
# © 2017 Therp BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

def deactivate_closed_accounts(env):
    accounts = env['account.analytic.account'].search([])
    for account in accounts:
        if account.account_type == 'closed':
            account.active == False


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    import pudb
    pudb.set_trace()
    deactivate_closed_accounts(env)
