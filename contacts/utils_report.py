from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.platypus import Table
from contacts.models import Contacts
from reportlab.lib.units import inch
from django.http import FileResponse
import io

pdf = canvas.Canvas('invoice_1.pdf', pagesize=A5)
pdf.setTitle('INVOICE OF PERSON')

buf = io.BytesIO()
    # Create a Canvas
p = canvas.Canvas(buf,  pagesize=A5, bottomup=0)
textob = p.beginText()
textob.setTextOrigin(inch, inch)
textob.setFont('Helvetica', 14)

contacts = Contact.objects.all()
# Loop

lines = []

for contact in contacts:
                lines.append(contact.status)
                lines.append(contact.sexe)
                lines.append(contact.nom)
                lines.append(contact.prenom)
                lines.append(contact.matricule)
                lines.append(contact.contact)
                lines.append('===============')
for line in lines:
 textob.textLine(line)
p.drawText(textob)
p.showPage()
p.save()
buf.seek(0)

# def genHeaderTable(width, height):
#
#     return 'HEADER'
#
#
# def genBodyTable(width, height):
#
#     Text = 'djcdjcndokcd'
#
#     return Text
#
# def genFooterTable(width, height):
#
#     Text = 'sjscdcdkvgjbj'
#
#     return 'FOOTER'
#
# pdf.showPage()
# pdf.save()