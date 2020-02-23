from PyPDF2 import (
    PdfFileReader as Reader, 
    PdfFileWriter as Writer
)
from dataclasses import dataclass


@dataclass
class RotatePDF:
    '''Class to rotate a PDF file. Class takes in a file path and the degrees clockwise to rotate the pdf as arguements'''
    path: str
    degrees: int
    
    
    def __post_init__(self):
        # open the pdf
        with open(self.path, 'rb') as pdf:
            # initialize a PyPDF2 reader object
            reader = Reader(pdf)
            # initialize a PyPDF2 writer object
            writer = Writer()
            # the number of pages in the pdf
            num_pages = reader.numPages
            
            for i in range(num_pages):
                page = reader.getPage(i)
                # rotate the page
                page.rotateClockwise(degrees)
                writer.addPage(page)
            
            with open('output.pdf', 'wb') as output:
                writer.write(output)
                print('job done')
            

if __name__ == '__main__':
    path = 'input.pdf'
    degrees = -90
    r = RotatePDF(path, degrees)
