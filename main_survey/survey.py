
from datetime import datetime
from . import geodecoder, geo_db_locator

non_idoneo = 27
idoneo = 28

class Report_maker():

    def produci_guida(request):
        ### INFO GENERICHE
        guida = {}
        guida['a1'] = "Questa guida ti indicherà di cosa hai bisogno per richiedere il nulla osta per la domanda di ricongiungimento familiare.\nPuoi richiedere aiuto in qualsiasi momento presso:\n"+str(geo_db_locator.sindacatipatronati(str(request.session.get('indirizzo_alloggio'))))
        guida['a2'] = "Per i servizi anagrafici puoi rivolgerti presso un municipio. "+str(geo_db_locator.anagrafe_milano_piu_vicina(str(request.session.get('indirizzo_alloggio'))))+"\nPer l'idoneità abitativa della tua casa "+str(geo_db_locator.idoneita_abitativa_vicina_milano(str(request.session.get('indirizzo_alloggio'))))
        guida['a3'] = str(geo_db_locator.valori_bollati_milano_piu_vicini(str(request.session.get('indirizzo_alloggio'))))+"\nTi occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€."
        return guida







class Family_manager():

    global idoneo, non_idoneo

    def dati_validi(request):
        request.session['contatore_familiari'] = int(request.session.get('n_genitori_min_65'))+int(request.session.get('n_genitori_mag_ug_65'))+int(request.session.get('n_partner_mag'))+int(request.session.get('n_figli_min_ug_14'))+int(request.session.get('n_figli_15_17'))+int(request.session.get('n_figli_magg'))
        if (int(request.session.get('n_genitori_min_65'))+int(request.session.get('n_genitori_mag_ug_65')))>2:
            request.session['alert'] = 'Hai inserito più di 2 genitori, riprova!'
            return False
        if int(request.session.get('contatore_familiari'))>0 and int(request.session.get('contatore_familiari'))<=5:
            return True
        else:
            if ((int(request.session.get('contatore_familiari'))>5) or int(request.session.get('contatore_familiari'))<1):
                if int(request.session.get('contatore_familiari'))==0:
                    request.session['alert'] = 'Non hai inserito alcun familiare! Riprova'
                    return False
                if int(request.session.get('contatore_familiari'))>5:
                    request.session['alert'] = 'Puoi ricongiungere al massimo 5 familiari! Riprova'
                    return False

    def ci_sono_altri_figli(request):
        if int(request.session.get('n_figli_min_ug_14'))>0 or int(request.session.get('n_figli_15_17'))>0 or int(request.session.get('n_figli_magg'))>0:
            return True
        return False

    def gestore_figli(request):
        if Family_manager.ci_sono_altri_figli(request):
            if int(request.session.get('n_figli_min_ug_14'))>0:
                print('Numero di figli <14: '+str(request.session.get('n_figli_min_ug_14')))#################################
                #request.session['n_figli_min_ug_14'] = int(request.session.get('n_figli_min_ug_14'))-1
                request.session['parente_specifico'] = 'figli_min_ug_14'
                request.session['parente'] = 'figli_min_ug_14'
                return request
            elif int(request.session.get('n_figli_15_17'))>0:
                print('Numero di figli 15-17: '+str(request.session.get('n_figli_15_17')))#################################
                #request.session['n_figli_15_17'] = int(request.session.get('n_figli_15_17'))-1
                request.session['parente_specifico'] = 'figli_15_17'
                request.session['parente'] = 'figli_15_17'
                return request
            elif int(request.session.get('n_figli_magg'))>0:
                print('Numero di figli maggiorenni: '+str(request.session.get('n_figli_magg')))#################################
                #request.session['n_figli_magg'] = int(request.session.get('n_figli_magg'))-1
                request.session['parente_specifico'] = 'figli_magg'
                request.session['parente'] = 'figli_magg'
                return request

        request.session['parente'] = "None"
        return request

    def c_e_altro_partner(request):
        if int(request.session.get('n_partner_mag'))==1:
            return True
        return False

    def gestore_partner(request):
        if Family_manager.c_e_altro_partner(request):
            request.session['parente'] = 'partner_mag'
            request.session['parente_specifico'] = 'partner_mag'
            #request.session['n_partner_mag'] = int(request.session.get('n_partner_mag'))-1
            return request
        else:
            request.session['parente'] = "None"
            return request

    def ci_sono_altri_genitori(request):
        if (int(request.session.get('n_genitori_min_65'))>0 or int(request.session.get('n_genitori_mag_ug_65'))>0):
            return True
        return False

    def gestore_genitori(request):
        if Family_manager.ci_sono_altri_genitori(request):
            request.session['parente'] = 'genitore'
            if int(request.session.get('n_genitori_min_65'))>0:
                request.session['parente_specifico'] = 'genitori_min_65'
                #request.session['n_genitori_min_65'] = int(request.session.get('n_genitori_min_65'))-1
                return request
            elif int(request.session.get('n_genitori_mag_ug_65'))>0:
                request.session['parente_specifico'] = 'genitori_mag_ug_65'
                #request.session['n_genitori_mag_ug_65'] = int(request.session.get('n_genitori_mag_ug_65'))-1
                return request
        else:
            request.session['parente'] = 'None'
            return request

    def ci_sono_altri_familiari(request):
        if (Family_manager.ci_sono_altri_figli(request) or Family_manager.c_e_altro_partner(request) or Family_manager.ci_sono_altri_genitori(request)):
            return True
        return False

    def prossimo_parente(request):

        print("Chiamata a prossimo_parente: - IL PARENTE in uscita è "+str(request.session.get('parente')))

        if Family_manager.ci_sono_altri_familiari(request):
            request = Family_manager.gestore_figli(request)
            if (not (str(request.session.get('parente'))=="None")):
                print("controllo FIGLI - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                request.session['numero_temporaneo_figlio'] = request.session.get('numero_temporaneo_figlio')+1
                return request
            request = Family_manager.gestore_genitori(request)
            if (not str(request.session.get('parente'))=="None"):
                print("controllo GENITORI - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                request.session['numero_temporaneo_genitore'] = request.session.get('numero_temporaneo_genitore')+1
                return request
            request = Family_manager.gestore_partner(request)
            if (not str(request.session.get('parente'))=="None"):
                print("controllo PARTNER - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                return request

        else:
            request.session['parente']="None"
            print("FINE - IL PROSSIMO PARENTE È "+str(request.session.get('parente'))+", quindi NON CI SONO PIÙ PARENTI")
            return request

    def check_coinquilini(request):
        request.session['n_tot_coinquilini_min_14'] = request.POST.get('n_tot_coinquilini_min_14')
        if (request.session.get('n_tot_coinquilini_min_14')>request.session.get('n_tot_coinquilini')):
            request.session['alert'] = 'Hai inserito dati errati. Riprova'
        else:
            request.session['n_coinquilini_da_contare_per_metratura'] = int(request.session.get('n_tot_coinquilini'))-int(request.session.get('n_tot_coinquilini_min_14'))
            if (not Family_manager.ci_sono_partner_o_genitori(request)):
                request.session['page_id'] = 24     ##se non ci sono partner o genitori si procede con la pagina per la misura della casa


    def rimuovi_parente_corrente(request):
        parente = "n_"+str(request.session.get('parente_specifico'))
        request.session[parente] = int(request.session.get(parente))-1
        request = Family_manager.prossimo_parente(request)
        return request

    def c_e_partner(request):
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if 'partner_mag' in familiari_temp:
            request.session['page_id'] = 18
            return True
        return False

    def c_e_genitore(request):
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if ('genitori_min_65' in familiari_temp) or ('genitori_mag_ug_65' in familiari_temp):
            request.session['page_id'] = 20
            return True
        return False

    def ci_sono_partner_o_genitori(request):
        return (Family_manager.c_e_genitore(request) and Family_manager.c_e_partner(request))

    def check_no_condizioni(request):
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if not (('figli_15_17' or 'figli_magg') in familiari_temp):
            request.session['page_id'] = idoneo



class Survey_manager():

    global idoneo, non_idoneo

    def calcola_metratura_casa(request):
        ### Secondo parametri indicati qui: http://mediagallery.comune.milano.it/cdm/objects/changeme:99769/datastreams/dataStream7876968358553620/content?pgpath=/SA_SiteContent/SEGUI_AMMINISTRAZIONE/GOVERNO/Municipi/municipio_8/servizi_municipio/attestazione_idoneita_abitativa
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        fm14= familiari_temp.count('figli_min_ug_14')
        numero_familiari_da_contare_per_metratura = len(familiari_temp)-fm14

        n_coinquilini_da_contare_per_metratura = int(request.session.get('n_tot_coinquilini'))-int(request.session.get('n_tot_coinquilini_min_14'))

        n_tot_persone_in_casa = numero_familiari_da_contare_per_metratura + n_coinquilini_da_contare_per_metratura
        if n_tot_persone_in_casa<=4:
            request.session['metratura_casa'] = 14*n_tot_persone_in_casa
            ###  minimo 14mq per i primi 4 abitanti
        elif n_tot_persone_in_casa>4:
            request.session['metratura_casa'] = 14*4 + ((n_tot_persone_in_casa-4)*10)
            ### dopo i primi 4 abitanti, minimo 10mq per i successivi
        return request.session['metratura_casa']


    def permesso_scaduto(request):##########################################CHECK SU DATE###########################################################################
        rilascio = request.session.get('rilascio_permesso')
        scadenza = request.session.get('scadenza_permesso')
        rilascio = datetime.strptime(rilascio, "%d/%m/%Y")
        scadenza = datetime.strptime(scadenza, "%d/%m/%Y")
        giorni = ((scadenza - rilascio).days)
        if (giorni>365):
            return False
        return True


    def calcola_importo_reddito(request):
        ###dati di riferimento presi da qui:
        #1) http://lavocedellaquila.com/2018/02/25/ricongiungimento-familiare-italia-reddito-annuo-minimo-2018/
        #2) http://www.integrazionemigranti.gov.it/normativa/procedureitalia/Pagine/Ricongiungimento-familiare.aspx

        request.session['importo_reddito'] = float(5889) ###base al singolo

        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        fm14= familiari_temp.count('figli_min_ug_14')
        elementi=len(familiari_temp)
        altri=elementi-fm14

        if(fm14>0):
            request.session['importo_reddito'] = float(request.session.get('importo_reddito'))+float(5889)+float(2944.50)*altri
        else:
            request.session['importo_reddito'] = float(request.session.get('importo_reddito'))+float(2944.50)*altri


        return float(request.session.get('importo_reddito'))


    def dispatcher(request):

        page = request.session.get('page_id')

        if page==0:
            request.session['page_id'] = 2

        if page==1:
            request.session['lingua'] = request.POST.get('lingua')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('lingua'))!='None':
                request.session['page_id'] = 0
                request.session['alert'] = ''
                request.session['temp_parente'] = ''
                request.session['lista_familiari'] = []

        elif page==2:
            #request.session['page_id'] = request.POST.get('page_id')
            request.session['nazionalità_user'] = request.POST.get('nazionalità_user')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('nazionalità_user'))!='None':
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==3:
            request.session['n_figli_min_ug_14'] = request.POST.get('n_figli_min_ug_14')
            request.session['n_figli_15_17'] = request.POST.get('n_figli_15_17')
            request.session['n_figli_magg'] = request.POST.get('n_figli_magg')
            request.session['n_genitori_min_65'] = request.POST.get('n_genitori_min_65')
            request.session['n_genitori_mag_ug_65'] = request.POST.get('n_genitori_mag_ug_65')
            request.session['n_partner_mag'] = request.POST.get('n_partner_mag')

            if (Family_manager.dati_validi(request)):
                request.session['alert'] = ''
                request = Family_manager.prossimo_parente(request)
                request.session['temp_parente'] = request.session.get('parente')
                print("PARENTI :"+str(request.session.get('n_figli_min_ug_14'))+"\n"+str(request.session.get('n_figli_15_17'))+"\n"+str(request.session.get('n_figli_magg'))+"\n"+str(request.session.get("n_genitori_min_65"))+"\n"+str(request.session.get("n_genitori_mag_ug_65"))+"\n"+str(request.session.get("n_partner_mag")))

                if (Family_manager.ci_sono_altri_familiari(request)):
                    request.session['page_id'] = page+1

        elif page==4:
            request.session['nazionalità_parente'] = request.POST.get('nazionalità_parente')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            request.session['temp_parente'] = request.session.get('parente')
            if str(request.session.get('nazionalità_parente'))!='None':
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==5:
            request.session['residenza_parente'] = request.POST.get('residenza_parente')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('residenza_parente'))!='None':
                request.session['alert'] = ''

                request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))

                request = Family_manager.rimuovi_parente_corrente(request)

                    #request.session['page_id']= 6


                if request.session.get('parente')=='None':
                    print("NON CI SONO PIÙ FAMILIARI DA INSERIRE, PROCEDO . . .")
                    request.session['page_id'] = page+1
                    request.session['temp_parente'] = ''

                else:
                    print("C'è un altro parente, proseguo per inserire "+str(request.session.get('parente')))
                    request.session['page_id'] = 4
                    request.session['temp_parente'] = request.session.get('parente')




                    '''
                else:
                    temp_lista = request.session.get('lista_familiari')[0]
                    print("temp_lista è QUESTA QUI=================================================\n"+str(temp_lista))
                    if ((str(request.session.get('parente'))=='figli_min_ug_14') or (str(request.session.get('parente'))=='figli_15_17') or (str(request.session.get('parente'))=='figli_magg')):
                        if (('figli_min_ug_14' in temp_lista) or ('figli_15_17' in temp_lista) or ('figli_magg' in temp_lista)):
                            print("NON È IL PRIMO FIGLIO INSERITO")
                            request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))
                            request = Family_manager.rimuovi_parente_corrente(request)
                            if ((str(request.session.get('parente'))=='figli_min_ug_14') or (str(request.session.get('parente'))=='figli_15_17') or (str(request.session.get('parente'))=='figli_magg')):
                                request.session['temp_parente'] = str(request.session.get('parente'))
                                request.session['page_id'] = 4

                    if request.session.get('parente')=='genitore' and (not ('hai_fratelli' in request.session)):
                        print("PRIMO GENITORE INSERITO")
                        request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))
                        request.session['page_id'] = 4
                    elif request.session.get('parente')=='genitore' and ('hai_fratelli' in request.session):
                        print("SECONDO GENITORE INSERITO")
                        request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))
                        request = Family_manager.rimuovi_parente_corrente(request)
                        if (request.session.get('tipologia_permesso')=='asilo politico'):
                            request.session['page_id'] = idoneo
                        else:
                            request.session['page_id'] = 24
                        if (request.session.get('parente')=='partner_mag'):
                            print("È NELLA CONDIZIONE DEL PARTNER CON GENITORE INSERITO")
                            request.session['temp_parente'] = str(request.session.get('parente'))
                            request.session['page_id'] = 4

                    if ((request.session.get('parente')=='partner_mag') and (not (int(request.session.get('page_id')))==4)):
                        print("PARTNER INSERITO SENZA AVER INSERITO GENITORI")
                        request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))
                        request.session['page_id'] = 4
                        '''



        elif page==6:
            request.session['temp_parente'] = ''
            request.session['tipologia_permesso'] = request.POST.get('tipologia_permesso')
            if str(request.session.get('tipologia_permesso'))=='None':
                request.session['alert'] = 'Non hai inserito una tipologia di permesso di soggiorno. Riprova'
            elif str(request.session.get('tipologia_permesso'))=='asilo politico':
                if (not Family_manager.ci_sono_partner_o_genitori(request)):
                    Family_manager.check_no_condizioni(request)
            else:
                request.session['page_id'] = page+1


        elif page==7:
            print(str(request.POST.get('rilascio_permesso')))
            request.session['rilascio_permesso'] = request.POST.get('rilascio_permesso')
            request.session['alert'] = 'Non hai inserito una data valida'
            if str(request.session.get('rilascio_permesso'))!='None':
                print(str(request.session.get('rilascio_permesso')))
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==8:
            print(str(request.POST.get('scadenza_permesso'))) ############################################################## CHECKS TO DO
            request.session['scadenza_permesso'] = request.POST.get('scadenza_permesso')
            request.session['alert'] = 'Non hai inserito una data valida'
            if not (request.session.get('scadenza_permesso')=='illimitato'):
                request.session['alert'] = ''
                if Survey_manager.permesso_scaduto(request):
                    request.session['page_id'] = page+1
                else:
                    request.session['page_id'] = 11
            elif request.session.get('scadenza_permesso')=='illimitato':
                request.session['alert'] = ''
                request.session['page_id'] = 11


        elif page==9:
            request.session['ricevuta_rinnovo_permesso'] = request.POST.get('ricevuta_rinnovo_permesso')
            if str(request.session.get('ricevuta_rinnovo_permesso'))=='si':
                request.session['page_id'] = 11
            elif str(request.session.get('ricevuta_rinnovo_permesso'))=='no':
                request.session['page_id'] = non_idoneo


        ##TO-DO DA SISTEMARE PAGINA 10
        elif page==10:
            print('nulla per ora')
            ##TO-DO CAMBIARE "11" ALLE DOMANDE 8 E 9 E SCALARE TUTTE LE DOMANDE DI 1 DA QUI IN POI
            ##QUINDI RICONTROLLARE LINK PRIMA D'ORA PER LE PAGINE SUCCESSIVE, QUANDO SCALATE


        elif page==11:
            request.session['quale_residenza'] = request.POST.get('quale_residenza')
            if not (str(request.session.get('quale_residenza'))=='None'):
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==12:
            request.session['posso_ospitare_in_alloggio'] = request.POST.get('posso_ospitare_in_alloggio')
            if str(request.session.get('posso_ospitare_in_alloggio'))=="None":
                request.session['alert'] = "Non hai selezionato nulla dall'elenco, riprova"
            elif str(request.session.get('posso_ospitare_in_alloggio'))=="no":
                request.session['page_id'] = non_idoneo
            elif (str(request.POST.get('città'))!='None' and str(request.POST.get('via'))!='None'):
                request.session['indirizzo_alloggio'] = str(str(request.POST.get('città'))+', '+str(request.POST.get('via')))
                if geodecoder.from_address_to_coords(str(request.session.get('indirizzo_alloggio')))=="None":
                    request.session['alert'] = 'Non hai inserito un indirizzo corretto, riprova'
                elif str(request.session.get('posso_ospitare_in_alloggio'))=="si":
                    request.session['page_id'] = page+1
                    request.session['alert'] = ''
                elif str(request.session.get('posso_ospitare_in_alloggio'))=="ospite":
                    request.session['alert'] = ''
                    request.session['page_id'] = 16
                    Family_manager.ci_sono_partner_o_genitori(request)

        elif page==13:
            request.session['contratto_locazione'] = request.POST.get('contratto_locazione')
            if str(request.session.get('contratto_locazione'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('contratto_locazione'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==14:
            request.session['contratto_locazione_registrato'] = request.POST.get('contratto_locazione_registrato')
            if str(request.session.get('contratto_locazione_registrato'))=='si':
                request.session['page_id'] = 16
            elif str(request.session.get('contratto_locazione_registrato'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==15:
            request.session['atto_compravendita'] = request.POST.get('atto_compravendita')
            if str(request.session.get('atto_compravendita'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('atto_compravendita'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==16:
            '''request.session['coinq_figli_min_ug_14'] = 0
            request.session['coinq_figli_15_17'] = 0
            request.session['coinq_figli_magg'] = 0
            request.session['coinq_genitori_min_65'] = 0
            request.session['coinq_genitori_mag_ug_65'] = 0
            request.session['coinq_partner_mag'] = 0
            request.session['vivi_solo'] = request.POST.get('vivi_solo')
            if str(request.session.get('vivi_solo'))=='si':
                if (str(request.session.get('parente'))=='partner_mag'):
                    request.session['page_id'] = 18
                elif (((str(request.session.get('parente'))=='figli_min_ug_14') or (str(request.session.get('parente'))=='figli_15_17') or (str(request.session.get('parente'))=='figli_magg'))):
                    Family_manager.check_coinquilini(request)
                    request = Family_manager.rimuovi_parente_corrente(request)
                    if (str(request.session.get('parente'))!="None"):
                        request.session['temp_parente'] = str(request.session.get('parente'))
                        request.session['page_id'] = 4
                    else:
                        request.session['page_id'] = 24
                elif (str(request.session.get('parente'))=='genitore'):
                    request.session['page_id'] = 20'''
            request.session['n_tot_coinquilini'] = request.POST.get('n_tot_coinquilini')
            request.session['n_tot_coinquilini_min_14'] = request.POST.get('n_tot_coinquilini_min_14')
            request.session['metratura_casa'] = Survey_manager.calcola_metratura_casa(request)
            request.session['importo_reddito'] = Survey_manager.calcola_importo_reddito(request)
            if int(request.session.get('n_tot_coinquilini'))==0:
                request.session['page_id'] = 18
            else:
                Family_manager.check_coinquilini(request)

        elif page==17:##TO-DO FARE PULIZIA
            '''request.session['coinq_figli_min_ug_14'] = request.POST.get('coinq_figli_min_ug_14')
            request.session['coinq_figli_15_17'] = request.POST.get('coinq_figli_15_17')
            request.session['coinq_figli_magg'] = request.POST.get('coinq_figli_magg')
            request.session['coinq_genitori_min_65'] = request.POST.get('coinq_genitori_min_65')
            request.session['coinq_genitori_mag_ug_65'] = request.POST.get('coinq_genitori_mag_ug_65')
            request.session['coinq_partner_mag'] = request.POST.get('coinq_partner_mag')
            if Family_manager.check_coinquilini(request):
                request.session['alert'] = ''



                if ((str(request.session.get('parente'))=='figli_min_ug_14') or (str(request.session.get('parente'))=='figli_15_17') or (str(request.session.get('parente'))=='figli_magg')):
                    request = Family_manager.rimuovi_parente_corrente(request)
                    if str(request.session.get('parente'))=="None":
                        if (request.session.get('tipologia_permesso')=='asilo politico'):
                            request.session['page_id'] = idoneo
                        else:
                            request.session['page_id'] = 24
                    else:
                        request.session['temp_parente'] = str(request.session.get('parente'))
                        request.session['page_id'] = 4

                elif str(request.session.get('parente'))=='partner_mag':
                        request.session['page_id'] = page+1

                elif str(request.session.get('parente'))=='genitore':
                    if not ('hai_fratelli' in request.session):
                        request.session['page_id'] = 20
                    elif ('hai_fratelli' in request.session):
                        request = Family_manager.rimuovi_parente_corrente(request)
                        request.session['page_id'] = 24'''



        elif page==18:
            request.session['tipo_partner'] = request.POST.get('tipo_partner')
            request.session['page_id'] = page+1

        elif page==19:
            request.session['relazione_legale'] = request.POST.get('relazione_legale')
            if str(request.session.get('relazione_legale'))=='no':
                request.session['page_id'] = non_idoneo
            elif str(request.session.get('relazione_legale'))=='si':
                if (Family_manager.c_e_genitore(request)):
                    request.session['page_id'] = page+1
                else:
                    if (request.session.get('tipologia_permesso')=='asilo politico'):
                        request.session['page_id'] = idoneo
                    else:
                        request.session['page_id'] = 24

        elif page==20:
            request.session['hai_fratelli'] = request.POST.get('hai_fratelli')
            if (request.session.get('tipologia_permesso')=='asilo politico'):
                request.session['page_id'] = idoneo
            else:
                request.session['page_id'] = 24

        elif page==24:
            request.session['casa_sufficiente'] = request.POST.get('casa_sufficiente')
            if str(request.session.get('casa_sufficiente'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('casa_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==25:
            request.session['alert'] = ''
            request.session['tipologia_lavoro'] = request.POST.get('tipologia_lavoro')
            if str(request.session.get('tipologia_lavoro'))=='None':
                request.session['alert'] = 'Non hai inserito una tipologia per il lavoro, riprova'
            elif str(request.session.get('tipologia_lavoro'))=='no':
                request.session['page_id'] = non_idoneo
            else:
                request.session['page_id'] = page+1


        elif page==26:
            request.session['reddito_sufficiente'] = request.POST.get('reddito_sufficiente')
            if str(request.session.get('reddito_sufficiente'))=='si':
                request.session['page_id'] = idoneo
            elif str(request.session.get('reddito_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==idoneo:
            request.session['guida'] = request.POST.get('guida')
            if request.session['guida'] == 'si':
                print('FINE')
                #Report_maker.produci_guida(request)

        elif page==non_idoneo:
            request.session['guida'] = request.POST.get('guida')
            if request.session['guida'] == 'no':
                request.session['page_id'] = 1

        return request
