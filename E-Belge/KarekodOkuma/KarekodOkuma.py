import cv2
from pyzbar.pyzbar import decode

# Karekodu okumak için bir fonksiyon tanımlayalım
def oku_karekodu(gorsel_yol):
    # Görseli oku
    gorsel = cv2.imread(gorsel_yol)

    # Karekodları tara ve çöz
    karekodlar = decode(gorsel)

    # Her bir karekodu yazdır
    for karekod in karekodlar:
        karekod_metni = karekod.data.decode('utf-8')
        print(f'Karekod Metni: {karekod_metni}')

# Kullanıcıdan görselin yolunu al
gorsel_yol = input("Lütfen görselin yolunu girin: ")

# Karekodu okuma fonksiyonunu kullanarak kullanıcının belirttiği görseldeki karekodu oku
oku_karekodu(gorsel_yol)
