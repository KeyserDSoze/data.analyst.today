## 16.8 Storytelling senza manipolazione: assi, scale e framing
Ogni visualizzazione seleziona una prospettiva.

La scelta della scala, del periodo, del denominatore e del confronto modifica ciò che appare importante.

Per questo il data storytelling richiede una disciplina etica oltre che tecnica.

## Bar chart: lo zero conta

Per i grafici a barre, la lunghezza della barra rappresenta direttamente la grandezza.

Se l'asse parte da 95 invece che da 0, un passaggio da 98 a 100 può apparire enorme.

L'Office for National Statistics raccomanda che gli assi dei bar chart partano da zero proprio perché una base troncata altera visivamente le proporzioni.

Per line chart e scatter plot la situazione è diversa: un asse troncato può essere utile per rendere visibili variazioni piccole, purché la scala sia chiarissima e non induca una lettura sproporzionata.

Fonte: https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines

## Caso realistico: “performance raddoppiata”

Un team presenta due conversion rate:

- controllo: 4,8%;
- nuova esperienza: 5,1%.

Nel grafico l'asse verticale parte da 4,7%.

La nuova barra sembra quasi tre volte più alta.

Il titolo dice:

> Nuova esperienza nettamente superiore

Il numero è corretto.

La rappresentazione è fuorviante.

La differenza assoluta è 0,3 punti percentuali; quella relativa è circa 6,25%.

E prima ancora di parlare di rollout dobbiamo conoscere incertezza, costi e guardrail.

## Periodi scelti ad arte

Anche la finestra temporale può manipolare.

Una campagna può sembrare eccezionale se confrontiamo la settimana di lancio con quella immediatamente precedente, ma ordinaria rispetto allo stesso periodo dell'anno precedente.

Una metrica può sembrare in crescita scegliendo gennaio come punto iniziale e in calo scegliendo marzo.

Il principio è semplice:

> il periodo deve essere scelto in funzione della domanda, non della storia che vogliamo raccontare.

## Dual axis: correlazioni costruite visivamente

Due serie con scale indipendenti possono essere ridimensionate fino a sembrare quasi perfettamente correlate.

L'ONS raccomanda di evitare i dual-axis chart perché sono difficili da interpretare e possono risultare fuorvianti.

Se vogliamo confrontare due trend, spesso è meglio usare due grafici allineati oppure normalizzare entrambe le serie rispetto a una baseline esplicita.

## Il framing del denominatore

“Il 90% dei clienti è soddisfatto” può significare cose diverse se:

- ha risposto solo il 12% degli invitati;
- il survey è stato mostrato soltanto agli utenti che hanno completato un acquisto;
- sono stati esclusi i reclami aperti;
- la definizione di soddisfatto include punteggi neutrali.

Lo storytelling non può correggere un denominatore sbagliato.

## Il test della versione opposta

Prima di pubblicare una visualizzazione importante, proviamo a chiederci:

> “Con gli stessi dati, potrei costruire un grafico apparentemente convincente che sostiene la conclusione opposta?”

Se la risposta è sì, dobbiamo capire quale scelta di framing produce la differenza e renderla esplicita.

**Un grafico persuasivo non è necessariamente un grafico informativo. Il nostro obiettivo è rendere l'evidenza leggibile senza deformarla.**
