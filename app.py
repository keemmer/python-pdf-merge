from PyPDF2 import PdfFileMerger

merger = PdfFileMerger(strict=False)
pdfs = ['D:\CODE\PYTHON\pdfMerge\\file1.pdf','D:\CODE\PYTHON\pdfMerge\\file2.pdf']

for pdf in pdfs:
    if pdf.endswith(".pdf"):
        print(pdf)
        merger.append(pdf,  import_bookmarks=False )
merger.write("result.pdf")
merger.close()