## 2.9 Quattro famiglie di domande analitiche

Non tutte le analisi cercano lo stesso tipo di risposta. Distinguere la natura della domanda è fondamentale perché cambia il metodo, il dato necessario e il livello di evidenza richiesto.

Una classificazione molto utile separa l'analytics in quattro famiglie:

1. **Descrittiva** — che cosa è successo?
2. **Diagnostica** — perché è successo?
3. **Predittiva** — che cosa potrebbe succedere?
4. **Prescrittiva** — che cosa dovremmo fare?

IBM utilizza esplicitamente questa distinzione nel descrivere il ciclo dell'analytics e sottolinea che le quattro categorie supportano livelli diversi del processo decisionale.

Fonte: https://www.ibm.com/think/topics/prescriptive-analytics

### Analisi descrittiva

L'analisi descrittiva organizza il passato e il presente.

Esempi:

- quanto abbiamo venduto?
- quanti clienti abbiamo perso?
- quali prodotti sono cresciuti?
- qual è il tasso di conversione per canale?

È spesso il punto di partenza, ma non necessariamente il punto di arrivo.

### Analisi diagnostica

L'analisi diagnostica cerca spiegazioni plausibili.

Esempi:

- perché il churn è aumentato?
- perché il margine è diminuito?
- quale segmento contribuisce maggiormente al calo?
- quale fase del funnel si è deteriorata?

Qui entrano in gioco drill-down, segmentazioni, confronti, decomposizioni, ipotesi e analisi delle possibili cause.

Un punto importante: una spiegazione diagnostica non è automaticamente una dimostrazione causale.

### Analisi predittiva

L'analisi predittiva cerca di stimare ciò che potrebbe accadere.

Esempi:

- quali clienti hanno maggiore probabilità di abbandono?
- quanta domanda ci aspettiamo il mese prossimo?
- quale probabilità ha un lead di convertire?

Si utilizzano modelli statistici, serie temporali, machine learning o altri metodi previsivi.

Una previsione può essere molto accurata senza spiegare la causa del fenomeno.

### Analisi prescrittiva

L'analisi prescrittiva cerca di collegare previsione e decisione.

Esempi:

- quali clienti dovremmo contattare?
- come allocare un budget limitato?
- quale prezzo massimizza il margine entro determinati vincoli?
- quale piano operativo minimizza tempi e costi?

IBM descrive la prescriptive analytics come il livello che, oltre a prevedere, raccomanda linee d'azione tenendo conto di obiettivi e vincoli.

### Una quinta domanda: causale

Per il lavoro dell'analista è utile aggiungere esplicitamente una quinta famiglia:

**Causale — che cosa succederebbe se intervenissimo?**

Domande come:

- una promozione aumenta davvero gli acquisti?
- il nuovo onboarding riduce il churn?
- aumentare il prezzo provoca una riduzione delle conversioni?

richiedono un livello di rigore diverso da una semplice correlazione.

Qui entrano in gioco esperimenti, A/B test, quasi-esperimenti e metodi di inferenza causale che approfondiremo più avanti.

### La domanda determina il metodo

Un errore tipico è usare un metodo solo perché è disponibile.

Se la domanda è descrittiva, un modello predittivo potrebbe essere inutile. Se la domanda è causale, un dashboard non basta. Se il problema è prescrittivo, prevedere il futuro senza modellare vincoli e conseguenze delle azioni potrebbe non produrre una decisione.

Prima del tool viene quindi una scelta fondamentale:

> **Che tipo di domanda stiamo realmente cercando di risolvere?**
