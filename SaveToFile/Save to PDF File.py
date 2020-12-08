# simple_demo.py

from fpdf import *
import os


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Order Number 123456"
                      "\n\nRoom Order: 1234"
                      "\nHotel:  Demo"
                      "\nPrice:  XXX", ln=1, align="C")
pdf.output("d:\\simple_demo.pdf")

## Open The File in Windows
os.startfile(r"d:\\simple_demo.pdf")
