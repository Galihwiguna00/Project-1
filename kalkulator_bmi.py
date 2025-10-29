#PROGRAM LATIHAN PERHITUNGAN BMI

print("#################################")
print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("#################################\n")

berat_badan = float(input("masukan berat badan anda (kg): ")) #meminta pengguna masukan berat badan , lalu mengkonversi angka ke type data float dan menyimpan ke variabel
tinggi_badan = float(input(f"masukan tinggi badan anda (cm): ")) #meminta pengguna masukan tinggi badan , lalu mengkonversi angka ke type data float dan menyimpan ke variabel
print()

bmi = berat_badan / ((tinggi_badan/100)**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*((tinggi_badan/100)**2)
berat_badan_ideal['atas'] = 25*((tinggi_badan/100)**2)

print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print("Nilai BMI normal adalah 18.5 kg/m^2 - 25 kg/m^2")
print(f"berat badan ideal anda adalah {berat_badan_ideal['bawah']:.2f} kg"
      f" - {berat_badan_ideal['atas']:.2f} kg, \n")

print("Terima kasih telah mmencoba program latihan ini")

