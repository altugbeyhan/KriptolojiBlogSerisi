def yer_degistirme_sifreleme(duz_metin,anahtar):
    
    duz_metin = duz_metin.replace(" ","")
    bloklar = []
    
    for i in range(0,len(duz_metin),len(anahtar)):
        bloklar.append(duz_metin[i:i+len(anahtar)])
        
    while len(bloklar[-1]) != len(anahtar):
        bloklar[-1] += "X"
    
    sifreli_bloklar = []
    for i in range(len(bloklar)):
        sifreli_bloklar.append("")
        while len(sifreli_bloklar[i]) != len(anahtar):
            for j in range(len(anahtar)):
                sifreli_bloklar[i] += bloklar[i][int(anahtar[j])-1]
                
    sifreli_metin = ""
    for i in range(len(sifreli_bloklar)):
        sifreli_metin += sifreli_bloklar[i]
    
    print("ŞİFRELİ METİN:", sifreli_metin)

def yer_degistirme_cozme(sifreli_metin, anahtar):
    
    n = len(anahtar)
    anahtar_ters = [0] * n
    for i in range(n):
        anahtar_ters[int(anahtar[i]) - 1] = i + 1

    sifreli_metin = sifreli_metin.replace(" ","")
    bloklar = []
    
    for i in range(0,len(sifreli_metin),len(anahtar)):
        bloklar.append(sifreli_metin[i:i+len(anahtar)])

    cozulen_bloklar = []
    for i in range(len(bloklar)):
        cozulen_bloklar.append("")
        for j in range(len(anahtar)):
            cozulen_bloklar[i] += bloklar[i][int(anahtar_ters[j])-1]
    
    duz_metin = ""
    for i in range(len(cozulen_bloklar)):
        duz_metin += cozulen_bloklar[i]
    
    print("DÜZ METİN:", duz_metin)


yer_degistirme_sifreleme("İSTANBUL TEKNİK",[3,5,2,1,4])
yer_degistirme_cozme("TNSİALEUBTİXNKK",[3,5,2,1,4])
