from PyPDF2 import PdfFileWriter, PdfFileReader

def kodlash(file,kod):
    parser=PdfFileWriter()
    pdf=PdfFileReader(file)

    for varoq in range(pdf.numPages):
        parser.addPage(pdf.getPage(varoq))
    parser.encrypt(kod)

    with open(f'Kodlangan_{file} ','wb') as f:
        parser.write(f)
        f.close()

    print('Kodlangan fayl yasaldi')

if __name__=='__main__':
    file="pdffayl.pdf"
    kod='12341234'
    kodlash(file,kod)