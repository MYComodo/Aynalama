import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np


root = tk.Tk()
root.withdraw()


#resmin yüklendiği kısım. Teriche göre değiştirilebilir.
dosya_yolu = filedialog.askopenfilename(title = 'Resim Seç', filetypes = [('image files', '*.png;*.jpg')])

resim = cv2.imread(dosya_yolu)

#resim yeniden boyutlandırılıyor.
resim = cv2.resize(resim,(500,500))


parsel_degeri = 20
#orjinal resmin özellikleri isteniyor
h1, w1, d1 = resim.shape

#kesme oranı yatay eksende parselleyeceğimiz resmin piz
kesme_orani = int(w1/parsel_degeri)

#boş siyah resim oluşturma
yeni_resim = np.zeros((h1,w1*2, d1), np.uint8)
h2, w2, d2 = yeni_resim.shape

#burada açıklaması yapılan işlemler ile resim manipülasyonu yapılıyor
for i,j in zip(range(0,parsel_degeri,1), range(0,parsel_degeri*2,2)):
	Bolge = resim[0:h1, i*kesme_orani:(i+1)*kesme_orani]
	yeni_resim[0:h2, j*kesme_orani:(j+1)*kesme_orani] = Bolge
	yeni_resim[0:h2, (j+1)*kesme_orani:(j+2)*kesme_orani] = Bolge
	
	
cv2.imwrite("Aynalanmis_resim.png", yeni_resim)
cv2.imshow("orjinal resim",resim)
cv2.imshow("Aynalanmis Resim", yeni_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()