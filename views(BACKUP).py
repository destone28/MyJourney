from django.shortcuts import render
from django.views.generic import DetailView

import time

from .models import Domande, Risposte
from main_survey.survey import Survey_manager as questionario
import main_survey.db_manager
import main_survey.survey

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

            current_timestamp_session = time.time()
            request.session['session_id'] = current_timestamp_session
            page_id = 1
            request.session['page_id'] = page_id

        elif request.method=="POST":
            request = questionario.dispatcher(request)
            page_id = request.session.get('page_id')


        #A seguire, conversioni per stampa a video dei valori ricavati dalle variabili raccolte dinamicamente:

        if str(request.session.get('temp_parente'))=="None":
            parente = ""
        elif str(request.session.get('temp_parente'))=="partner_mag":
            parente = "partner"
        elif ((str(request.session.get('temp_parente'))=='figli_min_ug_14') or (str(request.session.get('temp_parente'))=='figli_15_17') or (str(request.session.get('temp_parente'))=='figli_magg')):
            parente = "figlio"
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
            response = {'domanda': domanda, 'alert': alert, 'parente': parente, 'casa': casa, 'reddito': reddito}   #dizionario di risposta
        elif (str(request.session.get('page_id'))=="30"):
            template_name = "main_survey/answers_pages/guida.html"      #template per la guida
            response = questionario.Report_maker.produci_guida(request)


        return render(request, template_name, response)