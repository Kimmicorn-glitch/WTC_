from fpdf import FPDF
from fpdf.enums import XPos , YPos

def main():
    name = input("Name: ")
    make_pdf(name)

def make_pdf(name):

    pdf = FPDF(orientation ='P',format = 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(False)
    pdf.set_font("Helvetica","B", 24)
    pdf.cell(0,20,"CS50 Shirtificate",new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.image("shirtificate.png", x=0, y=60, w=210)

    pdf.set_font("Helvetica","B", 24)
    pdf.set_text_color(255,255,255)
    text_width = pdf.get_string_width(f"{name} took CS50")
    x = (210 - text_width) / 2
    y = 140
    pdf.text(x,y,f"{name} took CS50")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()



'''
Name: Kimmy
/workspaces/225066988/shirtificate/shirtificate.py:14: DeprecationWarning: The parameter "ln" is deprecated since v2.5.2. Instead of ln=True use new_x=XPos.LMARGIN, new_y=YPos.NEXT.
  pdf.cell(0,20,"CS50 Shirtificate",ln=True, align='C')
shirtificate/ $
#to research and fix.
'''
