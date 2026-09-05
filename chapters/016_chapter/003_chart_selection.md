## 16.2 Scegliere la forma in base al compito cognitivo

Il chart type viene dopo la decision question. La domanda non è quale visual sia più elegante o disponibile nel tool, ma **quale relazione deve diventare facile da percepire e quale errore di lettura dobbiamo rendere difficile**.

Per questo useremo un piccolo **Visual Encoding Contract**. Per ogni visual importante registriamo mentalmente quattro elementi: il task percettivo richiesto, l'encoding usato, il riferimento necessario e il failure mode più probabile.

| Domanda | Forma spesso utile | Riferimento essenziale | Rischio da controllare |
|---|---|---|---|
| Quale gruppo è più grande? | barre ordinate | zero / baseline comune | asse troncato |
| Come cambia nel tempo? | linea | periodo, baseline, eventi | finestra cherry-picked |
| Come è distribuito? | istogramma / boxplot / percentile | popolazione e unità | media che nasconde le code |
| Due variabili si muovono insieme? | scatter | scala e popolazione | correlazione letta come causa |
| Come cambia il mix? | stacked / small multiples | volume totale | quota confusa con volume |
| Dove si perde la popolazione? | funnel | denominatori coerenti | step non comparabili |
| Quanto siamo lontani da una soglia? | valore + delta + trend | target / switching value | gauge senza contesto |
| Servono valori precisi? | tabella | unità e ordinamento | decorazione al posto del lookup |

La tabella è un promemoria, non un catalogo rigido. La forma corretta dipende sempre da grain, semantica e decisione.

### Confrontare magnitudini

Quando il lettore deve distinguere valori relativamente vicini, una baseline comune e lunghezze allineate sono spesso più leggibili di angoli o aree. Se Home vale **€12,4M**, Beauty **€10,9M**, Sports **€9,8M** ed Electronics **€9,6M**, barre ordinate rendono il confronto diretto. La forma deve aiutare a vedere la differenza reale, non a creare varietà grafica.

L'Office for National Statistics raccomanda infatti che i bar chart partano da zero, perché la lunghezza della barra rappresenta direttamente la magnitudine.[^ons-axis]

### Una forma giusta non corregge un grain sbagliato

Una piattaforma food delivery può mostrare ordini mensili quasi invariati con un line chart perfettamente legittimo. Passando al dato giornaliero emerge però che lunedì–giovedì crescono mentre venerdì–domenica diminuiscono. I due movimenti si compensavano nell'aggregato.

Il failure mode non era il grafico. Era il **grain temporale**. Lo stesso vale per categoria, cohort, account o sessione: una visualizzazione chiara non salva una rappresentazione sbagliata del fenomeno.

### Centro, distribuzione e code

Un delivery time medio di **2,4 giorni** può apparire ottimo; se il 90° percentile è **6,8 giorni**, il problema decisionale può vivere nella coda. Se dobbiamo monitorare un service level, media e percentile possono essere più utili di una singola media; se dobbiamo confrontare gruppi, boxplot o distribuzioni possono rendere visibile ciò che il centro nasconde.

### Relazione non significa causalità

Uno scatter plot può rendere una correlazione estremamente convincente. Proprio per questo titolo e annotazioni devono rispettare il claim level. “Gli account con maggiore adoption mostrano NRR più alta” descrive una relazione; “l'adoption aumenta la NRR” richiede un disegno causale che il grafico non può fornire.

### Quota e volume devono restare distinguibili

Un 100% stacked chart può mostrare bene come cambia la composizione e, nello stesso tempo, nascondere che il totale si è dimezzato. Se entrambi sono decision-critical, mostriamo volume e mix in due layer coordinati invece di chiedere a un solo encoding di rispondere a due domande diverse.

Lo stesso principio vale per il funnel. Se `checkout_started` conta sessioni e `payment_success` conta ordini, la forma suggerisce una sequenza coerente mentre i denominatori non lo sono. Il visual contract eredita il semantic contract dei capitoli precedenti.

### Quando un asse ristretto è legittimo

Per line chart e scatter, in cui i punti non sono codificati come lunghezza dalla baseline, un asse ristretto può rendere leggibile una variazione piccola senza essere automaticamente manipolativo. ONS consente questo uso quando scala e contesto sono chiari; il problema nasce quando l'asse o il titolo producono un'impressione sproporzionata rispetto alla domanda.[^ons-axis]

La verifica finale resta semplice:

> **Se il destinatario avesse cinque secondi, quale relazione deve percepire correttamente?**

Poi controlliamo che scala, grain, denominatore, baseline e titolo non gli facciano percepire qualcos'altro.

> **Il chart type non è una preferenza estetica. È una decisione sul compito cognitivo che rendiamo economico e sul failure mode che dobbiamo rendere visibile.**

[^ons-axis]: Office for National Statistics, *Data visualisation guidance — Axes and gridlines*, https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines
