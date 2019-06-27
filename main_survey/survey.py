
from datetime import datetime
from . import geodecoder, geo_db_locator, report_maker

non_idoneo = 29
idoneo = 28

lingua = 'it'

text = {
    'dati_errati' : {
        'it': 'Hai inserito dati errati. Riprova',
        'en': "You have entered incorrect data. Try again",
        'ar': 'لقد أدخلت بيانات غير صحيحة. يرجى المحاولة مرة أخرى',
        'es': 'Has introducido datos incorrectos. Por favor, inténtelo de nuevo',
        'zh': '您输入的数据不正确。请再试一次',
        'fr': "Vous avez entré des données incorrectes. S'il vous plaît essayer de nouveau",
    },
    'limite_valori' : {
        'it': 'Immettere un valore compreso tra 1 e 6',
        'en': "Enter a value between 1 and 6",
        'ar': 'أدخِل قيمة ما بين 1 و 6',
        'es': 'Introducir un valor entre 1 y 6',
        'zh': ' 输入1至6之间的数字',
        'fr': "Saisissez une valeur comprise entre 1 et 6",
    },
    'scelte_non_valide' : {
        'it': 'Non hai effettuato scelte valide',
        'en': "You have not made a valid selection",
        'ar': 'لم تقم باختيارات صحيحة',
        'es': 'No has realizado una elección válida',
        'zh': ' 你未做出有效选择',
        'fr': "Vous n'avez pas effectué de choix valables",
    },
    'scopri_perché_qui' : {
        'it': 'Scopri perché qui',
        'en': "Find out why here",
        'ar': 'اكتشف لماذا هنا',
        'es': 'Descubre por qué aquí',
        'zh': '在这里找出原因',
        'fr': "Découvrez pourquoi ici",
    },
    'no_familiari' : {
        'it': 'Non hai inserito alcun familiare! Riprova',
        'en': "You didn't put in any family members. Try again",
        'ar': 'لم تدخِل أي فرد من أفراد العائلة ! حاول مرة أخرى',
        'es': '¡No has introducido a ningún familiar! Vuelve a intentarlo',
        'zh': ' 你未选择任何家人！请重试',
        'fr': 'Vous n''avez pas saisi de proches! Réessayez',
    }
}


