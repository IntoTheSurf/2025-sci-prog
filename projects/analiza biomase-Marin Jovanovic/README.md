# 🌊 Analiza biomase i bioraznolikosti u područjima različitog ribolovnog pritiska  
### _Projekt znanstvenog programiranja_

---

## 🔍 Opis projekta

Ovaj projekt temelji se na podacima dobivenima od **Instituta za oceanografiju i ribarstvo**.  
Podaci obuhvaćaju rezultate **istraživanja komercijalnog ribolova ramponom**, koji je proveden na više postaja u područjima gdje je **ribolov dozvoljen** i gdje je **zabranjen**.  
Svrha projekta je analizirati **razlike u biomasi**, **strukturi zajednica** i **odnosima između vrsta**, kako bismo bolje razumjeli ekološke procese koji oblikuju ta staništa.

Projekt kombinira analitički i vizualni pristup podacima kako bi se procijenio utjecaj ribolovnog pritiska na cjelokupni morski sustav te istražila povezanost bioloških i okolišnih čimbenika.

---

## 🎯 Ciljevi projekta

1. **Usporediti biomasu** između područja gdje je ribolov **dozvoljen** i gdje je **zabranjen**.  
2. Analizirati **kako razlike u biomasi** utječu na **strukturu i stabilnost ekosustava**.  
3. Istražiti **korelacije između dubine i zastupljenosti pojedinih vrsta**, kako bismo razumjeli prostornu raspodjelu zajednica.  
4. Ispitati **međusobne korelacije između različitih vrsta** i njihovih veličina — primjerice, postoji li povezanost između pojave određene vrste i smanjenja druge.  
5. Analizirati **povezanost veličine jedinki** s područjem ulova te istražiti kako se veličina mijenja s dubinom i zonom ribolova.  
6. Primijeniti **statističke metode i ekološke formule** kako bi se što preciznije opisala zastupljenost i dinamika vrsta.  
7. Vizualizirati rezultate u obliku **grafova, mreža korelacija i prostornih karata**.  
8. Ukoliko podaci to omogućuju, pokušati razviti **model koji opisuje razmnožavanje i održivost populacija**, čime bi se mogla procijeniti **održivost ribolova** na analiziranom području.

---

## 📊 Podaci i varijable

Podaci Instituta sadrže:
- informacije o **svakom potezu ribolova** (datum, vrijeme početka i kraja, lokacija, dubina, brzina, broj rampona),
- **vrste i količine ulova** izražene u kilogramima,
- **zone ribolova** (dozvoljena / zabranjena),
- **duljine i veličine jedinki**,
- **dodatne okolišne parametre** poput temperature, saliniteta i tipa podloge (potrebno pronaći).

Ti podaci omogućuju detaljnu **analizu odnosa između bioloških i okolišnih čimbenika**, što je ključno za razumijevanje strukture morskih zajednica.

---

## 🧮 Plan analize

1. **Učitavanje i priprema podataka**  
   - Čišćenje i standardizacija tablica  
   - Izračun izvedenih varijabli (trajanje poteza, površina zahvata, biomasa po km²)  
   - Oznaka područja prema statusu ribolova  

2. **Analiza biomase i bioraznolikosti**  
   - Izračun ukupne i prosječne biomase po postaji i zoni  
   - Izrada grafova koji prikazuju razlike između dozvoljenih i zabranjenih zona  
   - Usporedba brojnosti i udjela vrsta  

3. **Korelacijska analiza**  
   - Korelacija između dubine i zastupljenosti vrsta  
   - Korelacija između veličina jedinki i područja ulova  
   - Korelacija između samih vrsta (npr. prisutnost grabežljivih vs. plijenskih vrsta)  

4. **Vizualizacija podataka**  
   - Grafovi raspodjele biomase  
   - Mreže korelacija između vrsta  
   - Karte koje prikazuju biomase i bioraznolikost po lokacijama  

5. **Modeliranje (ako je moguće)**  
   - Razviti pojednostavljeni model koji opisuje **razmnožavanje i održivost populacija**  
   - Procijeniti **koliko je postojeći ribolovni napor održiv** kroz vremensku dinamiku populacija  

6. **Zaključci i interpretacija**  
   - Uočavanje prostorno-vremenskih obrazaca  
   - Preporuke za **održivo upravljanje ribolovom**  

---

## 🧭 Dijagram tijeka projekta

```mermaid
graph TD
A["Data loading (Institute of Oceanography)"] --> B["Data cleaning and preparation"]
B --> C["Biomass and biodiversity index calculation"]
C --> D["Comparison of fishing zones (allowed vs forbidden)"]
D --> E["Correlation analysis (depth, species, size)"]
E --> F["Visualization (maps and graphs)"]
F --> G["Sustainability and reproduction model"]
G --> H["Conclusions and management recommendations"]
