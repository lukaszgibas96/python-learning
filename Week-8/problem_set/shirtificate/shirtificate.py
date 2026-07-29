from fpdf import FPDF

def main():
    
    name = input("Name: ")
    shirt_pdf_generator(name)

def shirt_pdf_generator(name):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", style = "B", size = 44)
    pdf.set_y(20)
    pdf.cell(
             text = "CS50 Shirtificate",
             align = "C",
             center = True,
             new_y = "NEXT"
                )
    
    image_width = 170
    pdf.image(  name= "shirtificate.png",
                x = (210 - image_width)/2,
                y = 50,
                w = image_width
                )

    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_font("Times", "B", 24,)
    pdf.set_y(100)
    pdf.cell(
             text = f"{name} took CS50P",
             align = "C",
             center = True,
             )
    

    pdf.output("shirtificate.pdf")






if __name__ == "__main__":
    main()