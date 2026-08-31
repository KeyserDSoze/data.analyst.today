# 16.2 Scegliere il grafico in base alla domanda

La scelta del grafico dovrebbe partire dalla relazione che vogliamo far vedere, non dalla libreria di visualizzazioni disponibile.

Prima viene la domanda.

Poi la struttura del dato.

Solo dopo il tipo di grafico.

## Confrontare grandezze

Se la domanda è:

> “Quale categoria vende di più?”

un bar chart è spesso più leggibile di una torta.

Perché?

Perché il nostro sistema visivo confronta con maggiore precisione lunghezze allineate su una stessa scala rispetto ad angoli e aree.

Esempio:

| Categoria | Revenue |
|---|---:|
| Home | €12,4M |
| Beauty | €10,9M |
| Sports | €9,8M |
| Electronics | €9,6M |

In una torta, distinguere 10,9 da 9,8 richiede più sforzo.

In barre ordinate, la differenza è immediata.

## Mostrare un trend

Per una serie temporale, la linea è spesso la scelta naturale.

Ma anche qui dobbiamo chiederci:

- qual è la frequenza?
- il dato è continuo o intermittente?
- dobbiamo confrontare una o più serie?
- la stagionalità conta?
- serve una baseline?

## Caso realistico: il grafico mensile che nasconde il problema settimanale

Una piattaforma food delivery osserva ordini mensili sostanzialmente stabili.

Il grafico mensile non mostra nulla di particolare.

Passando al livello giornaliero emerge che:

- lunedì–giovedì gli ordini sono cresciuti;
- venerdì–domenica sono diminuiti sensibilmente;
- la crescita weekday compensa quasi esattamente il calo weekend.

Il problema non era il chart type.

Era il grain temporale.

La visualizzazione più elegante del mondo non corregge una granularità inadatta alla domanda.

## Mostrare una distribuzione

Quando media e totale non bastano, possiamo usare:

- histogram;
- boxplot;
- density plot;
- percentile chart.

Esempio: delivery time medio di 2,4 giorni.

Sembra ottimo.

Ma se il 90° percentile è 6,8 giorni, il problema di customer experience potrebbe essere concentrato nella coda.

## Mostrare una relazione

Uno scatter plot aiuta a vedere:

- relazione;
- dispersione;
- cluster;
- outlier;
- eteroschedasticità.

Ma attenzione: una nuvola inclinata non dimostra causalità.

Un grafico può rendere una correlazione visivamente potente e quindi psicologicamente più convincente di quanto meriti.

## Mostrare una composizione

Per la composizione possiamo usare:

- stacked bar;
- 100% stacked bar;
- small multiples;
- area chart in casi specifici.

La scelta dipende da cosa conta:

- valore assoluto;
- quota percentuale;
- evoluzione nel tempo;
- confronto tra gruppi.

## Mostrare un funnel

Un funnel visuale ha senso se esiste davvero una sequenza di passaggi e la popolazione è coerente.

Un funnel esteticamente perfetto costruito con denominatori incompatibili può essere completamente fuorviante.

## Mostrare target e performance

Per KPI rispetto a target, spesso bastano:

- valore attuale;
- target;
- delta assoluto;
- delta percentuale;
- trend recente.

Non serve sempre un gauge.

Un gauge occupa molto spazio per comunicare una singola relazione.

## La domanda guida

Prima di scegliere il grafico, chiediamoci:

1. voglio confrontare?
2. voglio mostrare un trend?
3. voglio mostrare distribuzione?
4. voglio mostrare relazione?
5. voglio mostrare composizione?
6. voglio mostrare percorso/funnel?
7. voglio mostrare performance rispetto a target?

Il grafico è la risposta visiva a una di queste domande.

**Il chart type non è una preferenza estetica. È una scelta su quale struttura rendere percettivamente evidente.**
