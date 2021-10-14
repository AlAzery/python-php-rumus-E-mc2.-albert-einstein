# python-php-rumus-E-mc2.-albert-einstein

<h5>copy script php</h5>

````php
   <?php
echo("==================  Rumus Albert einstein: E = mc2 ==================");
echo("=====================================================================");
echo("========= konversi menghitung Energi dari masa dan kecepatan ========");
echo("============ di ketahui E = energi, m = massa, dan c = cahaya ===========");

echo("masukan nilai m = massa :");
$m = trim(fgets(STDIN));
echo("masukan nilai c = kecepatan cahaya :");
$c = trim(fgets(STDIN));

if ($m == "" && $c == "") {
  echo("nilai kosong");
  return false;
}else{
  //c kuadrat
  $ck = $c*$c;
  $E = $m*$ck;
}
print("**********************************************************************");
print("maka E yang di hasilkan dari $m kg, dengan waktu $c s/m adalah ");
print($E);
echo(" ");
````

<h5>copy script python</h5>

<p>pip install tqdm</p>

````python
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

````
