from django.shortcuts import render
from django.views.generic import DetailView
from collections import OrderedDict

import time

from .models import Domande, Risposte
from main_survey.survey import Survey_manager as questionario
import main_survey.db_manager
import main_survey.survey
from . import report_maker

ANSWERS_TEMPLATE_PAGE_FOLDER = 'main_survey/answers_pages/'


#funzione per raccogliere l'indirizzo ip dell'utente, al momento non utilizzata:

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

stepsTranslations = {
    'Famiglia': {
        'it': 'Famiglia',
        'en': 'Family',
        'ar': 'العائلة',
        'es': 'Familia',
        'zh': '家庭',
        'fr': 'Famille',
    },
    'Permesso di Soggiorno': {
        'it': 'Permesso Di Soggiorno',
        'en': 'Residence Permit',
        'ar': 'تصريح الإقامة',
        'es': 'Permiso De Residencia',
        'zh': '居留证',
        'fr': 'Permis De Séjour',
    },
    'Casa': {
        'it': 'Casa',
        'en': 'Home',
        'ar': 'البيت',
        'es': 'Casa',
        'zh': '住房',
        'fr': 'Habitation',
    },
    'Reddito': {
        'it': 'Reddito',
        'en': 'Income',
        'ar': 'مجموع الدخل',
        'es': 'Renta',
        'zh': '收入',
        'fr': 'Revenu'
    }
}

class PageView(DetailView):

    def get(request):

        linguaDefault = 'it'

        if request.method=='GET':

            for key in request.session.keys():
                if key!='page_id':         #svuota le variabili, se già presenti, con la GET della prima pagina
                    request.session[key]=''
                    lingua = linguaDefault

            current_timestamp_session = time.time()     #inizializza un timestamp per identificare la sessione
            request.session['session_id'] = current_timestamp_session
            request.session['page_list'] = 0
            page_id = 1
            pagina_template = page_id
            request.session['page_id'] = page_id

            request.session['numero_temporaneo_figlio'] = 0
            request.session['numero_temporaneo_genitore'] = 0

        elif request.method=="POST":
            request = questionario.dispatcher(request)
            page_id = request.session.get('page_id')
            pagina_template = page_id
            lingua = request.session.get('lingua')
            if (lingua == "en"):
                page_id = request.session.get('page_id')+31
            if (lingua == "es"):
                page_id = request.session.get('page_id')+62
            if (lingua == "ar"):
                page_id = request.session.get('page_id')+93
            if (lingua == "zh"):
                page_id = request.session.get('page_id')+124
            if (lingua == "fr"):
                page_id = request.session.get('page_id')+155

        lingua = lingua or linguaDefault # fallback if not lingua in request session
        trackSteps = OrderedDict([
            ('img/track_family.png', stepsTranslations['Famiglia'][lingua]),
            ('img/track_documents.png', stepsTranslations['Permesso di Soggiorno'][lingua]),
            ('img/track_house.png', stepsTranslations['Casa'][lingua]),
            ('img/track_work.png', stepsTranslations['Reddito'][lingua]),
            ('img/fine.png', '&#9873;')
        ])

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
        if (pagina_template!=30):
            template_name = ANSWERS_TEMPLATE_PAGE_FOLDER+str(pagina_template)+'.html'      #template di default per domanda generica
            response = {'domanda': domanda, 'alert': alert, 'casa': casa, 'reddito': reddito, 'trackSteps': trackSteps, 'lingua': lingua}   #dizionario di risposta
            if (pagina_template==5):
                response = {'domanda': domanda, 'alert': alert, 'parente': parente, 'numero_temporaneo_parente': numero_temporaneo_parente, 'casa': casa, 'reddito': reddito, 'trackSteps': trackSteps, 'lingua': lingua}
        elif (pagina_template==30):
            response = report_maker.produci_guida(request)
            template_name = ANSWERS_TEMPLATE_PAGE_FOLDER+"guida.html"



        return render(request, template_name, response)
