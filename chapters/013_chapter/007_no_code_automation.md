## 13.6 No-code e low-code: automatizzare senza trasformare tutto in software
Gli strumenti no-code e low-code occupano una zona importante tra il foglio manuale e lo sviluppo software completo.

Possono collegare sorgenti, applicare trasformazioni, schedulare flussi, inviare notifiche, aggiornare file e orchestrare piccoli processi senza richiedere un'applicazione custom.

Il loro valore principale è ridurre il costo dell'automazione per processi relativamente semplici e ben definiti.

## 13.6.1 Caso realistico: il report del lunedì

Ogni lunedì un analyst:

1. scarica un CSV dal CRM;
2. scarica un file dal billing;
3. aggiorna una tabella di mapping;
4. unisce i dati;
5. genera un report;
6. invia il PDF a 18 manager.

Il processo richiede circa 90 minuti e viene ripetuto 50 volte l'anno.

Non serve necessariamente costruire un'applicazione Python completa. Un workflow Power Query/BI o una piattaforma low-code può automatizzare gran parte del lavoro.

Il beneficio non è solo risparmiare 75 ore all'anno. È ridurre:

- errori manuali;
- dimenticanze;
- dipendenza da una singola persona;
- variazioni nel processo.

## 13.6.2 Quando il no-code funziona bene

È adatto quando:

- il flusso è lineare;
- le sorgenti sono supportate;
- le regole sono semplici;
- il volume è moderato;
- il workflow è facilmente osservabile;
- il costo di una soluzione custom non è giustificato.

## 13.6.3 Quando diventa un labirinto

Un workflow visuale può sembrare semplice finché ha dieci blocchi.

Con cento nodi, condizioni annidate, retry, loop, mapping dinamici e chiamate API, il no-code può diventare più difficile da comprendere del codice.

### Caso realistico: 146 blocchi e nessuno sa più cosa succede

Un team Operations costruisce nel tempo un'automazione per riconciliare ordini, pagamenti e refund.

Il workflow raggiunge 146 blocchi e include:

- 11 branch condizionali;
- 8 retry;
- 4 integrazioni API;
- logica duplicata;
- eccezioni aggiunte manualmente.

Quando cambia il provider di pagamento, nessuno riesce a prevedere l'effetto completo della modifica.

Il processo era nato per evitare software engineering. È diventato software engineering senza gli strumenti tipici dello sviluppo software.

## 13.6.4 Il criterio di uscita

Un processo low-code dovrebbe migrare verso codice o piattaforma dati più strutturata quando aumentano:

- complessità;
- criticità;
- volume;
- requisiti di testing;
- necessità di versionamento;
- branching;
- gestione degli errori;
- dipendenze.

## 13.6.5 Automazione non significa analisi

Automatizzare un processo sbagliato significa produrre più velocemente risultati sbagliati.

Prima di automatizzare, chiediamoci:

- la metrica è definita?
- la sorgente è affidabile?
- le eccezioni sono note?
- il processo è abbastanza stabile?
- sappiamo cosa deve succedere se una sorgente manca?

> **Automatizzare è una decisione di industrializzazione. Prima bisogna essere sicuri di voler industrializzare proprio quel processo.**
