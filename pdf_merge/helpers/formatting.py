def format_filename(new_filename):
    name_list = new_filename.split('.')
    fixed_filename = ''

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