import tkinter as tk
from tkinter import filedialog, simpledialog
import cv2
import numpy as np
import pytesseract
import os

def order_points(pts):
    # Noktaları sıralama işlemi
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)
    rect[0] = pts[np.argmin(s)]  # Sol üst
    rect[2] = pts[np.argmax(s)]  # Sağ alt
    rect[1] = pts[np.argmin(diff)]  # Sağ üst
    rect[3] = pts[np.argmax(diff)]  # Sol alt
    return rect

def process_image(file_path, min_number, max_number):
    # Resmi okuma
    img = cv2.imread(file_path)
    if img is None:
        print(f"{file_path} okunamadı.")
        return
    # HSV renk uzayına dönüştürme
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Sarı renk aralığını tanımlama
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Etiketin konturlarını bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        print(f"{file_path} dosyasında etiket bulunamadı.")
        return
    label_contour = max(contours, key=cv2.contourArea)
    # Etiketin döndürülmüş dikdörtgenini elde etme
    rect = cv2.minAreaRect(label_contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    box = order_points(box)
    # Perspektif dönüşümü için hedef noktaları belirleme
    (tl, tr, br, bl) = box
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([
        [0, 0],
        [maxWidth -1, 0],
        [maxWidth -1, maxHeight -1],
        [0, maxHeight -1]], dtype="float32")
    M = cv2.getPerspectiveTransform(box.astype('float32'), dst)
    label_img = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
    # Kırmızı sayıları tespit etmek için HSV renk uzayına dönüştürme
    hsv_label = cv2.cvtColor(label_img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv_label, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_label, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask1, mask2)
    red_numbers = cv2.bitwise_and(label_img, label_img, mask=mask_red)
    # Gri tona dönüştürme ve eşikleme
    gray = cv2.cvtColor(red_numbers, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # OCR ile metni okuma
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    # Metni temizleme
    text = ''.join(filter(str.isdigit, text.strip()))
    if text == '':
        print(f"{file_path} dosyasında sayı bulunamadı.")
        return
    try:
        number = int(text)
    except ValueError:
        print(f"{file_path} dosyasındaki sayı okunamadı.")
        return
    if min_number <= number <= max_number:
        # Dosyayı yeniden adlandırma
        dir_name = os.path.dirname(file_path)
        new_file_path = os.path.join(dir_name, f"{number}.jpg")
        if os.path.exists(new_file_path):
            print(f"{new_file_path} zaten mevcut. {file_path} atlandı.")
            return
        try:
            os.rename(file_path, new_file_path)
            print(f"{file_path} dosyası {new_file_path} olarak yeniden adlandırıldı.")
        except Exception as e:
            print(f"{file_path} dosyası yeniden adlandırılamadı: {e}")
    else:
        print(f"{file_path} dosyasındaki sayı ({number}) aralık dışında.")

# Ana program
if __name__ == "__main__":
    # Tkinter penceresini başlatma
    root = tk.Tk()
    root.withdraw()

    # Sayı aralığını kullanıcıdan alma
    min_number = simpledialog.askinteger("Minimum Sayı", "En düşük sayıyı girin:", initialvalue=15000)
    max_number = simpledialog.askinteger("Maksimum Sayı", "En yüksek sayıyı girin:", initialvalue=25000)

    if min_number is None or max_number is None:
        print("Sayı aralığı girilmedi. Program sonlandırılıyor.")
        exit()

    if min_number > max_number:
        print("Minimum sayı, maksimum sayıdan büyük olamaz.")
        exit()

    # Dosyaları seçmek için arayüz
    file_paths = filedialog.askopenfilenames(
        title='İşlenecek resimleri seçin',
        filetypes=[('Resim Dosyaları', '*.jpg *.jpeg *.png')]
    )

    for file_path in file_paths:
        process_image(file_path, min_number, max_number)
