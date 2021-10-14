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
