kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang dicari: ")

kalimat_kecil = kalimat.lower()
kata_kata = kalimat_kecil.split()

count = 0
for i in kata_kata:
    if i == kata:
        count += 1
print(count)

