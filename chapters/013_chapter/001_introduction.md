# Capitolo 13 — Scegliere lo strumento giusto senza diventarne dipendenti

Un Data Analyst moderno lavora in un ecosistema pieno di strumenti: fogli di calcolo, SQL, Python, R, notebook, strumenti di BI, servizi cloud, workflow visuali, automazioni no-code e assistenti AI.

Il rischio è confondere la disponibilità di uno strumento con la necessità di usarlo.

Un problema semplice può essere trasformato in una pipeline distribuita, un'analisi esplorativa può diventare un progetto software, un dashboard può essere usato come sostituto di una domanda non definita e uno script Python può essere scritto per fare qualcosa che una pivot table avrebbe risolto meglio in tre minuti.

La competenza non consiste nel conoscere il maggior numero possibile di strumenti. Consiste nel riconoscere quale combinazione di strumenti riduce più rapidamente l'incertezza con un livello accettabile di affidabilità, ripetibilità, costo e complessità.

## 13.0.1 Il criterio non è: «Quale tool conosco meglio?»

La domanda corretta è:

> **Qual è lo strumento più semplice che risolve bene questo problema senza creare un costo futuro sproporzionato?**

Questa frase contiene quattro criteri:

1. **semplicità** — quanta complessità introduciamo;
2. **adeguatezza** — lo strumento supporta davvero il tipo di analisi necessario;
3. **affidabilità** — il risultato può essere verificato e riprodotto;
4. **costo futuro** — manutenzione, scalabilità, governance e passaggio ad altri utenti.

## 13.0.2 Un caso realistico: il forecast che diventa un progetto software

Una società B2B deve stimare i ricavi del trimestre successivo per un board meeting tra due giorni.

I dati sono già disponibili in un file con 4.800 opportunità commerciali e contengono:

- valore dell'opportunità;
- probabilità commerciale;
- data prevista di chiusura;
- segmento;
- account executive;
- storico delle modifiche recenti.

Il primo impulso del team analytics è costruire una pipeline Python, salvare i dati su un database locale e sviluppare un notebook parametrico.

Tecnicamente è possibile. Ma il vero problema è una stima una tantum con forte componente di judgment commerciale.

Per il primo ciclo, Excel o un foglio equivalente con Power Query, pivot, scenari e controlli espliciti può essere una scelta migliore: più veloce, più trasparente per Finance e Sales, e più facile da discutere durante il meeting.

Tre mesi dopo, se il processo diventa ricorrente, con dati provenienti da CRM, ERP e billing, allora la scelta cambia: SQL, modello dati stabile, pipeline automatizzata e semantic layer diventano più sensati.

La lezione non è che Excel sia migliore di Python.

La lezione è che **la scelta dipende dallo stadio del problema**.

## 13.0.3 Il framework di scelta

Prima di aprire uno strumento, valutiamo almeno queste dimensioni:

| Dimensione | Domanda |
|---|---|
| Frequenza | È una tantum o ricorrente? |
| Volume | Centinaia, milioni o miliardi di righe? |
| Complessità | Filtri e aggregazioni o modelli/algoritmi avanzati? |
| Collaborazione | Una persona o un'intera organizzazione? |
| Riproducibilità | Deve essere rifatto identico tra sei mesi? |
| Governance | Il dato è sensibile o regolamentato? |
| Freschezza | Batch giornaliero o quasi real time? |
| Auditing | Possiamo spiegare come nasce ogni numero? |
| Deployment | Il risultato resta un'analisi o diventa un processo operativo? |
| Costo | Quanto costa sviluppare, eseguire e mantenere? |

## 13.0.4 La maturità cambia lo strumento

Uno stesso problema può attraversare una sequenza naturale:

**foglio di calcolo → query SQL → notebook → pipeline → semantic model → dashboard/servizio operativo**

Non è obbligatorio percorrere tutti i passaggi.

Un buon analista riconosce quando fermarsi.

Una soluzione è abbastanza matura quando soddisfa il bisogno decisionale con un livello accettabile di rischio. Aggiungere architettura oltre quel punto può essere spreco.

## 13.0.5 L'AI cambia il costo della sintassi

Gli assistenti AI possono scrivere formule, SQL, codice Python, DAX e trasformazioni Power Query. Questo riduce il costo di esecuzione, ma aumenta il rischio di usare con grande velocità lo strumento sbagliato.

Un prompt può generare una query SQL perfettamente valida su un join semanticamente errato. Può costruire un modello Python sofisticato su un target contaminato da leakage. Può generare un dashboard elegante su un KPI mal definito.

Per questo, nell'era AI la domanda «come si scrive?» perde parte del suo valore, mentre diventano più importanti:

- perché lo stiamo facendo;
- quale dato serve;
- qual è il grain corretto;
- quale metodo è appropriato;
- quale strumento rende il processo più controllabile;
- come verifichiamo il risultato.

## 13.0.6 Il principio guida del capitolo

> **Lo strumento giusto non è quello più potente. È quello che minimizza il costo totale di ottenere una risposta affidabile.**

Nei prossimi paragrafi confronteremo Excel, SQL, Python/R, notebook, BI, cloud e no-code non come categorie concorrenti, ma come elementi complementari di una stessa cassetta degli attrezzi analitica.
