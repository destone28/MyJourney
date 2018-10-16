from django.shortcuts import render
from django.views.generic import DetailView

import time

from .models import Domande, Risposte
from main_survey.survey import Survey_manager as questionario
import main_survey.db_manager

ANSWERS_TEMPLATE_PAGE = 'main_survey/answers_pages/'

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

        if str(request.session.get('temp_parente'))=="None":
            parente = ""
        else:
            parente = request.session.get('temp_parente')

        if str(request.session.get('casa_sufficiente'))=="None":
            casa = ""
        else:
            casa = request.session.get('casa_sufficiente')

        if str(request.session.get('reddito_sufficiente'))=="None":
            reddito = ""
        else:
            reddito = request.session.get('reddito_sufficiente')

        print("\n\n*****************************************************************\nSIAMO A PAGINA "+str(page_id)+"\n\n*****************************************************************\n")
        domanda = Domande.objects.filter(id=page_id)[0]
        template_name = ANSWERS_TEMPLATE_PAGE+str(page_id)+'.html'
        response = {'domanda': domanda, 'alert': str(request.session.get('alert')), 'parente': parente, 'casa': casa, 'reddito': reddito}

        return render(request, template_name, response)
