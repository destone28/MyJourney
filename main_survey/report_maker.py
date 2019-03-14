
from datetime import datetime
from . import geodecoder, geo_db_locator

translations = {
    'a': {
        'it': 'Ecco la tua guida!',
        'en': "Here's your guide!",
        'ar': 'هذا هو دليلك',
        'es': '¡Aquí está tu guía!',
        'zh': '这是你的引导！',
        'fr': 'Voici votre guide',
    },
    'b': {
        'it': 'Per i tuoi dati anagrafici ti serve:',
        'en': 'For your personal data you need:',
        'ar': 'ما يتعلق في بياناتك الشخصية تحتاج إلى:',
        'es': 'Para tus datos personales necesitas:',
        'zh': '为了填写你的个人信息你需要：',
        'fr': 'Pour vos données personnelles, vous aurez besoin de:',
    },
    'b1': {
        'it': 'passaporto',
        'en': 'a passport',
        'ar': 'جواز',
        'es': 'pasaporte',
        'zh': '护照',
        'fr': 'votre passeport',
    },
    'b2': {
        'it': 'codice fiscale',
        'en': 'tax code',
        'ar': 'رقم كود الضريبة الشخصي',
        'es': 'código fiscal',
        'zh': '税号',
        'fr': 'votre code fiscal',
    },
    'b3_1': {
        'it': 'carta o permesso di soggiorno in corso di validità',
        'en': 'residence card or valid residence permit',
        'ar': 'بطاقة الهوية أو تصريح إقامة سارية المفعول',
        'es': 'tarjeta o permiso de residencia válido',
        'zh': '有效的居留或长期居留',
        'fr': 'titre ou permis de séjour en cours de validité',
    },
    'b3_2': {
        'it': 'copia del  permesso scaduto con ricevuta di presentazione  del rinnovo',
        'en': 'a copy of the expired permit with receipt of the application for renewal',
        'ar': 'نسخة من تصريح الإقامة منتهي الصلاحية مع إيصال استلام التجديد',
        'es': 'copia del permiso vencido con recibo de presentación de la renovación',
        'zh': '已过期的居留连同续签申请收据',
        'fr': 'une photocopie du permis expiré avec accusé de réception du renouvellement',
    },
    'b4': {
        'it': 'certificato di stato famiglia  rilasciato dal comune di residenza con la dicitura “uso immigrazione”.',
        'en': 'family status certificate (‘certificato di stato famiglia’) issued by your municipality of residence clearly marked for "immigration use" (“uso immigrazione”).',
        'ar': 'شهادة الحالة العائلية صادرة من البلدية لمكان الإقامة تحت عبارة "استخدام الهجرة  (uso immigrazione)".',
        'es': 'certificado de estado de familia expedido por el municipio de residencia con la frase “uso immigazione”',
        'zh': '户口所在的市政府开的填有“移民用途”字样的家庭状况证明。',
        'fr': "certificat de composition de famille délivré par la municipalité de résidence avec le libellé «usage relevant des services d'immigration» (‘uso immigrazione’).",
    },
    'b7': {
        'it': 'Dichiarazione di impegno a sottoscrivere una polizza assicurativa sanitaria o altro titolo idoneo a garantire la copertura di tutti i rischi nel territorio nazionale, in favore dei genitori ultrasessantacinquenni.',
        'en': 'Declaration of commitment to take out a health insurance policy, or other appropriate cover, for parents over sixty-five years of age to ensure coverage of all risks while in Italy',
        'ar': 'تصريح الالتزام بالتأمين من خلال التوقيع على بوليصة التأمين الصحي أو أي سند مناسب آخر لضمان تغطية جميع المخاطر على الأراضي الوطنية ، لصالح الوالدين البالغون اكثر من خمسة وستين عاماً.',
        'es': 'Declaración de compromiso de suscripción de una póliza de seguro sanitaria o de otro título que sirva para garantizar la cobertura de todos los riesgos en el territorio nacional, a favor de los padres de más de 75 años',
        'zh': '为自己超过六十五岁的双亲签下健康保险或其他在国家境内可覆盖所有风险的保险的承诺声明。',
        'fr': "Déclaration d'engagement à souscrire à une police d'assurance couvrant les soins de santé ou toute autre document valable en mesure de garantir la couverture de tous les risques sur le territoire national, pour les parents âgés de plus de 65 ans et plus.",
    },
    'c': {
        'it': "Le informazioni e la documentazione da procurarti per l'alloggio sono le seguenti: Originale del contratto di locazione/comodato/compravendita, ricevuta di registrazione e/o rinnovo contratto di locazione, certificato di idoneità abitativa e igienico-sanitaria rilasciato dal Comune per finalità di ricongiungimento familiare.",
        'en': 'The information and documentation you need to present regarding your accommodation is as follows: Original rental contract/free use agreement/purchase agreement, receipt of registration and/or renewal of the rental contract, certificate of suitability for housing and sanitation issued by the Municipality for the purpose of family reunification.',
        'ar': 'فيما يلي المعلومات والوثائق المتعلقة بالسكن التي يجب تقديمها: النسخة الأصلية لعقد الإيجار / أو عقد الأتفاق / سند البيع والشراء أو إيصال التسجيل و/ أو تجديد عقد الإيجار ، وشهادة صلاحية السكنى والصرف الصحي الصادرة عن البلدية لأغراض تتعلق في لم شمل العائلة.',
        'es': 'Las informaciones y documentación que necesitas para el alojamiento son las siguientes: original del contrato de alquiler/comodato/compraventa, recibo de registro y/o renovación contrato de locación, certificado de idoneidad de alojamiento e higiénico-sanitaria expedido por el Municipio a los efectos de reagrupación familiar',
        'zh': '居所所需要的信息和证件为以下：租赁/无偿租赁/购买合同原件，租赁合同的登记和/或更新凭据，由市政府为了家庭团聚而开的住房合格证明和卫生-健康证明。',
        'fr': "Les informations et la documentation à obtenir pour l'hébergement sont les suivantes: Original du bail/de l’accord de prêt/du contrat d’achat, accusé de réception de l’enregistrement et/ou du renouvellement du bail, certificat de disponibilité de logement conforme aux conditions hygiéniques et sanitaires requises délivré par la municipalité aux fins du regroupement familial.",
    }
}

