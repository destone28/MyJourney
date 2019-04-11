# MyJourney

Progetto vincitore dell'hackathon "services4MIgrants" - 10-11 marzo 2018 organizzato da Comune di Milano e Politecnico di Milano ( https://dati.comune.milano.it/hackathon2018 ).

Webapp sviluppata per il Comune di Milano da Emilio Destratis per conto della squadra TeamBallo.

## Perché
Lo scopo della webapp è quello di fornire uno strumento per semplificare il percorso di richiesta di ricongiungimento familiare da parte dei migranti extracomunitari.

La webapp fornisce un aiuto nella raccolta dei documenti necessari all'ottenimento del Nulla Osta per il ricongiungimento.

## Come
Il progetto si articola in un questionario che raccoglie informazioni sull'utente e dinamicamente cambia percorso per raccogliere solo le informazioni necessarie per quelle che sono le necessità dell'utente.

Alla fine del questionario, se l'utente è provvisto dei requisiti necessari, la webapp produce una guida personalizzata sulla base delle necessità dell'utente, in modo tale da permettere all'utente di scaricare il suo prontuario personale da consultare in qualsiasi momento.

### Specifiche tecniche

La webapp è sviluppata utilizzando le seguenti tecnologie:
- backend in Python3.5 con supporto del framework Django2.1.2;
- front-end in Html5, CSS e JavaScript con JQuery, Bootstrap e VueJS;

### Installazione

La webapp è stata caricata e testata su Ubuntu Server 16.04, ed i passi proposti qui sono stati effettuati in questo ambiente.

#### Requisiti
- Ubuntu Server 16.04
- python3.5 o python 3.6 (installazione indicata con python3.5)

#### Procedura d'installazione

1. Creare una nuova cartella nella quale si avranno permessi di lettura/scrittura

`mkdir nuova_cartella`

2. Posizionarsi in una nuova cartella e clonare questo repository

`cd nuova_cartella`
`git clone https://github.com/destone28/MyJourney.git`

3. Entrare nella nuova cartella scaricata "MyJourney"

`cd nuova_cartella`

4. Installare `pip` (possono esser necessari permessi da superutente)

`apt-get install python-pip`

5. Installare `virtualenv` per creare un ambiente virtuale nel quale far girare la webapp

`pip install virtualenv`

6. Creare l'ambiente virtuale ed accedervi

`virtualenv --python=python3.5 nuovo_ambiente`

7. Installare qui le dipendenze della webapp

`pip install django geopy`

8. Far partire la webapp

`python3.5 manage.py runserver 0.0.0.0:8000`

*9. (non sempre necessaria) Nel caso in cui vi fossero migrazioni di database da effettuare (messaggi come "You have 2 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth.
Run 'python manage.py migrate' to apply them."*), correggere come indicato
           
