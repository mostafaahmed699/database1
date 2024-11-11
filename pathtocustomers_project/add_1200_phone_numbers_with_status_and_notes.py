
import sqlite3
import os

# إنشاء المجلد وحفظ قاعدة البيانات
if not os.path.exists('customers_project'):
    os.makedirs('customers_project')

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('customers_project/customers_1200.db')
c = conn.cursor()

# إنشاء الجدول مع الأعمدة الجديدة
c.execute('''
CREATE TABLE IF NOT EXISTS customers_1200 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone_number TEXT,
    phone_status TEXT,
    note TEXT
)
''')

# قائمة الأسماء
names = ['Merna', 'Mai', 'Malak', 'Heba', 'Harvy', 'Reem', 'Hager', 'Hana', 'Mrehan', 'Rahma']

# إدخال الأسماء والأرقام مع الحالة والملاحظات في قاعدة البيانات
phone_number_prefix = '012345'
counter = 0
for name in names:
    for i in range(120):
        phone_number = f'{phone_number_prefix}{str(counter).zfill(4)}'
        phone_status = 'نشط'  # يمكنك تغيير هذه القيمة حسب الحاجة
        note = 'ملاحظة'  # يمكنك تغيير هذه القيمة حسب الحاجة
        c.execute('''
        INSERT INTO customers_1200 (name, phone_number, phone_status, note)
        VALUES (?, ?, ?, ?)
        ''', (name, phone_number, phone_status, note))
        counter += 1

# حفظ التغييرات
conn.commit()

# استرجاع البيانات للتأكد من التغيير
c.execute("SELECT * FROM customers_1200")
rows = c.fetchall()
for row in rows:
    print(row)

# إغلاق الاتصال
conn.close()
