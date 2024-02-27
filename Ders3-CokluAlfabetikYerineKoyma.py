def coklu_alfabetik_sifreleme(duz_metin,anahtar):
    
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    
    duz_metin = duz_metin.replace(" ","").replace("i", "İ").upper()
    sifreli_metin = ""
    
    for i in range(len(duz_metin)):
        if duz_metin[i] in alfabe:
            sifreli_metin += alfabe[alfabe.find(duz_metin[i])+anahtar[i%len(anahtar)]]
        else:
            sifreli_metin += i 
            
    print("ŞİFRELİ METİN:",sifreli_metin)

def coklu_alfabetik_cozme(duz_metin,anahtar):
    
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    
    sifreli_metin = duz_metin.replace(" ","").replace("i", "İ").upper()
    duz_metin = ""
    
    for i in range(len(sifreli_metin)):
        if sifreli_metin[i] in alfabe:
            duz_metin += alfabe[alfabe.find(sifreli_metin[i])-anahtar[i%len(anahtar)]]
        else:
            duz_metin += i 
            
    print("DÜZ METİN:",duz_metin)    


coklu_alfabetik_sifreleme("ASLA ASLA DEME",[1,2,3])
coklu_alfabetik_cozme("BTOBCUMCGFOĞ",[1,2,3])
