atama = {
    "A": "S","B": "N","C": "V","Ç": "Z","D": "F","E": "R","F": "G","G": "H","Ğ": "Ü","H": "J","I": "O","İ": "A","J": "K","K": "L","L": "Ş","M": "Ö","N": "M","O": "P","Ö": "Ç","P": "Ğ","Q": "W","R": "T","S": "D","Ş": "İ","T": "Y","U": "I","Ü": "Q","V": "B","W": "E","X": "C","Y": "U","Z": "X"
}

def tekli_alfabetik_sifreleme(duz_metin,anahtar):
    
    duz_metin = duz_metin.replace("i", "İ").upper()
    sifreli_metin = ""
    
    for i in duz_metin:
        if i in anahtar:
            sifreli_metin += anahtar[i]
        else:
            sifreli_metin += i 
            
    print("ŞİFRELİ METİN:",sifreli_metin)
    
def tekli_alfabetik_cozme(sifreli_metin,anahtar):
    
    anahtar_ters = dict(reversed(i) for i in anahtar.items())
    duz_metin = ""
    
    for i in sifreli_metin:
        if i in anahtar_ters:
            duz_metin += anahtar_ters[i]
        else:
            duz_metin += i 
            
    print("DÜZ METİN:",duz_metin)

    
tekli_alfabetik_sifreleme("MATEMATİK",atama)
tekli_alfabetik_cozme("ÖSYRÖSYAL",atama)
