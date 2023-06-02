modern_sozluk = {"LOL":"komik bir şeye verilen cevap","CRINGE":"garip ya da utandırıcı bir şey","ROFL":"bir şakaya karşılık cevap","SHEESH":"onaylamamak","CREEPY":"korkunç"}

print("Sözlüğümüze hoş geldin.")
print("Tanımını öğrenmek istediğin kelimeyi gir.")

kelime = input("Kelime:")

if kelime.upper() in modern_sozluk:
    print(modern_sozluk[kelime.upper()])
else:
    print("Kelime bulunamadı")
