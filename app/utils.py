from os import path, remove
from subprocess import run, PIPE
from re import search
from shutil import copy2
from pathlib import Path, PurePosixPath
from sys import platform


class Convert():
    "Приобразовывает файлы в PDF"

    def __init__(self, file, file_name: str, file_path: str):
        ext = Path(file_name).suffix.lower()
        self.output_path = file_path.replace(ext, ".pdf")

        temporary_files = f"./temporary_files/{file_name}"
        with open(temporary_files, "wb") as f:
            f.write(file)
        convert(file_name=file_name.replace(f"{ext}", ".pdf"),
                source=temporary_files,
                output_dir=file_path.replace(f"{file_name}", ""),
                soft=0)
        remove(temporary_files)


PLATFORMS_SUPPORTED = ["linux", "win32"]

if platform == "win32":
    from comtypes import client


def remove_files(temp_files_attach):
    """Remove temporary files."""
    for file_temp in temp_files_attach:
        if path.isfile(file_temp):
            remove(file_temp)


def convert_to_pdf_libreoffice(file_name,
                               source,
                               output_dir,
                               timeout=None) -> str:
    """Convert MS Office files to PDF using LibreOffice."""
    output = None
    temp_filename = path.join(output_dir, path.basename(source))
    copy2(source, temp_filename)
    try:
        process = run(
            ['soffice',
                '--headless',
                '--convert-to',
                'pdf',
                '--outdir',
                output_dir,
                temp_filename
             ],
            stdout=PIPE,
            stderr=PIPE,
            timeout=timeout,
            check=True
        )
        filename = search(r'-> (.*?) using filter',
                          process.stdout.decode("latin-1"))
        remove_files([temp_filename])
        output = filename.group(1).replace("\\", "/") if filename else None
    except Exception as e:
        print(f"Error converting with LibreOffice: {e}")
        return None

    return output


def convert_doc_to_pdf_msoffice(file_name, source, output_dir):
    """Convert .doc/.docx files to PDF using MS Office."""
    output = path.join(output_dir, Path(source).stem + ".pdf")
    ws_pdf_format = 17
    app = client.CreateObject("Word.Application")

    try:
        doc = app.Documents.Open(source)
        doc.ExportAsFixedFormat(output,
                                ws_pdf_format,
                                Item=7,
                                CreateBookmarks=0
                                )
        doc.Close()
    except Exception as e:
        print(f"Error converting Word document: {e}")
        return None
    finally:
        app.Quit()

    return output


def convert_xls_to_pdf_msoffice(file_name, source, output_dir):
    """Convert .xls/.xlsx files to PDF using MS Office."""
    output = path.join(output_dir, Path(source).stem + ".pdf")
    app = client.CreateObject("Excel.Application")

    try:
        sheets = app.Workbooks.Open(source)
        sheets.ExportAsFixedFormat(0, output)
        sheets.Close()
    except Exception as e:
        print(f"Error converting Excel document: {e}")
        return None
    finally:
        app.Quit()

    return output


def convert_ppt_to_pdf_msoffice(file_name, source, output_dir):
    """Convert .ppt/.pptx files to PDF using MS Office."""
    output = path.join(output_dir, Path(source).stem + ".pdf")
    app = client.CreateObject("PowerPoint.Application")

    try:
        presentation = app.Presentations.Open(source, False, False, False)
        presentation.ExportAsFixedFormat(output, 2, PrintRange=None)
        presentation.Close()
    except Exception as e:
        print(f"Error converting PowerPoint document: {e}")
        return None
    finally:
        app.Quit()

    return output


def verify_source_is_supported_extension(file_extension):
    """Verify if the source file extension is supported."""
    supported_extensions = [".doc",
                            ".docx",
                            ".xls",
                            ".xlsx",
                            ".ppt",
                            ".pptx",
                            ".txt",
                            ".xml"
                            ]
    return file_extension in supported_extensions


def convert_using_msoffice(file_name, source, output_dir, file_extension):
    """Convert files to PDF using MS Office based on their extension."""
    if file_extension in [".doc", ".docx", ".txt", ".xml"]:
        return convert_doc_to_pdf_msoffice(file_name, source, output_dir)
    elif file_extension in [".xls", ".xlsx"]:
        return convert_xls_to_pdf_msoffice(file_name, source, output_dir)
    elif file_extension in [".ppt", ".pptx"]:
        return convert_ppt_to_pdf_msoffice(file_name, source, output_dir)
    else:
        return None


def convert(file_name, source, output_dir, soft=0):
    """Convert file to PDF using the selected software."""
    file_extension = PurePosixPath(source).suffix

    if platform == "win32" and soft == 0:
        return convert_using_msoffice(file_name,
                                      source,
                                      output_dir,
                                      file_extension)
    elif platform in PLATFORMS_SUPPORTED and soft == 1:
        return convert_to_pdf_libreoffice(file_name,
                                          source,
                                          output_dir)
    elif platform in PLATFORMS_SUPPORTED:
        return convert_to_pdf_libreoffice(file_name,
                                          source,
                                          output_dir)
    else:
        raise Exception("Platform or conversion software not supported.")
