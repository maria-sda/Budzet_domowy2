import xlwt
from datetime import datetime
from budget.models import Transaction


def create_report():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    headers = ["Account name", "Amount", "Date"]
    for col, header in enumerate(headers, 0):
        ws.write(0, col, header)

    for row, tr in enumerate(Transaction.objects.all(), 1):
        ws.write(row, 0, tr.account.name)
        ws.write(row, 1, tr.amount)
        ws.write(row, 2, tr.date)

    wb.save('example.xls')

