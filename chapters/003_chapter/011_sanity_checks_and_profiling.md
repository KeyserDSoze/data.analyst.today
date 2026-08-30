## 3.10 Sanity check e data profiling: prima di credere al dataset, interrogalo

Prima di fare analisi sofisticate conviene eseguire controlli semplici.

Sono spesso proprio questi controlli a scoprire gli errori più costosi.

### Un set minimo di sanity check

Per quasi ogni dataset dovremmo conoscere almeno:

- numero di righe;
- numero di colonne;
- intervallo temporale coperto;
- cardinalità delle chiavi principali;
- percentuale di valori mancanti;
- distribuzione delle categorie principali;
- minimo, massimo, media e quantili delle variabili numeriche;
- presenza di valori impossibili;
- duplicati;
- variazioni improvvise nel volume dei dati.

### Caso studio simulato — Il mese con 31 giorni e mezzo

**VerdeMare Energy**, azienda che gestisce impianti fotovoltaici, riceve ogni notte le letture dei contatori.

Un analista deve calcolare la produzione media giornaliera di luglio.

Il dataset contiene 46 milioni di letture. Nulla sembra fuori posto.

Prima di iniziare l'analisi, l'analista aggrega semplicemente il numero di record per giorno.

Per quasi tutto il mese il volume oscilla attorno a 1,48 milioni di righe al giorno.

Il 18 luglio compaiono invece 2,96 milioni di righe.

Esattamente il doppio.

Non serve ancora un modello statistico.

Un semplice conteggio ha rivelato che l'intera giornata è stata caricata due volte dopo un recovery del sistema di ingestion.

Se l'analista avesse iniziato direttamente con medie e trend, avrebbe sovrappesato quella giornata.

### Profiling numerico

In Python:

```python
print(df.shape)
print(df.dtypes)
print(df.isna().mean().sort_values(ascending=False))
print(df.describe(include="all").T)
```

In SQL:

```sql
SELECT
    MIN(event_time) AS min_time,
    MAX(event_time) AS max_time,
    COUNT(*) AS rows,
    COUNT(DISTINCT event_id) AS events
FROM readings;
```

Questi comandi non costituiscono un'analisi completa.

Sono un'ispezione iniziale.

### Profiling categoriale

Per ogni variabile categorica chiediamoci:

- quante categorie esistono?
- ci sono categorie quasi identiche?
- esistono categorie inattese?
- una categoria domina quasi tutto il dataset?
- la distribuzione cambia bruscamente nel tempo?

Un campo `country` con questi valori:

```text
IT
ITA
Italy
Italia
italy
NULL
```

non è solo un problema estetico.

Può produrre segmentazioni sbagliate.

### Profiling temporale

Il tempo merita controlli specifici:

- giorni mancanti;
- ore mancanti;
- salti improvvisi nel volume;
- timestamp futuri;
- timezone incoerenti;
- ritardi di caricamento;
- backfill storici.

Un dataset può essere perfettamente pulito riga per riga e comunque essere incompleto come serie temporale.

### La regola dei cinque minuti

Prima di un'analisi complessa, dedica qualche minuto a domande molto semplici:

> Quante righe ho? Quante ne dovrei avere? Da quando a quando? Quali valori dominano? Cosa è palesemente strano?

Spesso questi cinque minuti valgono più di un'ora di modellazione.