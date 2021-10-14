from tqdm import tqdm

print("==================  Rumus Albert einstein: E = mc2 ==================")
print("=====================================================================")
print("========= konversi menghitung Energi dari masa dan kecepatan ========")
print("========== di ketahui E = energi, m = massa, dan c = cahaya =========")

print(" ")
print(" ")

m = float(input("masukan nilai m = massa : "))
c = float(input("masukan nilai c = kecepatan cahaya : "))
ck = c*c
E = c*ck

#loading tqdm
loop = tqdm(total = 2000, position = 0, leave = False )
for k in range(2000):
  loop.set_description("Loading".format(k))
  loop.update(1)
loop.close()

print(" ")
print("*********************************************************************")
print("Maka energi yang di hasilkan dari ", m,"kg, dengan waktu ", c,"s/m adalah = ", E)

print(" ")
print(" ")