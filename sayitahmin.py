import random

# rastgele sayı oluştur
secret_number = random.randint(1, 100)

# kaç hak kullanılacağını kullanıcıdan al
num_of_guesses = int(input("Kaç hak kullanmak istersiniz? "))

# her tahmin 2 puan değerinde
score = 0

# haklar bitene kadar tahmin yap
while num_of_guesses > 0:
    # kullanıcının tahmini
    guess = int(input("Tahmininizi girin (1-100 arası): "))

    # kalan hakları ekrana yazdır
    print("Kalan hakkınız:", num_of_guesses)

    # tahmin doğruysa tebrik et ve puan ekle
    if guess == secret_number:
        print("Tebrikler, doğru tahmin!")
        score += 2
        break

    # tahmin yanlışsa bilgilendirme yap
    if guess > secret_number:
        print("Aşağı!")
    else:
        print("Yukarı!")
    
    # bir hakkı kullandık
    num_of_guesses -= 1

# puanı ekrana yazdır
print("Puanınız:", score)
