# opencv kütüphanesini içe aktar
import cv2

# görüntü dosyasının yolunu belirle
image_path = "rice.jpg"

# görüntüyü oku ve gri seviyeye dönüştür
image = cv2.imread (image_path)
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

# görüntüyü eşikle
thresh = cv2.threshold (gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]

# eşiklenmiş görüntüdeki istenmeyen arka planları kaldırmak için morfolojik işlemler uygula
kernel = cv2.getStructuringElement (cv2.MORPH_ELLIPSE, (3, 3))
opening = cv2.morphologyEx (thresh, cv2.MORPH_OPEN, kernel)

# pirinç tanesi konturlarını bul
contours, hierarchy = cv2.findContours (opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# pirinç tanesi sayısını hesapla
rice_count = len (contours)

# pirinç tanesi sayısını konsola yazdır
print ("Pirinç tanesi sayısı:", rice_count)

# eşiklenmiş görüntüyü konsola yazdır
print ("Eşiklenmiş görüntü:")
print (thresh)

# orijinal görüntü üzerine pirinç tanesi konturlarını çiz
cv2.drawContours (image, contours, -1, (0, 255, 0), 2)

# sonucu göster
cv2.imshow ("Sonuç", image)
cv2.waitKey (0)
cv2.destroyAllWindows ()
