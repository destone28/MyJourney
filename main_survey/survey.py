import datetime

class Family_manager():

    def dati_validi(request):
        if (int(request.session.get('n_genitori_min_65'))+int(request.session.get('n_genitori_mag_ug_65')))>2:
            request.session['alert'] = 'Hai inserito più di 2 genitori, riprova!'
            return False
        else:
            if ('contatore_familiari' not in request.session) or int(request.session.get('contatore_familiari'))<1:
                request.session['contatore_familiari'] = int(request.session.get('n_genitori_min_65'))+int(request.session.get('n_genitori_mag_ug_65'))+int(request.session.get('n_partner_mag'))+int(request.session.get('n_figli_min_ug_14'))+int(request.session.get('n_figli_15_17'))+int(request.session.get('n_figli_magg'))
                if int(request.session.get('contatore_familiari'))>0 and int(request.session.get('contatore_familiari'))<=5:
                    return True
                request.session['alert'] = 'Puoi ricongiungere al massimo 5 familiari! Riprova'
                return False

    def ci_sono_altri_figli(request):
        if int(request.session.get('n_figli_min_ug_14'))>0 or int(request.session.get('n_figli_15_17'))>0 or int(request.session.get('n_figli_magg'))>0:
            return True
        return False

    def gestore_figli(request):
        if Family_manager.ci_sono_altri_figli(request):
            request.session['parente'] = 'figlio'
            if int(request.session.get('n_figli_min_ug_14'))>0:
                print('Numero di figli <14: '+str(request.session.get('n_figli_min_ug_14')))#################################
                request.session['n_figli_min_ug_14'] = int(request.session.get('n_figli_min_ug_14'))-1
                request.session['parente_specifico'] = 'figli_min_ug_14'
                return request
            elif int(request.session.get('n_figli_15_17'))>0:
                print('Numero di figli 15-17: '+str(request.session.get('n_figli_15_17')))#################################
                request.session['n_figli_15_17'] = int(request.session.get('n_figli_15_17'))-1
                request.session['parente_specifico'] = 'figli_15_17'
                return request
            elif int(request.session.get('n_figli_magg'))>0:
                print('Numero di figli maggiorenni: '+str(request.session.get('n_figli_magg')))#################################
                request.session['n_figli_magg'] = int(request.session.get('n_figli_magg'))-1
                request.session['parente_specifico'] = 'figli_magg'
                return request

        request.session['parente'] = "None"
        return request

    def c_e_altro_partner(request):
        if int(request.session.get('n_partner_mag'))==1:
            return True
        return False

    def gestore_partner(request):
        if Family_manager.c_e_altro_partner(request):
            request.session['parente'] = 'partner'
            request.session['parente_specifico'] = 'partner'
            request.session['n_partner_mag'] = int(request.session.get('n_partner_mag'))-1
            return request
        else:
            request.session['parente'] = "None"
            return request

    def ci_sono_altri_genitori(request):
        if int(request.session.get('n_genitori_min_65'))>0 or int(request.session.get('n_genitori_mag_ug_65'))>0:
            return True
        return False

    def gestore_genitori(request):
        if Family_manager.ci_sono_altri_genitori(request):
            request.session['parente'] = 'genitore'
            if int(request.session.get('n_genitori_min_65'))>0:
                request.session['parente_specifico'] = 'genitori_min_65'
                request.session['n_genitori_min_65'] = int(request.session.get('n_genitori_min_65'))-1
                return request
            elif int(request.session.get('n_genitori_mag_ug_65'))>0:
                request.session['parente_specifico'] = 'genitori_mag_ug_65'
                request.session['n_genitori_mag_ug_65'] = int(request.session.get('n_genitori_mag_ug_65'))-1
                return request
        else:
            request.session['parente'] = 'None'
            return request

    def ci_sono_altri_familiari(request):
        if Family_manager.ci_sono_altri_figli(request) or Family_manager.c_e_altro_partner(request) or Family_manager.ci_sono_altri_genitori(request):
            return True
        return False

    def prossimo_parente(request):
        if Family_manager.ci_sono_altri_familiari(request):
            request = Family_manager.gestore_figli(request)
            print("1 - IL PROSSIMO PARENTE È "+str(request.session.get('parente'))+"\nIL VALORE DI str(request.session.get('parente'))=='None' è " + str(request.session.get('parente'))=="None")
            if not (str(request.session.get('parente'))=="None"):
                return request
            request = Family_manager.gestore_partner(request)
            print("2 - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
            if not (str(request.session.get('parente'))=="None"):
                return request
            request = Family_manager.gestore_genitori(request)
            print("3 - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
            if not (str(request.session.get('parente'))=="None"):
                return request
        request.session['parente'] = "None"
        return request

    def coinquilini_ok(request):
        tot_figli_coinquilini = int(request.session.get('coinq_figli_min_ug_14'))+int(request.session.get('coinq_figli_15_17'))+int(request.session.get('coinq_figli_magg'))
        tot_genitori = int(request.session.get('n_genitori_min_65'))+int(request.session.get('n_genitori_mag_ug_65'))+int(request.session.get('coinq_genitori_min_65'))+int(request.session.get('coinq_genitori_mag_ug_65'))
        tot_partner = int(request.session.get('n_partner_mag'))+int(request.session.get('coinq_partner_mag'))
        if tot_genitori>2:
            request.session['alert'] = 'Hai inserito troppi genitori, riprova!'
        if tot_partner>1:
            request.session['alert'] = 'Hai inserito più di un partner, riprova!'
        if (tot_genitori<=2) and (tot_partner<=1):
            request.session['n_tot_coinquilini'] = tot_figli_coinquilini+int(request.session.get('coinq_genitori_min_65'))+int(request.session.get('coinq_genitori_mag_ug_65'))+int(request.session.get('coinq_partner_mag'))
            if (request.session.get('contatore_familiari')+request.session.get('n_tot_coinquilini'))<=5:
                request.alert['La procedura prevede un massimo di 5 persone nella stessa abitazione.<br>Al momento la somma del numero dei familiari da ricongiungere e quelli che vivono con te supera le 5 persone!']
                return True
        return False





class Survey_manager():

    def dispatcher(request):

        page = request.session['page_id']
        non_idoneo = 28
        idoneo = 29

        if page==1:
            request.session['lingua'] = request.POST.get('lingua')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('lingua'))!='None':
                request.session['page_id'] = page+1
                request.session['alert'] = ''
                request.session['temp_parente'] = ''

        elif page==2:
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

            request = Family_manager.prossimo_parente(request)
            print(request.session.get('parente'))
            print("PARENTI :"+str(request.session.get('n_figli_min_ug_14'))+"\n"+str(request.session.get('n_figli_15_17'))+"\n"+str(request.session.get('n_figli_magg'))+"\n"+str(request.session.get("n_genitori_min_65"))+"\n"+str(request.session.get("n_genitori_mag_ug_65"))+"\n"+str(request.session.get("n_partner_mag")))

            if (Family_manager.ci_sono_altri_familiari(request)):
                request.session['page_id'] = page+1

        elif page==4:
            request.session['nazionalità_parente'] = request.POST.get('nazionalità_parente')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('nazionalità_parente'))!='None':
                request.session['page_id'] = page+1
                request.session['alert'] = ''
                request.session['temp_parente'] = ''

        elif page==5:
            request.session['residenza_parente'] = request.POST.get('residenza_parente')
            request.session['alert'] = 'Non hai effettuato scelte valide'
            if str(request.session.get('residenza_parente'))!='None':
                request.session['page_id'] = page+1
                request.session['alert'] = ''
                if str(request.session.get('parente')=="figlio"):
                    if ('lista_familiari' not in request.session):
                        request.session['lista_familiari'] = [(request.session.get('parente'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente'))]
                    else:
                        request.session.get('lista_familiari').append((request.session.get('parente'), request.session.get('nazionalità_parente'), request.session.get('residenza_parente')))

        elif page==6:
            request.session['durata_permesso'] = request.POST.get('durata_permesso')
            print(request.session.get('durata_permesso'))
            if str(request.session.get('durata_permesso'))=='illimitato':
                request.session['page_id'] = 10
            elif str(request.session.get('durata_permesso'))=='a scadenza':
                request.session['page_id'] = page+1
            elif str(request.session.get('durata_permesso'))=='no':
                request.session['page_id'] = non_idoneo
            elif str(request.session.get('durata_permesso'))=='None':
                request.session['alert'] = 'Non hai selezionato alcuna durata per il permesso, riprova'

        elif page==7:
            print(str(request.POST.get('rilascio_permesso')))
            request.session['rilascio_permesso'] = datetime.datetime.strptime(request.POST.get('rilascio_permesso'), "%Y-%m-%d").strftime("%d-%m-%Y")
            request.session['alert'] = 'Non hai inserito una data valida'
            if str(request.session.get('rilascio_permesso'))!='None':
                print(str(request.session.get('rilascio_permesso')))
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==8:
            print(str(request.POST.get('scadenza_permesso')))
            request.session['scadenza_permesso'] = datetime.datetime.strptime(request.POST.get('scadenza_permesso'), "%Y-%m-%d").strftime("%d-%m-%Y")
            request.session['alert'] = 'Non hai inserito una data valida'
            if str(request.session.get('scadenza_permesso'))!='None':
                intervallo = (request.session.get('scadenza_permesso')-request.session.get('rilascio_permesso')).days
                if intervallo<=365:
                    request.session['page_id'] = page+2
                    request.session['alert'] = ''
                else:
                    request.session['page_id'] = page+1
                    request.session['alert'] = ''

        elif page==9:
            request.session['ricevuta_permesso'] = request.POST.get('ricevuta_permesso')
            if str(request.session.get('ricevuta_permesso'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('ricevuta_permesso'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==10:
            request.session['tipologia_permesso'] = request.POST.get('tipologia_permesso')
            if str(request.session.get('tipologia_permesso'))=='asilo politico':
                if str(request.session.get('parente'))=='partner':
                    request.session['page_id'] = 19
                elif str(request.session.get('parente'))=='genitore':
                    request.session['page_id'] = 21
                elif str(request.session.get('parente'))=='figlio':
                    request=Family_manager.prossimo_parente(request)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\nIL PROSSIMO PARENTE RISULTA ESSERE "+str(request.session.get('parente'))+"\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    if str(request.session.get('parente'))=='None':### GUARDA SE C'È ANCHE ALTROVE ###
                        request.session['page_id'] = idoneo
                    else:
                        request.session['page_id'] = 4
            elif str(request.session.get('tipologia_permesso'))!='asilo politico':
                request.session['page_id'] = page+1

        elif page==11:
            request.session['residente_a_Milano'] = request.POST.get('residente_a_Milano')
            if str(request.session.get('residente_a_Milano'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('residente_a_Milano'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==12:
            request.session['tipo_alloggio'] = request.POST.get('tipo_alloggio')
            request.session['indirizzo_alloggio'] = str(request.POST.get('città')+', '+request.POST.get('via'))
            if str(request.session.get('tipo_alloggio'))=="no":
                request.session['page_id'] = non_idoneo
                if geolocalizzazione(str(request.session.get('indirizzo_alloggio'))):   ################### CHECK GEOLOCALIZZAZIONE INDIRIZZO errato
                    request.session['alert'] = 'Non hai inserito un indirizzo corretto, riprova'
                else:
                    request.session['alert'] = ''
                    if str(request.session.get('tipo_alloggio'))=="None":
                        request.session['alert'] = "Non hai selezionato nulla dall'elenco, riprova"
                    elif str(request.session.get('tipo_alloggio'))=="affitto":
                        request.session['page_id'] = page+1
                    elif str(request.session.get('tipo_alloggio'))=="proprietario":
                        request.session['page_id'] = 15
                    elif str(request.session.get('tipo_alloggio'))=="ospite":
                        request.session['page_id'] = 16

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
            request.session['alert'] = ''
            request.session['tipologia_lavoro'] = request.POST.get('tipologia_lavoro')
            if str(request.session.get('tipologia_lavoro'))=='None':
                request.session['alert'] = 'Non hai inserito una tipologia per il lavoro, riprova'
            elif str(request.session.get('tipologia_lavoro'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==17:
            request.session['vivi_solo'] = request.POST.get('vivi_solo')
            if str(request.session.get('vivi_solo'))=='si':
                request.session['page_id'] = 19
            elif str(request.session.get('vivi_solo'))=='no':
                request.session['page_id'] = page+1

        elif page==18:
            request.session['alert'] = ''
            request.session['coinq_figli_min_ug_14'] = request.POST.get('coinq_figli_min_ug_14')
            request.session['coinq_figli_15_17'] = request.POST.get('coinq_figli_15_17')
            request.session['coinq_figli_magg'] = request.POST.get('coinq_figli_magg')
            request.session['coinq_genitori_min_65'] = request.POST.get('coinq_genitori_min_65')
            request.session['coinq_genitori_mag_ug_65'] = request.POST.get('coinq_genitori_mag_ug_65')
            request.session['coinq_partner_mag'] = request.POST.get('coinq_partner_mag')
            if Family_manager.coinquilini_ok(request):
                if str(request.session.get('parente'))=='partner':
                    request.session['page_id'] = page+1
                elif str(request.session.get('parente'))=='genitore':
                    request.session['page_id'] = 21
                elif str(request.session.get('parente'))=='figlio':
                    request = Family_manager.prossimo_parente(request)
                    if str(request.session.get('parente'))=="None":
                        request.session['page_id'] = 25
                    else:
                        request.session['page_id'] = 4


        elif page==19:
            request.session['tipo_partner'] = request.POST.get('tipo_partner')
            request.session['page_id'] = page+1

        elif page==20:
            request.session['relazione_legale'] = request.POST.get('relazione_legale')
            if str(request.session.get('relazione_legale'))=='no':
                request.session['page_id'] = non_idoneo
            elif str(request.session.get('relazione_legale'))=='si':
                request = Family_manager.prossimo_parente(request)
                if str(request.session.get('parente'))=="None":
                    request.session['page_id'] = 25
                else:
                    request.session['page_id'] = 4

        elif page==21:
            request.session['hai_fratelli'] = request.POST.get('hai_fratelli')
            if str(request.session.get('hai_fratelli'))=='no':
                request = Family_manager.prossimo_parente(request)
                if str(request.session.get('parente'))=="None":
                    request.session['page_id'] = 25
                else:
                    request.session['page_id'] = 4
            elif str(request.session.get('hai_fratelli'))=='si':
                request.session['page_id'] = page+1

        elif page==22:
            request.session['fratelli_o_sorelle_residenti_con_genitore'] = request.POST.get('fratelli_o_sorelle_residenti_con_genitore')
            if str(request.session['fratelli_o_sorelle_residenti_con_genitore'])=='no':
                request = Family_manager.prossimo_parente(request)
                if str(request.session.get('parente'))=="None":
                    request.session['page_id'] = 25
                else:
                    request.session['page_id'] = 4
            elif str(request.session.get('fratelli_o_sorelle_residenti_con_genitore'))=='si':
                request.session['page_id'] = page+1

        elif page==23:
            request.session['fratelli_possono_mantenere_genitore'] = request.POST.get('fratelli_possono_mantenere_genitore')
            if str(request.session.get('fratelli_possono_mantenere_genitore'))!='None':
                if str(request.session('fratelli_possono_mantenere_genitore'))=='no altro' or str(request.session('fratelli_possono_mantenere_genitore'))=='si':
                    request.session['page_id'] = non_idoneo
                elif str(request.session['fratelli_possono_mantenere_genitore'])=='no salute':
                    request.session['page_id'] = page+1
            elif str(request.session.get('fratelli_possono_mantenere_genitore'))=='None':
                request.session['alert'] = "Non hai selezionato nulla, riprova"

        elif page==24:
            request.session['certificato_fratelli'] = request.POST.get('certificato_fratelli')
            if str(request.session.get('certificato_fratelli'))=='si':
                request = Family_manager.prossimo_parente(request)
                if str(request.session.get('parente'))=="None":
                    request.session['page_id'] = 25
                else:
                    request.session['page_id'] = 4
            elif str(request.session.get('certificato_fratelli'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==25:
            request.session['casa_sufficiente'] = request.POST.get('casa_sufficiente')
            if str(request.session.get('casa_sufficiente'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('casa_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo

        elif page==26:
            request.session['reddito_sufficiente'] = request.POST.get('reddito_sufficiente')
            if str(request.session.get('reddito_sufficiente'))=='si':
                request.session['page_id'] = idoneo
            elif str(request.session.get('reddito_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo
























        return request
