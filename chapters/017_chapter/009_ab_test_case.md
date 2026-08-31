## 17.8 A/B test: quando il risultato “positivo” non basta
Un esperimento ben progettato non risponde soltanto alla domanda:

> “La variante B ha performato meglio?”

Risponde a una domanda più utile:

> “Abbiamo evidenza sufficiente per cambiare il comportamento del sistema o del business?”

## Caso composito: VelaPay checkout

VelaPay introduce un nuovo checkout semplificato.

Obiettivo: aumentare la conversione pagamento completato.

Dopo 14 giorni:

- controllo: 71,4%;
- variante: 72,3%;
- uplift assoluto: +0,9 pp;
- p-value: 0,018.

Il messaggio superficiale sarebbe:

> “Test vinto, rollout.”

Ma l'analista verifica i guardrail.

Scopre che:

- payment authorization rate è stabile;
- chargeback rate cresce da 0,42% a 0,57%;
- customer support contacts aumentano del 6%;
- su Android low-end la conversione peggiora di 1,8 pp;
- il campione mostra una lieve ma significativa anomalia di allocazione per una versione obsoleta dell'SDK.

## Il risultato principale non è tutta la decisione

L'esperimento ha un effetto positivo sul primary metric, ma presenta tre questioni:

1. integrità dell'esperimento;
2. effetti collaterali;
3. eterogeneità tra segmenti.

Il team decide di non fare rollout globale.

Prima corregge l'allocazione, ripete una fase limitata e introduce un guardrail economico:

**incremental gross profit per 1.000 checkout**, includendo chargeback e costo supporto.

Il secondo test mostra uplift più piccolo ma stabile e nessun peggioramento dei guardrail.

La decisione diventa rollout progressivo con monitoraggio.

## L'errore possibile: confondere significatività con valore

Un effetto può essere statisticamente rilevabile e business-irrilevante.

Viceversa, un effetto economicamente importante può non raggiungere una soglia convenzionale se il test è sottodimensionato.

La decisione richiede almeno:

- effect size;
- intervallo di confidenza;
- costo/beneficio;
- guardrail;
- qualità della randomizzazione;
- durata e novelty effects;
- segmenti critici;
- reversibilità del rollout.

## Dal test alla politica di rollout

VelaPay definisce tre fasi:

1. 10% utenti, osservazione 72 ore;
2. 50%, controllo di chargeback e latency;
3. 100% solo se i guardrail restano entro soglia.

L'esperimento quindi non finisce con una tabella statistica.

Finisce quando il risultato è tradotto in una politica operativa sicura.

> **Un A/B test non produce una decisione. Produce evidenza per una decisione.**
