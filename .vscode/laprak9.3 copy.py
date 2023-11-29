#membiuat fungsi yang mengembalikan nilai
def cek_bilangan(a):
    if a %2 == 0 :
        print ("Bilangan tersebut adalah genap")
    elif a %2 !=0 :
        print ("Bilangan tersebut adalah ganjil")
    return (a)

cek_bilangan(33)