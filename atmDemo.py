print("**********ATM Giriş Paneli**********");

username = "omerfaruk";
password = "python";

userInput = input("Lütfen Kullanıcı Adınızı Giriniz  :  ");
passwordInput = input("Lütfen Parolanızı Giriniz  :  ");

if(username != userInput and password == passwordInput):
    print("Kullanıcı Adını Hatalı Girdiniz");
elif(username == userInput and password != passwordInput):
    print("Parolanızı Hatalı Girdiniz");
elif(username != userInput and password != password):
    print("Kullanıcı Adını ve Parolanızı Hatalı Girdiniz");
else:
    print("Atm sistemine Başarıyla Giriş Yaptınız. Hoşgeldiniz!");