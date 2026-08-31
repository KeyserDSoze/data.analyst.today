## 16.12 Caso studio: da dashboard confusa a decisione chiara
## Il contesto

BlueHarbor Foods è un'azienda alimentare omnicanale con circa €620 milioni di fatturato annuo.

Il team commerciale segnala che il margine del canale online è peggiorato negli ultimi due trimestri.

La dashboard esistente contiene:

- revenue;
- gross margin;
- contribution margin;
- ordini;
- clienti;
- CAC;
- AOV;
- resi;
- promozioni;
- costi logistici;
- 11 filtri;
- 9 tab.

Il management guarda la dashboard e conclude:

> “Le promozioni stanno distruggendo il margine.”

L'analyst riceve la richiesta di preparare una presentazione per decidere se ridurre gli sconti.

## Primo errore: partire dalla slide

La tentazione è aprire PowerPoint e cercare il grafico migliore.

Ma il problema non è ancora visivo.

La domanda decisionale è:

> “Ridurre le promozioni migliorerebbe abbastanza il contribution margin da compensare l'eventuale perdita di volume?”

Serve quindi scomporre il deterioramento.

## L'analisi

Il contribution margin passa dal 21,6% al 18,9%.

La decomposition mostra:

- promozioni: -0,5 pp;
- costo prodotto: -0,8 pp;
- mix verso prodotti chilled: -0,7 pp;
- last-mile logistics: -0,9 pp;
- altri effetti: +0,2 pp.

Le promozioni contribuiscono, ma non sono il driver principale.

Inoltre il maggiore sconto è concentrato su clienti ad alta frequenza, dove la riduzione promozionale potrebbe avere un impatto non banale sulla retention.

## La prima visualizzazione

Un waterfall mostra la transizione dal 21,6% al 18,9%.

È molto più utile di cinque grafici separati perché risponde alla domanda:

> “Quali componenti spiegano il delta?”

Il titolo non dice:

> Contribution margin bridge

ma:

> **Logistica e mix spiegano circa il 59% del deterioramento del contribution margin**

## La seconda visualizzazione

Uno small multiple confronta contribution margin e repeat rate per quattro segmenti di cliente.

Il segmento più sensibile agli sconti mostra anche il repeat rate più alto.

Questo non prova causalità, ma rende visibile il trade-off che deve essere testato.

## La terza visualizzazione

Un grafico di scenario mostra tre opzioni:

| Scenario | Riduzione promo | Impatto stimato CM | Rischio volume |
|---|---:|---:|---|
| A | nessuna | baseline | basso |
| B | selettiva | +0,3–0,5 pp | medio-basso |
| C | generalizzata | +0,7–1,0 pp | alto |

L'analyst non presenta lo scenario C come “migliore” solo perché ha il massimo upside teorico.

Evidenzia che l'incertezza sul volume lo rende poco robusto.

## L'executive summary

La prima slide dice:

> **Non raccomandiamo un taglio generalizzato delle promozioni. Le promozioni spiegano solo una parte del calo di margine; logistica e mix hanno un impatto maggiore. Proponiamo un test selettivo sugli sconti e un intervento separato sui costi last-mile.**

Sotto:

- contribution margin: 21,6% → 18,9%;
- circa 59% del deterioramento associato a logistica + mix;
- promozioni: circa 0,5 pp del delta;
- rischio principale: danneggiare retention nei clienti ad alta frequenza;
- next step: test controllato su segmenti selezionati.

## Il meeting

Il CFO chiede:

> “Quindi le promozioni non sono un problema?”

La risposta corretta non è sì/no.

È:

> “Sono parte del problema, ma il dato non supporta un taglio generalizzato come prima leva. Se interveniamo solo lì rischiamo di sacrificare volume senza risolvere la maggior parte del deterioramento.”

Il COO chiede:

> “Quanto siamo sicuri che la logistica sia davvero il driver?”

L'analyst mostra il backup:

- costo per consegna;
- mix geografico;
- peso medio ordine;
- surcharge dei carrier;
- confronto per area.

## La decisione

Il management approva:

1. test selettivo di riduzione promozioni;
2. revisione delle regole di free delivery;
3. negoziazione sui carrier per ordini chilled;
4. monitoraggio separato di margin, volume e repeat rate.

## La lezione

La dashboard originale conteneva quasi tutti i numeri necessari.

Ciò che mancava era una struttura decisionale.

L'analyst non ha creato valore aggiungendo altri grafici.

Ha creato valore:

- scegliendo la domanda;
- decomponendo il delta;
- usando visualizzazioni coerenti con il ragionamento;
- mostrando l'incertezza;
- distinguendo evidenza e raccomandazione;
- preparando il meeting attorno alla decisione.

**Data storytelling non significa trasformare i dati in una storia convincente. Significa trasformare un'analisi complessa in una sequenza di evidenze che permette a qualcuno di decidere senza perdere il significato originale.**
