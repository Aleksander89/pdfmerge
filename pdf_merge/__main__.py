import argparse
from pdf_merge import app

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", dest="src_dir", help="Source folder of input PDF(s). Paths for Windows-systems must be specified within single or double quotes, or with an additional '\\'-character.", required=True)
    parser.add_argument("-n", "--name", dest="new_name", help="Filename of output PDF. Can be specified with or without .pdf extension.", required=True)
    args = parser.parse_args()

    if not args.src_dir:
        parser.error("[-] Please specify the source directory of the PDFs, use --help for more info.")
    elif not args.new_name:
        parser.error("[-] Please specify the filename of the output PDF, use --help for more info.")
    return (args.src_dir, args.new_name)

if __name__ == '__main__':
    directory, filename = get_arguments()
    app.run(directory, filename)

