import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('customers_project/customers_1200.db')
with open('customers_project/customers_1200_export.sql', 'w', encoding='utf-8') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

# إغلاق الاتصال بقاعدة البيانات
conn.close()