class Family_manager():

    global idoneo, non_idoneo

    def dati_validi(request):
        request.session['contatore_familiari'] = int(request.session.get('n_genitori'))+int(request.session.get('n_partner_mag'))+int(request.session.get('n_figli_min_ug_14'))+int(request.session.get('n_figli_15_17'))+int(request.session.get('n_figli_magg'))
        if int(request.session.get('contatore_familiari'))>0 and int(request.session.get('contatore_familiari'))<=5:
            return True
        else:
            if ((int(request.session.get('contatore_familiari'))>5) or int(request.session.get('contatore_familiari'))<1):
                if int(request.session.get('contatore_familiari'))==0:
                    request.session['alert'] = text['no_familiari'][request.session.get('lingua')]
                    return False
                #if int(request.session.get('contatore_familiari'))>5:
                #    request.session['alert'] = 'Puoi ricongiungere al massimo 5 familiari! Riprova'
                #    return False

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
        if (int(request.session.get('n_genitori'))>0):
            return True
        return False

    def gestore_genitori(request):
        if Family_manager.ci_sono_altri_genitori(request):
            request.session['parente'] = 'genitore'
            request.session['parente_specifico'] = 'genitori'
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
            request = Family_manager.gestore_partner(request)
            if (not str(request.session.get('parente'))=="None"):
                print("controllo PARTNER - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                return request
            request = Family_manager.gestore_figli(request)
            if (not (str(request.session.get('parente'))=="None")):
                print("controllo FIGLI - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                if ('numero_temporaneo_figlio' in request.session):
                    request.session['numero_temporaneo_figlio'] = request.session.get('numero_temporaneo_figlio')+1
                else:
                    request.session['numero_temporaneo_figlio'] = 1
                return request
            request = Family_manager.gestore_genitori(request)
            if (not str(request.session.get('parente'))=="None"):
                print("controllo GENITORI - IL PROSSIMO PARENTE È "+str(request.session.get('parente')))
                if not ('numero_temporaneo_genitore' in request.session):
                    request.session['numero_temporaneo_genitore'] = 0
                request.session['numero_temporaneo_genitore'] = request.session.get('numero_temporaneo_genitore')+1
                return request
        else:
            request.session['parente']="None"
            print("FINE - IL PROSSIMO PARENTE È "+str(request.session.get('parente'))+", quindi NON CI SONO PIÙ PARENTI")
            return request

    def check_coinquilini(request):
        request.session['n_coinquilini_da_contare_per_metratura'] = int(request.session.get('n_tot_coinquilini'))-int(request.session.get('n_tot_coinquilini_min_14'))
        if (not Family_manager.ci_sono_partner_o_genitori(request)):
            request.session['metratura_casa'] = Survey_manager.calcola_metratura_casa(request)
            request.session['importo_reddito'] = Survey_manager.calcola_importo_reddito(request)
            request.session['page_id'] = 24     ##se non ci sono partner o genitori si procede con la pagina per la misura della casa

    def aggiungi_coinquilini_a_carico(request):
        request.session['coinquilini_a_carico']=int(request.session.get('coinquilini_a_carico'))
        lista_familiari = len(request.session.get('lista_familiari'))
        #familiari_temp = [item[0] for item in lista_familiari]
        print("Familiari dalla lista: "+lista_familiari)
        familiari = len(lista_familiari)+int(request.session.get('coinquilini_a_carico'))
        print("Familiari in totale a carico: "+familiari)
        if (familiari>6):
            #request.session['page_id'] = non_idoneo
            request.session['alert'] = text['limite_valori'][lingua]
            print("TROPPI FAMILIARI A CARICO!")
        if (int(request.session.get('coinquilini_a_carico'))>int(request.session.get('n_tot_coinquilini'))):
            request.session['alert'] = text['dati_errati'][lingua]


    def rimuovi_parente_corrente(request):
        parente = "n_"+str(request.session.get('parente_specifico'))
        request.session[parente] = int(request.session.get(parente))-1
        request = Family_manager.prossimo_parente(request)
        return request

    def c_e_partner(request):
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if 'partner_mag' in familiari_temp:
            return True
        return False

    def c_e_genitore(request):
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if ('genitori' in familiari_temp):
            return True
        return False

    def ci_sono_partner_o_genitori(request):
        return (Family_manager.c_e_genitore(request) and Family_manager.c_e_partner(request))

    def reset_parenti(request):
        if ('n_figli_min_ug_14' in request.session):
            del request.session['n_figli_min_ug_14']
        if ('n_figli_15_17' in request.session):
            del request.session['n_figli_15_17']
        if ('n_figli_magg' in request.session):
            del request.session['n_figli_magg']
        if ('n_genitori' in request.session):
            del request.session['n_genitori']
        if ('n_partner_mag' in request.session):
            del request.session['n_partner_mag']
        if ('temp_parente' in request.session):
            del request.session['temp_parente']
        if ('numero_temporaneo_figlio' in request.session):
            del request.session['numero_temporaneo_figlio']
        if ('numero_temporaneo_genitore' in request.session):
            del request.session['numero_temporaneo_genitore']
        if ('numero_temporaneo_parente' in request.session):
            del request.session['numero_temporaneo_parente']
        if ('lista_familiari' in request.session):
            del request.session['lista_familiari']


class Survey_manager():

    global idoneo, non_idoneo

    def calcola_metratura_casa(request):
        ### Secondo parametri indicati qui: http://mediagallery.comune.milano.it/cdm/objects/changeme:100450/datastreams/dataStream9068411603675629/content?pgpath=/SA_SiteContent/SEGUI_AMMINISTRAZIONE/GOVERNO/Municipi/municipio_7/servizi_municipio/attestazione_idoneita_abitativa
        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        #fm14= familiari_temp.count('figli_min_ug_14')
        #numero_familiari_da_contare_per_metratura = len(familiari_temp)-fm14

        numero_familiari_da_contare_per_metratura = len(familiari_temp)

        if ('n_tot_coinquilini' in request.session):
            n_tot_coinquilini = int(request.session['n_tot_coinquilini'])
        else:
            n_tot_coinquilini = 0

        #n_coinquilini_da_contare_per_metratura = int(request.session.get('n_tot_coinquilini'))-int(request.session.get('n_tot_coinquilini_min_14'))

        n_tot_persone_in_casa = numero_familiari_da_contare_per_metratura + n_tot_coinquilini +1 #+1 è l'utente!
        if n_tot_persone_in_casa<=4:
            request.session['metratura_casa'] = 14*n_tot_persone_in_casa
            ###  minimo 14mq per i primi 4 abitanti
        elif n_tot_persone_in_casa>4:
            request.session['metratura_casa'] = 14*4 + ((n_tot_persone_in_casa-4)*10)
            ### dopo i primi 4 abitanti, minimo 10mq per i successivi

        print("Persone da contare per metratura casa: "+str(n_tot_persone_in_casa)+"\n"+str(numero_familiari_da_contare_per_metratura)+" familiari e "+str(n_tot_coinquilini)+" coinquilini già in casa")

        return request.session['metratura_casa']


    def permesso_valido(request):
        rilascio = request.session.get('rilascio_permesso')
        scadenza = request.session.get('scadenza_permesso')
        try:
            rilascio = datetime.strptime(rilascio, "%d/%m/%Y")
            scadenza = datetime.strptime(scadenza, "%d/%m/%Y")
        except:
            request.session['validita_permesso'] = "date_non_valide"
            return False
        giorni = ((scadenza - rilascio).days)
        if (giorni<365):
            request.session['validita_permesso'] = "meno_di_un_anno"
            return False
        elif (scadenza<datetime.today()):
            request.session['validita_permesso'] = "scaduto"
            return False

        return True



    def calcola_importo_reddito(request):
        ###dati di riferimento presi da qui:
        #1) http://lavocedellaquila.com/2018/02/25/ricongiungimento-familiare-italia-reddito-annuo-minimo-2018/
        #2) http://www.integrazionemigranti.gov.it/normativa/procedureitalia/Pagine/Ricongiungimento-familiare.aspx

        lista_familiari = request.session.get('lista_familiari')
        familiari_temp = [item[0] for item in lista_familiari]
        if ('coinquilini_a_carico' in request.session):
            familiari = len(familiari_temp)+int(request.session.get('coinquilini_a_carico'))
        else:
            familiari = len(familiari_temp)

        if (familiari==1):
            request.session['importo_reddito'] = float(744.23)
        elif (familiari==2):
            request.session['importo_reddito'] = float(992.31)
        elif (familiari==3):
            request.session['importo_reddito'] = float(1240.38)
        elif (familiari==4):
            request.session['importo_reddito'] = float(1488.46)
        elif (familiari==5):
            request.session['importo_reddito'] = float(1736.54)
        elif (familiari==6):
            request.session['importo_reddito'] = float(1984.62)

        return float(request.session.get('importo_reddito'))


    def dispatcher(request):

        flag_back = request.POST.get('flag_back')
        page = int(request.session.get('page_id'))
        if (page!=29):
            request.session['pagina_indietro'] = page
        page_before = page-1  #pagine interessate: 3, 4, 9, 13, 14, 17, 25, 26
        #pagine nulle: 1, 2, 11, 19, 20, 21, 22, 23
        if ((page==5) or (page==6) or (page==7) or (page==8) or (page==18) or (page==24)):
            page_before=3
        if ((page==10) or (page==15) or (page==16)):
            page_before=12
        if (page==12):
            page_before=8
        if (page==27):
            page_before=25
        if (page==29):
            page_before=request.session.get('pagina_indietro')


        lingua = request.session.get('lingua')
        #if (request.session.get('lingua') == "None"):
        if (page==1):
            lingua = "it"



        if page==0:
            pagina_indietro=page
            request.session['page_id'] = 2

        if page==1:
            pagina_indietro=page
            lingua = request.POST.get('lingua')
            request.session['alert'] = text['scelte_non_valide'][lingua]
            if ((str(request.session.get('lingua'))!='None') or ('lingua' not in request.session)):
                request.session.clear()
                request.session['lingua'] = lingua
                request.session['page_id'] = 0

        elif page==2:
            pagina_indietro=page
            lingua = request.session.get('lingua')
            request.session['nazionalità_user'] = request.POST.get('nazionalità_user')
            request.session['alert'] = text['scelte_non_valide'][lingua]
            if str(request.session.get('nazionalità_user'))!='':
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==3:
            pagina_indietro=page
            request.session['n_figli_min_ug_14'] = request.POST.get('n_figli_min_ug_14')
            request.session['n_figli_15_17'] = request.POST.get('n_figli_15_17')
            request.session['n_figli_magg'] = request.POST.get('n_figli_magg')
            request.session['n_genitori'] = request.POST.get('n_genitori')
            request.session['n_partner_mag'] = request.POST.get('n_partner_mag')
            if(int(request.session.get('n_figli_min_ug_14'))>0 or int(request.session.get('n_figli_15_17'))>0):
                request.session['ha_figli_minorenni'] = "si"

            if (Family_manager.dati_validi(request)):
                request.session['alert'] = ''
                request = Family_manager.prossimo_parente(request)
                request.session['temp_parente'] = request.session.get('parente')
                print("PARENTI :"+str(request.session.get('n_figli_min_ug_14'))+"\n"+str(request.session.get('n_figli_15_17'))+"\n"+str(request.session.get('n_figli_magg'))+"\n"+str(request.session.get("n_genitori"))+"\n"+str(request.session.get("n_partner_mag")))

                if (Family_manager.ci_sono_altri_familiari(request)):
                    request.session['page_id'] = 5

        elif page==5:
            pagina_indietro=page
            request.session['residenza_parente'] = request.POST.get('residenza_parente')
            request.session['alert'] = text['scelte_non_valide'][lingua]
            if str(request.session.get('residenza_parente'))!='':
                request.session['alert'] = ''
                if not ('lista_familiari' in request.session):
                    request.session['lista_familiari'] = []
                request.session.get('lista_familiari').append((request.session.get('parente_specifico'), request.session.get('residenza_parente')))

                request = Family_manager.rimuovi_parente_corrente(request)

                    #request.session['page_id']= 6

                if request.session.get('parente')=='None':
                    print("NON CI SONO PIÙ FAMILIARI DA INSERIRE, PROCEDO . . .")
                    request.session['page_id'] = 7
                    request.session['temp_parente'] = ''

                else:
                    print("C'è un altro parente, proseguo per inserire "+str(request.session.get('parente')))
                    request.session['page_id'] = 5
                    request.session['temp_parente'] = request.session.get('parente')


        elif page==6:
            pagina_indietro=page
            request.session['temp_parente'] = ''
            request.session['tipologia_permesso'] = request.POST.get('tipologia_permesso')
            if str(request.session.get('tipologia_permesso'))=='asilo politico':
                if not (Family_manager.c_e_partner(request)):
                    request.session['page_id'] = 11
                else:
                    request.session['page_id'] = 18
            elif str(request.session.get('tipologia_permesso'))=='altro':
                request.session['page_id'] = 12


        elif page==7:
            pagina_indietro=page
            print(str(request.POST.get('rilascio_permesso')))
            request.session['rilascio_permesso'] = request.POST.get('rilascio_permesso')
            request.session['alert'] = text['scelte_non_valide'][lingua]
            if str(request.session.get('rilascio_permesso'))!='Inserisci una data':
                print(str(request.session.get('rilascio_permesso')))
                request.session['page_id'] = page+1
                request.session['alert'] = ''

        elif page==8:
            pagina_indietro=page
            print(str(request.POST.get('scadenza_permesso')))
            request.session['scadenza_permesso'] = request.POST.get('scadenza_permesso')
            request.session['alert'] = text['scelte_non_valide'][lingua]
            if not (request.session.get('scadenza_permesso')=='illimitato'):
                if str(request.session.get('rilascio_permesso'))!='Inserisci una data':
                    request.session['alert'] = ''
                    if Survey_manager.permesso_valido(request):
                        request.session['page_id'] = 6
                    else:
                        if (request.session.get('validita_permesso')=="scaduto"):
                            request.session['page_id'] = 9
                        elif (request.session.get('validita_permesso')=="meno_di_un_anno"):
                            request.session['page_id'] = non_idoneo;
                            request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/01.html"
                        elif (request.session.get('validita_permesso')=="date_non_valide"):
                            request.session['page_id'] = 7
                            request.session['alert'] = text['dati_errati'][lingua]
            elif request.session.get('scadenza_permesso')=='illimitato':
                request.session['alert'] = ''
                request.session['page_id'] = 6


        elif page==9:
            pagina_indietro=page
            request.session['ricevuta_rinnovo_permesso'] = request.POST.get('ricevuta_rinnovo_permesso')
            if str(request.session.get('ricevuta_rinnovo_permesso'))=='si':
                request.session['page_id'] = 12
            elif str(request.session.get('ricevuta_rinnovo_permesso'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/01.html"

        elif page==10:
            pagina_indietro=page
            request.session['contratto_locazione'] = request.POST.get('contratto_locazione')
            if str(request.session.get('contratto_locazione'))=='si':
                request.session['page_id'] = 14
            elif str(request.session.get('contratto_locazione'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"

        elif page==11:
            pagina_indietro=page
            if (str(request.POST.get('città'))!='' and str(request.POST.get('via'))!='' and (request.session.get('tipologia_permesso')=='asilo politico')):
                request.session['città'] = str(request.POST.get('città'))
                request.session['via'] = str(request.POST.get('via'))
                request.session['indirizzo_alloggio'] = str(request.POST.get('via'))+', '+str(str(request.POST.get('città')))
                if (geodecoder.from_address_to_coords(str(request.session.get('indirizzo_alloggio')))=="None"):
                    request.session['alert'] = text['dati_errati'][lingua]
                else:
                    request.session['page_id'] = idoneo


        elif page==12:
            pagina_indietro=page
            request.session['posso_ospitare_in_alloggio'] = request.POST.get('posso_ospitare_in_alloggio')
            if (request.session.get('tipologia_permesso')=='asilo politico'):
                request.session['page_id'] = idoneo
            if str(request.session.get('posso_ospitare_in_alloggio'))=="None":
                request.session['alert'] = text['dati_errati'][lingua]
            elif ((str(request.session.get('posso_ospitare_in_alloggio'))=="no") and not (request.session.get('tipologia_permesso')=='asilo politico')):
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"
            elif (str(request.POST.get('città'))!='' and str(request.POST.get('via'))!='' and not (request.session.get('tipologia_permesso')=='asilo politico')):
                request.session['città'] = str(request.POST.get('città'))
                request.session['via'] = str(request.POST.get('via'))
                request.session['indirizzo_alloggio'] = (str(request.POST.get('via'))+', '+str(str(request.POST.get('città'))))
                if geodecoder.from_address_to_coords(str(request.session.get('indirizzo_alloggio')))=="None":
                    request.session['alert'] = text['dati_errati'][lingua]
                elif str(request.session.get('posso_ospitare_in_alloggio'))=="si":
                    request.session['page_id'] = page+1
                    request.session['alert'] = ''
                elif str(request.session.get('posso_ospitare_in_alloggio'))=="ospite":
                    request.session['alert'] = ''
                    request.session['page_id'] = 10
                    Family_manager.ci_sono_partner_o_genitori(request)

        elif page==13:
            pagina_indietro=page
            request.session['contratto_locazione'] = request.POST.get('contratto_locazione')
            if str(request.session.get('contratto_locazione'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('contratto_locazione'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"

        elif page==14:
            pagina_indietro=page
            request.session['contratto_locazione_registrato'] = request.POST.get('contratto_locazione_registrato')
            if str(request.session.get('contratto_locazione_registrato'))=='si':
                request.session['page_id'] = 16
            elif str(request.session.get('contratto_locazione_registrato'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"

        elif page==15:
            pagina_indietro=page
            request.session['atto_compravendita'] = request.POST.get('atto_compravendita')
            if str(request.session.get('atto_compravendita'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('atto_compravendita'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"

        elif page==16:
            pagina_indietro=page
            request.session['n_tot_coinquilini'] = request.POST.get('n_tot_coinquilini')
            request.session['n_tot_coinquilini_min_14'] = request.POST.get('n_tot_coinquilini_min_14')
            if (request.session.get('n_tot_coinquilini')==''):
                request.session['n_tot_coinquilini']=0
            if (request.session.get('n_tot_coinquilini_min_14')==''):
                request.session['n_tot_coinquilini_min_14']=0
            if (Family_manager.c_e_partner(request)): #controlla che ci sia partner e vai a pag18
                request.session['page_id'] = 18
            if (not Family_manager.c_e_partner(request)):   #se non c'è partner controlla coinquilini, e vai a pag24
                Family_manager.check_coinquilini(request)
                request.session['metratura_casa'] = Survey_manager.calcola_metratura_casa(request)
                request.session['importo_reddito'] = Survey_manager.calcola_importo_reddito(request)
            if (not request.session.get('n_tot_coinquilini')==0):
                request.session['page_id'] = 17


        elif page==17:
            pagina_indietro=page

            request.session['coinquilini_a_carico'] = request.POST.get('coinquilini_a_carico')
            if (request.session.get("coinquilini_a_carico")=='' or request.session.get("coinquilini_a_carico")=='None'):
                request.session["coinquilini_a_carico"] = 0
            if ( int(request.session.get('coinquilini_a_carico')) > int(request.session.get('n_tot_coinquilini')) ): #check per valori coinquilini
                request.session['alert'] = text['dati_errati'][lingua]
                request.session['page_id'] = 16
            else:
                request.session['metratura_casa'] = Survey_manager.calcola_metratura_casa(request)
                request.session['importo_reddito'] = Survey_manager.calcola_importo_reddito(request)
                if int(request.session.get('n_tot_coinquilini'))==0:
                    if (not Family_manager.c_e_partner(request)):   #se non c'è partner controlla coinquilini, e vai a pag24, altrimenti
                        Family_manager.check_coinquilini(request)
                else:
                    if (Family_manager.c_e_partner(request)): #controlla che ci sia partner e vai a pag18
                        request.session['page_id'] = 18
                if not (Family_manager.ci_sono_partner_o_genitori(request)):
                    request.session['page_id'] = 24


        elif page==18:
            pagina_indietro=page
            request.session['alert'] = ''
            request.session['tipo_partner'] = request.POST.get('tipo_partner')
            if (request.session.get('tipologia_permesso')=='asilo politico'):
                request.session['page_id'] = 11
            else:
                if (request.session.get('posso_ospitare_in_alloggio') == 'no'):
                    request.session['page_id'] = 25
                else:
                    request.session['metratura_casa'] = Survey_manager.calcola_metratura_casa(request)
                    request.session['importo_reddito'] = Survey_manager.calcola_importo_reddito(request)
                    request.session['page_id'] = 24

        elif page==24:
            pagina_indietro=page
            request.session['alert'] = ''
            request.session['casa_sufficiente'] = request.POST.get('casa_sufficiente')
            if str(request.session.get('casa_sufficiente'))=='si':
                request.session['page_id'] = page+1
            elif str(request.session.get('casa_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/07.html"

        elif page==25:
            pagina_indietro=page
            request.session['alert'] = ''
            request.session['tipologia_lavoro'] = request.POST.get('tipologia_lavoro')
            if str(request.session.get('tipologia_lavoro'))=='':
                request.session['alert'] = 'Non hai inserito una tipologia per il lavoro, riprova'
            elif str(request.session.get('tipologia_lavoro'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ":<br> https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/06.html"
            else:
                request.session['page_id'] = 27


        elif page==26:
            pagina_indietro=page
            request.session['reddito_sufficiente'] = request.POST.get('reddito_sufficiente')
            if str(request.session.get('reddito_sufficiente'))=='si':
                request.session['page_id'] = idoneo
            elif str(request.session.get('reddito_sufficiente'))=='no':
                request.session['page_id'] = non_idoneo
                request.session['alert'] = text['scopri_perché_qui'][lingua] + ':<br>https://ondata.gitbooks.io/guida-per-il-ricongiungimento-extra-ue/content/08.html'

        elif page==27:
            pagina_indietro=page
            request.session['ha_documenti_lavoro'] = request.POST.get('ha_documenti_lavoro')
            if ((str(request.session.get('ha_documenti_lavoro'))=="si") and ('n_tot_coinquilini' in request.session)):
                request.session['page_id'] = 26
            elif str(request.session.get('ha_documenti_lavoro'))=="no":
                request.session['page_id'] = non_idoneo

        elif page==idoneo:
            request.session['guida'] = request.POST.get('guida')
            if request.session['guida'] == 'si':
                print('FINE')
                request.session['page_id'] = 30
                #report_maker.produci_guida(request)

        elif page==non_idoneo:
            request.session['guida'] = request.POST.get('guida')
            if request.session['guida'] == 'no':
                request.session['page_id'] = 1
            request.session['alert'] = ""

        elif page==30:
            request.session['guida'] = request.POST.get('guida')
            if request.session['guida'] == 'si':
                print('FINE')
                request.session['page_id'] = 30
                #report_maker.produci_guida(request)

        if (flag_back):
            request.session['page_id'] = page_before
            flag_back = False
            if (page_before==3):
                Family_manager.reset_parenti(request)



        return request
