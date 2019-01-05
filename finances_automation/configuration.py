""" Configuration constants for users of finances_automation; these determine how the database is set up,
which columns are relevant in statements, how dates are parsed, and which categories are applied to transactions.
"""
import os


package_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

db_name = 'finances'
db_cluster = os.path.join(package_root, 'data', 'database_cluster')
user = 'Marcus1'

categories = {
    'income': [
        'job',
        'bursaries_and_scholarships',
        'transfers_in',
        'other_income'
    ],

    'expense': [
        'rent',
        'utility_bills',
        'essentials',
        'health',
        'clothes',
        'subscriptions',
        'cash',
        'fun',
        'coffee',
        'holidays',
        'travel',
        'credit_card',
        'savings_and_investments',
        'loan_repayments',
        'charity',
        'other_expenses'
    ],

    'adjustment': [
        'make_balance',
        'ignore'
    ]
}

table_configurations = {
    'current_transactions': {
        'name': 'current_transactions',
        'type': 'transactions',
        'schema': {
            'id': 'serial PRIMARY KEY',
            'date': 'DATE NOT NULL',
            'card': 'VARCHAR',
            'description': 'VARCHAR',
            'money_in': 'VARCHAR',
            'money_out': 'VARCHAR',
            'balance': 'DECIMAL',
            'category_code': 'DECIMAL',
            'category': 'VARCHAR'
        },
        'monetary_columns': ['money_in', 'money_out', 'balance'],
        'date_columns': ['date'],
        'date_format': '%d/%m/%Y',
        'category_columns': ['category_code', 'category']
    },

    'credit_transactions': {
        'name': 'credit_transactions',
        'type': 'transactions',
        'schema': {
            'id': 'serial PRIMARY KEY',
            'date': 'DATE NOT NULL',
            'card': 'VARCHAR',
            'description': 'VARCHAR',
            'money_in': 'VARCHAR',
            'money_out': 'VARCHAR',
            'balance': 'DECIMAL',
            'category_code': 'DECIMAL',
            'category': 'VARCHAR'
        },
        'monetary_columns': ['money_in', 'money_out', 'balance'],
        'date_columns': ['date'],
        'date_format': '%d/%m/%Y',
        'category_columns': ['category_code', 'category']
    },

    'totals': {
        'name': 'totals',
        'type': 'analysis',
        'schema': {
            'id': 'serial PRIMARY KEY',
            'tables_analysed': 'VARCHAR',
            'start_date': 'DATE NOT NULL',
            'end_date': 'DATE NOT NULL',
            'analysis_datetime': 'TIMESTAMPTZ NOT NULL',
            **{category: 'DECIMAL' for category in [*categories['income'], *categories['expense']]}
        },
        'monetary_columns': [*categories['income'], *categories['expense']],
        'date_columns': ['start_date', 'end_date', 'analysis_datetime'],
        'date_format': '%d/%m/%Y'
    },

    'totals_across_all_accounts': {
        'name': 'totals_across_all_accounts',
        'type': 'analysis',
        'schema': {
            'id': 'serial PRIMARY KEY',
            'tables_analysed': 'VARCHAR',
            'start_date': 'DATE NOT NULL',
            'end_date': 'DATE NOT NULL',
            'analysis_datetime': 'TIMESTAMPTZ NOT NULL',
            **{category: 'DECIMAL' for category in [*categories['income'], *categories['expense']]}
        },
        'monetary_columns': [*categories['income'], *categories['expense']],
        'date_columns': ['start_date', 'end_date', 'analysis_datetime'],
        'date_format': '%d/%m/%Y'
    },

    'monthly_averages': {
        'name': 'monthly_averages',
        'type': 'analysis',
        'schema': {
            'id': 'serial PRIMARY KEY',
            'tables_analysed': 'VARCHAR',
            'start_date': 'DATE NOT NULL',
            'end_date': 'DATE NOT NULL',
            'analysis_datetime': 'TIMESTAMPTZ NOT NULL',
            **{category: 'DECIMAL' for category in [*categories['income'], *categories['expense']]}
        },
        'monetary_columns': [*categories['income'], *categories['expense']],
        'date_columns': ['start_date', 'end_date', 'analysis_datetime'],
        'date_format': '%d/%m/%Y'
    }
}

table_names = (table_name for table_name in table_configurations)

transaction_table_names = (
    table['name'] for table in list(table_configurations.values()) if table['type'] == 'transactions'
)

analysis_table_names = (
    table['name'] for table in list(table_configurations.values()) if table['type'] == 'analysis'
)

parser = {
    'delimiter': ',',
    'header': 3,
    'usecols': None,
    'dtype': None
}
