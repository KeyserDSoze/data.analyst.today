# Capitolo 0 — Al timone

## L'AI può fare il lavoro. La responsabilità resta tua.

Per gran parte della storia dell'analisi dati, essere bravi significava anche saper eseguire personalmente molte attività.

Scrivere query. Pulire file. Costruire formule. Cercare errori. Preparare grafici. Scrivere codice. Leggere documentazione. Creare presentazioni.

L'AI cambia radicalmente questo equilibrio.

Un analista può oggi chiedere a un sistema di:

- esplorare uno schema dati;
- generare SQL;
- scrivere Python;
- controllare data quality;
- costruire un forecast;
- cercare anomalie;
- proporre ipotesi;
- verificare una query;
- preparare grafici;
- scrivere una sintesi per il management.

E può farlo non più soltanto con un singolo assistente, ma con più agenti specializzati che lavorano in parallelo.

Questo potrebbe sembrare il momento in cui l'analista perde importanza.

È probabilmente il contrario.

Quando l'esecuzione diventa abbondante, economica e velocissima, aumenta il valore di chi sa decidere:

- cosa chiedere;
- a chi delegarlo;
- quali dati usare;
- quali assunzioni sono accettabili;
- come verificare;
- quando fermarsi;
- cosa non automatizzare;
- quale conclusione è abbastanza solida da diventare una decisione.

La competenza si sposta dall'eseguire tutto personalmente al **governare un sistema capace di eseguire molto più di quanto una singola persona potrebbe fare**.

Ma c'è una condizione.

Dobbiamo restare al timone.

## La frase che non dovrebbe mai bastare

Immaginiamo un meeting.

Il CFO chiede perché il forecast inviato la settimana precedente fosse sbagliato del 18%.

L'analista risponde:

> “Non lo so. L'ha fatto l'AI.”

Questa frase sembra una spiegazione tecnica.

Non lo è.

È la dichiarazione che nessuno aveva realmente la responsabilità del processo.

Se utilizziamo un agente per scrivere una query e la query duplica la revenue, il fatto che non abbiamo scritto personalmente il `JOIN` non elimina la nostra responsabilità professionale.

Se un agente genera un modello con leakage, non possiamo difenderci dicendo che il modello è stato costruito automaticamente.

Se un sistema suggerisce di bloccare una campagna, cambiare un prezzo o intervenire su clienti ad alto rischio, dobbiamo sapere quali evidenze sostengono la decisione.

Il nuovo standard professionale non può essere:

> “L'ho fatto io.”

Ma nemmeno:

> “L'ha fatto l'AI.”

Deve diventare:

> **“Posso spiegare come è stato prodotto, quali controlli abbiamo eseguito, dove potrebbe sbagliare e perché ritengo il risultato sufficientemente affidabile per questa decisione.”**

## Un'analogia utile: manager, non passeggero

Pensiamo a un manager con dieci collaboratori.

Il manager non svolge personalmente ogni attività del team. Non scrive ogni documento, non calcola ogni numero e non partecipa a ogni analisi.

Ma un buon manager deve sapere:

- chi sta facendo cosa;
- quali obiettivi sono stati assegnati;
- quali dipendenze esistono;
- quali risultati richiedono review;
- quando una persona sta andando nella direzione sbagliata;
- quali problemi devono essere escalati;
- quando una decisione può essere presa.

Con gli agenti AI succede qualcosa di simile, con una differenza fondamentale: questi collaboratori possono lavorare a una velocità enorme e produrre quantità di output impossibili da verificare riga per riga con i metodi tradizionali.

Questo richiede una nuova disciplina.

**Non dobbiamo controllare tutto manualmente. Dobbiamo progettare un sistema di controllo.**

## L'AI moltiplica capacità e errori

Un analista umano può scrivere cinque query sbagliate in una giornata.

Un sistema agentico può generarne cinquecento.

Può anche generare cinquecento query corrette.

Il punto è che la velocità amplifica entrambe le possibilità.

La produttività non è quindi:

**più output per unità di tempo.**

È:

**più output utile e affidabile per unità di tempo.**

Una pipeline che genera cento analisi al giorno ma richiede continue correzioni può essere meno produttiva di una che ne genera dieci e mantiene alta affidabilità.

Da qui una delle tesi fondamentali di questo libro:

> **La velocità senza supervisione non è produttività. È capacità di produrre errori più velocemente.**

## La nuova catena professionale

Nel lavoro AI-native, il processo dovrebbe assomigliare a:

**Intento → Delega → Osservazione → Verifica → Critica → Decisione → Responsabilità**

non a:

**Prompt → Output → Copia e incolla**

Il resto di questo capitolo riguarda esattamente questa differenza.
