from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.platypus import Table
from contacts.models import Contact
from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable


pdf = canvas.Canvas('invoice_1.pdf', pagesize=A5)
pdf.setTitle('INVOICE OF PERSON')

width, height = A5

heightList = [
    height * 20 / 100, # header.py
    height * 75 / 100, # body
    height * 5 / 100,  # footer
]
contacts = Contact.objects.all()

mainTable = Table([
         [genHeaderTable(width, heightList[0])],
         [genBodyTable(width, heightList[1])],
         [genFooterTable(width, heightList[2])],
],
     colWidths=width,
     rowHeights=heightList
)

mainTable.setStyle([
    # ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ('LEFTPADDING', (0, 0), (0, 2), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
]
)

mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf, 0, 0)

pdf.showPage()
pdf.save()