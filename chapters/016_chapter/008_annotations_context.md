## 16.7 Annotazioni e Context Contract: ciò che il segno non contiene

Una linea, una barra o un punto non contengono da soli tutto ciò che serve per interpretarli. Mancano spesso baseline, target, denominatore, definizione della metrica, stato del dato, cambio metodologico o evento operativo. Se uno di questi elementi può cambiare il significato del visual, non è una nota accessoria: è parte del **Context Contract**.

Per un elemento decision-critical dobbiamo poter recuperare almeno:

| Campo | Domanda |
|---|---|
| Metric definition | che cosa misura davvero? |
| Population / denominator | su chi è calcolata? |
| Time window | quale periodo rappresenta? |
| Baseline | rispetto a cosa lo giudichiamo? |
| Target / switching value | quale soglia ha significato operativo? |
| Freshness | fino a quando il dato è aggiornato? |
| Maturity | provisional, reconciled o final? |
| Method break | è cambiata definizione, tracking o sistema? |
| Event annotation | quale evento osservabile aiuta a leggere la serie? |

Non tutti questi campi devono occupare spazio nella headline. Devono però essere disponibili al layer giusto della Decision Communication Pack.

### Annotare eventi, non inventare spiegazioni

“14 aprile — release 6.12 distribuita al 65% degli utenti” documenta un fatto. “14 aprile — la release causa il calo” trasforma una coincidenza temporale in un claim causale. Un'annotazione deve rispettare lo stesso livello di evidenza del testo che accompagna.

Questo confine è particolarmente importante nei grafici temporali: la vicinanza visiva tra evento e cambiamento rende la causalità intuitivamente plausibile anche quando non è identificata.

### Caso simulato/composito — Il crollo creato da una definizione

Una piattaforma SaaS mostra i daily active users. Il **14 aprile** la serie scende del **16%** e la prima headline parla di engagement in forte calo. Quel giorno, però, cambia la definizione di `active_user`: prima bastava aprire l'app, dopo serve almeno un'azione significativa.

I valori prima e dopo il 14 aprile possono essere entrambi validi secondo le rispettive definizioni. È la **comparabilità della serie** a essersi rotta. Una linea verticale e una nota come “nuova definizione di active user; livelli pre/post non direttamente comparabili” impediscono al visual di sostenere implicitamente un trend che i dati non possono misurare.

## Baseline: il numero non decide da solo

`Conversion = 3,8%` può essere sopra la settimana precedente (**3,7%**), sotto il target (**4,2%**), dentro il range storico (**3,5–4,1%**) e vicino a un controllo (**3,9%**) nello stesso momento. La baseline deve essere scelta perché risponde alla decision question, non perché crea il contrasto più interessante.

Questo collega direttamente il Context Contract al Decision Record: il riferimento corretto è quello che cambia l'interpretazione dell'alternativa, non quello più spettacolare sulla slide.

## Il denominatore può cambiare la storia

“Il 90% dei clienti è soddisfatto” ha un significato molto diverso se ha risposto solo il **12% degli invitati**, il survey appare soltanto dopo un acquisto completato o i ticket aperti sono esclusi. Quando eligibility e denominator sono materialmente importanti, non devono essere sepolti in un data dictionary che il pubblico non consulterà.

## Freshness e maturity

Alle 08:00 una dashboard può avere ordini completi fino alle 07:45, pagamenti fino alle 07:30, refund D+2 e logistics cost D+1. Un contribution margin “di oggi” costruito su questi feed non è finalizzato. La comunicazione corretta può dire:

> **Data as of 07:45 — margin provisional; refund e logistics reconciliation D+2.**

Ora il lettore sa se quel numero è abbastanza maturo per l'azione richiesta.

## Titolo e contesto devono dire la stessa cosa

“DAU 2026” è troppo generico. “I DAU post-14 aprile non sono comparabili con lo storico dopo il cambio di definizione” rende esplicita la vera proprietà decisionale della serie. “La nuova definizione ha ridotto l'engagement” sarebbe invece un claim non supportato.

La regola è semplice:

> **Il titolo può guidare l'attenzione; non può aggiungere evidenza che il visual non possiede.**

La provenance deve poi restare vicina al punto d'uso: fonte, metrica/versione, timestamp, nota metodologica e collegamento al Decision Record o all'appendix devono essere facili da recuperare.

> **Il contesto non è decorazione del grafico. È parte del significato che il grafico pretende di comunicare.**

### Fonte

- Office for National Statistics, *Data visualisation guidance*, https://service-manual.ons.gov.uk/data-visualisation
