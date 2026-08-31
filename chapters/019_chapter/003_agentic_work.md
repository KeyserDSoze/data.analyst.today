# 19.2 Dal singolo assistente ai team di agenti

Il cambiamento più profondo potrebbe non essere che ogni analyst utilizzerà un chatbot più bravo.

Potrebbe essere che una parte crescente del lavoro analitico venga svolta da **sistemi composti da più agenti con ruoli diversi**.

Microsoft, nel Work Trend Index 2025, descrive una traiettoria in tre fasi:

1. AI come assistente;
2. agenti come “digital colleagues” che svolgono task specifici sotto direzione umana;
3. sistemi in cui gli esseri umani impostano la direzione e gli agenti gestiscono parti intere del processo, intervenendo quando serve.

Il punto interessante per l’analista non è il nome commerciale dell’agente.

È il cambiamento del modello operativo.

## Un possibile team analitico del futuro

Immaginiamo una domanda:

> “Perché il margine è sceso in Germania e cosa possiamo fare?”

Un analyst potrebbe coordinare:

- un agente che verifica data freshness;
- uno che controlla le definizioni di margin;
- uno che decomprime il delta per volume, price, mix e cost;
- uno che cerca anomalie nei supplier cost;
- uno che controlla le promozioni;
- uno che analizza resi e logistica;
- uno che produce contro-ipotesi;
- uno che prepara scenari economici;
- uno che verifica le query;
- uno che prepara una sintesi per il CFO.

In termini di capacità grezza, una singola persona può quindi dirigere più lavoro di quanto avrebbe potuto eseguire manualmente.

Ma questo crea una nuova classe di problemi.

## La produzione non è più il collo di bottiglia

Con molti agenti, il rischio è ottenere troppo output.

Se dieci agenti generano ciascuno cinque ipotesi, non abbiamo necessariamente cinquanta insight.

Abbiamo cinquanta elementi da ordinare.

Il collo di bottiglia diventa:

- priorità;
- coordinamento;
- semantica;
- verifica;
- risoluzione dei conflitti;
- comprensione del business;
- decisione.

Questo cambia anche il modo in cui valutiamo la seniority.

Il senior analyst del futuro non è necessariamente chi scrive più codice.

Potrebbe essere chi sa:

- dividere bene un problema;
- assegnare task agli agenti appropriati;
- costruire criteri di accettazione;
- riconoscere output incoerenti;
- decidere quando serve un essere umano specialista;
- sapere quando fermare il workflow.

## Il rischio della falsa abbondanza

Quando l’AI rende economica la produzione di analisi, può emergere una nuova illusione:

> più analisi = più conoscenza.

Non è vero.

Un’organizzazione potrebbe passare da 50 report a 5.000 report generati automaticamente senza migliorare una sola decisione.

La scarsità si sposta.

Da:

**“non abbiamo abbastanza capacità analitica”**

verso:

**“non sappiamo distinguere quali analisi meritano attenzione.”**

## Caso realistico: 23 spiegazioni per un solo calo

Un’azienda subscription registra un calo del 7% nelle conversioni.

Gli agenti generano 23 spiegazioni plausibili:

- prezzo;
- competitor;
- campagne;
- lentezza del sito;
- mix geografico;
- payment failures;
- nuova release;
- stagionalità;
- tracking incompleto;
- ecc.

Il sistema sembra potente.

Ma senza un metodo di ranking, l’abbondanza crea paralisi.

L’analista costruisce quindi una matrice:

| Ipotesi | Evidenza iniziale | Impatto potenziale | Verificabilità | Costo del test |
|---|---:|---:|---:|---:|
| payment failures | alta | alta | alta | basso |
| price increase | media | alta | media | medio |
| competitor | bassa | media | bassa | alto |
| tracking bug | alta | alta | alta | basso |

Il workflow cambia subito.

La qualità non deriva dal numero di ipotesi generate.

Deriva dalla capacità di trasformarle in un **ordine di investigazione**.

## L’agent boss non è un titolo

Microsoft usa l’espressione “agent boss” per descrivere lavoratori che costruiscono, delegano e gestiscono agenti.

Per un Data Analyst, possiamo tradurla così:

> **diventare responsabili di un sistema di capacità analitiche, non soltanto dell’output delle proprie mani.**

Questo è un ampliamento del ruolo.

Ma comporta anche più accountability.

Quando un workflow diventa potente, aumenta la necessità di sapere:

- cosa può fare;
- cosa non può fare;
- a quali dati accede;
- quali controlli esegue;
- quali azioni richiedono approvazione;
- cosa succede quando due agenti non sono d’accordo.

Il futuro del lavoro agentico non elimina quindi il principio del Capitolo 0.

Lo rende ancora più importante:

> **più capacità deleghiamo, più dobbiamo essere chiari su ciò che resta sotto la nostra responsabilità.**

Fonte pubblica di riferimento:

- Microsoft, *2025 Work Trend Index — The Year the Frontier Firm Is Born*: https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
