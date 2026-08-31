# 0.2 Delegare l'esecuzione, non la responsabilità

L'AI rende possibile separare due cose che per molto tempo sono state quasi inseparabili:

- **fare materialmente il lavoro**;
- **essere responsabili del lavoro**.

Un analista può non scrivere personalmente una query e rimanere pienamente responsabile del numero che quella query produce.

Può non costruire a mano un modello e restare responsabile del modo in cui quel modello viene usato.

Può non preparare personalmente una presentazione e restare responsabile del messaggio consegnato al management.

Questa distinzione è fondamentale.

## Il falso dilemma: “o faccio tutto io o non controllo nulla”

Quando si parla di AI, emergono spesso due estremi.

### Estremo 1 — Rifiutare la delega

> “Se non scrivo io il codice, non mi fido.”

È una posizione destinata a diventare sempre meno sostenibile. Se l'AI può accelerare attività meccaniche, rifiutarla per principio significa rinunciare a capacità utile.

### Estremo 2 — Delegare anche il giudizio

> “Se il modello l'ha detto, sarà giusto.”

Questo è ancora più pericoloso.

La posizione professionale sta nel mezzo:

> **delegare ciò che può essere delegato, mantenendo controllo sulle assunzioni e sulla qualità dell'evidenza.**

## Caso realistico: il report del lunedì

Un'azienda B2B automatizza il weekly business review.

Ogni lunedì un agente:

1. estrae i KPI;
2. confronta con forecast e anno precedente;
3. identifica anomalie;
4. genera tre spiegazioni principali;
5. produce una slide con raccomandazioni.

Per otto settimane funziona bene.

Alla nona, l'agente segnala:

- pipeline coverage: +22%;
- expected bookings: +14%;
- raccomandazione: aumentare il target del trimestre.

Il VP Sales nota però qualcosa di strano: il numero di opportunità aperte non è cresciuto.

L'indagine scopre che una modifica CRM ha duplicato il valore di alcune opportunità multi-currency durante il consolidamento.

Il sistema non aveva “inventato” nulla. Aveva letto correttamente un dato sbagliato.

Se il team avesse risposto:

> “Il report è automatico.”

avrebbe dimostrato di aver confuso automazione con responsabilità.

## Accountability significa avere un owner

Ogni output importante dovrebbe avere un proprietario umano o organizzativo chiaro.

Non serve che quella persona faccia tutto.

Serve che sappia:

- quali sistemi contribuiscono all'output;
- quali metriche sono usate;
- quali controlli vengono eseguiti;
- quali failure mode sono noti;
- come si effettua rollback;
- chi viene coinvolto quando qualcosa non torna.

## Il principio “show me the evidence”

Quando un agente produce una conclusione importante, l'analista dovrebbe poter chiedere:

> “Mostrami l'evidenza.”

Non una spiegazione narrativa generata dopo il fatto, ma elementi verificabili:

- query;
- filtri;
- sorgenti;
- conteggi;
- controlli;
- grafici;
- confronti alternativi;
- risultati di test.

Un agente che dice “la Francia è il driver” dovrebbe essere in grado di mostrare come il delta è stato decomposto.

Un agente che dice “questa campagna ha causato un aumento” dovrebbe esplicitare il design causale, non solo una correlazione.

Un agente che dice “il modello è migliorato” dovrebbe mostrare split, baseline e metriche.

## La responsabilità non può essere automatizzata via disclaimer

Scrivere sotto un report:

> “Output generato dall'AI, verificare prima dell'uso.”

non risolve il problema se il report viene poi usato davvero per prendere decisioni.

Il disclaimer è utile per comunicare limiti, ma non sostituisce un processo di review.

## Una regola semplice

Più un'azione è:

- costosa;
- difficile da invertire;
- impattante su persone;
- legalmente o finanziariamente rilevante;
- visibile esternamente;

più la delega deve essere accompagnata da controlli e approvazione umana.

**La capacità dell'AI modifica chi esegue il lavoro. Non cancella la necessità di sapere chi ne risponde.**
