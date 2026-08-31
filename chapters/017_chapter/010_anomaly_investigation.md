## 17.9 Anomaly investigation: l'allarme non è la spiegazione
Un sistema di anomaly detection può dirci che qualcosa è insolito.

Non può, da solo, dirci perché sia successo.

## Caso composito: Atlas Streaming

Atlas gestisce una piattaforma video in abbonamento.

Alle 09:12 il monitoring segnala un'anomalia:

**trial-to-paid conversion -17% rispetto al baseline atteso.**

L'incidente viene classificato come high severity perché la metrica impatta direttamente ricavi futuri.

### Prima ipotesi: problema di pagamento

Il team controlla:

- authorization rate;
- payment provider errors;
- latency;
- decline codes.

Nessun segnale anomalo.

### Seconda ipotesi: tracking

Il numero di eventi `subscription_started` è diminuito, ma anche la fatturazione mostra un calo reale.

Quindi non è solo telemetry.

### Terza ipotesi: mix geografico

Il calo è concentrato in tre paesi.

Una nuova campagna partnership ha generato un forte aumento dei trial proprio in quei mercati.

Gli utenti entrano con un'offerta di 30 giorni invece dei 7 giorni standard.

La metrica “trial-to-paid entro 14 giorni” li classifica inevitabilmente come non convertiti.

## L'anomalia era reale per il KPI, ma non per il fenomeno economico

Il sistema aveva correttamente rilevato un cambiamento nella metrica.

Ma il significato della metrica era cambiato perché il processo commerciale aveva introdotto una nuova durata del trial.

Il problema non era conversione.

Era **semantic drift**.

## L'errore possibile: trattare ogni alert come un incidente operativo

Se il team avesse reagito bloccando la partnership o modificando il checkout, avrebbe agito su un falso problema.

Un buon playbook di anomaly investigation separa:

1. **data anomaly** — pipeline, tracking, duplicazioni, lateness;
2. **definition anomaly** — metrica non più coerente con il processo;
3. **mix anomaly** — cambia la popolazione;
4. **behavior anomaly** — cambia davvero il comportamento;
5. **system anomaly** — bug o performance;
6. **external shock** — mercato, festività, competitor, eventi esterni.

## Metodo operativo: dalla sirena alla diagnosi

Per ogni alert critico:

- verificare freschezza e completezza;
- riconciliare con una sorgente indipendente;
- decomporre per dimensioni rilevanti;
- controllare release ed eventi di business;
- verificare definizione e denominatore;
- cercare controesempi;
- stimare impatto economico reale;
- definire cosa falsificherebbe l'ipotesi principale.

> **Anomaly detection riduce il tempo necessario per accorgersi che qualcosa è cambiato. L'analisi serve a capire che cosa è cambiato davvero.**
