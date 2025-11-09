# Facial Emotion Recognition - Srđan Machiedo

**Project:** Facial Emotion Recognition
**Student:** Srđan Machiedo
**Status:** In Progress

## 🎯 Project Overview

Cilj projekta je razviti sustav koji može prepoznati emocije na ljudskom licu koristeći slike.    

Problem koji rješavam je **kako trenirati model koji može točno prepoznati osnovne emocije**  
(sreća, tuga, ljutnja, iznenađenje, strah, gađenje i neutralno) koristeći skup slika lica.

---

## 💡 Hipoteza
Ako neuronska mreža nauči dovoljno reprezentativne obrasce lica (npr. osmijeh, podignute obrve, namrgođeno čelo),  
moći će točno prepoznati emocije i na slikama koje prethodno nije vidjela.  

---

## 📊 Podaci
Koristim **FER2013 dataset**, dostupan na [Kaggleu](https://www.kaggle.com/datasets/msambare/fer2013).  
- Sadrži oko **35.000 crno-bijelih slika lica** (48×48 piksela).  
- Svaka slika ima oznaku emocije (0–6) koja odgovara jednoj od sedam kategorija:  
  - 😠 **Ljutnja**  
  - 🤢 **Gađenje**  
  - 😨 **Strah**  
  - 🙂 **Sreća**  
  - 😞 **Tuga**  
  - 😲 **Iznenađenje**  
  - 😐 **Neutralno**  
- Podaci su organizirani u CSV datoteci s tri stupca:  
  - `emotion` — oznaka emocije (0–6)  
  - `pixels` — niz vrijednosti piksela slike  
  - `Usage` — oznaka je li slika dio train, validation ili test skupa  

---

## ⚙️ Metodologija i pristup
1. **Učitavanje i obrada podataka**  
   - Parsiranje `pixels` polja u 48×48 slike  
   - Normalizacija vrijednosti piksela (0–1)  
   - One-hot encoding emocija  

2. **Izgradnja i treniranje modela**  
   - Jednostavna **neuronska mreža (CNN)** koja uči prepoznati obrasce lica  

3. **Evaluacija performansi**  
   - Graf točnosti i gubitka kroz epohe  
   - Matrica konfuzije za analizu pogrešaka  

4. **Predikcija novih slika**  
   - Testiranje modela na slikama koje nisu bile u skupu za treniranje  

5. **(Opcionalno)** Real-time prepoznavanje emocija pomoću web kamere  
   - Pomoću `OpenCV` biblioteke  

## 👤 Student Information

- **Student Name**: Srđan Machiedo
- **GitHub**: @Machiedo81
