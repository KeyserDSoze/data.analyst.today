## 5.12 Intervalli di confidenza: smettere di fingere che una stima sia esatta

Un singolo numero comunica spesso più certezza di quanta ne abbiamo davvero.

Se una survey stima che il 62% dei clienti è soddisfatto, quel 62% non è un valore scolpito nella pietra. È una stima ottenuta da un campione.

L'intervallo di confidenza serve a rendere visibile questa incertezza.

Per una media, una forma classica dell'intervallo è:

\[
\bar{x} \pm t \cdot \frac{s}{\sqrt{n}}
\]

L'intervallo combina quindi tre elementi:

- la stima osservata;
- la variabilità dei dati;
- la dimensione del campione.

### Caso realistico: quale filiale ha davvero migliorato la soddisfazione?

Una banca monitora il Customer Satisfaction Score di tre filiali pilota dopo un nuovo processo di onboarding.

| Filiale | CSAT stimato | Intervallo 95% |
|---|---:|---:|
| Torino Centro | 84% | 82%-86% |
| Novara | 87% | 79%-93% |
| Biella | 83% | 81%-85% |

Se guardassimo soltanto il valore puntuale, Novara sembrerebbe la migliore.

Ma Novara ha raccolto soltanto 74 risposte, mentre Torino Centro e Biella ne hanno oltre 1.000.

L'intervallo di Novara è molto più largo.

Questo non significa che il suo 87% sia sbagliato. Significa che **non sappiamo ancora con grande precisione dove si trovi il valore reale della popolazione**.

Un management che premiasse automaticamente Novara sulla base del valore puntuale starebbe ignorando una parte essenziale dell'informazione.

### Cosa significa davvero “95%”

Una delle interpretazioni più comuni, ma tecnicamente errate, è:

> c'è il 95% di probabilità che il vero parametro sia dentro questo intervallo.

Nell'interpretazione frequentista classica non è così.

Il parametro della popolazione è considerato fisso. È il procedimento di costruzione dell'intervallo a possedere una copertura del 95%: se ripetessimo il campionamento moltissime volte e costruissimo ogni volta l'intervallo con lo stesso metodo, circa il 95% degli intervalli conterrebbe il vero parametro.[^nist-ci]

Nella pratica manageriale non serve trasformare questa distinzione in una disputa filosofica. Serve però evitare di raccontare l'intervallo come una certezza probabilistica che il metodo non sta fornendo.

### Intervallo stretto non significa risultato importante

Supponiamo che una piattaforma con 15 milioni di sessioni rilevi che una modifica al checkout aumenta la conversione dal 4,000% al 4,015%.

Con una numerosità enorme, l'intervallo potrebbe essere strettissimo.

La stima può essere molto precisa e allo stesso tempo avere un impatto economico trascurabile.

Precisione statistica e rilevanza business sono due domande diverse.

### Intervallo largo non significa analisi inutile

All'opposto, un intervallo largo può essere esattamente l'informazione che serve.

Un nuovo servizio B2B ha soltanto 42 clienti. Il churn annualizzato stimato è 12%, ma l'incertezza è elevata.

La conclusione corretta potrebbe essere:

> non disponiamo ancora di dati sufficienti per distinguere un churn strutturalmente basso da uno potenzialmente problematico.

Questa non è una mancata conclusione. È una conclusione sull'incertezza disponibile.

### Comunicare stima e intervallo insieme

Una buona abitudine è evitare frasi come:

> la soddisfazione è 84%.

Preferire:

> nel campione osservato la soddisfazione è stimata all'84%, con un intervallo di confidenza al 95% compreso tra 82% e 86%.

Ancora meglio, se il pubblico non è tecnico:

> la nostra migliore stima è 84%; sulla base del campione, un intervallo plausibile ottenuto con il metodo statistico usato va circa dall'82% all'86%.

L'obiettivo non è impressionare con la statistica. È impedire che una stima venga interpretata come un fatto esatto.

### Fonti

[^nist-ci]: NIST/SEMATECH e-Handbook of Statistical Methods, *Confidence Limits for the Mean*, https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm ; NIST, *What are confidence intervals?*, https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
