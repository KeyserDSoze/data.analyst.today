## 11.4 CTE e trasformazioni leggibili: rendere esplicito il percorso del dato

Una query complessa può essere tecnicamente corretta e tuttavia quasi impossibile da verificare.

Le Common Table Expressions, o CTE, non servono solo a “spezzare” SQL lungo. Servono a rendere leggibile il percorso analitico.

Un buon flusso può assomigliare a questo:

```text
raw events
→ filtro qualità
→ normalizzazione grain
→ arricchimento dimensioni
→ aggregazione intermedia
→ metrica finale
```

### Caso simulato — BrightCart e la conversione che cambiava ogni lunedì

BrightCart calcola la conversione settimanale con una query di circa 230 righe, piena di subquery annidate.

Ogni lunedì il numero differisce di qualche decimo di punto rispetto al dashboard del team Product.

Nessuno riesce a capire rapidamente perché.

La query viene riscritta in blocchi logici:

```sql
WITH eligible_sessions AS (...),
orders_deduped AS (...),
orders_by_session AS (...),
session_outcomes AS (...),
weekly_metrics AS (...)
SELECT *
FROM weekly_metrics;
```

Durante la riscrittura emerge il problema: le sessioni generate da bot venivano filtrate dopo il join con gli ordini. In alcuni casi il join moltiplicava già le righe prima del filtro.

La nuova struttura non è “più bella”. È più auditabile.

### Una CTE dovrebbe spesso avere un grain dichiarabile

Un buon test è riuscire a descrivere ogni blocco in una frase.

- `eligible_sessions`: una riga per sessione valida;
- `orders_by_session`: una riga per sessione con ordini aggregati;
- `session_outcomes`: una riga per sessione con flag di conversione;
- `weekly_metrics`: una riga per settimana e canale.

Se non sappiamo descrivere il grain di una CTE, probabilmente il blocco sta facendo troppe cose insieme.

### Trasformazioni idempotenti e riproducibili

Una trasformazione analitica dovrebbe produrre lo stesso risultato partendo dagli stessi input.

Questo sembra ovvio, ma query che dipendono da:

```sql
CURRENT_DATE
```

oppure da tabelle mutate retroattivamente possono cambiare risultato nel tempo senza che il codice sia cambiato.

Per analisi importanti è utile rendere espliciti:

- periodo di osservazione;
- timestamp di cut-off;
- versione della logica;
- fonti utilizzate.

### Dal notebook alla trasformazione condivisa

Molte analisi iniziano in una query ad hoc. Va bene.

Il problema nasce quando una logica diventa ricorrente e continua a vivere in cinque copie diverse:

- dashboard;
- notebook;
- foglio Excel;
- query Finance;
- query CRM.

A quel punto la trasformazione dovrebbe essere promossa verso un livello condiviso.

### Caso simulato — Atlas Mobility e cinque definizioni di “active rider”

Atlas Mobility scopre che Growth, Finance, Product e Operations riportano quattro numeri diversi per gli utenti attivi mensili.

Le definizioni sono:

1. almeno un login;
2. almeno una ricerca corsa;
3. almeno una corsa iniziata;
4. almeno una corsa completata.

Non esiste una query “più corretta” in assoluto. Esistono quattro concetti diversi chiamati con lo stesso nome.

La soluzione è creare metriche semanticamente distinte:

- `monthly_logged_in_users`;
- `monthly_trip_searchers`;
- `monthly_trip_starters`;
- `monthly_completed_riders`.

Poi il business può decidere quale usare per quale decisione.

> **Una trasformazione condivisa non elimina le ambiguità di business. Le rende visibili e governabili.**

### Pattern operativo

Quando una query cresce:

1. separare fonti raw e filtri qualità;
2. deduplicare prima dei join critici;
3. portare ogni blocco a un grain chiaro;
4. assegnare nomi che descrivano il significato, non la tecnica;
5. inserire controlli intermedi;
6. materializzare o promuovere la logica quando diventa riusabile.
