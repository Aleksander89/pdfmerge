#! python3

import PyPDF2
import os
import argparse

"""
Merges multiple single- or multipage PDFs to one, single PDF-file. 
The output PDF will be structured according to the lexicographical order of the filenames of the input PDFs.
The input PDFs should therefore be renamed (for example page1.pdf, page2.pdf,..., pagen.pdf) before running.

Needs two command-line arguments:

src_dir: Directory where input PDFs are located
output_name: Name of the resulting PDF.
"""

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", dest="src_dir", help="Source folder of input PDF(s)", required=True)
    parser.add_argument("-n", "--name", dest="new_name", help="Filename of output PDF", required=True)
    args = parser.parse_args()

    if not args.src_dir:
        parser.error("[-] Please specify a source directory, use --help for more info.")
    elif not args.new_name:
        parser.error("[-] Please specify a new filename, use --help for more info.")
    return args

def locate_pdfs_to_merge(directory):
    pdf_list = []
    
    os.chdir(directory)
    print(directory)
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_list.append(filename)

    return pdf_list

def merge_pdf(writer):
    for pdf_file in pdfs_to_merge:
        pdf_object = open(pdf_file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_object, strict=False)
    
        for page_num in range (0, pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page_num)
            writer.addPage(page_obj)

def write_pdf(filename):
    pdf_writer = PyPDF2.PdfFileWriter()
    merge_pdf(pdf_writer)
    
    pdf_output = open(filename, 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

def check_name(new_filename):
    name_list = new_filename.split('.')
    fixed_filename = ""

    if len(name_list) < 2:
        fixed_filename = new_filename + '.pdf'
    elif len(name_list) == 2:
        if not name_list[1] == '.pdf':
            fixed_filename = name_list[0] + '.pdf'
    elif len(name_list) > 2:
        raise Exception('The format of the specified filename is incorrect. Valid format: "filename" or "filename.pdf"') 
    else:
        fixed_filename = new_filename

    return fixed_filename

# Retrives arguments from command line
arguments = get_arguments()
directory = arguments.src_dir
filename = arguments.new_name

# Finds and sorts PDFs from the source directory
pdfs_to_merge = locate_pdfs_to_merge(directory)
pdfs_to_merge.sort(key=str.lower)

# Merges and writes to new PDF
try:
    corrected_filename = check_name(filename)
    write_pdf(corrected_filename)
except Exception as e: 
    print("Error:\n" + str(e))


