import os			    
import time			  
import calendar 	
from PyPDF2 import PdfMerger

dir_files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
epoch_time = int(calendar.timegm(time.gmtime()))
print(dir_files)

for file in dir_files: 
	if file.endswith('.pdf'): 
		print('Working on converting: ' + file)
		
		file = file.replace('.pdf', '') 
		folder = str(int(epoch_time)) + '_' + file 
		combined = folder + '/' + file 
		
		if not os.path.exists(folder): 
			os.makedirs(folder)
		
		magick = 'magick -density 150 "' + file + '.pdf" "' + combined + '-%04d.png"'
		print(magick)
		os.system(magick)
		
		pngs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
		for pic in pngs:
			if pic.endswith('.png'):
				combined_pic = folder + '/' + pic
				print(combined_pic)
				tesseract = 'tesseract "' + combined_pic + '" "' + combined_pic + '-ocr" -l hin PDF'
				print(tesseract)
				os.system(tesseract)
		
		ocr_pdfs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

		merger = PdfMerger()
		for pdf in ocr_pdfs:
			if pdf.endswith('.pdf'):
				merger.append(folder + '/' + pdf)

		merger.write(file + '-ocr-combined.pdf')
		merger.close()
