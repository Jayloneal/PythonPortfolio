import pypdf 

def compare_pdf(pdf1, pdf2):
    with open(pdf1, 'rb') as f1:
        with open(pdf2, 'rb') as f2:
            pdf1_data = f1.read()
            pdf2_data = f2.read()

    if pdf1_data == pdf2_data:
        return True
    else:
        return False

# Replace 'file1.pdf' and 'file2.pdf' with the paths to your PDF files
if compare_pdf('D:/PDF/file1.pdf', 'D:/PDF/file2.pdf'):
    print('These PDF files are the same.')
else:
    print('These PDF files are not the same.')
