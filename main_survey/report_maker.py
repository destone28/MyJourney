
from datetime import datetime
from . import geodecoder, geo_db_locator

def produci_guida(request):
        ### INFO GENERICHE
        guida = {}



        guida['a'] = "<h1><u>Ciao! Ecco la tua guida</u></h1>"



        guida['b'] = "<h2><u>Per quanto riguarda i tuoi dati anagrafici e quelli relativi ai tuoi familiari dovrai produrre la seguente documentazione:</u></h2>"

        guida['b1'] = "Il tuo passaporto"
        guida['b2'] = "Il tuo codice fiscale"

        #Se permesso valido
        if ('ricevuta_rinnovo_permesso' not in request.session):
            guida['b3_1'] = "La tua carta di soggiorno o del permesso di soggiorno"

        #Se permesso scaduto
        if (str(request.session.get('ricevuta_rinnovo_permesso'))=='si'):
            guida['b3_2'] = "Il tuo permesso scaduto, accompagnato da ricevuta di presentazione dell'istanza di rinnovo"

        città = str(request.session.get('città'))
        guida['b4'] = "Certificato dello stato di famiglia rilasciato dal Comune di "+ città +" con la dicitura 'uso immigrazione'"

        ##Per ogni parente presente

        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        parente = ""
        if ('partner_mag' in familiari_temp):
            parente = parente+" partner"
        if ('figli_min_ug_14' or 'figli_15_17' or 'figli_magg' in familiari_temp):
            parente = parente+" figlio"
        if ('genitori' in familiari_temp):
            parente = parente+" genitore"
            ##Se ci sono genitori_mag_ug_65
            guida['b7'] = "Dichiarazione di impegno a sottoscrivere una polizza assicurativa sanitaria o altro titolo idoneo a garantire la copertura di tutti i rischi nel territorio nazionale, in favore dei genitori ultrasessantacinquenni."

        guida['b5'] = "Fotocopie delle pagine con dati anagrafici e numero di Passaporto per "+ parente

        ##Per ogni coinquilino
        if (str(request.session.get('n_tot_coinquilini'))=="None"):
            request.session['n_tot_coinquilini'] = 0
        if (int(request.session.get('n_tot_coinquilini'))!=0):
            guida['b6'] = "Certificato dello stato di famiglia delle persone che abitano nel tuo alloggio, rilasciato dal loro Comune di residenza con la dicitura 'uso immigrazione'"

        guida['c'] = "<h2><u>Le informazioni e la documentazione da procurarti per l'alloggio sono le seguenti:</u></h2>"

        #Se contratto di locazione
        if (('contratto_locazione_registrato' in request.session) or ('atto_compravendita' in request.session) or (request.session.get('posso_ospitare_in_alloggio')=='ospite')):
            if (str(request.session.get('contratto_locazione_registrato'))=="si"):
                alloggio = "locazione registrato"
                guida['c2_1'] = "Ricevuta di registrazione e/o rinnovo del contratto di locazione"
                #Se proprietario
            elif (str(request.session.get("atto_compravendita"))=="si"):
                alloggio = "compravendita"
                if (str(request.session.get("posso_ospitare_in_alloggio"))=="ospite"):
                    alloggio = alloggio+ " e comodato d'uso"
                    guida['c2_2'] = "Dichiarazione redatta dal titolare/i dell’appartamento su mod. “S2”, attestante il consenso ad ospitare anche i ricongiunti"
                    guida['c2_3'] = "Fotocopia del documento d’identità del titolare/i dell’alloggio, firmata dal medesimo/i"
                    guida['c1'] = "Contratto di "+ alloggio +" per l'alloggio, di durata non inferiore a sei mesi a decorrere dalla data di presentazione della domanda"


        guida['c3'] = "Certificato di idoneità abitativa e igienico-sanitaria, rilasciata dal Comune di "+ città +" per finalità di ricongiungimento familiare"

        guida['d'] = "<h2><u>Per certificare le informazioni sul lavoro dovrai invece fornire i seguenti documenti:</u></h2>"

        guida['d1'] = "Certificazione Unica (C.U. ex C.U.D)"


        #Se lavoratore dipendente
        if (str(request.session.get('tipologia_lavoro'))=="dipendente"):
            guida['d1'] = "Certificazione Unica (C.U. ex C.U.D)"
            guida['d2'] = "Fotocopia del contratto di lavoro/lettera di assunzione (modulo C/Ass - Unilav)"
            guida['d3_1'] = "Ultime tre buste paga"
            guida['d3_2'] = "Autocertificazione del datore di lavoro, redatta su modello 'S3' con data non anteriore ad un mese, da cui risulti l'attualità del rapporto di lavoro e la retribuzione mensile corrisposta"
            guida['d3_3'] = "Fotocopia del documento d'identità del datore di lavoro, debitamente firmata dal medesimo"

        #Se lavoratore domestico
        if (str(request.session.get('tipologia_lavoro'))=="domestico"):
            guida['d1'] = "Ultima dichiarazione dei redditi, ove posseduta"
            guida['d2'] = "Comunicazione di assunzione al Centro per l’Impiego o all’INPS"
            guida['d3_1'] = "Ultimo bollettino di versamento dei contributi INPS, con attestazione dell’avvenuto pagamento"
            guida['d3_2'] = "Autocertificazione del datore di lavoro, redatta su modello “S3”, con data non anteriore di mesi 1 da cui risulti l’attualità del rapporto di lavoro e la retribuzione mensile corrisposta"
            guida['d3_3'] = "Fotocopia del documento d’identità del datore di lavoro, debitamente firmata dal medesimo"

        #Se lavoratore titolare di ditta individuale
        if (str(request.session.get('tipologia_lavoro'))=="titolare_ditta"):
            guida['d1'] = "Visura camerale/certificato di iscrizione alla Camera di Commercio recente"
            guida['d2'] = "Certificato di attribuzione P. IVA"
            guida['d3_1'] = "Licenza comunale, ove prevista"
            guida['d3_2'] = "Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta"
            guida['d3_3'] = "Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visuracamerale aggiornata inerente l’attività svolta"
            guida['d3_4'] = "Tutte le fatture relative all’anno in corso"

        #Se lavoratore con partecipazione in società
        if (str(request.session.get('tipologia_lavoro'))=="partecipazione_società"):
            guida['d1'] = "Visura camerale della società, di data recente"
            guida['d2'] = "Certificato di attribuzione P. IVA"
            guida['d3_1'] = "Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta;"
            guida['d3_2'] = "Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta"

        #Se socio lavoratore
        if (str(request.session.get('tipologia_lavoro'))=="socio_lavoratore"):
            guida['d1'] = "Visura camerale della cooperativa"
            guida['d2'] = "Certificato di attribuzione P. IVA"
            guida['d3_1'] = "Dichiarazione del presidente della cooperativa da cui risulti l’attualità del rapporto di lavoro"
            guida['d3_2'] = "Dichiarazione dei redditi (modello UNICO), ove posseduto"
            guida['d3_3'] = "Ultime tre buste paga"
            guida['d3_4'] = "Fotocopia del contratto di lavoro/lettera di assunzione (modulo C/Ass – Unilav)"

        #Se libero professionista
        if (str(request.session.get('tipologia_lavoro'))=="libero_professionista"):
            guida['d1'] = "Iscrizione all’albo del libero professionista"
            guida['d2'] = "Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta"
            guida['d3_1'] = "Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta"

        guida['e'] = "<h2><u>Infine, eccoti qualche informazione aggiuntiva:</u></h2>"
        guida['f'] = "Puoi richiedere aiuto presso:\n"+str(geo_db_locator.sindacati_e_patronati(str(request.session.get('indirizzo_alloggio'))))
        guida['g'] = "Il municipio di riferimento per i servizi anagrafici è:\n"+str(geo_db_locator.anagrafe_milano_piu_vicina(str(request.session.get('indirizzo_alloggio'))))
        guida['h'] = "Per l'idoneità abitativa della tua casa:\n"+str(geo_db_locator.idoneita_abitativa_vicina_milano(str(request.session.get('indirizzo_alloggio'))))
        guida['i'] = "Ti occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€."


        return guida
