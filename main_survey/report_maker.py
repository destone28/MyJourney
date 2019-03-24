
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
        'it': 'passaporto, carta o permesso di soggiorno in corso di validità  o, se scaduto,  copia del  permesso scaduto con ricevuta di presentazione  del rinnovo,  codice fiscale,  certificato di stato famiglia  rilasciato dal comune di residenza con la dicitura “uso immigrazione”.',
        'en': 'a passport, residence card or valid residence permit or, if expired, a copy of the expired permit with receipt of the application for renewal, tax code, family status certificate (‘certificato di stato famiglia’) issued by your municipality of residence clearly marked for "immigration use" (“uso immigrazione”).',
        'ar': 'ما يتعلق في بياناتك الشخصية تحتاج إلى: جواز سفر أو بطاقة الهوية أو تصريح إقامة سارية المفعول أو إذا انتهت صلاحيتها ، نسخة من تصريح الإقامة منتهي الصلاحية مع إيصال استلام التجديد ، رقم كود الضريبة الشخصي ، شهادة الحالة العائلية صادرة من البلدية لمكان الإقامة تحت عبارة "استخدام الهجرة  (uso immigrazione)".',
        'es': 'pasaporte, tarjeta o permiso de residencia válido o, si está vencido, copia del permiso vencido con recibo de presentación de la renovación, código fiscal, certificado de estado de familia expedido por el municipio de residencia con la frase “uso immigazione”',
        'zh': '为了填写你的个人信息你需要：护照，有效的居留或长期居留，或者如果已经过期，已过期的居留连同续签申请收据，税号，户口所在的市政府开的填有“移民用途”字样的家庭状况证明。',
        'fr': 'votre passeport, titre ou permis de séjour en cours de validité ou, si celui-ci a expiré, une photocopie du permis expiré avec accusé de réception du renouvellement, votre code fiscal, certificat de composition de famille délivré par la municipalité de résidence avec le libellé «usage relevant des services d''immigration» (‘uso immigrazione’).',
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
    },
    'c1': {
        'it':"ATTENZIONE: in caso di ricongiungimento familiare di figli minori di 18 anni, nell’alloggio dove dimoreranno deve necessariamente abitare almeno uno dei genitori. In caso di ricongiungimento familiare per un solo minore di anni 14 qualora nell’alloggio non siano presenti altri minori di anni 14, il certificato idoneità abitativa e igienico sanitaria può essere sostituito dal contratto di locazione/comodato/compravendita, unitamente alla dichiarazione di ospitalità del titolare/i dell’appartamento redatta su mod. “S1”, oltre a fotocopia del documento d’identità del dichiarante/i, firmata dal medesimo/i.",
        'en':"ATTENTION: for family reunification of children under 18 years of age, at least one of the parents must live in the accommodation where the children or child will live. In the case of family reunification for a single child under the age of 14 if there are no other children under the age of 14 in the accommodation, the certificate of housing suitability and health and hygiene can be replaced by the rental contract/free use agreement/purchase deed, together with the declaration of hospitality of the owner(s) of the apartment on form 'S1', as well as a photocopy of the identity document of the declarant(s), signed by him/her, and family status certificate (‘certificato stato famiglia’) of the host issued by the Municipality of residence marked for “immigration use” (“uso immigrazione”).",
        'ar':"تنبيه: في حالة لم شمل العائلة للأطفال دون سن 18 سنة ، يجب أن يكون أحد الوالدين على الأقل يقيم في السكن . أما في حالة لم شمل العائلة لقاصر واحد من 14 عامًا ، إن لم يكن هناك أطفال آخرون تحت 14 سنة في السكن ، فيمكن الإستعاضة عن شهادة الصلاحية والصرف الصحي بعقد الإيجار / أو عقد الأتفاق / أو سند البيع والشراء ، بالإضافة إلى تصريح الضيافة من طرف صاحب الملك المتواجدة على النموذج 'S1' ، بالإضافة إلى نسخة من وثيقة هوية صاحب التصريح  وموقعة من طرفه.",
        'es':"ATENCIÓN: en caso de reagrupación familiar de hijos menores de 18 años, en el alojamiento donde vivan debe vivir necesariamente al menos uno de los padres. En el caso de reagrupación familiar para sólo un menor de 14 años, si en el alojamiento no están presentes otros menores de 14 años, el certificado de idoneidad de alojamiento e higiénico-sanitaria puede sustituirse por el contrato de alquiler/comodato/compraventa, junto con la declaración de alojamiento del/los titular/a de la vivienda redactada en el modelo “S1”, junto a la fotocopia del documento de identidad del/los declarante/s, firmada por el/los mismo/s.",
        "zh":"注意：如果团聚的是18岁以下的孩子，父母其中一个必须住在他们所居住的房屋内。如果团聚的是一个14岁以下的儿童，并且在房屋内不存在其他14岁以下的儿童，房屋合格证明和卫生健康证明可由租赁/无偿租赁/购买合同，连同由公寓持有人按照“S1”表格填的接纳声明，以及声明人的身份证复印件替代，声明人的身份证复印件由他自己签字。",
        "fr":"ATTENTION: en cas de regroupement familial impliquant des enfants de moins de 18 ans, au moins l’un des deux parents devra impérativement habiter dans le logement. En cas de regroupement familial impliquant uniquement un mineur âgé 14 ans, si d'autres mineurs également âgés de 14 ans ne sont pas présents dans le logement, le certificat de disponibilité de logement conforme aux conditions hygiéniques et sanitaires peut être remplacé par le bail/accord de prêt/contrat d’achat, ainsi que la déclaration d'un accueil avec hébergement par le(s) propriétaire(s) du logement, rédigée sur le modèle «S1», accompagnée d'une photocopie du/des document(s) d'identité du/des déclarant(s), signée par la/les même(e) personne(s).",
    },
    'c2': {
        'it':"copia del contratto di locazione/comodato/compravendita,  ricevuta di registrazione e/o rinnovo contratto di locazione, certificato di idoneità abitativa e igienico-sanitaria rilasciato dal Comune per finalità di ricongiungimento familiare, dichiarazione redatta dal titolare/i dell’appartamento su mod. “S2”, attestante il consenso ad ospitare anche i ricongiunti, fotocopia del documento d’identità del titolare/i dell’alloggio, firmata dal medesimo/i e con indicazione del suo recapito telefonico, certificato stato di famiglia dell’ospitante rilasciato dal comune di residenza con la dicitura “uso immigrazione”.",
        'en':'copy of the rental contract/free use agreement/purchase agreement, receipt of registration or renewal of the rental contract, certificate of suitability for housing and sanitation issued by the Municipality for family reunification purposes, declaration drawn up by the owner(s) of the apartment on form "S2", giving their consent to host the family members, photocopy of the identity document of the owner(s) of the accommodation, signed by them with details of their telephone number, certificate of family status (‘certificato di stato famiglia’) of the host issued by the municipality of residence with the words "immigration use" (“uso immigrazione”).',
        'ar':'إذا كنت ضيفًا يجب إحضار : نسخة من عقد الإيجار / أو عقد الأتفاق / سند البيع والشراء ،  إيصال التسجيل و/ أو تجديد عقد الإيجار ، وشهادة صلاحية السكنى والصرف الصحي الصادرة عن البلدية لأغراض تتعلق في لم شمل العائلة ، تصريح من مالك الشقة المتواجد على النموذج "S2" ، التصريح بالموافقة على إمكانية الضيافة الى من يتم دعوته الى لم الشمل ، نسخة من وثيقة هوية صاحب الملك ، مُوَقّعة من قبله إضافة الى رقم هاتفه ، شهادة الحالة العائلية للمضيف صادرة عن بلدية مكان الإقامة تحت عبارة "استخدام الهجرة  (uso immigrazione)".',
        'es':'copia del contrato de alquiler/comodato/compraventa, recibo de registro y/o renovación contrato de alquiler, certificado de idoneidad de alojamiento e higiénico-sanitaria expedido por el Municipio a los efectos de reagrupación familiar, declaración redactada por el/los titular/es de la vivienda en el modelo “S2”, que certifica el consentimiento para alojar también a las personas reagrupadas, fotocopia del documento de identidad del/de los titular/es del alojamiento firmada por el/los mismo/s y con indicación de su número de teléfono, certificado de estado de familia de quien aloja expedido por el Municipio de residencia con la frase “uso immigrazione”',
        'zh':'如果你是房客：租赁/无偿租赁/购买合同复印件，租赁登记和/或更新凭据，市政府为了家庭团聚而开的住房合格证明和卫生健康证明，公寓持有人按照“S2”表格填的声明，证明也同意接纳团聚的家人，住房持有人的身份证复印件，由他们自己签字并写有其电话号码，由户口所在的市政府开的填有“移民用途”字样的房主的家庭状况证明。',
        'fr':'copie du bail /accord de prêt/contrat d’achat, accusé de réception de l’enregistrement et/ou du renouvellement du bail, certificat de disponibilité de logement conforme aux conditions hygiéniques et sanitaires requises délivré par la municipalité aux fins du regroupement familial, déclaration rédigée par le(s) propriétaire(s) du logement conformément au modèle «S2», attestant le consentement à également accueillir les membres de la famille qui font l''objet d''un regroupement, la photocopie du document d''identité du/des propriétaire(s) de l''habitation, signée par la/les même(e) personne(s) et avec indication de son/leur numéro de téléphone, le certificat de composition de famille de l’hébergeur(euse) délivré par la municipalité de résidence avec les mots «usage relevant des services d''immigration» (‘uso immigrazione’).'
    },
    'd': {
        'it':"Lavoro",
        'en':"Job",
        'ar':"وظيفة",
        'es':"Trabajo",
        'zh':"工作",
        'fr':"Emploi",
    },
    'd1_a': {
        'it':"Lavoratore dipendente: Certificazione Unica (C.U. ex C.U.D.) e relativa ricevuta di presentazione,  contratto di lavoro/lettera di assunzione (modulo C/Ass – Unilav),  ultime tre buste paga, autocertificazione del datore di lavoro, redatta su modello “S3” con data non anteriore di mesi 1, da cui risulti l’attualità del rapporto di lavoro e la retribuzione mensile corrisposta,  fotocopia del documento d’identità del datore di lavoro, debitamente firmata dal medesimo.",
        'en':"Employee: Unified Salary Certificate (called C.U. formerly called C.U.D.) and receipt of submission, employment contract/letter of employment (form C/Ass - Unilav), last three pay slips, a self-certification from your employer on form 'S3' not more than 1 month old, with details of the employment contract and the monthly salary paid, photocopy of the identity document of the employer, signed by him/her.",
        'ar':"العامل الموظف: شهادة التصريح بالدخل (CU ex CUD) وإيصال التقديم ، وعقد العمل/أو خطاب التوظيف (نموذج C/Ass - Unilav)) ، الثلاثة الأخيرة لكشوف المعاش الشهري ، أو التصريح بالدفع من طرف رب العمل معطاه عن طريع النموذج  'S3' لتاريخ لا يتجاوز الشهر الواحد ، مما يدل على الوضع الحالي فيما يخص العمل والراتب الشهري المدفوع ، صورة عن وثيقة هوية رب العمل وموقعة حسب الأصول من طرفه.",
        'es':"Trabajador subordinado: Certificación Única (C.U. antiguo C.U.D.) y su correspondiente recibo de presentación, contrato de trabajo/carta de contratación (formulario C/Ass – Unilav), las tres últimas minutas, certificación del empleador, redactada en el formulario “S3” con fecha no anterior a 1 mes, donde resulte que la relación laboral está en vigor y el sueldo mensual pagado, fotocopia del documento de identidad del empleador, debidamente firmado por el mismo.",
        'zh':"劳工：年收入总结证明（C.U.前C.U.D.）和呈交凭据，劳工合同/雇用信（C/Ass – Unilav表格），最后三个月的月薪单，雇主根据“S3”表格填写的自我声明，日期在前一个月内，由此证明现行的雇佣关系，和支付的月薪，雇主身份证复印件，由他自己签字。",
        'fr':"Travailleur(euse) salarié(e): Certification unique (C.U., p. ex., C.U.D.) et accusé de réception connexe, contrat de travail/lettre d'embauche (formulaire C/Ass – Unilav), trois derniers bulletins de paie, auto-certification de l'employeur rédigée sur le modèle «S3» avec une date non antérieure à un (1) mois certifiant la pertinence du contrat de travail et la rémunération mensuelle correspondante, photocopie du document d'identité de l'employeur dûment signée par ce dernier.",
    },
    'd1_b': {
        'it':"Lavoratore domestico, colf, badante: ultima dichiarazione dei redditi, ove posseduta, e relativa ricevuta di presentazione, 730/Unico in caso di reddito superiore agli 8.000 euro annui, comunicazione di assunzione al Centro per l’Impiego o all’INPS , ultimo bollettino di versamento dei contributi INPS, con attestazione dell’avvenuto pagamento, autocertificazione del datore di lavoro, redatta su modello “S3”, con data non anteriore di mesi 1 da cui risulti l’attualità del rapporto di lavoro e la retribuzione mensile corrisposta, fotocopia del documento d’identità del datore di lavoro, debitamente firmata dal medesimo",
        'en':"Domestic worker, domestic helper, care worker: for those with an income over € 8.000 a year your last tax form 730/UNICO, and receipt of submission, copy of notification of employment given to the Employment Centre or to INPS, latest INPS contributions payment slip, with proof of payment, self-certification by the employer on form 'S3', not more than 1 month old with details of the employment contract and the monthly salary paid, photocopy of the identity document of the employer, signed by the him/her.",
        'ar':"عامل منزلي ، عاملة منزلية ، مقدم الرعاية : آخر كشف بتصرح الدخل بحوزته وإيصال التقديم  ، (730/Unico) في حال تجاوز الدخل اﻠ   8.000يورو في السنة ، أو إشعار بالتوظيف إلى مركز التوظيف أو INPS ، آخر قسيمة للدفع  في اشتراكات اﻠ INPS ، مع إثبات إجراء الدفع ، والتصريح من قبل رب العمل ، التي يتم إعدادها على نموذج 'S3' ، مع تاريخ لا يتجاوز الشهر الواحد مما يدل على الوضع الحالي فيما يخص العمل والراتب الشهري المدفوع ، صورة عن وثيقة هوية رب العمل وموقعة حسب الأصول من طرفه.",
        'es':"Trabajador del hogar, empleado doméstico, cuidador: última declaración de la renta, si la posee, y correspondiente recibo de presentación, 730/Único en caso de renta superior a 8.000 euros al año, comunicación de contratación al Centro de Empleo o al INPS, último boletín de pago de cotizaciones INPS, con certificado de pago, autocertificación del empleador, redactada en el modelo “S3”, con fecha no anterior a 1 mes, donde resulte que la relación laboral está en vigor y el sueldo mensual pagado, fotocopia del documento de identidad del empleador, debidamente firmado por el mismo. ",
        'zh':"家庭工，家政人员，护理人员：最后一次的纳税申报表，如果有的话，以及相关的呈交凭据，730/自然人收入申报表格，在年薪超过8.000欧元的情况下，寄给就业中心和国家社会保障机构的雇用通知，最近一次社会保险税的发票，证明已交付，雇主根据“S3”表格填写的自我声明，日期在前一个月内，由此证明现行的雇佣关系，和支付的月薪，雇主身份证复印件，由他自己签字。",
        'fr':"Personnel de maison, femme/homme de ménage, aidant(e)s: dernière déclaration d'impôt lorsque celle-ci est disponible et accusé de réception connexe, «730/Unique» en cas de revenu excédant 8 000 euros par an, avis de prise de fonctions émise par le Centre pour l'emploi («Centro per l'impiego» ou «INPS»), derniers ordres de virement des cotisations de l’INPS accompagnés de l’attestation du paiement, auto-certification de l'employeur rédigée sur le modèle «S3» avec une date non antérieure à un (1) mois, certifiant la pertinence du contrat de travail et la rémunération mensuelle correspondante, photocopie du document d'identité de l'employeur dûment signée par celui-ci.",
    },
    'd1_c': {
        'it':"Lavoratore autonomo: visura camerale/certificato di iscrizione alla Camera di Commercio recente, certificato di attribuzione P. IVA, licenza comunale, ove prevista, se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta, se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta, tutte le fatture (acquisto e vendita) relative all’anno in corso, durc certificato o copia modelli F24",
        'en':"Self-employed: business profile (‘visura camerale’)/recent certificate of Chamber of Commerce enrollment, VAT number certificate, if applicable municipal license, if the business was started more than 1 year ago, income tax return (UNICO form) with receipt of electronic presentation attached and accounts for the current year, which must be stamped and signed by a professional accountant with copy of his/her identity document attached, the membership card of the professional body or the updated chamber of commerce business profile (‘visura camerale’) with details of the business. If the activity has been started for less than 1 year, accounts for the current year, which must be stamped and signed by the professional with a copy of his/her identity document, membership card of the professional body or updated chamber of commerce business profile with details of the business, all invoices (purchase and sale) for the current year, DURC certificate or copy",
        'ar':"العامل المستقل: شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة حديثة ، شهادة رقم ضريبة القيمة المضافة P.IVA ، رخصة البلدية ، إن كانت مطلوبة ، وإذا كان النشاط التجاري قد بدأ منذ أكثر من سنة ، أو التصريح بالدخل الضريبي (نموذج UNICO) مرفق به إيصال التقديم الإلكتروني والميزانية العمومية المتعلقة للسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة ، فيما يتعلق بالنشاط التجاري ، إن كان النشاط قد بدأ منذ أقل من سنة واحدة ، الميزانية العمومية المتعلقة بالسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة فيما يتعلق بالنشاط التجاري المنجز ، وجميع الفواتير (الشراء والبيع) المتعلقة بالسنة الجارية ، أو شهادة معتمدة أو نسخة من النوذج F2",
        'es':"Trabajador autónomo: certificado del Registro de Mercantil/certificado de inscripción en la Cámara de Comercio reciente, certificado de atribución de N° de IVA, licencia municipal, si estuviera prevista, si la actividad ha iniciado hace más de 1 año, declaración de la renta (modelo UNICO) adjuntando recibo de presentación telemática y balance relativo al año en curso, que deberá estar sellado y firmado por el profesional con anexa fotocopia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado inherente a la actividad realizada, si la actividad se ha iniciado hace menos de 1 año, balance referente al año en curso, que deberá estar sellado y firmado por el profesional con anexa fotocopia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado inherente a la actividad realizada, todas las facturas (de compra y venta) relativas al año en curso, certificado Durc o copia modelos F24",
        'zh':"独立工作者：商会注册/最近的在商会的注册证明，增值税号分配证明，市政府许可证，如有预期，如果业务开始了超过1年，当下年份的纳税申报表（收入申报表格），并附上电子呈交凭据和收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于其进行的工作的商会注册更新，如果业务开始了的时间少于1年，当下年份的收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于进行的工作的商会注册更新，关于当下年份的所有的发票（购买和销售），税务合规证明书或者F24表格副本。",
        'fr':"Travailleur(euse) indépendant(e): certificat récent établi par la chambre de commerce pertinente, certificat d'attribution de la P. IVA (TVA), permis municipal, s'il y a lieu, si l'activité est déjà démarrée depuis plus d'un (1) an, déclaration de revenus (modèle UNIQUE) avec l’accusé de réception annexé du dépôt électronique et des états financiers prévus pour l'année en cours, qui devront être estampés et signés par le professionnel avec la copie accompagnant le document d'identité de ce dernier, la carte d’identification attestant de l’accréditation à l’Ordre ou la certification établie par la chambre mise à jour sur la base de l'activité effectuée, si l'activité est déjà démarrée depuis moins d'un (1), les états financiers prévus pour l'année en cours, qui devront être estampés et signés par le professionnel avec la copie accompagnant le document d'identité de ce dernier, la carte d’identification attestant de l’accréditation à l’Ordre ou la certification établie par la chambre mise à jour sur la base de l'activité effectuée, toutes les factures (achat et vente) relatives à l'année en cours, la certification DURC (Documento Unico di Regolarità Contributiva) ou une copie des modèles «F24»",
    },
    'd1_d': {
        'it':"Liberi Professionisti: iscrizione all’albo del libero professionista, se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta, se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta.",
        'en':"Freelancers: registration in the register of the freelance professionals, if the business has been in existence for more than 1 year, income tax return (UNICO form) with receipt of electronic presentation attached and accounts for the current year, which must be stamped and signed by the professional with copy of his/her identity document attached, copy of their registration with a professional body, or of the updated chamber of commerce business profile (‘visura camerale’) with details of the business. If the business is less than 1 year old, accounts for the current year, which must be stamped and signed by the professional with a copy of his/her identity document attached, a copy of their registration with a professional body or the updated chamber of commerce business profile (‘visura camerale’) with details of the business.",
        'ar':"الأعمال الحرة: شهادة التسجيل في السجل المهني ، إذا كان النشاط قد بدأ منذ أكثر من سنة ، التصريح بالدخل الضريبي (نموذج UNICO) مرفق مع إيصال التقديم الإلكتروني والميزانية العمومية  المتعلقة بالسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة ، فيما يتعلق بالنشاط التجاري ، إن كان النشاط قد بدأ منذ أقل من سنة واحدة ، الميزانية العمومية المتعلقة بالسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة فيما يتعلق بالنشاط التجاري المنجز .",
        'es':"Profesionales independientes: colegiación en el colegio profesional del profesional independientes, si la actividad se ha iniciado desde hace más de 1 año, declaración de la renta (modelo UNICO) adjuntando recibo de presentación telemática y balance relativo al año en curso, que deberá estar sellado y firmado por el profesional con anexa fotocopia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado, si la actividad se ha iniciado hace menos de un año, balance referente al año en curso, que deberá estar sellado y firmado por profesional con anexa copia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado inherente a la actividad realizada.",
        'zh':"自由工作者：在自由专业人士名册的注册，如果业务开始超过1年，关于当下年份的纳税申报表（收入申报表格）并附上电子呈交凭据和收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于进行的工作的商会注册更新， 如果业务开始了的时间少于1年，关于当下年份的收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于进行的工作的商会注册更新。",
        'fr':"Professionnels indépendants: inscription à l’Ordre des professions libérales s'il y a lieu, si l'activité est déjà démarrée depuis plus d'un (1) an, déclaration de revenus (modèle UNIQUE) avec l’accusé de réception annexé du dépôt électronique et des états financiers prévus pour l'année en cours, qui devront être estampés et signés par le professionnel avec la copie accompagnant le document d'identité de ce dernier, la carte d’identification attestant de l’accréditation à l’Ordre ou la certification établie par la chambre de commerce, mise à jour sur la base de l'activité effectuée, si l'activité est déjà démarrée depuis moins d'un (1), les états financiers prévus pour l'année en cours, qui devront être estampés et signés par le professionnel avec la copie accompagnant le document d'identité de ce dernier, la carte d’identification attestant de l’accréditation à l’Ordre ou la certification établie par la chambre mise à jour sur la base de l'activité effectuée.",
    },
    'd1_e': {
        'it':"Socio Lavoratore: visura camerale della cooperativa, certificato di attribuzione Partita IVA, dichiarazione del presidente della cooperativa da cui risulti l’attualità del rapporto di lavoro, redatta su modello “S3”, con data non anteriore di mesi 1 da cui risulti l’attualità del rapporto di lavoro e la retribuzione mensile corrisposta, fotocopia del documento d’identità del datore di lavoro, debitamente firmata dal medesimo, dichiarazione dei redditi (modello UNICO), ove posseduto, ultime tre buste paga,  contratto di lavoro/lettera di assunzione (modulo C/Ass – Unilav).",
        'en':"Partners in a cooperative: chamber of commerce business profile (‘visura camerale’) of the cooperative, certificate of allocation of VAT number, declaration of the president of the cooperative detailing the employment relationship not more than 1 month old on form “S3” form with details of employment and the monthly salary paid, photocopy of the identity document of the employer, signed by him/her, tax return (UNICO form) if in you have one, the last three pay slips, employment contract/letter of employment (form C/ASS - Unilav).",
        'ar':"عامل شريك: شهادة غرفة التجارة في تسجيل الشركة التعاونية ، في غرفة التجارة حديثة ، شهادة رقم ضريبة القيمة المضافة P.IVA ، وتصريح رئيس الشركة التعاونية والتي يبين من خلالها الوضع الحالي للأعمال ، والمعدّة على نموذج 'S3' ، مع تاريخ لا يتجاوز الشهر الواحد يُظهر الوضع الحالي المتعلق بالعمل والراتب الشهري المدفوع ، صورة عن وثيقة هوية رب العمل ، موقعة حسب الأصول من طرفه ، تصريح الدخل الضريبي (نموذج UNICO) الحاصل عليه ، الثلاثة الأخيرة لكشوف المعاش الشهري/ خطاب التوظيف  (Modulo C/Ass - Unilav).",
        'es':"Socio Trabajador: certificado del Registro Mercantil de la cooperativa, certificado de atribución del Número de IVA, declaración del presidente de la cooperativa en la que resulte que la relación laboral está en vigor, redactada en el modelo “S3”, con fecha no anterior a 1 mes, donde resulte que la relación laboral está en vigor y el sueldo mensual pagado, fotocopia del documento de identidad del empleador, debidamente firmado por el mismo, declaración de la renta (modelo UNICO), si se poseen, últimas tres recibos de pago, contrato de trabajo/carta de contratación (formulario C/Ass – Unilav).",
        'zh':"合伙人员工：合作社的商会注册，增值税号分配证明，合作社主席按照“S3”表格填写的声明，日期在前一个月内，由此证明现行的雇佣关系，和支付的月薪，雇主身份证复印件，由他自己签字，纳税申报表（收入申报表格），如果有的话，最后三个月的月薪单，工作合同/雇用信（C/Ass – Unilav表格）。",
        'fr':"Associé(e) exploitant(e): accréditation par la chambre de commerce dont la coopérative dépend, certificat d'attribution de la P. IVA (TVA), déclaration du président de la coopérative, rédigée sur le modèle «S3» avec une date non antérieure à un (1) mois, certifiant la pertinence du contrat de travail et la rémunération mensuelle correspondante, photocopie du document d'identité de l'employeur dûment signée par celui-ci, déclaration de revenus (modèle UNIQUE), lorsque celle-ci est disponible, trois derniers bulletins de paie, contrat de travail/lettre d'embauche (formulaire C/Ass – Unilav),",
    },
    'e': {
        'it':"Infine, eccoti qualche informazione aggiuntiva:",
        'en':"Finally, here's some additional information:",
        'ar':"أخيرًا ، إليك بعض المعلومات الإضافية:",
        'es':"Por último, aquí tienes algunas informaciones más:",
        'zh':"最后，更多信息在这里:",
        'fr':"Enfin, voici quelques informations supplémentaires:",
    },
    'f': {
        'it':"Puoi richiedere aiuto presso:",
        'en':"You can get help from:",
        'ar':"يمكنك طلب المساعدة لدى:",
        'es':"Puedes solicitar ayuda en:",
        'zh':"在这里可以寻求帮助：",
        'fr':"Vous pouvez demander de l'aide auprès de:",
    },
    'g': {
        'it':"Puoi richiedere lo stato di famiglia uso immigrazione presso:",
        'en':"You can apply for family status certificate (‘certificazione di stato di famiglia’) for immigration use at:",
        'ar':"يمكنك طلب شهادة الحالة العائلية لدى:",
        'es':"Puede solicitar el estado de familia ‘uso immigrazione’ en:",
        'zh':"移民用途的家庭状况证明可在这里申请：",
        'fr':"Vous pouvez faire votre demande de certificat de composition de famille pour usage relevant des services d'immigration auprès de:",
    },
    'h': {
        'it':"Il municipio di riferimento per la richiesta dell'attestazione dell'Idoneità abitativa e igienico-sanitaria per il ricongiungimento familiare è:",
        'en':"The Town Hall for the request for certification of housing and sanitary suitability for family reunification is:",
        'ar':"البلدية المرجع لطلب الحصول على شهادة صلاحية السكنى والصرف الصحي من أجل لم شمل العائلة هي:",
        'es':"El municipio de referencia para la solicitud del certificado de Idoneidad del alojamiento e higiénico-sanitaria para la reagrupación familiar es:",
        'zh':"可申请用于家庭团聚的住房合格证明和卫生健康证明的地方政府大楼为：",
        'fr':"La mairie de référence pour la demande d'attestation de logement conforme aux conditions hygiéniques et sanitaires requises aux fins de regroupement familial est:",
    },
    'i': {
        'it':"Una marca da bollo da €. 16,00. La domanda telematica è soggetta al pagamento della marca da bollo di €.16,00.I numeri del codice a barre riportato sulla marca da bollo dovranno essere inseriti nella domanda on line. La marca da bollo dovrà essere conservata perché andrà consegnata al SUI della Prefettura quando verrai convocato per l’appuntamento .",
        'en':"A € 16.00 tax revenue stamp. The online application is subject to payment of a revenue stamp (‘marca da bollo’) of € 16.00. The barcode number on the revenue stamp must be entered in the online application. The stamp must be kept because it has to be delivered to the SUI (Immigration Office) of the Prefecture when you come for your appointment.",
        'ar':"طابع  16.00 €  الطلب الإلكتروني يخضع الى تطبيق الدفع لمبلغ ضريبة الطابع بقيمة  16.00 € ، ويجب إدخال رقم الرمز الشريطي (codice a barre) الموجود على الطابع في الطلب عبر الإنترنت. يجب أن يتم الاحتفاظ بالطابع  ليتم تسليمه إلى SUI (مكتب الهجرة الموحد)  في المحافظة حين استدعاؤك للموعد.",
        'es':"Un timbre fiscal de 16,00 €. La solicitud telemática está sujeta al pago del timbre fiscal de 16,00 €. En la solicitud online deberán introducirse los números del código de barras que aparece en el timbre fiscal. Deberás conservar el timbre fiscal porque hay que entregarlo al SUI de la Delegación de Gobierno cuando te den cita.",
        'zh':"€. 16,00的邮票。电子申请必须支付€. 16,00的邮票。邮票上条形码号必须输入到在线申请中。必须保存邮票，因为在预约日期到达时必须将其交给省督府的唯一移民办公室。",
        'fr':"Un timbre fiscal de 16,00 euros. La demande par voie télématique est soumise au paiement d’un timbre fiscal d’un montant de 16,00 euros. Les numéros de code-barres présents sur le timbre fiscal susmentionné devront être inclus dans la demande en ligne. Le timbre fiscal devra impérativement être conservé parce que celui-ci sera transmis au siège du SUI (Sportello Unico per l’Immigrazione) ou «Guichet unique pour l’immigration» de la préfecture dont vous dépendez lorsque vous serez convoqué(e) pour le rendez-vous.",
    }


}

