from smtplib import SMTP


# Simple Mail Transfer Protocol
# Basit Mail Transfer Protokolü

class SmtpMailService:

    def send_mail(self, subject, message):
        # Mail Mesaj Bilgisi
        self.subject = subject
        self.message = message
        content = "Subject: {0}\n\n{1}".format(subject, message)

        # Hesap Bilgileri                   NOT : Hesap bilgilerini farklı bir dosyadan çekmek daha güvenlidir.
        myMailAdress = "sender mail address"  # maili gönderecek olan mail hesabınızı giriniz.
        password = "password" # hesabın parolasını giriniz.

        # Kime Gönderilecek Bilgisi
        sendTo = ""
        try:
            mail = SMTP("smtp.gmail.com", 587)  # gmail servisi için 587 değerini parametre olarak veriyoruz.
            mail.ehlo()                         # Farklı bir servisi kullanmak isterseniz bu değeri değiştirmeniz gerekecek
            mail.starttls()
            mail.login(myMailAdress, password)
            mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
            print("[+] Mail Sending..")
        except Exception as e:
            print("Hata Oluştu!\n {0}".format(e))
