# NoSQL

## Mongo DB

### Functions in Mongo DB
| Function | Explanation |
| ----- | ----- |
| mongo | Function for launching the mongo shell |

<!-- 
	import PyPDF2

# Open the PDF file
with open('original.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(file)
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # Add the desired pages to the writer object
    pdf_writer.addPage(pdf.getPage(0)) # first page
    pdf_writer.addPage(pdf.getPage(2)) # third page
    pdf_writer.addPage(pdf.getPage(5)) # sixth page

    # Create a new PDF file
    with open('extracted_pages.pdf', 'wb') as output:
        pdf_writer.write(output)
This code will create a new PDF file called "extracted_pages.pdf" that contains only the first, third, and sixth pages from the original file.

You can also use this library to extract pages from a range, for example from page 2 to page 5 you can use the following code:

Copy code
for i in range(2,6):
    pdf_writer.addPage(pdf.getPage(i))
It's important to note that you should have the PyPDF2 library installed in your environment to use it. you can install it by running !pip install pypdf2

You also can use other libraries as pdfminer and pdfquery, they also provide functionality to extract pages from PDFs.





 -->