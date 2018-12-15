from django.shortcuts import render
from django.views.generic import DetailView

import time

from .models import Domande, Risposte
from main_survey.survey import Survey_manager as questionario
import main_survey.db_manager
import main_survey.survey
import main_survey.report_maker

ANSWERS_TEMPLATE_PAGE_FOLDER = 'main_survey/answers_pages/'


#funzione per raccogliere l'indirizzo ip dell'utente, al momento non utilizzata:

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip






class PageView(DetailView):

    def get(request):

        if request.method=='GET':

            for key in request.session.keys():
                if key!='page_id':         #svuota le variabili, se già presenti, con la GET della prima pagina
                    request.session[key]=''

            current_timestamp_session = time.time()     #inizializza un timestamp per identificare la sessione
            request.session['session_id'] = current_timestamp_session
            page_id = 1
            request.session['page_id'] = page_id
            request.session['numero_temporaneo_figlio'] = 0
            request.session['numero_temporaneo_genitore'] = 0

        elif request.method=="POST":
            request = questionario.dispatcher(request)
            page_id = request.session.get('page_id')


        #A seguire, conversioni per stampa a video dei valori ricavati dalle variabili raccolte dinamicamente:

        if str(request.session.get('temp_parente'))=="None":
            parente = ""

        elif str(request.session.get('temp_parente'))=="partner_mag":
            parente = "Il partner"

        elif ((str(request.session.get('temp_parente'))=='figli_min_ug_14') or (str(request.session.get('temp_parente'))=='figli_15_17') or (str(request.session.get('temp_parente'))=='figli_magg')):
            numero_temporaneo_parente = request.session.get('numero_temporaneo_figlio')
            parente = "Il "+str(numero_temporaneo_parente)+"° figlio"

        elif (str(request.session.get('temp_parente'))=='genitore'):
            numero_temporaneo_parente = request.session.get('numero_temporaneo_genitore')
            parente = "Il "+str(numero_temporaneo_parente)+"° genitore"

        else:
            parente = request.session.get('temp_parente')

        if str(request.session.get('metratura_casa'))=="None":
            casa = ""
        else:
            casa = str(request.session.get('metratura_casa'))

        if str(request.session.get('importo_reddito'))=="None":
            reddito = ""
        else:
            reddito = str(request.session.get('importo_reddito'))

        if str(request.session.get('alert'))=="None":
            alert = ""
        else:
            alert = request.session.get('alert')

        if str(request.session.get('numero_temporaneo_parente'))=="None":
            numero_temporaneo_parente = ""

        #fine valori convertiti



        #Stampa di debug lato server:

        print("\n\nLA SITUAZIONE DI SESSION È QUESTA:\n")
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        print('\n\n')

        print("\n\n*****************************************************************\nSIAMO A PAGINA "+str(page_id)+"\n\n*****************************************************************\n")

        #fine stampa di debug lato server




        domanda = Domande.objects.filter(id=page_id)[0]     #la domanda proposta è trovata nel db principale, filtrata per page_id
        if (str(request.session.get('page_id'))!="30"):
            template_name = ANSWERS_TEMPLATE_PAGE_FOLDER+str(page_id)+'.html'      #template di default per domanda generica
            response = {'domanda': domanda, 'alert': alert, 'parente': parente, 'numero_temporaneo_parente': numero_temporaneo_parente, 'casa': casa, 'reddito': reddito}   #dizionario di risposta
        elif (str(request.session.get('page_id'))=="28"):
            response = report_maker.produci_guida(request)
            template_name = ANSWERS_TEMPLATE_PAGE_FOLDER+"guida.html"      #template per la guida



        return render(request, template_name, response)
