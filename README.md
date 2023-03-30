# D'hont Sistemi
Genel seçimlerde kullanılacak D'hont sistemi için şehir bazlı % lik oylar ile hesaplama yapılabilmesi için yazılmıştır.

D'hont sistemine göre şu örnek üzerinden anlatım yapılabilir:

Örnek şehirde toplamda 5 milletvekili çıkarılabildiğini düşünelim,

A Partisi: %33
B Partisi: %27
C Partisi: %22
D Partisi: %10
E Partisi: %8

Yukarıdaki oy oranları ile şu hesaplama bu kodda yapılmaktadır ve sonucu ekrana göstermektedir:

Milletvekili hakkı kadar her partinin yüzdelik oyu bölünür. Buradaki örnekte 5 olduğu için yüzdelik oylar 5'e varıncaya kadar 
1'e, 2'ye, 3'e, 4'e ve 5'e bölünmüştür:

            1     2     3    4     5
A Partisi: **%33** **%16.5**  %11  %8.25  %6.6         =  2 Milletvekili
B Partisi: **%27** **%13.5**  %9   %6.25  %5.4         =  2 Milletvekili
C Partisi: **%22** %11    %7.3 %5.5   %4.4             =  1 Milletvekili
D Partisi: %10 %5     %3.3 %2.5   %2                   =  0 Milletvekili
E Partisi: %8  %4     %2.6 %2     %1.6                 =  0 Milletvekili

Şeklinde milletvekilliği dağılımını üstlenirler, kalın yazı ile gösterilen bölümler milletvekilliği alınan yüzdelerdir.

Burada yazmış kodda bu hesaplama yapılmaktadır. 
