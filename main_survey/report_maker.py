
from datetime import datetime
from . import geodecoder, geo_db_locator

def produci_guida(request):
        ### INFO GENERICHE
        guida = {}



        guida['a'] = "Ciao! Ecco la tua guida"



        guida['b'] = "Per quanto riguarda i tuoi dati anagrafici e quelli relativi ai tuoi familiari dovrai produrre la seguente documentazione:"

        guida['b1'] = "Il tuo passaporto"
        guida['b2'] = "Il tuo codice fiscale"

        ##Se permesso valido
        guida['b3_1'] = "La tua carta di soggiorno o del permesso di soggiorno"
        ##
        guida['b3_2'] = "Il tuo permesso scaduto, accompagnato da ricevuta di presentazione dell'istanza di rinnovo"

        guida['b4'] = "Certificato dello stato di famiglia rilasciato dal Comune di "+ città_indirizzo +" con la dicitura 'uso immigrazione'"

        ##Per ogni parente presente
        guida['b5'] = "Fotocopie delle pagine con dati anagrafici e numero di Passaporto del tuo "+ parente

        ##Per ogni coinquilino
        guida['b6'] = "Certificato dello stato di famiglia delle persone che abitano nel tuo alloggio, rilasciato dal loro Comune di residenza con la dicitura 'uso immigrazione'"

        ##Se ci sono genitori_mag_ug_65
        guida['b7'] = "Dichiarazione di impegno a sottoscrivere una polizza assicurativa sanitaria o altro titolo idoneo a garantire la copertura di tutti i rischi nel territorio nazionale, in favore dei genitori ultrasessantacinquenni."




        guida['c'] = "Le informazioni e la documentazione da procurarti per l'alloggio sono le seguenti:"

        guida['c1'] = "Contratto di "+ alloggio +" di durata non inferiore a sei mesi a decorrere dalla data di presentazione della domanda"

        #Se contratto di locazione
        guida['c2_1'] = "Ricevuta di registrazione e/o rinnovo del contratto di locazione"

        guida['c3'] = "Certificato di idoneità abitativa e igienico-sanitaria, rilasciata dal Comune di "+ città_indirizzo +" per finalità di ricongiungimento familiare"




        guida['d'] = "Per certificare le informazioni sul lavoro dovrai invece fornire i seguenti documenti:"

        guida['d1'] = "Certificazione Unica (C.U. ex C.U.D)"

        guida['d2'] = "Fotocopia di "+ sceltaTraContrattoDiLavoroELetteraDiAssunzione +" (modulo C/Ass - Unilav)"

        ##Se dipendente
        guida['d3_1'] = "Ultime tre buste paga"
        guida['d3_2'] = "Autocertificazione del datore di lavoro, redatta su modello 'S3' con data non anteriore ad un mese, da cui risulti l'attualità del rapporto di lavoro e la retribuzione mensile corrisposta"
        guida['d3_3'] = "Fotocopia del documento d'identità del datore di lavoro, debitamente firmata dal medesimo"

        ###AGGIUNGERE DATI PER LAVORO AUTONOMO ECC...

        guida['e'] = "Infine, eccoti qualche informazione aggiuntiva:"
        guida['f'] = "Puoi richiedere aiuto presso:\n"+str(geo_db_locator.sindacatipatronati(str(request.session.get('indirizzo_alloggio'))))
        guida['g'] = "Il municipio di riferimento per i servizi anagrafici è:\n"+str(geo_db_locator.anagrafe_milano_piu_vicina(str(request.session.get('indirizzo_alloggio'))))
        guida['h'] = "Per l'idoneità abitativa della tua casa:\n"+str(geo_db_locator.idoneita_abitativa_vicina_milano(str(request.session.get('indirizzo_alloggio'))))
        guida['i'] = "Ti occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€."


        return guida
