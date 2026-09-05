## 4.6 Un workflow pratico per l'EDA: restringere il problema senza inventare una causa

L'EDA non dovrebbe essere una sequenza casuale di `groupby`, correlazioni e grafici. Parte da un dataset già dichiarato **pronto o pronto con caveat** nel Capitolo 3 e da una domanda costruita nell'Analytical Brief del Capitolo 2. Il suo compito è restringere progressivamente lo spazio delle spiegazioni possibili senza confondere ciò che osserviamo con ciò che immaginiamo possa averlo prodotto.

Per questo, qui una sequenza operativa ha davvero senso. I passaggi non sono una tassonomia da memorizzare: rappresentano l'ordine con cui impediamo all'esplorazione di trasformarsi in data fishing.

### 1. Dichiarare il fenomeno prima di aprire il notebook

La domanda deve essere abbastanza precisa da stabilire quale cambiamento stiamo cercando di descrivere. Per esempio:

> **Il renewal rate trimestrale è sceso dall'81% al 74%: dove si concentra il cambiamento e quali caratteristiche lo accompagnano?**

Il linguaggio è intenzionale. Non chiediamo ancora che cosa abbia “causato” il calo. Stiamo costruendo una mappa del fenomeno.

### 2. Costruire il quadro aggregato che farà da riferimento

Prima di segmentare, fissiamo il livello corrente, la baseline, la variazione assoluta e relativa, il volume del numeratore e del denominatore e, quando conta, l'andamento temporale e la distribuzione sottostante. Questo quadro serve perché ogni drill-down deve poter tornare al totale e spiegare **quanto del fenomeno complessivo sta localizzando**.

### 3. Descrivere le distribuzioni che possono cambiare l'interpretazione

Per le variabili numeriche osserviamo centro, dispersione, quantili, forma e code; per le categoriche frequenze, proporzioni e composizione. Non perché ogni EDA debba produrre tutte queste statistiche, ma perché vogliamo individuare le proprietà che renderebbero fuorviante il riepilogo aggregato.

Se media e mediana divergono, se il P95 peggiora mentre il P50 è stabile o se una categoria domina improvvisamente il mix, la prossima segmentazione nasce da una ragione e non dalla disponibilità di una colonna.

### 4. Segmentare soltanto quando una differenza potrebbe cambiare qualcosa

Piano, canale, mercato, coorte, prodotto, tenure, device e tipologia cliente sono tutte dimensioni plausibili, ma non devono entrare automaticamente nell'analisi. Per ciascuna chiediamo:

> **Se il pattern fosse molto diverso in questo gruppo, cambierebbe una nostra ipotesi o la prossima decisione?**

La domanda lega l'EDA al brief e riduce la tentazione di cercare tra centinaia di tagli finché ne appare uno interessante.

### 5. Cercare relazioni e produrre spiegazioni concorrenti

Dopo aver compreso le singole variabili possiamo osservare differenze tra gruppi, scatter plot, correlazioni, tabelle di contingenza, pattern condizionati e sequenze temporali. Ogni associazione interessante dovrebbe però generare almeno un'alternativa alla storia più immediata.

Se i clienti con più ticket mostrano churn maggiore, per esempio, i problemi che generano ticket potrebbero favorire il churn. Ma è anche possibile che clienti già in difficoltà contattino più spesso il supporto, che un segmento più complesso produca entrambe le cose o che tenure e prodotto spieghino parte dell'associazione. L'EDA ha valore quando **mantiene vive queste spiegazioni abbastanza a lungo da poterle distinguere**.

### 6. Stressare il pattern prima di chiamarlo insight

Prima di promuovere una relazione a conclusione, cambiamo in modo ragionevole la lente: media contro mediana, baseline alternative sensate, periodo completo contro settimane eccezionali, totale contro segmenti motivati, valori assoluti contro tassi, dataset completo contro sensitivity analysis senza punti molto influenti.

Se il risultato cambia completamente per una scelta plausibile, il pattern è fragile. La fragilità non deve essere nascosta: è una proprietà dell'evidenza.

### 7. Conservare separati fatti, ipotesi e prossimo controllo

Un piccolo registro evita che durante le iterazioni un'interpretazione diventi “vera” soltanto perché viene ripetuta:

| Osservazione | Ipotesi candidata | Evidenza a favore | Spiegazioni alternative | Prossimo controllo |
|---|---|---|---|---|
| churn concentrato nei nuovi SMB | onboarding insufficiente | completion più bassa | acquisition mix | confronto per canale/coorte |
| P95 delivery alto nel weekend | capacity insufficiente | volumi +35% | mix geografico | segmentare per area |

Il valore della tabella non è burocratico. Ci costringe a registrare **ciò che sappiamo e ciò che stiamo ancora cercando di spiegare**.

## Caso simulato/composito: il rinnovo SaaS

Una piattaforma SaaS per studi professionali ha **18.200 clienti** e vede il renewal rate trimestrale scendere dall'81% al 74%. Il totale è preoccupante, ma non dice dove intervenire.

La prima segmentazione per piano mostra che Enterprise passa dal 92% al 91%, Professional dall'84% all'82% e Basic dal 76% al 63%. Dentro Basic, i clienti con più di 12 mesi di tenure restano quasi stabili, quelli tra 6 e 12 mesi scendono dal 73% al 70%, mentre i clienti con meno di 6 mesi passano dal 74% al **52%**.

Quando isoliamo questi ultimi, il canale restringe ancora il fenomeno: organic 69%, referral 72%, paid search 48%, affiliate 44%. Le coorti più deboli coincidono inoltre con una promozione del **60% sui primi tre mesi**.

A questo punto sarebbe facile scrivere “lo sconto causa churn”. Ma i dati hanno guadagnato una conclusione più limitata e più utile: **il deterioramento aggregato è concentrato nelle coorti Basic recenti, soprattutto paid e affiliate, acquisite durante la promozione; il ritorno al prezzo pieno è una spiegazione candidata insieme a customer fit e mix di acquisizione**.

La nuova domanda è molto più precisa: quali differenze tra coorti promozionali e comparabili spiegano il minor rinnovo, e quale disegno permetterebbe di separare selezione ed effetto della promozione? A quel punto un altro `groupby` può avere meno valore di un metodo inferenziale o causale diverso.

## Quando fermare l'EDA

L'EDA può teoricamente continuare all'infinito. Conviene fermarsi quando sappiamo dove si concentra il fenomeno, i pattern principali hanno superato sensitivity check ragionevoli, fatti e ipotesi sono separati e le spiegazioni concorrenti più importanti sono esplicite. Se la domanda successiva richiede inferenza, esperimento, causalità o forecasting, continuare a produrre grafici non rende la conclusione più forte.

> **L'output dell'EDA non è “ho guardato i dati”. È una rappresentazione più precisa di ciò che sappiamo, di quanto è robusto e della domanda che merita il prossimo investimento analitico.**
