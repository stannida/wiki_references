"""
A python script to extract the limited number of files from a zip archive with json files. 
It extracts them in a folder in the chosen directory.


Usage: $ python dearchive.py -i <input_zip_file> -o <output_dir> -l <limit>(optional, the default is 5)
"""

import getopt
import os
import sys
import zipfile


def unzip(zip_file, dest_dir, limit):
    """
    Unzips the files from a zip file and puts them in the given destination (can be a non-existing folder). 
    Out put can be filtered by providing the file extension.
    :param zip_file: zip file to extract.
    :param dest_dir: destination folder.
    :param limit: the number of files to extract, the default is 5.
    :return: nothing
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    try:
        zfile = zipfile.ZipFile(zip_file, 'r')
        for filename in zfile.namelist():
            if limit > 0:
                print(limit)
                print('Extracting {f} to {d}'.format(f=filename, d=dest_dir))
                zfile.extract(filename, dest_dir)
                limit -= 1
    except zipfile.BadZipfile:
        print("Cannot extract {f}: Not a valid zipfile (BadZipfile Exception)".format(f=zip_file))




def cmd_error(prog_name):
    """
    Prints out the usage instruction and exits with error status 2
    :param prog_name: Name of the script to print in the usage prompt
    """
    print('Usage: $ python {prog} -i <input_file> -o <output_dir> -l <limit>'.format(prog=prog_name))
    sys.exit(2)


def read_cmd_line(argv):
    """
    Reads the command line arguments and extracts options from it.
    :param argv: Command line arguments (including the script name)
    :return: The input zip file, destination directory and limit
    """
    opts = []
    try:
        opts, args = getopt.getopt(argv[1:], 'i:o:l:')
    except getopt.GetoptError as err:
        # print help information and exit:
        print("Here")
        print(str(err))
        usage()
        sys.exit(2)

    print(opts)
    input_file = ''
    output_dir = ''
    limit = 5
    for opt, arg in opts:
        if opt == '-i':
            input_file = arg
        elif opt == '-o':
            output_dir = arg
        elif opt == '-l':
            limit = int(arg)

    if not input_file or not output_dir:

        cmd_error(argv[0])
    return input_file, output_dir, limit


def main(argv):
    zip_file, dest_dir, limit = read_cmd_line(argv)


    # Unzip the file
    unzip(zip_file, dest_dir, limit)



if __name__ == "__main__":
    main(sys.argv)