def produci_guida(request):
        ### INFO GENERICHE
        guida = {}
        lingua = request.session.get('lingua')

        guida['a'] = "<h1><u>" + translations['a'][lingua] + "</u></h1>"



        guida['b'] = "<h2><u>" + translations['b'][lingua] + "</u></h2>"

        guida['b1'] = "<li>" + translations['b1'][lingua] + "</li>"

        ##Per ogni parente presente
        #if ('lista_familiari' in request.session):
        #    lista_familiari = request.session.get('lista_familiari')
        #    familiari_temp = [item[0] for item in lista_familiari]
        #    parente = ""
        #    if ('partner_mag' in familiari_temp):
        #        parente = parente+" partner"
        #    if ('figli_min_ug_14' or 'figli_15_17' or 'figli_magg' in familiari_temp):
        #        parente = parente+" figlio"
        #    if ('genitori' in familiari_temp):
        #        parente = parente+" genitore"
        #        ##Se ci sono genitori_mag_ug_65
        #        guida['b7'] = "<li>" + translations['b7'][lingua] + "/li>"

        #    guida['b5'] = "<li>Fotocopie delle pagine con dati anagrafici e numero di Passaporto per "+ parente + "</li>"

        ##Per ogni coinquilino
        if ('n_tot_coinquilini' in request.session):
            if (str(request.session.get('n_tot_coinquilini'))=="None"):
                request.session['n_tot_coinquilini'] = 0
                guida['c'] = "<h2><u>" + translations['c'][lingua] + "</u></h2>"
            guida['c2'] = translations['c2'][lingua]

        #Se contratto di locazione
        if (('contratto_locazione_registrato' in request.session) or ('atto_compravendita' in request.session) or (request.session.get('posso_ospitare_in_alloggio')=='ospite')):
            guida['c1'] = translations['c1'][lingua]

        guida['d'] = "<h2><u>"+translations['d'][lingua]+"</u></h2>"

        #Se lavoratore dipendente
        if (str(request.session.get('tipologia_lavoro'))=="dipendente"):
            guida['d1'] = translations['d1_a'][lingua]

        #Se lavoratore domestico
        if (str(request.session.get('tipologia_lavoro'))=="domestico"):
            guida['d1'] = translations['d1_b'][lingua]

        #Se lavoratore titolare di ditta individuale
        if (str(request.session.get('tipologia_lavoro'))=="titolare_ditta"):
            guida['d1'] = translations['d1_c'][lingua]

        #Se lavoratore con partecipazione in società
        if (str(request.session.get('tipologia_lavoro'))=="partecipazione_società"):
            guida['d1'] = translations['d1_c'][lingua]

        #Se socio lavoratore
        if (str(request.session.get('tipologia_lavoro'))=="socio_lavoratore"):
            guida['d1'] = translations['d1_d'][lingua]

        #Se libero professionista
        if (str(request.session.get('tipologia_lavoro'))=="libero_professionista"):
            guida['d1'] = translations['d1_d'][lingua]


        if ('indirizzo_alloggio' in request.session):
            guida['e'] = "<h2><u>"+translations['e'][lingua]+"</u></h2>"
            guida['f'] = translations['f'][lingua]+ "<br>"+str(geo_db_locator.sindacati_e_patronati(request.session.get('indirizzo_alloggio')))
            guida['g'] = translations['g'][lingua]+ "<br>"+str(geo_db_locator.anagrafe_milano_piu_vicina(request.session.get('indirizzo_alloggio')))
            guida['h'] = translations['h'][lingua]+ "<br>"+str(geo_db_locator.idoneita_abitativa_vicina_milano(request.session.get('indirizzo_alloggio')))
            guida['i'] = translations['i'][lingua]


        return guida
