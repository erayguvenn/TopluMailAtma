import smtplib   #smtp mail gönderme kütüphanemizi ekliyoruz.

eposta="epostaAdresiniz@gmail.com"#e-posta adresinizi giriniz.
sifre ="şifreniz"#şifrenizi giriniz.


# Mail Mesaj Bilgisi
subcjet = "Veri Bilimi ve Makine Öğreniminde Python’un Yeri"
message = """ Bu bir otomatik mesajdır,dikkate almayınız.
Sofistike veri analizleri günümüzde IT için en önemli konular haline gelmiştir. 
Python ise bu durumlar için en elverişli programlama dili olmuştur. 
Python arayüzündeki kütüphanelerin birçoğu makine öğrenimi ve veri bilimi üzerine elverişlidir. 
Bu alanlardaki kütüphanelerde ki yüksek kaliteli komutları, makine öğrenimi kütüphanelerinin ve 
diğer nümerik algoritma kütüphanelerinin sürekli gelişmesine çok yardımcı olmuştur. """

content = "Subject: {0}\n\n{1}".format(subcjet, message)


with open("mailler.txt","r") as f: #burada mail adreslerimizi bir metin belgesinden alıyoruz.
    satir=f.readline() #belgedeki ilk satırımızı okuyoruz.
    while satir: # satır var ise
        try:
            mail=smtplib.SMTP("smtp.gmail.com",587) #smtp host ve port ayarlarımızı yapıyoruz.
            mail.ehlo()
            mail.starttls() #Güvenli bağlantımızı açıyoruz.
            mail.login(eposta,sifre) #e-posta adresimizi ve şifresini giriyoruz
            print("bağlantı başarılı") #kullanıcı adı ve şifreyle yapılan bağlantıyı kontrol ediyor
            mail.sendmail(eposta,satir,content.encode("utf-8")) #gönderici,alıcı,ve mail içeriği.
            print("{}’e mail adresine gönderildi".format(satir)) #gönderilen maili yazdırıyoruz.
            mail.close()
        except:
            print("{}’e mail gönderilemedi".format(satir)) #gönderilemeyen maili yazdırıyoruz.
            f.close()  #okuma işlemini bitiriyoruz.
        satir=f.readline() # mail listesinde alt satırı okutuyoruz.

