
# ---------------PDF MERGING-----------------

import PyPDF2
import os


# C:\Users\Admin\PycharmProjects\Scripting_with_python\02_pdf_processing\twopage.pdf
def pdf_merge():
    try:
        address_list = []
        loop = 1
        count = input('Number of files to be merged: ')

        if count.isdecimal() and int(count) > 1:
            print("Please add complete address of pdf that need to be merged.")

            while loop <= int(count):
                user_input = input(
                    f'Enter address of file {loop} to be merged: ')

# path validity and append
                if os.path.exists(user_input):
                    address_list.append(user_input)
                    loop += 1
                else:
                    print('Please add valid path')
                    continue
# PDF merging
            merger = PyPDF2.PdfFileMerger()
            for pdf in address_list:
                merger.append(pdf)

            merger.write(f'{os.getcwd()}\\combined.pdf')
            print(f'Merged file is created at {os.getcwd()}\\combined.pdf')
            print('Merging Successful.!!')

        else:
            raise ValueError

# ERROR handling
    except ValueError as err:
        print(
            f'Please enter valid number and There should be at least 2 files to be merged. {err}')
    except TypeError as err:
        print(f'Please enter valid number {err}')
    except FileNotFoundError as err:
        print(f'Please check file path or name, {err}')
    except Exception as err:
        print('Something went Wrong. :(', err)


pdf_merge()
