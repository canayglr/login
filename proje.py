from random import randint
email="can@hotmail.com"
sifre="47474747"
telefon="5555555555"
hak=3
while True:
    if hak==0:
        print("Başka zaman tekrar dene!")
        break
    else:
        islem=input("""
        Giriş Yapmak İçin [1]
        Şifremi Unuttum [2]
        E-posta Adresimi Unuttum [3]
        """)
        if islem=="1":
            m=input("""
            E-mail adresinizi giriniz!
            """)
            if m==email:
                s=input("""
                Şifrenizi giriniz!
                """)
                if s==sifre:
                    print("Giriş başarılı!")
                    break
                else:
                    hak=hak-1
                    print(f"Şifre yanlış {hak} hakkınız kaldı!")
            else:
                hak=hak-1
                print(f"E-posta yanlış {hak} hakkınız kaldı")
        elif islem=="2":
            m=input("""Şifresini unuttuğunuz E-mail adresinizi giriniz!""")
            if m==email:
                kod=randint(1000, 9999)
                print(f"Telefonunuza bir kod gönderildi! [{kod}]")
                k=int(input("""Lütfen Kodu Giriniz!"""))
                if k==kod:
                    yenisifre=input("""
                    Lütfen Yeni Şifreyi Giriniz!
                    """)
                    yenisifre1=input("""
                    Yeni Şifrenizi Tekrar Giriniz!
                    """)
                    if yenisifre==yenisifre1:
                        sifre=yenisifre
                        print(f"Şifreniz {yenisifre} olarak güncellenmiştir!")
                    else:
                        print("Şifreler Uyuşmuyor!")
                        continue
                else:
                    print("Kod yanlış!")
                    break
            else:
                hak=hak-1
                print(f"E-posta yanlış {hak} hakkınız kaldı!")
                continue
        elif islem=="3":
            t=input("""
            E-postanızın kayıtlı olduğu telefon numarasını giriniz!
            NOT:Başında 0 Olmadan Giriniz!
            """)
            if t==telefon:
                kodd=randint(1000, 9999)
                print(f"Telefonunuza bir kod gönderildi! [{kodd}]")
                kk=int(input("""
                Lütfen Kodu Giriniz
                """))
                if kk==kodd: 
                    print(f"E-posta adresiniz {email}")
                    continue
                else:
                    print("Kod yanlış!")
                    break
            else:
                hak=hak-1
                print(f"Telefon numarası yanlış {hak} hakkınız kaldı!")
                continue

        else:
            print("Geçersiz İşlem!")
            continue