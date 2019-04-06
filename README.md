# Aynalama

Projede amaç seçilen resmi aynalamaktır. Bu aynalama belirli bir parselin simetriğini yansıtmak değildir. 

Resmin genişliğinin boyutu belirli sayıda parsellere ayrılır. Bu parseller ikinci bir resimde her parsel ikişer defa tekrar edecek şekilde yeni bir resim oluşturulur. Burada yeni resimin genişliği orjinal resmin 2 katıdır. 

Matetatiksel açıklamasına geçeresek NxM boyutunda bir resim ele alalım. Bu resmin yüksekliği N ve genişliği M olsun. 

Bizim projedeki manipülasyonumuz yatay eksende olacağı için M değeri ile işlem yapılacaktır. Bunun için öncelikle parsel değeri seçeriz. Bu parsel değeri bize yatay eksende resimi kaç parçaya ayıracağımızı bildirir. Parsel değeri P olan bir durum için M/P bize resmin yatay ekseninde parselleme işlemi yapılması için her adımda kaç piksel atlamamız gerektiğini bildirecektir. Buna kesme oranı diyebiliriz. Dikey eskende resmi 0 dan N değerine kadar alınır. 

Yeni resim boş olarak Nx2M olarak alınır. 

n Pozitif tam sayılar kümesinin elemanıdır.

P ={p0+p1+..+p(n-1)+pn} ve p0 = 1 ve pn = p(n-1) + 1 olacak şekilde sıralı p değerlerine sahip olsun.
M ={m0+m1+...+mn} olacak şekilde M genişlik değeri alt mn değişkenlerinden oluşduğunu kabul edelim.
Bu durumda mn = p0 + M/P dir.
O zaman,

Her parsel için ilk parsel yani p0(h, w) = (0:N ,m0 : m1) dir. Bu formülün açıklaması: ilk parsel(p0) için yükseklik(h) ve genişlik(w) değerleri; h = 0:N ve w = m0:m1 dir. 

Burada dikkat edilmesi gereken biz M ve P değerini biliyoruz ve ulaşmak istediğimiz değerler m ve p alt değerleridir. 

Sonuçta mn ve pn için n herhangi bir değeri için sonuç elde edilebilir. 

Bolge değişkeni ile n herhangi bir değer aldığında bir parselin değerlerini tutar. 
Bolge = resim(0:h, nxM/P:(n+1)xM/P) ile bulunur.

yeni_resim(0:h2, jxM/P:(j+1)xM/P) = Bolge
yeni_resim(0:h2, (j+1)xM/P:(j+2)xM/P) = Bolge

işlemleri yapılır. Burada j için J = 2P dir. J ={j0+j1+j2+...+jn} için jn = j(n-1) + 1 dir. P orjinal resmi parsellemede J ise yeni resmi parsellemede kullanılır. J = 2P ise yeni resmin yatay eksende 2 kat olması dolayısıyladır.



#Kodlarla ilgili açıklama dosyanın içerisinde yapılmıştır.

Bununla birlikte kendi girdi ve çıktımı yine burada paylaştım. 

Soru olursa: my956024@gmail.com dan ulaşabilirsiniz. 

Saygılarımla....
	
