# Örnek 1: Yaş kontrolü
yas = 25
ehliyet_var = True

if yas >= 18 and ehliyet_var:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")

# Örnek 2: Mevsim kontrolü
mevsim = "kış"

if mevsim == "kış" or mevsim == "sonbahar":
    print("Bugün soğuk bir gün.")
else:
    print("Bugün sıcak bir gün.")


# Örnek 3: Sosyal medya kullanıcı doğrulama
email_dogrulandi = True
telefon_dogrulandi = False

if email_dogrulandi and telefon_dogrulandi:
    print("Hesabınız doğrulandı, giriş yapabilirsiniz.")
elif email_dogrulandi or telefon_dogrulandi:
    print("Hesabınızı doğrulamak için diğer yöntemi deneyin.")
else:
    print("Hesabınızı doğrulamak için email ve telefon doğrulaması gereklidir.")
