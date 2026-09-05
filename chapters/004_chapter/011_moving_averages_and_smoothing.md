## 4.10 Moving average e smoothing: scegliere la scala temporale senza cancellare l'evento

Le serie operative contengono oscillazioni che possono rendere difficile vedere un movimento di fondo. Una media mobile riduce parte di quel rumore, ma introduce immediatamente una scelta analitica: **quanta storia vogliamo incorporare in ogni punto e quale tipo di cambiamento rischiamo di rendere meno visibile?**

Lo smoothing non produce nuova evidenza. Cambia la lente con cui osserviamo quella già disponibile.

Consideriamo un marketplace B2B che registra normalmente circa **8.200 ordini al giorno**. Martedì 14 maggio il volume scende a 5.900, circa **-28%**, e l'escalation è immediata. L'analista affianca alla serie grezza una media mobile a sette giorni, osserva i pagamenti completati nei giorni successivi e controlla il calendario degli incidenti operativi. Scopre che lunedì sera un provider bancario ha avuto un'interruzione e molte transazioni sono state completate mercoledì. La media mobile settimanale resta quasi invariata.

Le due osservazioni non si contraddicono. Martedì è esistito un problema reale di esperienza e conversione temporanea; allo stesso tempo non emerge un deterioramento persistente del volume settimanale. La media mobile non “corregge” il crollo: lo colloca in una scala temporale diversa.

## La finestra è una domanda implicita

Una finestra di 7 giorni e una di 90 non sono versioni più o meno precise della stessa statistica. Una finestra breve reagisce rapidamente e conserva molta variabilità; una lunga stabilizza maggiormente il segnale ma risponde con ritardo ai cambiamenti recenti. La scelta riflette quindi un trade-off inevitabile tra **ridurre rumore e reagire velocemente**.

La finestra dovrebbe seguire il ritmo del processo e della decisione. Una media a sette giorni può neutralizzare parte dell'effetto giorno-della-settimana in un e-commerce; una finestra di novanta giorni può essere utile per osservare un movimento di fondo ma quasi inutile per decidere se un problema operativo iniziato ieri richieda intervento.

Anche la direzione della finestra conta. Una **trailing moving average** usa soltanto il presente e il passato ed è quindi compatibile con un monitoraggio operativo. Una **centered moving average** usa osservazioni prima e dopo il punto rappresentato: può essere molto utile per descrivere storicamente la struttura, ma incorpora informazione che in quel momento non sarebbe stata ancora disponibile. Presentarla come indicatore “in tempo reale” introdurrebbe implicitamente informazione futura, un problema che tornerà nel Capitolo 7 quando parleremo di forecasting e leakage temporale.

## Il rischio non è soltanto statistico, ma narrativo

Più una serie viene smussata, più diventa visivamente ordinata. Questa proprietà può trasformarsi in un rischio comunicativo. Un outage di due ore può scomparire nella media giornaliera, un picco di difettosità nella media settimanale, una brusca inversione recente in una finestra di novanta giorni.

Per questo nell'EDA è spesso utile mostrare insieme serie originale, versione smussata, finestra utilizzata ed eventi di business rilevanti. Il lettore può così vedere sia la variabilità che abbiamo compresso sia il movimento che volevamo rendere visibile.

NIST descrive le moving average come una tecnica semplice di smoothing per mettere in evidenza la componente sottostante di una serie, ma la scelta dello smoothing dipende dal comportamento del processo.[^nist-smoothing] Una linea smussata che sale non dimostra quindi l'esistenza di un trend stabile né dice quanto durerà. In questo capitolo rimane una lente esplorativa; l'analisi formale della struttura temporale appartiene al Capitolo 7.

Questa stessa idea di sensitivity analysis rispetto alla lente usata si applica anche alle osservazioni estreme. La prossima sezione non chiederà se un outlier sia “vero” — problema già affrontato nel Capitolo 3 — ma quanto il pattern dipenda da pochi casi reali.

> **Lo smoothing è una lente: può chiarire il movimento di fondo oppure nascondere l'evento che conta. La scelta della finestra decide quale dei due effetti privilegiamo.**

[^nist-smoothing]: NIST/SEMATECH, *What are Moving Average or Smoothing Techniques?*. https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc42.htm
