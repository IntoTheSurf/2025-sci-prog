# SiteSecGym

**SiteSecGym** — playground web za testiranje agenata (LLM-ovi, browser automation agenti, RL-agenti) protiv malicioznih i rizičnih web elemenata i ponašanja.

---

## Uvod i predstavljanje problema

Ggenerativni modeli i agenti sve češće surađuju s web‑sadržajem: čitaju stranice, klikaju na linkove, ispunjavaju obrasce i autonomno obavljaju zadatke. Međutim neke web stranice često sadrže zlonamjerne elemente — poput prompt-injekcija, lažnih formi ili skripti koje pokušavaju prikupiti podatke. Takvi elementi mogu dovesti do kompromitacije povjerljivih informacija ili neispravnog izvršavanja zadataka.

Cilj SiteSecGym‑a je stvoriti kontrolirano okruženje u kojem se mogu reproducirati i pratiti ovakve situacije, omogućujući sigurno testiranje i evaluaciju agenata.

* izložiti agente širokom spektru statičkih i dinamičkih web prijetnji;
* prikupiti telemetriju njihovog ponašanja;
* automatski evaluirati sigurnost i robusnost putem verifikatora;
* proizvesti dataset koji se može koristiti za treniranje, testiranje i nagrađivanje sigurnih agenata.

## Naša hipoteza

* Agenti izloženi različitim malicioznim elementima web stranica pokazat će različite razine rizika, a reprodukcijom scenarija moguće je pouzdano kvantificirati i usporediti njihovu sklonost riziku.

## Podaci i prikupljanje

* Događaji (Events): klikovi, submit forme, mrežni zahtjevi...

* Rezultati verifikatora: pass/warn/fail s evidencijom događaja.

* Telemetrija se prikuplja sa klijent-side i šalje backendu za analizu i generiranje dataset-a.

## Metrike i evaluacija

* **Outcome**: PASS / WARN / FAIL
* **Risk score** [0..1] — ponderirana suma verifier delta‑scoreova