def produci_guida(request):
        ### INFO GENERICHE
        guida = {}
        lingua = 'it'

        guida['a'] = "<h1><u>" + translations['a'][lingua] + "</u></h1>"



        guida['b'] = "<h2><u>" + translations['b'][lingua] + "</u></h2>"

        guida['b1'] = "<li>" + translations['b1'][lingua] + "</li>"
        guida['b2'] = "<li>" + translations['b2'][lingua] + "</li>"

        #Se permesso valido
        if ('ricevuta_rinnovo_permesso' not in request.session):
            guida['b3_1'] = "<li>" + translations['b3_1'][lingua] + "</li>"

        #Se permesso scaduto
        if (str(request.session.get('ricevuta_rinnovo_permesso'))=='si'):
            guida['b3_2'] = "<li>" + translations['b3_2'][lingua] + "</li>"
        #città = str(request.session.get('città'))
        guida['b4'] = "<li>" + translations['b4'][lingua] + "</li>"

        ##Per ogni parente presente
        if ('lista_familiari' in request.session):
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
                guida['b7'] = "<li>" + translations['b7'][lingua] + "/li>"

            guida['b5'] = "<li>Fotocopie delle pagine con dati anagrafici e numero di Passaporto per "+ parente + "</li>"

        ##Per ogni coinquilino
        if ('n_tot_coinquilini' in request.session):
            if (str(request.session.get('n_tot_coinquilini'))=="None"):
                request.session['n_tot_coinquilini'] = 0
            if (int(request.session.get('n_tot_coinquilini'))!=0):
                guida['b6'] = "<li>Certificato dello stato di famiglia delle persone che abitano nel tuo alloggio, rilasciato dal loro Comune di residenza con la dicitura 'uso immigrazione'</li>"

            guida['c'] = "<h2><u>" + translations['c'][lingua] + "</u></h2>"

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


        if ('indirizzo_alloggio' in request.session):
            guida['e'] = "<h2><u>Infine, eccoti qualche informazione aggiuntiva:</u></h2>"
            guida['f'] = "Puoi richiedere aiuto presso:<br>"+str(geo_db_locator.sindacati_e_patronati(request.session.get('indirizzo_alloggio')))
            guida['g'] = "Il municipio di riferimento per i servizi anagrafici è:<br>"+str(geo_db_locator.anagrafe_milano_piu_vicina(request.session.get('indirizzo_alloggio')))
            guida['h'] = "Per l'idoneità abitativa della tua casa:<br>"+str(geo_db_locator.idoneita_abitativa_vicina_milano(request.session.get('indirizzo_alloggio')))
            guida['i'] = "Ti occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€."


        return guida
