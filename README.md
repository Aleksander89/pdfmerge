# PDFmerge

Simple CLI-tool that merges multiple single- or multipage PDFs to one, single PDF-file. 
The output PDF will be structured according to the lexicographical order of the filenames of the input PDFs.
The input PDFs should therefore be renamed (for example 1.pdf, 2.pdf,..., n.pdf) before running.

<b>Example Usage:</b>

python -m pdf_merge --source 'C:\PDFs\' --name new_name
