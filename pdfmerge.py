#! python3

import PyPDF2
import os

"""
Merges multiple single- or multipage PDFs to one, single PDF-file. 
The output PDF will be structured according to the lexicographical order of the filenames of the input PDFs.
The input PDFs should therefore be renamed (for example 1.pdf, 2.pdf,..., n.pdf) before running.

Needs two command-line arguments:

src_dir: Directory where input PDFs are located
output_name: Name of the resulting PDF.
"""

pdfs_to_merge = []
directory = 'D:\\Skole\\DAPE2101\\Oblig1'

os.chdir(directory)

for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        pdfs_to_merge.append(filename)

pdfs_to_merge.sort(key=str.lower)


pdf_writer = PyPDF2.PdfFileWriter()

for file in pdfs_to_merge:
    pdf_object = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_object)
    
    for page_num in range (0, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)


pdf_output = open('s1874287DAPE2101Oblig1.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()