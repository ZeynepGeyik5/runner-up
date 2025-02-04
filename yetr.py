n=int(input("kaç adet sayı istiyorsunuz ? "))
arr=list(map(int,input("n adet sayıyı giriniz. ").split()))
benzersizsayilar=sorted(set(arr),reverse=True)
if len(benzersizsayilar)>1:
    result=benzersizsayilar[1]
    print(f"sonucunuz {result}")
else:
    print("no runner-up found ")