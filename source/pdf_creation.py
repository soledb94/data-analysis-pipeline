from fpdf import FPDF
import webbrowser as wb

def createPDF(info,city):
    pdf=FPDF("P","mm","A4")
    pdf.add_page()
    pdf.set_font("Arial","B",14)
    pdf.cell(195,10,f"Comparación de agente contaminate actual con la media de Febrero en {city}",1,1)
    
    pdf.set_font("Arial","",14)

    pdf.text(10,110,f"{info}")
    
    pdf.image("graph.jpg",x=50,y=30,w=100)



    pdf.output("report.pdf")

    return wb.open_new("report.pdf")