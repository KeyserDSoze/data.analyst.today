## 5.17 Significatività statistica e materialità: l'effetto deve essere abbastanza grande da contare

Arrivati a questo punto possiamo separare con precisione due domande che nel lavoro quotidiano vengono spesso fuse.

La prima è inferenziale: **quanto precisamente conosciamo l'effetto e quanto i dati sono compatibili con lo scenario di riferimento?**

La seconda è decisionale: **l'effetto è abbastanza grande da cambiare ciò che conviene fare?**

La statistica può rispondere molto bene alla prima e non contenere quasi nulla della seconda. Confondere i due livelli produce errori speculari: implementare effetti minuscoli soltanto perché il p-value è piccolo oppure ignorare effetti potenzialmente importanti perché, con pochi dati, non sono ancora stimati con precisione.

## Una campagna “vincente” che non paga il proprio costo

Una catena retail invia una nuova sequenza CRM a **2,8 milioni di clienti**. Il repeat purchase rate a 30 giorni passa dal 18,42% al 18,55%, quindi il delta è **+0,13 punti percentuali**.

Con una base così ampia il segnale può essere stimato con grande precisione. Il team marketing propone il rollout.

La nuova sequenza costa però 0,09 € in più per cliente tra piattaforma, messaggistica e incentivo. Il margine incrementale prodotto dagli acquisti aggiuntivi non copre quel costo.

Non c'è contraddizione. La statistica ha rilevato una differenza reale o comunque ben stimata rispetto al modello; l'economia ha stabilito che **quella dimensione dell'effetto non crea valore**.

> **Significativo non significa sufficiente.**

## Effect size prima della storia

Un risultato dovrebbe essere tradotto in unità che il business può leggere. Se la conversione passa da 4,20% a 4,44%, abbiamo:

- delta assoluto: **+0,24 pp**;
- delta relativo: **+5,7%**.

Entrambe le formulazioni sono corrette. La prima rende visibile la differenza sulla scala originale; la seconda la rapporta alla baseline. Nessuna delle due, da sola, ci dice ancora quanto valore economico produca.

La traduzione successiva deve arrivare a conversioni incrementali, revenue, contribution margin, costi operativi e guardrail. È lì che l'effect size diventa una quantità decisionale.

## La soglia business è spesso più utile dello zero

Prima di raccogliere dati è utile definire il più piccolo effetto che renderebbe ragionevole cambiare comportamento. Possiamo chiamarlo **Minimum Business-Relevant Effect** o, in termini più generali, *minimum effect of interest*.

Supponiamo che un nuovo sistema costi 600.000 € l'anno e raggiunga il break-even soltanto sopra **+0,18 pp di conversione**. Se stimiamo:

`+0,24 pp [CI 95%: +0,07 ; +0,41]`

la lettura interessante non è soltanto che l'intervallo sia sopra zero per una parte importante del suo range. L'effetto centrale supera il break-even, ma l'intervallo contiene anche scenari sotto +0,18 pp. La decisione economica è quindi promettente e, nello stesso tempo, ancora esposta a un'incertezza materialmente rilevante.

Questa frase contiene più informazione di “p = 0,012, significativo”.

## MDE e soglia business devono parlarsi

Il **Minimum Detectable Effect**, o MDE, appartiene al disegno statistico: indica l'ordine di grandezza dell'effetto che un test è progettato per riuscire a distinguere con una certa potenza sotto le assunzioni adottate.

La soglia business appartiene invece alla decisione: indica quale effetto merita davvero un'azione.

Idealmente i due livelli sono coerenti. Se il business non agirebbe sotto +0,5 pp, un esperimento enorme progettato per distinguere +0,03 pp rischia di essere una macchina costosa per scoprire effetti irrilevanti. Il Capitolo 9 renderà operativa questa relazione attraverso MDE, power, sample size e durata.

## La stessa effect size può valere cose diverse

Un'azienda logistica testa un algoritmo di routing su 420.000 consegne. Il tempo medio passa da 41,8 a 41,5 ore: **18 minuti** di miglioramento, stimati con grande precisione.

Se l'algoritmo costa 0,47 € in più per spedizione e non modifica metriche customer-facing, i 18 minuti possono non giustificare il rollout. Se invece proprio quei 18 minuti spostano migliaia di consegne sotto una soglia SLA molto costosa, la stessa differenza può generare enorme valore.

L'importanza non vive nell'unità statistica. Vive nel meccanismo economico e operativo che collega l'effetto alla decisione.

Per questo la seguente matrice è un vero artefatto decisionale, non un riepilogo decorativo:

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

L'ASA ricorda esplicitamente che il p-value non misura né la dimensione dell'effetto né l'importanza pratica del risultato.[^asa-business]

Una conclusione professionale può quindi assumere questa forma:

> **Stimiamo un miglioramento di +0,24 pp, CI 95% +0,07/+0,41. Il break-even è +0,18 pp. L'effetto centrale è economicamente interessante, ma l'intervallo include scenari sotto soglia; la decisione dipende dal costo dell'attesa, dalla reversibilità e dai guardrail.**

La frase non nasconde l'incertezza e non rinuncia alla decisione. Usa l'incertezza per calibrare la decisione.

> **La statistica ci dice quanto bene conosciamo l'effetto. Il business stabilisce quanto grande deve essere l'effetto per meritare un'azione.**

---

### Fonte

[^asa-business]: American Statistical Association, *Statement on Statistical Significance and P-Values*. https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
