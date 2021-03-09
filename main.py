import os
import shutil


def replacement_txt():
    with os.scandir('C:/Users/xxxde/Downloads') as entries:
        for entry in entries:
            if 'txt' in entry.name[-3:]:
                try:
                    os.rename('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/txt_download/{}'.format(entry.name))
                    shutil.move('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/txt_download/{}'.format(entry.name))
                except:
                    pass


def replacement_zip_rar():
    with os.scandir('C:/Users/xxxde/Downloads') as entries:
        for entry in entries:
            if 'zip' in entry.name[-3:]:
                try:
                    os.rename('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/zip_rar_download/{}'.format(entry.name))
                    shutil.move('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/zip_rar_download/{}'.format(entry.name))
                except:
                    pass


def replacement_exe():
    with os.scandir('C:/Users/xxxde/Downloads') as entries:
        for entry in entries:
            if 'exe' in entry.name[-3:]:
                try:
                    os.rename('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/exe_download/{}'.format(entry.name))
                    shutil.move('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/exe_download/{}'.format(entry.name))
                except:
                    pass


def replacement_pics():
    with os.scandir('C:/Users/xxxde/Downloads') as entries:
        for entry in entries:
            if 'jpg' in entry.name[-3:]:
                try:
                    os.rename('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/pics_download/{}'.format(entry.name))
                    shutil.move('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/pics_download/{}'.format(entry.name))
                except:
                    pass


def replacement_pdf():
    with os.scandir('C:/Users/xxxde/Downloads') as entries:
        for entry in entries:
            if 'pdf' in entry.name[-3:]:
                try:
                    os.rename('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/pdf_download/{}'.format(entry.name))
                    shutil.move('C:/Users/xxxde/Downloads/{}'.format(entry.name),
                                'C:/Users/xxxde/OneDrive/Pulpit/pdf_download/{}'.format(entry.name))
                except:
                    pass


while True:
    replacement_txt()
    replacement_exe()
    replacement_pdf()
    replacement_pics()
    replacement_zip_rar()
    print("Done")