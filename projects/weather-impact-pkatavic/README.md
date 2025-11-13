🌦️ Utjecaj vremenskih uvjeta na vanjske čimbenike – Predikcija neintuitivnih varijabli
🧠 Uvod i problem

Cilj ovog projekta je istražiti postoji li mjerljiva povezanost između vremenskih uvjeta i drugih vanjskih čimbenika koji na prvi pogled nisu intuitivno povezani s vremenom – poput kvalitete zraka (PM2.5) ili turističke aktivnosti (npr. broj dostupnih smještaja, cijene noćenja).
Hipoteza je da se promjene vremenskih uvjeta (temperatura, vlažnost, vjetar, tlak) mogu koristiti za predikciju određenih obrazaca u ponašanju tih vanjskih varijabli.

🎯 Hipoteza

H0 (nul hipoteza): vremenski uvjeti nemaju značajan utjecaj na razinu zagađenja zraka ili turističku aktivnost.

H1 (alternativna hipoteza): vremenski uvjeti imaju mjerljiv i predvidiv utjecaj na barem jedan vanjski čimbenik.

📊 Opis podataka

Podaci će se prikupljati iz sljedećih izvora:

    Meteorološki podaci: preuzeti putem Meteostat
    API-ja (temperatura, vlaga, tlak, vjetar).

    Podaci o zagađenju zraka: preuzeti s aqicn.org
    ili otvorenih postaja (npr. Split – Brda, Zagreb – Maksimir).

    Turistički podaci (ako se koristi): moguće scrapati s booking.com
    ili [airbnb.com] pomoću BeautifulSoup.

Nakon prikupljanja, podaci će se očistiti i standardizirati pomoću pandas, te spojiti prema datumu i lokaciji.

🧮 Metodologija

1. Scraping i obrada podataka

    Scrapanje podataka o vanjskim čimbenicima (turizam ili zagađenje zraka).

    Dohvat vremenskih podataka pomoću API-ja.

    Spajanje datasetova, čišćenje, popunjavanje nedostajućih vrijednosti.

2. Analiza i vizualizacija

    Analiza korelacija i odnosa između vremenskih varijabli i ciljne varijable.

    Vizualizacija pomoću matplotlib i plotly (scatter, heatmap, time series).

3. Modeliranje

    Treniranje modela (npr. RandomForestRegressor, XGBoost).

    Procjena performansi (R², MAE, RMSE).

    Usporedba rezultata različitih modela.

4. Interpretacija rezultata

    Koje vremenske varijable najviše utječu na ciljnu?

    Može li se ciljna varijabla predvidjeti s razumnom točnošću?