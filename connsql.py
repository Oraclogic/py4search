# -*- coding: utf-8 -*-
import pyodbc
import xlsxwriter
sheet1 = ['一', '二', '三']
# sheet1 = ["Oracle","Java","Python"]
workbook = xlsxwriter.Workbook('YourResults.xlsx')
worksheet = []

for i in range(0, len(sheet1)):
    print sheet1[i]
    worksheet = workbook.add_worksheet(unicode(sheet1[i], 'utf-8'))

# # format = workbook.add_format({'bold': True, 'font_color': 'red'})
#     format = workbook.add_format()
#     format.set_num_format('yyyy/mm/dd hh:mm:ss')

#     row = 0
#     col = 0

#     cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;PORT=1433;DATABASE=master;')
#     cursor = cnxn.cursor()
#     cursor.execute("""select session_id,
#     login_time,
#     host_name,
#     login_name,
#     last_request_start_time
#     from sys.dm_exec_sessions""")
#     for data in cursor:
#         for i in range(0,4):
#             if i in (1,4):
#                 worksheet.write(row, i, data[i],format)
#             else:
#                 worksheet.write(row, i, data[i])
#         # worksheet.write(row, col, data[0])
#         row += 1



workbook.close()
# cursor.close()
# cnxn.close()
