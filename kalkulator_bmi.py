#PROGRAM LATIHAN PERHITUNGAN BMI

print("#################################")
print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("#################################\n")

berat_badan = float(input("masukan berat badan anda (kg): ")) #meminta pengguna masukan berat badan , lalu mengkonversi angka ke type data float dan menyimpan ke variabel
tinggi_badan = float(input(f"masukan tinggi badan anda (cm): ")) #meminta pengguna masukan tinggi badan , lalu mengkonversi angka ke type data float dan menyimpan ke variabel


bmi = berat_badan / ((tinggi_badan/100)**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*((tinggi_badan/100)**2)
berat_badan_ideal['atas'] = 25*((tinggi_badan/100)**2)

if bmi< 18.5 :
      kategori = "Anda kekurangan berat badan"
elif bmi< 25 :
      kategori = "Nilai BMI anda normal"
elif bmi< 30 :
      kategori = "Anda kelebihan berat badan"
else :
      kategori = "Anda mengalami Obesitas"

print("\nHasil kalkulator BMI anda sebagai berikut ini :\n")
print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print(kategori)
print(f"berat badan ideal anda adalah {berat_badan_ideal['bawah']:.2f} kg"
      f" - {berat_badan_ideal['atas']:.2f} kg, \n")

print("#Terima kasih telah mencoba kalkulator bmi ini#")

