# Capitolo 9 - Experimentation e A/B testing nel mondo reale

> Un A/B test non è un bottone che trasforma una correlazione in causalità. È un sistema operativo per prendere decisioni sotto incertezza, e funziona solo se il disegno sperimentale, i dati e l’interpretazione sono affidabili.

Nei capitoli precedenti abbiamo visto perché la causalità richiede un controfattuale credibile. L’esperimento randomizzato è uno dei modi più forti per costruirlo: se l’assegnazione al trattamento avviene in modo casuale e il test è implementato correttamente, le differenze osservate tra trattamento e controllo possono essere attribuite con molta più fiducia all’intervento.

Ma la pratica è meno pulita dei diagrammi da manuale. Nei sistemi reali succedono cose come:

- utenti assegnati a una variante che non la vedono;
- eventi persi nella telemetria;
- bot filtrati in modo diverso tra gruppi;
- utenti che entrano da più dispositivi;
- metriche che migliorano mentre peggiorano costi o retention;
- team che fermano il test appena compare `p < 0.05`;
- campagne marketing che contaminano contemporaneamente controllo e trattamento;
- marketplace in cui il comportamento di un utente cambia l’esperienza di altri utenti.

Un Data Analyst deve quindi pensare a un esperimento come a una catena:

**ipotesi -> unità di randomizzazione -> assegnazione -> esposizione -> telemetria -> metrica -> analisi -> decisione**

Se uno solo di questi passaggi è difettoso, una conclusione statisticamente elegante può essere operativamente falsa.

## Un caso che useremo come filo conduttore

Immaginiamo una piattaforma e-commerce europea con 4,8 milioni di utenti mensili. Il team checkout vuole introdurre un pulsante di pagamento rapido. Il business case iniziale è semplice:

- conversion rate attuale: 3,92%;
- obiettivo: superare 4,05%;
- margine medio per ordine: 17,40 euro;
- traffico mensile eleggibile: circa 3,1 milioni di sessioni.

Il Product Manager propone: “Facciamo 50/50 per una settimana e se la conversione sale lo lanciamo”.

Sembra ragionevole, ma prima di avviare il test dobbiamo chiarire almeno:

- randomizziamo per sessione, utente o account?
- cosa succede se lo stesso utente usa due device?
- la metrica primaria è conversione sessione->ordine o utente->ordine?
- consideriamo cancellazioni e resi?
- il metodo rapido aumenta frodi o chargeback?
- una settimana contiene abbastanza cicli settimanali?
- cosa facciamo se i gruppi non risultano 50/50?
- possiamo guardare i risultati ogni ora?

Il resto del capitolo risponde a queste domande.

## Obiettivo del capitolo

Alla fine dovresti saper progettare e leggere un esperimento senza ridurlo alla frase “la variante B ha vinto”. Dovresti riuscire a distinguere:

- un vero effetto da un problema di assegnazione;
- una vittoria locale da un danno su una guardrail metric;
- un test con potenza sufficiente da un test inconcludente;
- una fluttuazione temporanea da un effetto stabile;
- un risultato statisticamente significativo da una decisione economicamente sensata.

L’esperimento non elimina il giudizio. Lo rende più disciplinato.