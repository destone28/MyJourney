
from datetime import datetime
from . import geodecoder, geo_db_locator

def produci_guida(request):
        ### INFO GENERICHE
        guida = {}



        guida['a'] = "<h1><u>Ecco la tua guida</u></h1>"



        guida['b'] = "<h2><u>Per quanto riguarda i tuoi dati anagrafici e quelli relativi ai tuoi familiari dovrai produrre la seguente documentazione:</u></h2>"

        guida['b1'] = "<li>Il tuo passaporto</li>"
        guida['b2'] = "<li>Il tuo codice fiscale</li>"

        #Se permesso valido
        if ('ricevuta_rinnovo_permesso' not in request.session):
            guida['b3_1'] = "<li>La tua carta di soggiorno o del permesso di soggiorno</li>"

        #Se permesso scaduto
        if (str(request.session.get('ricevuta_rinnovo_permesso'))=='si'):
            guida['b3_2'] = "<li>Il tuo permesso scaduto, accompagnato da ricevuta di presentazione dell'istanza di rinnovo</li>"

        città = str(request.session.get('città'))
        guida['b4'] = "<li>Certificato dello stato di famiglia rilasciato dal Comune di Milano con la dicitura 'uso immigrazione'</li>"

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
            guida['b7'] = "<li>Dichiarazione di impegno a sottoscrivere una polizza assicurativa sanitaria o altro titolo idoneo a garantire la copertura di tutti i rischi nel territorio nazionale, in favore dei genitori ultrasessantacinquenni.<br>I tuoi genitori potranno ricevere il visto per entrare in Italia solo se hanno più di 65 anni e se i tuoi fratelli hanno gravi problemi di salute.</li>"

        guida['b5'] = "<li>Fotocopie delle pagine con dati anagrafici e numero di Passaporto per "+ parente + "</li>"

        ##Per ogni coinquilino
        if (str(request.session.get('n_tot_coinquilini'))=="None"):
            request.session['n_tot_coinquilini'] = 0
        if (int(request.session.get('n_tot_coinquilini'))!=0):
            guida['b6'] = "<li>Certificato dello stato di famiglia delle persone che abitano nel tuo alloggio, rilasciato dal loro Comune di residenza con la dicitura 'uso immigrazione'</li>"

        guida['c'] = "<h2><u>Le informazioni e la documentazione da procurarti per l'alloggio sono le seguenti:</u></h2>"

        #Se contratto di locazione
        if (('contratto_locazione_registrato' in request.session) or ('atto_compravendita' in request.session) or (request.session.get('posso_ospitare_in_alloggio')=='ospite')):
            if (str(request.session.get('contratto_locazione_registrato'))=="si"):
                alloggio = "locazione registrato"
                guida['c2_1'] = "<li>Ricevuta di registrazione e/o rinnovo del contratto di locazione</li>"
                #Se proprietario
            elif (str(request.session.get("atto_compravendita"))=="si"):
                alloggio = "compravendita"
                if (str(request.session.get("posso_ospitare_in_alloggio"))=="ospite"):
                    alloggio = alloggio+ " e comodato d'uso"
                    guida['c2_2'] = "<li>Dichiarazione redatta dal titolare/i dell’appartamento su mod. “S2”, attestante il consenso ad ospitare anche i ricongiunti</li>"
                    guida['c2_3'] = "<li>Fotocopia del documento d’identità del titolare/i dell’alloggio, firmata dal medesimo/i</li>"
                    guida['c1'] = "<li>Contratto di "+ alloggio +" per l'alloggio, di durata non inferiore a sei mesi a decorrere dalla data di presentazione della domanda</li>"


        guida['c3'] = "<li>Certificato di idoneità abitativa e igienico-sanitaria, rilasciata dal Comune di Milano per finalità di ricongiungimento familiare</li>"

        guida['d'] = "<h2><u>Per certificare le informazioni sul lavoro dovrai invece fornire i seguenti documenti:</u></h2>"

        guida['d1'] = "<li>Certificazione Unica (C.U. ex C.U.D)</li>"


        #Se lavoratore dipendente
        if (str(request.session.get('tipologia_lavoro'))=="dipendente"):
            guida['d1'] = "<li>Certificazione Unica (C.U. ex C.U.D)</li>"
            guida['d2'] = "<li>Fotocopia del contratto di lavoro/lettera di assunzione (modulo C/Ass - Unilav)</li>"
            guida['d3_1'] = "<li>Ultime tre buste paga</li>"
            guida['d3_2'] = "<li>Autocertificazione del datore di lavoro, redatta su modello 'S3' con data non anteriore ad un mese, da cui risulti l'attualità del rapporto di lavoro e la retribuzione mensile corrisposta</li>"
            guida['d3_3'] = "<li>Fotocopia del documento d'identità del datore di lavoro, debitamente firmata dal medesimo</li>"

        #Se lavoratore domestico
        if (str(request.session.get('tipologia_lavoro'))=="domestico"):
            guida['d1'] = "<li>Ultima dichiarazione dei redditi, ove posseduta</li>"
            guida['d2'] = "<li>Comunicazione di assunzione al Centro per l’Impiego o all’INPS</li>"
            guida['d3_1'] = "<li>Ultimo bollettino di versamento dei contributi INPS, con attestazione dell’avvenuto pagamento</li>"
            guida['d3_2'] = "<li>Autocertificazione del datore di lavoro, redatta su modello “S3”, con data non anteriore di mesi 1 da cui risulti l’attualità del rapporto di lavoro e la retribuzione mensile corrisposta</li>"
            guida['d3_3'] = "<li>Fotocopia del documento d’identità del datore di lavoro, debitamente firmata dal medesimo</li>"

        #Se lavoratore titolare di ditta individuale
        if (str(request.session.get('tipologia_lavoro'))=="titolare_ditta"):
            guida['d1'] = "<li>Visura camerale/certificato di iscrizione alla Camera di Commercio recente</li>"
            guida['d2'] = "<li>Certificato di attribuzione P. IVA</li>"
            guida['d3_1'] = "<li>Licenza comunale, ove prevista</li>"
            guida['d3_2'] = "<li>Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta</li>"
            guida['d3_3'] = "<li>Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visuracamerale aggiornata inerente l’attività svolta</li>"
            guida['d3_4'] = "<li>Tutte le fatture relative all’anno in corso</li>"

        #Se lavoratore con partecipazione in società
        if (str(request.session.get('tipologia_lavoro'))=="partecipazione_società"):
            guida['d1'] = "<li>Visura camerale della società, di data recente</li>"
            guida['d2'] = "<li>Certificato di attribuzione P. IVA</li>"
            guida['d3_1'] = "<li>Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta;</li>"
            guida['d3_2'] = "<li>Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta</li>"

        #Se socio lavoratore
        if (str(request.session.get('tipologia_lavoro'))=="socio_lavoratore"):
            guida['d1'] = "<li>Visura camerale della cooperativa</li>"
            guida['d2'] = "<li>Certificato di attribuzione P. IVA</li>"
            guida['d3_1'] = "<li>Dichiarazione del presidente della cooperativa da cui risulti l’attualità del rapporto di lavoro</li>"
            guida['d3_2'] = "<li>Dichiarazione dei redditi (modello UNICO), ove posseduto</li>"
            guida['d3_3'] = "<li>Ultime tre buste paga</li>"
            guida['d3_4'] = "<li>Fotocopia del contratto di lavoro/lettera di assunzione (modulo C/Ass – Unilav)</li>"

        #Se libero professionista
        if (str(request.session.get('tipologia_lavoro'))=="libero_professionista"):
            guida['d1'] = "<li>Iscrizione all’albo del libero professionista</li>"
            guida['d2'] = "<li>Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta</li>"
            guida['d3_1'] = "<li>Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta</li>"

        guida['e'] = "<h2><u>Infine, eccoti qualche informazione aggiuntiva:</u></h2>"
        guida['f'] = "Puoi richiedere aiuto presso:<br>"+str(geo_db_locator.sindacati_e_patronati(request.session.get('indirizzo_alloggio')+","+str(request.session.get('città'))))
        guida['g'] = "Il municipio di riferimento per i servizi anagrafici è:<br>"+str(geo_db_locator.anagrafe_milano_piu_vicina(request.session.get('indirizzo_alloggio')+","+str(request.session.get('città'))))
        guida['h'] = "Per l'idoneità abitativa della tua casa:<br>"+str(geo_db_locator.idoneita_abitativa_vicina_milano(request.session.get('indirizzo_alloggio')+","+str(request.session.get('città'))))
        guida['i'] = "Ti occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€."


        return guida
