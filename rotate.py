from PyPDF2 import PdfReader, PdfWriter

input_pdf = "doc.pdf"  
output_pdf = "rotated_output.pdf"  

reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    page.rotate(180)   
    writer.add_page(page)

with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"All pages have been rotated and saved to {output_pdf}")
