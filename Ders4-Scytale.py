def skytale_sifreleme(duz_metin,sarim_sayisi):
    
    duz_metin = duz_metin.replace(" ","")
    if len(duz_metin)%sarim_sayisi !=0:
        satir_sayisi = (len(duz_metin)//sarim_sayisi)+1
    else:
        satir_sayisi = (len(duz_metin)//sarim_sayisi)
    doldurma_sayisi = (satir_sayisi*sarim_sayisi)-len(duz_metin)
    duz_metin += "X"*doldurma_sayisi
    sifreli_metin = ""
    
    for i in range(sarim_sayisi):
        for j in range(i,len(duz_metin),sarim_sayisi):
            sifreli_metin += duz_metin[j]
    
    print("ŞİFRELİ METİN:",sifreli_metin)

def skytale_cozme(sifreli_metin,sarim_sayisi):
    
    satir_sayisi = len(sifreli_metin)//sarim_sayisi
    duz_metin = ""
    
    for i in range(satir_sayisi):
        for j in range(i,len(sifreli_metin),satir_sayisi):
            duz_metin += sifreli_metin[j]
    
    print("DÜZ METİN:",duz_metin)
    
skytale_sifreleme("İSTİKBAL GÖKLERDEDİR",4)
skytale_cozme("İKGEDSBÖRİTAKDRİLLEX",4)
