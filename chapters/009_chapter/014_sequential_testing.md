## 9.13 Sequential testing: guardare i risultati durante il test senza ingannarsi

Nella pratica, quasi nessun team aspetta passivamente la fine di un esperimento senza guardare i risultati. Il problema è che osservare continuamente il p-value e fermarsi appena scende sotto 0,05 aumenta la probabilità di falsi positivi.

Questo comportamento è noto come **peeking**: il team controlla i risultati ogni giorno, o ogni ora, e interrompe il test nel momento più favorevole.

### Caso simulato — StreamNow

StreamNow testa una nuova pagina di pricing.

Dopo 3 giorni:

- control conversion: 6,2%
- treatment conversion: 6,8%
- p-value: 0,041

Il product manager propone di fermare immediatamente il test e lanciare la nuova pagina.

Il team data decide invece di continuare secondo il piano prestabilito.

Dopo 14 giorni:

- control conversion: 6,31%
- treatment conversion: 6,38%
- differenza: +0,07 punti percentuali
- risultato non statisticamente significativo

La vittoria iniziale era rumore.

### Perché succede

Ogni volta che controlliamo il test e applichiamo una regola del tipo "fermati se p < 0,05", stiamo aggiungendo un'altra opportunità di fermarci su una fluttuazione casuale favorevole.

Il problema non è guardare i dati in sé. Il problema è applicare una regola di decisione che non tiene conto dei controlli ripetuti.

### Due strategie corrette

#### 1. Fixed horizon

Prima del test si definiscono:

- durata;
- sample size;
- MDE;
- metriche;
- regola finale di decisione.

Poi si analizza formalmente il risultato alla fine della finestra.

#### 2. Sequential testing

Si usa una metodologia statistica progettata per consentire analisi intermedie controllando comunque l'errore di tipo I.

Il concetto importante per un Data Analyst non è memorizzare tutte le formule, ma capire che:

> **se il processo decisionale cambia, deve cambiare anche il metodo statistico.**

### Quando fermarsi prima per motivi di sicurezza

Esiste una differenza importante tra fermare un test perché il risultato business sembra positivo e fermarlo perché una guardrail metric indica un danno serio.

Se durante un esperimento emergono:

- crash rate molto più alto;
- errori di pagamento;
- perdita dati;
- rischio sicurezza;
- danni finanziari evidenti;

il test può e deve essere fermato secondo regole operative prestabilite.

Questo non è p-hacking. È risk management.

### Regola pratica

Prima di iniziare un esperimento, il team dovrebbe scrivere esplicitamente:

- quando è consentito guardare i risultati;
- quali criteri consentono uno stop anticipato;
- quali metriche possono causare un rollback immediato;
- quale metodo statistico supporta il processo scelto.
