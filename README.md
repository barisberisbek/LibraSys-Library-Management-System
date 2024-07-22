# LibraSys: Kütüphane Yönetim Sistemi

LibraSys, kullanıcı dostu arayüzü ve ileri seviye Python özellikleriyle tasarlanmış, kapsamlı bir kütüphane yönetim sistemidir. Bu uygulama, kütüphanedeki kitapların ve öğrencilerin takibini kolaylaştırır, kitap ödünç alma ve iade işlemlerini etkin bir şekilde yönetir ve kullanıcılara çeşitli arama ve listeleme seçenekleri sunar.

## İçindekiler

1. [Giriş](#giriş)
   - [Genel Bakış](#genel-bakış)
   - [Nasıl Çalıştırılır](#nasıl-çalıştırılır)
   - [Kullanım](#kullanım)
2. [Başlatma ve Etkileşim](#başlatma-ve-etkileşim)
   - [Kullanılan Veri Yapıları](#kullanılan-veri-yapıları)
   - [Önemli Notlar](#önemli-notlar)
   - [Dosya Formatları](#dosya-formatları)
3. [Fonksiyonlar ve Özellikler](#fonksiyonlar-ve-özellikler)
4. [Fonksiyonlara Genel Bakış](#fonksiyonlara-genel-bakış)

## Giriş

### Genel Bakış

LibraSys, Python tabanlı bir Kütüphane Yönetim Sistemidir. Kütüphane kaynaklarının etkili yönetimi için kullanıcı dostu bir arabirim sunar.

### Nasıl Çalıştırılır

1. Projeyi GitHub'dan klonlayın:

git clone https://github.com/kullanici-adiniz/LibraSys.git
cd LibraSys

2. Metin dosyalarını ana script ile aynı dizine yerleştirin.

3. Terminalde şu komutu çalıştırın:
python main.py

Alternatif olarak:
- ZIP dosyasını açın ve klasörü PyCharm'a sürükleyip bırakın.
- PyCharm'da 'play' ikonuna tıklayarak çalıştırın.

### Kullanım

- Programı başlatın ve menü seçeneklerini takip edin.
- Kütüphane yönetimi işlemlerini gerçekleştirmek için ilgili sayısal seçimleri girin.

## Başlatma ve Etkileşim

### Kullanılan Veri Yapıları

- `books`: ISBN numaralarına göre kitap bilgilerini içeren sözlük.
- `students`: Öğrenci ID'lerine göre öğrenci bilgilerini içeren sözlük.
- `borrowed_books`: Öğrenci ID'lerine göre ödünç alınan kitapların ISBN'lerini içeren sözlük.

### Önemli Notlar

- Dosya bütünlüğü: `students.txt`, `books.txt` ve `borrowed_books.txt` dosyalarının doğru formatlanması önemlidir.
- Kullanıcı arayüzü: Program, kolay gezinme sağlayan menü tabanlı bir arayüze sahiptir.

### Dosya Formatları

- `students.txt`: Her satır "123456 John Doe" formatında.
- `books.txt`: Her satır "0385472579,Kitap Adı,Yazar Adı,T/F" formatında.
- `borrowed_books.txt`: Her satır "123456,013284737X,0385472579" formatında.

## Fonksiyonlar ve Özellikler

1. Tüm kitapları listeleme
2. Ödünç alınmış kitapları listeleme
3. Yeni kitap ekleme
4. Kitap silme (ödünç alınmamışsa)
5. ISBN ile kitap arama
6. İsim ile kitap arama
7. Öğrenciye kitap ödünç verme
8. Öğrencileri ve ödünç aldıkları kitapları listeleme

## Fonksiyonlara Genel Bakış

### Kitaplar
- Tüm kitapları listeleme
- Ödünç alınmış kitapları listeleme
- Yeni kitap ekleme
- Kitap silme
- ISBN ile arama
- İsim ile arama

### Kitap Ödünç Alma
- Kitap ödünç verme
- Kitap iade etme

### Öğrenciler
- Öğrencileri ve kitaplarını listeleme
- Tüm öğrencileri listeleme
- Öğrenci ekleme
- Öğrenci silme

### Menü Gösterimi ve Giriş
- Menü gösterme
- Ana fonksiyon

Bu kütüphane yönetim sistemi, kitapların ve öğrencilerin etkili bir şekilde yönetilmesini sağlar. Kullanıcı dostu arayüzü ve kapsamlı özellikleriyle, kütüphane işlemlerini kolaylaştırır ve verimli hale getirir.
