#! python3

import PyPDF2
import os
import argparse

"""
Merges multiple single- or multipage PDFs to one, single PDF-file. 
The output PDF will be structured according to the lexicographical order of the filenames of the input PDFs.
The input PDFs should therefore be renamed (for example 1.pdf, 2.pdf,..., n.pdf) before running.

Needs two command-line arguments:

src_dir: Directory where input PDFs are located
output_name: Name of the resulting PDF.
"""

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", dest="src_dir", help="Source destination for input PDF(s)", required=True)
    parser.add_argument("-n", "--name", dest="new_name", help="Filename of output PDF", required=True)
    args = parser.parse_args()

    if not args.src_dir:
        parser.error("[-] Please specify a source directory, use --help for more info.")
    elif not args.new_name:
        parser.error("[-] Please specify a new filename, use --help for more info.")
    return args

arguments = get_arguments()
directory = arguments.src_dir
new_filename = arguments.new_name

pdfs_to_merge = []

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


pdf_output = open(new_filename, 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()