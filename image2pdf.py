import fpdf
import sys, os

opts, destinationDir, width, height, pdf_filename = sys.argv
if not os.path.isdir(destinationDir) or not os.path.exists(destinationDir):
    print("Please, specify a directory with images")
    exit(0)

image_types = ("jpg", "png", "jpeg")

files = [f for f in os.listdir(destinationDir) if f.endswith(image_types)]
if len(files) == 0:
    print("Please, specify full path to directory")
    exit(0)

pdfProcessor = fpdf.FPDF()

for filename in files:
    pdfProcessor.add_page()
    pdfProcessor.image(destinationDir + "/" + filename, w=int(width), h=int(height))

pdfProcessor.output(pdf_filename, "F")
