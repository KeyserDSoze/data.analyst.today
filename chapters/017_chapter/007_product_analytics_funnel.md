## 17.6 PulseNote — “Cosa si è rotto nell'onboarding?” Forse niente

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

PulseNote, SaaS freemium di collaborazione con **420.000 utenti attivi mensili**, vede l'activation dei nuovi account scendere dal **43% al 35%** in sei settimane. Il product manager chiede che cosa si sia rotto nell'onboarding. La formulazione sembra innocua, ma contiene già una causa: presume che il prodotto sia peggiorato.

Il failure cost non è soltanto fare un redesign inutile. È **ottimizzare una metrica che potrebbe non rappresentare più il valore creato dalla nuova popolazione**. Per questo la stop rule viene prima del funnel: **non ridisegnare il flow finché non sappiamo se il calo esiste a parità di popolazione e se la definizione di activation è ancora fit for purpose**.

### Il funnel localizza una perdita e rischia di farci innamorare del punto sbagliato

Il funnel aggregato sembra indicare un colpevole evidente:

| Step | Prima | Dopo | Delta |
|---|---:|---:|---:|
| Signup completato | 100% | 100% | — |
| Workspace creato | 82% | 80% | -2 pp |
| Primo invito inviato | 61% | 52% | -9 pp |
| Primo documento condiviso | 49% | 41% | -8 pp |
| Activation entro 7 giorni | 43% | 35% | -8 pp |

Il primo invito è il drop più visibile. Se il team trattasse il funnel come spiegazione, la soluzione sarebbe quasi automatica: riparare o spingere il flow `Invite`.

La Data Readiness Review, però, non trova rotture rilevanti nel tracking. Event coverage, duplicate/missing event e versioni sono stabili. Il cambiamento forte è nella **popolazione in ingresso**.

Prima della nuova campagna paid, gli account erano per il **68% aziendali e 32% individuali**. Dopo, il mix diventa **47% aziendali e 53% individuali**. Il segmento storico B2B mantiene un funnel quasi stabile; il calo aggregato è concentrato nei freelance e studenti portati dalla nuova acquisition policy.

Gli utenti individuali invitano meno persone per una ragione banale: spesso usano PulseNote da soli. La metrica non sta necessariamente rilevando una peggiore esperienza. Sta applicando una vecchia definizione di valore a una popolazione nuova.

### La formula non è cambiata; il significato sì

L'activation ufficiale richiede:

> workspace creato + almeno un invito + almeno un documento condiviso entro sette giorni.

Questa definizione aveva senso quando il prodotto era quasi interamente collaborativo. Con un use case single-player emergente, può confondere **mancata creazione di valore** e **creazione di valore lungo un percorso diverso**.

Il routing cambia quindi prima di qualsiasi redesign. La domanda non è più “come aumentiamo gli inviti?”, ma **quali comportamenti precoci rappresentano valore e anticipano retention nei diversi use case?**

Il Lifecycle Diagnostic Map identifica due percorsi candidati. Nel percorso collaborativo restano workspace → invito → documento condiviso → ritorno di almeno due membri. Nel percorso individuale emerge workspace → almeno tre note → uso in almeno tre giorni distinti → ritorno entro sette giorni. Nel segmento individuale il secondo pattern è molto più associato alla retention a 30 giorni dell'invio di un invito.

Questo finding non dimostra che “tre note causano retention”. Dimostra qualcosa di sufficiente per la prima decisione: **l'attuale KPI di activation non misura bene il nuovo percorso di valore**.

### Qui è professionale fermare la diagnosi e cambiare la domanda

A questo punto non serve un churn model e non serve un Causal Identification Brief per dichiarare la metrica semanticamente obsoleta. Il team ha già evidence sufficiente per non ottimizzare il bottone `Invite` come se rappresentasse il problema.

Restano però tre ipotesi economicamente diverse. Il nuovo traffico può essere di bassa qualità; può creare valore attraverso un percorso differente; oppure può rappresentare un vero use case single-player che merita onboarding e packaging specifici. Per distinguerle servono retention 30/60 giorni, paid conversion, CAC/payback, feature adoption, support/contact rate e cohort economics.

Solo quando il team decide di **cambiare il prodotto** entra l'Experiment Contract. La variante standard mantiene l'onboarding collaborativo; la variante alternativa consente di scegliere `uso individuale` o `uso con team` e propone azioni coerenti. Il primary outcome non è il numero di click su `Invite`, ma la quota di utenti che raggiunge un activation path coerente con l'intento, con guardrail su retention 30 giorni, paid conversion, support contacts, spam/invite complaints e time-to-first-value.

L'esperimento ha quindi un compito preciso: testare se il nuovo percorso di onboarding migliora il valore, non “riparare” retroattivamente la vecchia metrica.

### La decisione cambia forma

Riparare il flow invite per tutti è una soluzione al sintomo aggregato. Spegnere subito la nuova campagna elimina il mix shift ma può scartare un segmento economicamente interessante prima di capirlo. La scelta preferita è separare i percorsi di activation, misurare retention e monetizzazione per segmento, testare un onboarding differenziato e rivalutare l'economia della campagna prima di decidere se il nuovo use case merita investimento.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| activation 43%→35% | il KPI attuale è poco adatto ai single-player | valore economico di lungo periodo del nuovo segmento |
| mix aziendale/individuale 68/32→47/53 | parte importante del calo è composition effect | effetto causale del nuovo onboarding |
| B2B funnel quasi stabile | un use case individuale plausibile esiste | CAC/payback e paid conversion maturi |
| percorso individuale associato a D30 retention | | |

La headline decisionale può dire:

> **Il calo aggregato di activation è quasi interamente associato a un mix shift: il nuovo segmento individuale attraversa un percorso di valore diverso e rende obsoleta parte della metrica attuale. Separiamo i percorsi e testiamo l'onboarding differenziato prima di concludere che il prodotto sia peggiorato.**

L'outcome review segue retention 30/60 giorni, paid conversion, time-to-first-value, CAC/payback per segmento, feature adoption e stabilità della nuova definizione di activation.

**Percorso effettivo:** Data Readiness Review → Lifecycle Diagnostic Map → EDA Evidence Map → **prima decisione: ridefinire il problema** → Experiment Contract per il redesign → Decision Record → Decision Communication Pack.

> **Un funnel può indicarci dove il comportamento cambia. Il capstone deve anche riconoscere il momento in cui il vero problema è che stiamo misurando il nuovo comportamento con una vecchia idea di valore.**
