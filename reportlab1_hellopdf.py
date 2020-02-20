# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
# https://www.reportlab.com/docs/reportlab-userguide.pdf

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas

c = canvas.Canvas("first.pdf", pagesize=letter)

c.drawString(200, 250, "Hello PDF")
c.showPage()
c.save()
width, height = letter
print(width, height)