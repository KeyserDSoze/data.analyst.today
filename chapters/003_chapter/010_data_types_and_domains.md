## 3.9 Tipi, domini e unità: una colonna non è solo un contenitore

Una colonna possiede almeno quattro livelli di significato:

1. **tipo tecnico** — integer, decimal, string, date, boolean;
2. **dominio ammesso** — quali valori sono validi;
3. **unità di misura** — euro, dollari, secondi, chilometri, percentuali;
4. **significato di business** — che cosa rappresenta davvero il campo.

Un dataset può essere tecnicamente valido e semanticamente pericoloso se anche uno solo di questi livelli è implicito.

### Caso simulato/composito — Il CAP che perse gli zeri

**Mercurio Express** importa ogni notte un CSV con gli indirizzi dei clienti.

Il campo `postal_code` viene interpretato automaticamente come intero.

`00144` diventa `144`.

Il dato è ancora un numero perfettamente valido. Ma il CAP non è una quantità: è un codice. Non ha senso farne somme, medie o eliminare zeri iniziali.

La correzione tecnica è semplice. Il principio è più importante:

> **La rappresentazione tecnica deve seguire il significato del dato, non il contrario.**

Un identificatore composto solo da cifre può dover essere una stringa. Un importo richiede una valuta. Una durata richiede un'unità. Una percentuale deve chiarire se `0.12` significa 12% oppure 0,12%.

### Caso reale documentato — Mars Climate Orbiter

Il 23 settembre 1999 NASA perse il **Mars Climate Orbiter** durante l'arrivo su Marte.

La spiegazione ufficiale è diventata un caso classico di errore di interfaccia e semantica delle unità: un componente del software di terra produceva dati in unità inglesi mentre il sistema di navigazione li interpretava secondo le specifiche metriche. NASA descrive la causa come una mancata traduzione tra unità inglesi e metriche; il rapporto d'indagine specifica che dati che avrebbero dovuto essere espressi in newton-secondi furono forniti in pound-force seconds.[^nasa-mco][^nasa-mco-report]

Non era un problema di sintassi.

Il valore numerico esisteva. Il file veniva prodotto. Il software lo leggeva.

Era sbagliato il **significato attribuito al numero**.

Il caso è estremo, ma il principio è quotidiano nell'analytics:

- `weight = 80` — chilogrammi o libbre?
- `duration = 90` — secondi o minuti?
- `revenue = 1200` — euro o centesimi?
- `temperature = 70` — Celsius o Fahrenheit?
- `rate = 0.15` — frazione o punti percentuali?

Quando l'unità resta implicita, una pipeline può funzionare perfettamente e produrre una conclusione sbagliata.

### Tipi tecnici e rischi analitici

**Numeri interi e decimali**

Possono rappresentare quantità, importi, durate, codici o identificatori. Il fatto che una colonna sia numerica non significa che sia una misura.

**Stringhe**

Possono contenere categorie, codici, testo libero, JSON o numeri memorizzati male. La flessibilità del tipo stringa può nascondere molti problemi di standardizzazione.

**Date e timestamp**

Richiedono semantica temporale, timezone e precisione. `2026-09-01` può significare data locale, data contabile o data UTC trasformata.

**Boolean**

Un `is_active = true` sembra autoesplicativo, ma serve conoscere la regola e il momento con cui viene aggiornato.

**Categorie**

`IT`, `ITA`, `Italy` e `Italia` possono essere sinonimi, categorie prodotte da sistemi differenti o codici con significati specifici.

### Il dominio è una dichiarazione di ciò che può esistere

Esempi:

- `discount_pct`: tra 0 e 100 se memorizzato in punti percentuali;
- `currency`: codice appartenente all'elenco supportato;
- `order_status`: valori previsti dal workflow;
- `birth_date`: non futura;
- `quantity`: coerente con la semantica di vendita/resi;
- `country_code`: formato standard adottato dall'organizzazione.

Le regole di dominio sono preziose perché trasformano conoscenza tacita in condizioni verificabili.

### Valido non significa accurato

Un valore può rispettare perfettamente il dominio e descrivere male la realtà.

`country_code = IT` è valido se `IT` è ammesso. Ma può essere inaccurato se il cliente appartiene a un altro Paese.

Allo stesso modo una data può avere formato corretto ma riferirsi all'evento sbagliato.

Per questo dobbiamo tenere distinte **validità** e **accuratezza**.

### Scheda minima per una variabile critica

Per i campi da cui dipendono KPI o decisioni, documenta almeno:

```text
Campo:
Significato:
Tipo tecnico:
Unità:
Dominio:
Null ammesso:
Momento di validità:
Sistema sorgente:
Casi speciali:
```

È una piccola quantità di documentazione con un grande rendimento.

> **Un numero senza unità, dominio e significato non è ancora una misura. È soltanto un valore memorizzato.**

[^nasa-mco]: NASA Science, *Mars Climate Orbiter*. https://science.nasa.gov/mission/mars-climate-orbiter/
[^nasa-mco-report]: NASA, *Mars Climate Orbiter Mishap Investigation Board — Phase I Report*. https://discovery.larc.nasa.gov/discovery/PDF_FILES/MCO_report_2.pdf