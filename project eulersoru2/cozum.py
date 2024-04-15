#Fibonacci dizisindeki her yeni terim, önceki iki terim eklenerek üretilir. 1 ve 2 ile başlayarak ilk 10 terim şöyle olacaktır:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
#Değerleri dört milyonu aşmayan Fibonacci dizisindeki terimleri dikkate alarak, çift sayıların toplamını bulun.

class fibo:
    def __init__(self,a,b,toplam):
        self.a=a
        self.b=b
        self.toplam=toplam


    def üret(self):
        self.a=1
        self.b=2
        self.toplam=0

        while self.b < 4000:
            if self.b % 2 == 0:
                self.toplam +=self.b
                self.a,self.b=self.b,self.a+self.b













