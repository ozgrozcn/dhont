# D'hont Sistemi
Genel seçimlerde kullanılacak D'hont sistemi için şehir bazlı yüzdelik oylar ile hesaplama yapılabilmesi için yazılmıştır.

D'hont sistemine göre şu örnek üzerinden anlatım yapılabilir:

Örnek şehirde toplamda <b>5</b> milletvekili çıkarılabildiğini düşünelim,
<pre>
A Partisi: %33
B Partisi: %27
C Partisi: %22
D Partisi: %10
E Partisi: %8
</pre>
Yukarıdaki oy oranları ile şu hesaplama bu kodda yapılmaktadır ve sonucu ekrana göstermektedir:

Milletvekili hakkı kadar her partinin yüzdelik oyu bölünür. Buradaki örnekte 5 olduğu için yüzdelik oylar 5'e varıncaya kadar sırayla
1'e, 2'ye, 3'e, 4'e ve 5'e bölünmüştür:
<pre>
            1           2           3           4           5
A Partisi: <ins><b>%33</b></ins>        <ins><b>%16.5</b></ins>        %11         %8.25       %6.6          =  2 Milletvekili <br>
B Partisi: <ins><b>%27</b></ins>        <ins><b>%13.5</b></ins>        %9          %6.25       %5.4          =  2 Milletvekili <br>
C Partisi: <ins><b>%22</b></ins>        %11          %7.3        %5.5        %4.4          =  1 Milletvekili <br>
D Partisi: %10        %5           %3.3        %2.5        %2            =  0 Milletvekili <br>
E Partisi: %8         %4           %2.6        %2          %1.6          =  0 Milletvekili <br>
</pre>
Şeklinde milletvekilliği dağılımını üstlenirler, kalın yazı ile gösterilen bölümler milletvekilliği alınan yüzdelerdir.

Burada yazdığım kodda bu hesaplama yapılmaktadır. ref: dhont.py

dipnot: Kodun en üstündeki parti listelerine istenilen parti eklenerek hesaplamaya dahil edilebilir.
