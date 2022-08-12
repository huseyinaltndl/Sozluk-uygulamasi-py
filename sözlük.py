import ast    #Json'daki veriyi sözlük olarak okumak için
import json   #Sözlüğü stringe çevirip tekrar json'a yazmak için
import time


f=open("data.json","r")          #Json dosyasını okuma formatında açalım
sözlük=ast.literal_eval(f.read())    #Json dosyasını string şeklinde okuyup sözlüğe çevirir
sözlük2=sözlük.copy()               #Elimizde bir kopya bulunsun.

orj="şçöğüıŞÇÖĞUİ"
hedef="scoguiSCOGUI"
translated=str.maketrans(orj,hedef)      #Türkçe karakterleri ingilizceleriyle değiştirelim.



while True:
    #Sözlüğe veri ekleme de yapabilmek için aşağıdaki kodu yazdık.
    que=input("Sözlük (e), veri ekleme (v), çıkış (q) :")
    que.lower()

    if que=="v":      #veri ekleme aşaması
        
        que1=input("Hangi kelimeyi ekleyeceksiniz : ")     #sözlüğe eklenecek key ögesini oluşturur.
        que2=input("Anlamı ne : ")                         #sözlüğe eklenecek value ögesini oluşturur.
        que1=que1.translate(translated).lower()
        que2=que2.translate(translated).lower().capitalize()    #ögelerin karakterlerini ingilizceye çevirip küçültelim.
        sözlük2.setdefault(que1,que2)                   #sözlüğe ögeleri ekleyelim.
        metin=json.dumps(sözlük2)                  #güncellenmiş sözlüğü jsona yazabilmek için stringe dönüştürelim.
        f2=open("data.json","w")        #jsonu "w" formatında açalım ki üstüne yazmasın.
        f2.write(metin)                 #stringi jsona yazalım.
        f2.close()                      #dosyayı kapatmayı unutmuyoruz.
        print("Veri eklendi. ")
    
    #sözlüğü kullanmak için;
    if que=="e":
        
        
        while True:
            que3=input("Kelime ? : ")             #anlamını görmek istediği keyi sorar.
            que3=que3.translate(translated).lower()         
            
            try:                                #ögenin sözlükte olup olmamasına bakar  
                print(sözlük2[que3])            #sözlükte varsa değerini gösterir.
                
            except KeyError:                    #sözlükte yoksa en başa döndürür, veriyi eklemesini ister.
                print("Bu kelime veritabanında yok. Ekleyiniz.")
                time.sleep(2)
                break
    if que=="q":
        exit()