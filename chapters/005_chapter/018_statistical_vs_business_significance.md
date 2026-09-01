## 5.17 Significatività statistica e materialità: l'effetto deve essere grande abbastanza da contare

Una delle competenze più importanti di un Data Analyst è tenere separate due domande:

1. **Quanto è precisa e convincente l'evidenza statistica rispetto al modello?**
2. **L'effetto è abbastanza grande da cambiare una decisione reale?**

La prima riguarda l'inferenza.

La seconda riguarda economia, operazioni, strategia e vincoli.

Confonderle produce due errori opposti:

- implementare effetti minuscoli soltanto perché il p-value è piccolo;
- ignorare effetti potenzialmente importanti soltanto perché il campione non è ancora abbastanza preciso.

### Caso simulato/composito — Una campagna CRM “vincente” che non paga il proprio costo

Una catena retail invia una nuova sequenza CRM a 2,8 milioni di clienti.

Il repeat purchase rate a 30 giorni passa:

- controllo: 18,42%;
- nuova sequenza: 18,55%;
- delta: **+0,13 punti percentuali**.

Con una base così ampia il segnale può essere stimato con grande precisione.

Il team marketing propone il rollout.

Ma la nuova sequenza costa 0,09 € in più per cliente tra piattaforma, messaggistica e incentivo. Il margine incrementale prodotto dagli acquisti aggiuntivi non copre quel costo.

La statistica ha rilevato una differenza.

L'economia ha stabilito che, a quella dimensione, la differenza non crea valore.

> **Significativo non significa sufficiente.**

### Effect size: quanto cambia realmente il fenomeno?

Quando riportiamo un risultato dobbiamo mostrare la dimensione dell'effetto in unità comprensibili.

Esempio:

- conversione: 4,20% → 4,44%;
- delta assoluto: **+0,24 pp**;
- delta relativo: **+5,7%**.

Dire soltanto “+5,7%” rende il cambiamento più impressionante. Dire soltanto “+0,24 pp” può nascondere il valore su una base enorme.

Una comunicazione corretta può mostrare entrambi e poi tradurli in:

- conversioni incrementali;
- revenue;
- contribution margin;
- costo operativo;
- eventuali effetti sui guardrail.

### Minimum Business-Relevant Effect

Prima di raccogliere i dati è utile definire una soglia del tipo:

> **Qual è il più piccolo effetto che renderebbe ragionevole cambiare comportamento?**

Possiamo chiamarlo **Minimum Business-Relevant Effect**, o più genericamente *minimum effect of interest*.

Esempio:

Un nuovo sistema costa 600.000 € l'anno. Sotto +0,18 punti percentuali di conversione non raggiunge il break-even atteso.

La soglia `+0,18 pp` diventa quindi molto più informativa dello zero statistico.

Se l'intervallo stimato è:

`+0,24 pp [CI 95%: +0,07 ; +0,41]`

abbiamo una situazione interessante:

- l'effetto stimato supera il break-even;
- l'intervallo include anche valori sotto il break-even;
- i dati non rendono ancora completamente robusta la decisione economica.

Questa è una lettura molto più utile di:

> “p = 0,012, significativo”.

### MDE e soglia business non sono la stessa cosa

Nei test incontreremo spesso il **Minimum Detectable Effect (MDE)**.

È una proprietà del disegno statistico: quale effetto il test è pianificato per riuscire a rilevare con una certa potenza, date le assunzioni.

La soglia business risponde invece a:

> **Quale effetto ci interessa davvero?**

Idealmente il disegno deve essere costruito in modo coerente con la decisione.

Se il business non agirebbe sotto +0,5 pp, un test enorme progettato per rilevare +0,03 pp può trasformarsi in una macchina costosa per scoprire effetti irrilevanti.

Il Capitolo 9 renderà operativa questa relazione tra MDE, power, sample size e durata.

### Caso simulato/composito — Diciotto minuti statisticamente credibili

Un'azienda logistica testa un algoritmo di routing su 420.000 consegne.

- controllo: 41,8 ore;
- nuova logica: 41,5 ore;
- differenza: -0,3 ore = **18 minuti**.

La stima è molto precisa.

Ma l'algoritmo aumenta il costo di 0,47 € per spedizione e non produce differenze osservabili nelle metriche customer-facing rilevanti.

Il risultato può essere reale e ancora non meritare rollout.

Al contrario, se quei 18 minuti riducessero sistematicamente il numero di consegne oltre una soglia SLA molto costosa, la stessa effect size potrebbe avere enorme valore.

Il valore non vive nell'unità statistica. Vive nel **meccanismo decisionale**.

### La matrice che dovrebbe accompagnare ogni effetto

| Elemento | Domanda |
|---|---|
| Effect size | Quanto cambia? |
| Confidence interval | Quanto è precisa la stima? |
| Baseline | Rispetto a quale livello? |
| Soglia business | Quanto dovrebbe cambiare per contare? |
| Volumi | Quante unità economiche coinvolge? |
| Costi | Quanto costa ottenere l'effetto? |
| Guardrail | Che cosa peggiora altrove? |
| Reversibilità | Quanto costa sbagliare rollout? |

L'ASA ricorda esplicitamente che il p-value non misura la dimensione dell'effetto né l'importanza pratica del risultato.[^asa-business]

Per questo una frase professionale dovrebbe assomigliare a:

> **“Stimiamo un miglioramento di +0,24 pp, CI 95% +0,07/+0,41. Il break-even è +0,18 pp. L'effetto medio stimato è economicamente interessante, ma l'intervallo include anche scenari sotto la soglia: la decisione dipende dal costo dell'attesa, dalla reversibilità e dagli altri guardrail.”**

Questa frase non nasconde l'incertezza e non rinuncia alla decisione.

> **La statistica ci dice quanto bene conosciamo l'effetto. Il business decide quanto grande deve essere l'effetto per meritare un'azione.**

[^asa-business]: American Statistical Association, *Statement on Statistical Significance and P-Values*: https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
