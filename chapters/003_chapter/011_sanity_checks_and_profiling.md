## 3.10 Sanity check e data profiling: prima di descrivere il business, descrivi il dataset

Prima di cercare pattern sofisticati conviene costruire una fotografia elementare del dato.

Non perché i controlli semplici siano "junior", ma perché molte anomalie costose diventano evidenti proprio quando confrontiamo ciò che **abbiamo** con ciò che **ci aspettiamo**.

### Il profiling non è `describe()`

Un comando che produce minimi, massimi e medie è utile, ma non basta.

Il vero data profiling cerca di rispondere a cinque domande:

1. **quanto dato abbiamo?**
2. **quale periodo e popolazione copre?**
3. **quali valori e categorie contiene?**
4. **quali proprietà dovrebbero essere vere?**
5. **dove il comportamento cambia rispetto al normale?**

La quinta domanda è quella che trasforma un riepilogo in un controllo analitico.

### Un set minimo di controlli

Per quasi ogni dataset dovremmo conoscere almeno:

- numero di righe;
- cardinalità delle chiavi principali;
- intervallo temporale;
- numero di record per giorno/settimana/mese;
- missing rate dei campi critici;
- distribuzione delle categorie principali;
- minimi, massimi e quantili delle misure;
- presenza di valori fuori dominio;
- duplicati al grain atteso;
- record orfani rispetto alle relazioni principali;
- freshness e ultimo timestamp disponibile.

Ma ogni valore ha bisogno di una baseline.

`2.000.000 righe` non ci dice se il dataset è completo. Se ieri ne avevamo 2,4 milioni e il business è stabile, la differenza è una pista.

### Caso simulato/composito — Il giorno con il doppio delle letture

**VerdeMare Energy** gestisce impianti fotovoltaici e riceve ogni notte le letture dei contatori.

Un analista deve calcolare la produzione media giornaliera di luglio.

Il dataset contiene circa 46 milioni di letture e nessun errore evidente a livello di schema.

Prima dell'analisi, l'analista conta i record per giorno.

Per quasi tutto il mese il volume oscilla attorno a **1,48 milioni** di righe giornaliere.

Il 18 luglio ne compaiono **2,96 milioni**.

Esattamente il doppio.

L'indagine mostra che, dopo un recovery, una giornata di dati è stata caricata due volte.

Non serviva un algoritmo di anomaly detection. Bastava conoscere il volume atteso.

### Profilare per dimensione, non soltanto in aggregato

Una media complessiva può nascondere un difetto localizzato.

Esempio:

```text
missing_rate(delivery_date) = 4,8%
```

Può sembrare accettabile.

Poi segmentiamo per carrier:

```text
Carrier A: 0,7%
Carrier B: 1,1%
Carrier C: 19,4%
```

La domanda cambia da "abbiamo un po' di missing" a "cosa succede nell'integrazione del Carrier C?".

Profilare significa quindi osservare le proprietà del dato lungo le dimensioni in cui il processo potrebbe comportarsi diversamente.

### Profiling temporale

Il tempo merita controlli propri:

- giorni o ore mancanti;
- volumi che cambiano improvvisamente;
- timestamp futuri;
- cambio di timezone;
- ritardi di caricamento;
- backfill;
- cambi di schema o di categoria che iniziano da una data precisa.

Un dataset può essere perfettamente valido riga per riga e incompleto come storia.

### Profiling categoriale

Per ogni campo categorico chiediamo:

- quante categorie esistono?
- quali sono le più frequenti?
- sono comparse categorie nuove?
- alcune categorie sono scomparse?
- esistono quasi-sinonimi?
- la distribuzione cambia bruscamente dopo una release?

Un `country` che contiene:

```text
IT
ITA
Italy
Italia
italy
NULL
```

non è solo "sporco". Potrebbe indicare che più sistemi producono lo stesso concetto con standard differenti.

### Dall'osservazione all'invariante

I controlli migliori derivano da aspettative esplicite.

Esempi:

- un ordine dovrebbe avere almeno una riga d'ordine;
- il numero di account non dovrebbe diminuire del 20% in una notte senza un evento noto;
- la valuta di una transazione deve appartenere a un insieme previsto;
- il volume giornaliero dovrebbe restare entro un intervallo plausibile rispetto allo storico;
- la data massima dovrebbe essere compatibile con la SLA di aggiornamento.

Queste aspettative diventeranno, quando serve, controlli automatici nella sezione 3.15.

### La regola dei primi minuti

Prima di un'analisi complessa, prova a rispondere rapidamente:

> **Quante righe ho? Quante dovrei averne? Da quando a quando? Quali chiavi dovrebbero essere uniche? Dove manca il dato? Quali categorie dominano? Che cosa è cambiato recentemente?**

Il profiling non serve a dimostrare che il dataset sia corretto.

Serve a trovare abbastanza rapidamente i motivi per cui potrebbe non esserlo.