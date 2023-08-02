x = 10

if x > 5:
    print("x, 5'ten büyük.")


age = 25

if age >= 18:
    print("Ehliyet alabilirsin.")
else:
    print("Ehliyet için yaşınız uygun değil.")


grade = 85

if grade >= 90:
    print("Harf notunuz: A")
elif grade >= 80:
    print("Harf notunuz: B")
elif grade >= 70:
    print("Harf notunuz: C")
elif grade >= 60:
    print("Harf notunuz: D")
else:
    print("Harf notunuz: F")


score = 75
is_passed = True

if score >= 50 and is_passed:
    print("Tebrikler, sınavı geçtiniz!")
else:
    print("Üzgünüz, sınavı geçemediniz.")


x = 15

if x > 10:
    if x < 20:
        print("x, 10 ile 20 arasında.")
    else:
        print("x, 20'den büyük.")
else:
    print("x, 10'dan küçük.")
