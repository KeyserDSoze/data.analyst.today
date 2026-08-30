## 4.10 Moving average e smoothing: vedere il segnale senza cancellare il problema

I dati operativi sono rumorosi. Un giorno molto alto o molto basso può attirare l'attenzione anche quando non rappresenta un cambiamento strutturale.

Le tecniche di smoothing aiutano a ridurre la variazione casuale per rendere più visibili trend e componenti cicliche. NIST descrive le moving average come uno degli approcci più semplici per attenuare il rumore di una serie temporale e mostrare più chiaramente il movimento sottostante.[^nist-smoothing]

### Caso: il crollo degli ordini del martedì

Un marketplace B2B monitora gli ordini giornalieri. Martedì 14 maggio gli ordini scendono da circa 8.200 a 5.900. Il calo del 28% genera immediatamente un'escalation.

L'analista evita però di interpretare il singolo giorno. Calcola una media mobile a 7 giorni e verifica il calendario operativo. Scopre che lunedì sera un importante sistema bancario ha avuto un'interruzione e molti pagamenti sono stati completati mercoledì.

La media mobile settimanale resta quasi invariata.

Non significa che il problema vada ignorato: il disservizio è reale e può aver avuto conseguenze sull'esperienza cliente. Significa che non esiste evidenza sufficiente per parlare di un deterioramento strutturale della domanda.

### La finestra cambia ciò che vediamo

Una media mobile a 7 giorni risponde a una domanda diversa da una media mobile a 90 giorni.

Una finestra breve reagisce rapidamente ma conserva più rumore. Una finestra lunga è più stabile ma può ritardare la percezione di un cambiamento reale.

Immaginiamo un'app con utenti attivi giornalieri:

- media mobile 7 giorni: segnala una flessione già dopo una settimana;
- media mobile 30 giorni: mostra il calo più lentamente;
- media mobile 90 giorni: può continuare a sembrare stabile mentre il comportamento recente è già cambiato.

Non esiste una finestra universalmente corretta. La scelta deve seguire il ciclo decisionale e la frequenza naturale del fenomeno.

### Lo smoothing può anche nascondere

Un rischio importante è usare il smoothing come cosmetica.

Se una fabbrica ha picchi improvvisi di difettosità che durano due ore, una media giornaliera può renderli quasi invisibili. Se un servizio digitale ha outage brevi ma gravi, una media settimanale dell'uptime può apparire eccellente pur nascondendo incidenti concentrati negli orari di picco.

Per questo una buona EDA mostra spesso sia la serie originale sia la versione smussata.

Il principio è semplice: **lo smoothing deve aiutare a vedere la struttura, non cancellare gli eventi che contano**.

[^nist-smoothing]: NIST/SEMATECH, *What are Moving Average or Smoothing Techniques?*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc42.htm