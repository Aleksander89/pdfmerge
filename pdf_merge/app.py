import PyPDF2
import os
from pdf_merge.helpers import validation, formatting

def run(directory, filename):
    try:
        if validation.is_valid_directory(directory):
            pdf_list = locate_pdfs_to_merge(directory)
            new_filename = formatting.format_filename(filename)
            write_pdf_to_disk(pdf_list, new_filename)
    except Exception as e:  
        print("Error: " + str(e))

def locate_pdfs_to_merge(directory):
    pdf_list = []
    
    os.chdir(directory)
    print(directory)
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_list.append(filename)

    return pdf_list

def write_pdf_to_disk(pdf_list, filename):
    pdf_writer = PyPDF2.PdfFileWriter()
    merge_pdfs(pdf_list, pdf_writer)
    
    pdf_output = open(filename, 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

def merge_pdfs(pdfs_to_merge, pdf_writer):
    for pdf_file in pdfs_to_merge:
        pdf_object = open(pdf_file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_object, strict=False)
    
        for page_num in range (0, pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)