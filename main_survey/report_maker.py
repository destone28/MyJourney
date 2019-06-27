
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
    'b5': {
        'it':"Fotocopia delle pagine del passaporto relative al numero del documento e alle generalità anagrafiche ",
        'en':"Photocopy of the pages of the passport with the document number and personal data ",
        'ar':"صورة عن صفحات جواز السفر التي تشمل رقم جواز السفر و البيانات الشخصية ",
        'es':"Para los datos personales de tus familiares deberás aportar la siguiente documentación: fotocopia de las páginas del pasaporte referentes al número de documento y a los datos personales ",
        'zh':"填有证件号和个人信息的护照页面的复印件 ",
        'fr':"Photocopie des pages du passeport sur lesquelles figurent le numéro du document et autres détails pertinents ",
    },
    'b6': {
        'it': "Certificato dello stato di famiglia delle persone che abitano nel tuo alloggio, rilasciato dal loro Comune di residenza con la dicitura 'uso immigrazione'",
        'en': "Family status certificate (‘certificato di stato famiglia’) issued by your municipality of residence for those people living with you where is clearly marked for 'immigration use' ('uso immigrazione').",
        'ar': "إخراج قيد عائلي  (‘certificato di stato famiglia’) صادر عن البلدية لمكان الإقامة تحت عبارة ' استخدامات متعلق بالهجرة (uso immigrazione)",
        'es': "Certificado de estado de familia expedido por el municipio de residencia con la frase 'uso inmigración'",
        'zh': "户口所在的市政府开的填有“移民用途”字样的家庭状况证明",
        'fr': "photocopie des pages du passeport sur lesquelles figurent le numéro du document et autres détails pertinents",
    },
    'b7': {
        'it': 'Dichiarazione di impegno a sottoscrivere una polizza assicurativa sanitaria o altro titolo idoneo a garantire la copertura di tutti i rischi nel territorio nazionale, in favore dei genitori ultrasessantacinquenni.',
        'en': 'Declaration of commitment to take out a health insurance policy, or other appropriate cover, for parents over sixty-five years of age to ensure coverage of all risks while in Italy',
        'ar': 'تصريح الالتزام بالتأمين من خلال التوقيع على بوليصة التأمين الصحي أو أي سند مناسب آخر لضمان تغطية جميع المخاطر على الأراضي الوطنية ، لصالح الوالدين البالغون اكثر من خمسة وستين عاماً.',
        'es': 'Declaración de compromiso de suscripción de una póliza de seguro sanitaria o de otro título que sirva para garantizar la cobertura de todos los riesgos en el territorio nacional, a favor de los padres de más de 75 años',
        'zh': '为自己超过六十五岁的双亲签下健康保险或其他在国家境内可覆盖所有风险的保险的承诺声明。',
        'fr': "Déclaration d'engagement à souscrire à une police d'assurance couvrant les soins de santé ou toute autre document valable en mesure de garantir la couverture de tous les risques sur le territoire national, pour les parents âgés de plus de 65 ans et plus.",
    },
    'c0': {
        'it': 'Casa',
        'en': 'House',
        'ar': 'منزل',
        'es': 'Casa',
        'zh': '房子',
        'fr': 'Maison'
    },
    'c': {
        'it': "Le informazioni e la documentazione da procurarti per l'alloggio sono le seguenti:",
        'en': 'The information and documentation you need to present regarding your accommodation is as follows:',
        'ar': "المعلومات والمستندات المتعلقة بالسكن الواجب تقديمها هي كالتالي:",
        'es': 'Las informaciones y documentación que necesitas para el alojamiento son las siguientes:',
        'zh': "居所所需要的信息和证件为以下：",
        'fr': "Les informations et la documentation à obtenir pour l'hébergement sont les suivantes:",
    },
    'c2_1': {
        'it': "Ricevuta di registrazione e/o rinnovo del contratto di locazione",
        'en': "Receipt of registration and/or renewal of the rental contract",
        'ar': "إيصال تسجيل و/ أو تجديد عقد الإيجار.",
        'es': "Original del contrato de alquiler",
        'zh': "租赁合同的登记和/或更新凭据",
        'fr': "Accusé de réception de l’enregistrement et/ou du renouvellement du bail",
    },
    'locazione': {
        'it': "locazione registrato",
        'en': "rental registered",
        'ar': "إيجار مسجل",
        'es': "recibo de registro y/o renovación contrato de alquiler",
        'zh': "租赁登记",
        'fr': "bail",
    },
    'compravendita': {
        'it': "compravendita",
        'en': "purchase",
        'ar': "شراء",
        'es': "compraventa",
        'zh': "购买",
        'fr': "commerce",
    },
    'comodato': {
        'it': "comodato",
        'en': "free use agreement",
        'ar': " اتفاقية الاستخدام الحر.",
        'es': "acuerdo de uso libre",
        'zh': "无偿租赁合同",
        'fr': "prêt à usage",
    },
    'c2_2': {
        'it': "Dichiarazione redatta dal titolare/i dell’appartamento su mod. “S2”, attestante il consenso ad ospitare anche i ricongiunti",
        'en': "Declaration drawn up by the owner(s) of the apartment on form “S2“, giving their consent to host the family members,",
        'ar': "تصريح من مالك الشقة وفقا للنموذج 'S2' ، مصرحا بالموافقة على إمكانية استضافة أفراد العائلة المعنيين بلم الشمل.",
        'es': "Declaración redactada por el/los titular/es de la vivienda en el modelo “S2”, que certifica el consentimiento para alojar también a las personas reagrupadas",
        'zh': "公寓持有人按照“S2”表格填的声明，证明也同意接纳团聚的家人",
        'fr': "Déclaration rédigée par le(s) propriétaire(s) du logement conformément au modèle « S2 », attestant le consentement à également accueillir les membres de la famille qui font l'objet d'un regroupement",
    },
    'c2_3': {
        'it': "Contratto di acquisto per l'alloggio, di durata non inferiore a sei mesi a decorrere dalla data di presentazione della domanda",
        'en': "Contract for your appartment/house with a duration longer than 6 months from the date of Family Reunion request",
        'ar': "عقد الإيجار للشقة أو المنزل لفترة لا تتخطى الستة أشهر ابتداءا من تاريخ طلب لم شمل الأسرة.",
        'es': "Contrato del apartamento / casa con una duración superior a 6 meses a partir de la fecha de la solicitud de reagrupación familiar",
        'zh': "自家庭请求之日起6个月以上的公寓/房屋合同",
        'fr': "Contrat de logement d'une durée minimale de six mois à compter de la date de dépôt de la demande",
    },
    'c3': {
        'it': "Certificato di idoneità abitativa e igienico-sanitaria, rilasciata dal Comune di Milano per finalità di ricongiungimento familiare",
        'en': "Certificate of suitability for housing and sanitation issued by the Municipality for family reunification purposes",
        'ar': "شهادة أهلية السكن وشروط الصحة العامة الصادرة عن البلدية بغية لم شمل الأسرة.",
        'es': "Certificado de idoneidad de alojamiento e higiénico-sanitaria expedido por el Municipio a los efectos de reagrupación familiar",
        'zh': "由市政府为了家庭团聚而开的住房合格证明和卫生-健康证明",
        'fr': "Certificat de disponibilité de logement conforme aux conditions hygiéniques et sanitaires requises délivré par la municipalité aux fins du regroupement familial",
    },
    'd0': {
        'it': "Lavoro",
        'en': "Job",
        'ar': "وظيفة",
        'es': "Trabajo",
        'zh': "工作",
        'fr': "Emploi",
    },
    'd': {
        'it': "Per certificare le informazioni sul lavoro dovrai invece fornire i seguenti documenti:",
        'en': "To prove your job conditions you will be asked to supply the following documents:",
        'ar': "لإثبات ظروف عملك ، سيُطلب منك تقديم المستندات التالية:",
        'es': "Para demostrar las condiciones de su trabajo, se le pedirá que proporcione los siguientes documentos:",
        'zh': "劳工证明：",
        'fr': "Pour certifier les informations sur le travail, vous devez fournir les documents suivants:",
    },
    'cud': {
        'it': "Certificazione Unica (C.U. ex C.U.D)",
        'en': "Unified Salary Certificate (called C.U. formerly called C.U.D.)",
        'ar': "شهادة التصريح بالدخل (CU ex CUD).",
        'es': "Certificación Única (C.U. antiguo C.U.D.) y su correspondiente recibo de presentación",
        'zh': "年收入总结证明（C.U.前C.U.D.）和呈交凭据",
        'fr': "Certification unique (C.U., p. ex., C.U.D.) et accusé de réception connexe",
    },
    'unilav': {
        'it': "Fotocopia del contratto di lavoro/lettera di assunzione (modulo C/Ass - Unilav)",
        'en': "Photocopy of the employment contract/letter of employment (form C/Ass - Unilav)",
        'ar': "نسخة عن عقد العمل/رسالة التوظيف (نموذج C/Ass - Unilav).",
        'es': "contrato de trabajo/carta de contratación (formulario C/Ass – Unilav)",
        'zh': "劳工合同/雇用信（C/Ass – Unilav表格）的复印件",
        'fr': "contrat de travail/lettre d'embauche (formulaire C/Ass – Unilav)",
    },
    'paga': {
        'it': "Ultime tre buste paga",
        'en': "latest three pay slips",
        'ar': "آخر ثلاث قسائم دفع الراتب.",
        'es': "las tres últimas minutas",
        'zh': "最后三个月的月薪单",
        'fr': "trois derniers bulletins de paie",
    },
    'autocertificazione': {
        'it': "Autocertificazione del datore di lavoro, redatta su modello 'S3' con data non anteriore ad un mese, da cui risulti l'attualità del rapporto di lavoro e la retribuzione mensile corrisposta",
        'en': "self-certification from your employer on form 'S3' not more than 1 month old, with details of the employment contract and the monthly salary paid",
        'ar': "التصريح بالدفع من طرف رب العمل معطاه عن  طريق النموذج 'S3' لتاريخ لا يتجاوز الشهر الواحد مع تفاصيل عقد العمل والراتب الشهري المدفوع.",
        'es': "certificación del empleador, redactada en el formulario “S3” con fecha no anterior a 1 mes, donde resulte que la relación laboral está en vigor y el sueldo mensual pagado",
        'zh': "雇主根据“S3”表格填写的自我声明，日期在前一个月内，由此证明现行的雇佣关系，和支付的月薪",
        'fr': "auto-certification de l'employeur rédigée sur le modèle « S3 » avec une date non antérieure à un (1) mois certifiant la pertinence du contrat de travail et la rémunération mensuelle correspondante",
    },
    'fcdatlav': {
        'it': "Fotocopia del documento d'identità del datore di lavoro, debitamente firmata dal medesimo",
        'en': "Photocopy of the identity document of the employer, signed by him/her.",
        'ar': "صورة عن وثيقة هوية رب العمل موقعة  من طرفه",
        'es': "fotocopia del documento de identidad del empleador, debidamente firmado por el mismo",
        'zh': "雇主身份证复印件，由他自己签字",
        'fr': "photocopie du document d'identité de l'employeur dûment signée par ce dernier.",
    },
    'redditi': {
        'it': "Ultima dichiarazione dei redditi, ove posseduta",
        'en': "Latest tax form 730/UNICO if afflicable",
        'ar': "(آخر تصريح للدخل (730/Unico) في حال توفره",
        'es': "Último formulario de impuestos 730 / UNICO si corresponde",
        'zh': "最后一次的纳税申报表，如果有的话，以及相关的呈交凭据，730/自然人收入申报表格",
        'fr': "dernière déclaration d'impôt lorsque celle-ci est disponible et accusé de réception connexe",
    },
    'assinps': {
        'it': "Comunicazione di assunzione al Centro per l’Impiego o all’INPS",
        'en': "Copy of notification of employment given to the Employment Centre or to INPS",
        'ar': "نسخة من الإشعار بالتوظيف المقدم إلى مركز التوظيف أو إلى INPS ",
        'es': "Copia de la comunicación de contratación al Centro de Empleo o al INPS",
        'zh': "寄给就业中心和国家社会保障机构的雇用通知",
        'fr': "avis de prise de fonctions émise par le Centre pour l'emploi (« Centro per l'impiego » ou « INPS »)",
    },
    'bollettino': {
        'it': "Ultimo bollettino di versamento dei contributi INPS, con attestazione dell’avvenuto pagamento",
        'en': "Latest INPS contributions payment slip, with proof of payment",
        'ar': "آخر قسيمة للدفع في اشتراكات اﻠ INPS ، مع إثبات إجراء الدفع",
        'es': "último boletín de pago de cotizaciones INPS, con certificado de pago",
        'zh': "最近一次社会保险税的发票，证明已交付",
        'fr': "derniers ordres de virement des cotisations de l’INPS accompagnés de l’attestation du paiement",
    },
    'vcc': {
        'it': "Visura camerale/certificato di iscrizione alla Camera di Commercio recente",
        'en': "business profile (‘visura camerale’)/recent certificate of Chamber of Commerce enrolment",
        'ar': "نبذة عن الأعمال ('visura camerale') / شهادة حديثة لتسجيل غرفة التجارة",
        'es': "perfil comercial (‘visura camerale’) / certificado reciente de inscripción en la Cámara de Comercio",
        'zh': "商会注册/最近的在商会的注册证明",
        'fr': "certificat récent établi par la chambre de commerce pertinente",
    },
    'piva': {
        'it': "Certificato di attribuzione P. IVA",
        'en': "VAT number certificate",
        'ar': "شهادة رقم ضريبة القيمة المضافة P.IVA",
        'es': "certificado de atribución de N° de IVA",
        'zh': "增值税号分配证明",
        'fr': "certificat d'attribution de la P. IVA (TVA)",
    },
    'liccom': {
        'it': "Licenza comunale, ove prevista",
        'en': "if applicable municipal license",
        'ar': "رخصة البلدية ، إن كانت مطلوبة",
        'es': "licencia municipal, si estuviera prevista",
        'zh': "市政府许可证",
        'fr': "permis municipal, s'il y a lieu",
    },
    'att1': {
        'it': "Se l’attività è stata avviata da più di 1 anno, dichiarazione dei redditi (modello UNICO) con allegata ricevuta di presentazione telematica e bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visura camerale aggiornata inerente l’attività svolta",
        'en': "If the business was started more than 1 year ago, income tax return (UNICO form) with receipt of electronic presentation attached and accounts for the current year, which must be stamped and signed by a professional accountant with copy of his/her identity document attached, the membership card of the professional body or the updated chamber of commerce business profile (‘visura camerale’) with details of the business.",
        'ar': "إذا كان النشاط التجاري قد بدأ منذ أكثر من سنة ، أو التصريح بالدخل الضريبي (نموذج UNICO) مرفق به إيصال التقديم الإلكتروني والميزانية العمومية المتعلقة بالسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة ، فيما يتعلق بالنشاط التجاري",
        'es': "si la actividad ha iniciado hace más de 1 año, declaración de la renta (modelo UNICO) adjuntando recibo de presentación telemática y balance relativo al año en curso, que deberá estar sellado y firmado por el profesional con anexa fotocopia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado inherente a la actividad realizada",
        'zh': "如果业务开始了超过1年，当下年份的纳税申报表（收入申报表格），并附上电子呈交凭据和收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于其进行的工作的商会注册更新",
        'fr': "si l'activité est déjà démarrée depuis plus d'un (1) an, déclaration de revenus (modèle UNIQUE) avec l’accusé de réception annexé du dépôt électronique et des états financiers prévus pour l'année en cours",
    },
    'att0': {
        'it': "Se l’attività è stata avviata da meno di 1 anno, bilancino, relativo all’anno in corso, che dovrà essere timbrato e sottoscritto dal professionista con allegata copia del documento di identità dello stesso, del tesserino d’iscrizione all’ordine o della visuracamerale aggiornata inerente l’attività svolta",
        'en': "If the activity has been started for less than 1 year, accounts for the current year, which must be stamped and signed by the professional with a copy of his/her identity document, membership card of the professional body or updated chamber of commerce business profile (‘visure camerale’) with details of the business.",
        'ar': "إن كان النشاط قد بدأ منذ أقل من سنة واحدة ، الميزانية العمومية المتعلقة بالسنة الجارية ، والتي يجب ختمها وتوقيعها من قبل المختص مع صورة مرفقة من وثيقة الهوية الخاصة به وبطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة للشركة حديثة فيما يتعلق بالنشاط التجاري المنجز ",
        'es': "si la actividad se ha iniciado hace menos de 1 año, balance referente al año en curso, que deberá estar sellado y firmado por el profesional con anexa fotocopia de su documento de identidad, de la tarjeta de colegiación o del certificado del Registro Mercantil actualizado inherente a la actividad realizada",
        'zh': "如果业务开始了的时间少于1年，当下年份的收支平衡表，必须由专业人士签字盖章，并附上专业人士的身份证副本，在专业协会的注册牌，或者关于进行的工作的商会注册更新",
        'fr': "si l'activité est déjà démarrée depuis moins d'un (1), les états financiers prévus pour l'année en cours, qui devront être estampés et signés par le professionnel avec la copie accompagnant le document d'identité de ce dernier, la carte d’identification attestant de l’accréditation à l’Ordre ou la certification établie par la chambre mise à jour sur la base de l'activité effectuée",
    },
    'fatture': {
        'it': "Tutte le fatture relative all’anno in corso",
        'en': "all invoices (purchase and sale) for the current year",
        'ar': "جميع الفواتير (شراء و بيع) المتعلقة بالسنة الجارية ",
        'es': "balance referente al año en curso",
        'zh': "关于当下年份的所有的发票（购买和销售）",
        'fr': "toutes les factures (achat et vente) relatives à l'année en cours",
    },
    'vcs': {
        'it': "Visura camerale della società, di data recente",
        'en': "Company profile supplied by the Chamber of Commerce or recent certificate of Chamber of Commerce enrolment of the company",
        'ar': "نبذة عن الشركة مقدمة من غرفة التجارة أو شهادة حديثة لتسجيل غرفة التجارة للشركة",
        'es': "Perfil de la empresa proporcionado por la Cámara de Comercio o certificado reciente de inscripción en la Cámara de Comercio de la empresa (Registro Mercantil)",
        'zh': "税务合规证明书或者F24表格副本",
        'fr': "Certification de la chambre de commerce, de date récente",
    },
    'vccoop': {
        'it': "Visura camerale della cooperativa",
        'en': "Business profile (‘visura camerale’) of the cooperative supplied by the chamber of commerce",
        'ar': "نبذة عن الأعمال التجارية ('visura camerale') للتعاونية التي توفرها غرفة التجارة",
        'es': "Perfil de la empresa («visura camerale») de la cooperativa emitido por la Cámara de Comercio",
        'zh': "合作社的商会注册",
        'fr': "Certification de la chambre de commerce de la coopérative",
    },
    'prescoop': {
        'it': "Dichiarazione del presidente della cooperativa da cui risulti l’attualità del rapporto di lavoro",
        'en': "Declaration of the president of the cooperative detailing the employment relationship",
        'ar': "تصريح رئيس الشركة التعاونية والتي يبين من خلالها الوضع الحالي للعمال",
        'es': "declaración del presidente de la cooperativa en la que resulte que la relación laboral está en vigor",
        'zh': "合作社主席按照“S3”表格填写的声明",
        'fr': "déclaration du président de la coopérative certifiant la pertinence du contrat de travail et la rémunération mensuelle correspondante",
    },
    'albo': {
        'it': "Iscrizione all’albo del libero professionista",
        'en': "Copy of the registration with a professional body",
        'ar': "بطاقة التسجيل في النقابة أو شهادة غرفة التجارة/شهادة التسجيل في غرفة التجارة",
        'es': "Copia de la tarjeta de colegiación",
        'zh': "在专业协会的注册牌",
        'fr': "inscription à l’Ordre des professions libérales",
    },
    'fine': {
        'it': "Infine, eccoti qualche informazione aggiuntiva:",
        'en': "Please, find here additional info:",
        'ar': "من فضلك ، هنا تجد معلومات إضافية:",
        'es': "Por favor, encuentre aquí información adicional:",
        'zh': "请在此处查找其他信息：",
        'fr': "Veuillez trouver ici des informations supplémentaires:",
    },
    'f': {
        'it': "Puoi richiedere aiuto presso:",
        'en': "You can ask for help at:",
        'ar': "يمكنك طلب المساعدة على:",
        'es': "Puedes pedir ayuda en:",
        'zh': "您可以通过以下方式寻求帮助：",
        'fr': "Vous pouvez demander de l'aide à:",
    },
    'g': {
        'it': "Il riferimento per i servizi anagrafici è",
        'en': "The reference for 'servizi anagrafici' is:",
        'ar': "المرجع ل 'anagrafici SERVIZI' هو:",
        'es': "La referencia para 'servizi anagrafici' es:",
        'zh': "“服务名称”的参考是：",
        'fr': "La référence pour 'servizi anagrafici' est:",
    },
    'h': {
        'it': "Per l'idoneità abitativa della tua casa:",
        'en': "For the 'suitability for housing' certificate of your appartment:",
        'ar': 'للحصول على شهادة "ملاءمة السكن" لشقتك:',
        'es': "Para el certificado de 'idoneidad para la vivienda' de su vivienda:",
        'zh': "关于贵公司设备的“住房适用性”证书：",
        'fr': "Pour le certificat 'd''aptitude au logement' de votre appartement:",
    },
    'i': {
        'it': "Ti occorrerà una marca da bollo per te, più una marca da bollo per ogni familiare che vuoi ricongiungere. Ogni marca da bollo ha il costo di 16€.",
        'en': "You will need to bring with you the €16,00 tax revenue stamp that you used for the online application and a €16,00 tax revenue stamp for each family member for whom you have requested a clearance certificate (‘nulla osta’).",
        'ar': "يجب إحضار طابع من فئة 16.00 € الذي قمت بإستخدامه في تعبئة الطلب عبر الإنترنت ، وكذلك طابع من فئة 16.00 € عن كل فرد من أفراد الأسرة بحسب طلبك الى عدم الممانعة له (nulla osta) ",
        'es': "Deberá llevar consigo el timbre fiscal de 16,00 € que utilizó para la solicitud en línea y un timbre fiscal de 16,00 € para cada miembro de la familia para el que haya solicitado la autorización ('nulla osta')",
        'zh': "يجب إحضار طابع من فئة 16.00 € الذي قمت بإستخدامه في تعبئة الطلب عبر الإنترنت ، وكذلك طابع من فئة 16.00 € عن كل فرد من أفراد الأسرة بحسب طلبك الى عدم الممانعة له (nulla osta)",
        'fr': "vous devrez également apporter avec vous le timbre fiscal de 16,00 euros que vous avez utilisé pour cette demande en ligne, et un timbre fiscal de 16,00 euros pour chaque membre de la famille pour lequel vous avez effectué une demande d'autorisation",
    },
    'partner': {
        'it': "partner",
        'en': "partner",
        'ar': "الشريك",
        'es': "compañera/o",
        'zh': "配偶",
        'fr': "partner",
    },
    'figlio': {
        'it': "figlio",
        'en': "son/daughter",
        'ar': "الابن/الابنة",
        'es': "hija/o",
        'zh': "儿子/女儿",
        'fr': "fils",
    },
    'genitore': {
        'it': "genitore",
        'en': "parent",
        'ar': "الأبوين ",
        'es': "madre/padre",
        'zh': "父母",
        'fr': "parent",
    }
}

def produci_guida(request):
    ### INFO GENERICHE
    guida = {}
    lingua = request.session.get('lingua')

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
        temp_string_da_accodare = ""
        if ('partner_mag' in familiari_temp):
            parente = translations['partner'][lingua]
            temp_string_da_accodare = temp_string_da_accodare + "<li>" + translations['b5'][lingua] + "(" + parente + ") </li>"
        if ('figli_min_ug_14' or 'figli_15_17' or 'figli_magg' in familiari_temp):
            parente = translations['figlio'][lingua]
            temp_string_da_accodare = temp_string_da_accodare + "<li>" + translations['b5'][lingua] + "(" + parente + ") </li>"
        if ('genitori' in familiari_temp):
            parente = translations['genitore'][lingua]
            temp_string_da_accodare = temp_string_da_accodare + "<li>" + translations['b5'][lingua] + "(" + parente + ") </li>"
            ##Se ci sono genitori_mag_ug_65
            guida['b7'] = "<li>" + translations['b7'][lingua] + "</li>"

        guida['b5'] = temp_string_da_accodare

    ##Per ogni coinquilino
    if ('n_tot_coinquilini' in request.session):
        if (str(request.session.get('n_tot_coinquilini'))=="None"):
            request.session['n_tot_coinquilini'] = 0
        if (int(request.session.get('n_tot_coinquilini'))!=0):
            guida['b6'] = "<li>" + translations['b6'][lingua] + "</li>"

    guida['c0'] = "<h2><u>" + translations['c0'][lingua] + "</u></h2>"
    
    if (str(request.session.get('tipologia_permesso'))=="altro"):
        guida['c'] = translations['c'][lingua]
        
        #Se contratto di locazione
        if (('contratto_locazione_registrato' in request.session) or ('atto_compravendita' in request.session) or (request.session.get('posso_ospitare_in_alloggio')=='ospite')):
            if (str(request.session.get('contratto_locazione_registrato'))=="si"):
                alloggio = translations['locazione'][lingua]
                guida['c2_1'] = "<li>" + translations['c2_1'][lingua] + "</li>"
            #Se proprietario
            if (str(request.session.get("atto_compravendita"))=="si"):#CONTROLLARE
                alloggio = translations['compravendita'][lingua]
                if (str(request.session.get("posso_ospitare_in_alloggio"))=="ospite"):
                    alloggio = alloggio+ translations['comodato'][lingua]
                    guida['c2_2'] = "<li>" + translations['c2_2'][lingua] + "</li>"
                    guida['c2_3'] = "<li>" + translations['c2_3'][lingua] + "</li>"
    
        guida['c3'] = "<li>" + translations['c3'][lingua] + "</li>"

    guida['d0'] = "<h2><u>" + translations['d0'][lingua]  + " </u></h2>"
    guida['d'] = translations['d'][lingua]

    guida['d1'] = "<li>" + translations['cud'][lingua] + "</li>"


    #Se lavoratore dipendente
    if (str(request.session.get('tipologia_lavoro'))=="dipendente"):
        guida['d1'] = "<li>" + translations['cud'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['unilav'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['paga'][lingua] + "</li>"
        guida['d3_2'] = "<li>" + translations['autocertificazione'][lingua] + "</li>"
        guida['d3_3'] = "<li>" + translations['fcdatlav'][lingua] + "</li>"

    #Se lavoratore domestico
    if (str(request.session.get('tipologia_lavoro'))=="domestico"):
        guida['d1'] = "<li>" + translations['redditi'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['assinps'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['bollettino'][lingua] + "</li>"
        guida['d3_2'] = "<li>" + translations['autocertificazione'][lingua] + "</li>"
        guida['d3_3'] = "<li>" + translations['fcdatlav'][lingua] + "</li>"

    #Se lavoratore titolare di ditta individuale
    if (str(request.session.get('tipologia_lavoro'))=="titolare_ditta"):
        guida['d1'] = "<li>" + translations['vcc'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['piva'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['liccom'][lingua] + "</li>"
        guida['d3_2'] = "<li>" + translations['att1'][lingua] + "</li>"
        guida['d3_3'] = "<li>" + translations['att0'][lingua] + "</li>"
        guida['d3_4'] = "<li>" + translations['fatture'][lingua] + "</li>"

    #Se lavoratore con partecipazione in società
    if (str(request.session.get('tipologia_lavoro'))=="partecipazione_società"):
        guida['d1'] = "<li>" + translations['vcs'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['piva'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['att1'][lingua] + "</li>"
        guida['d3_2'] = "<li>" + translations['att0'][lingua] + "</li>"

    #Se socio lavoratore
    if (str(request.session.get('tipologia_lavoro'))=="socio_lavoratore"):
        guida['d1'] = "<li>" + translations['vccoop'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['piva'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['prescoop'][lingua] + "</li>"
        guida['d3_2'] = "<li>" + translations['redditi'][lingua] + "</li>"
        guida['d3_3'] = "<li>" + translations['paga'][lingua] + "</li>"
        guida['d3_4'] = "<li>" + translations['unilav'][lingua] + "</li>"

    #Se libero professionista
    if (str(request.session.get('tipologia_lavoro'))=="libero_professionista"):
        guida['d1'] = "<li>" + translations['albo'][lingua] + "</li>"
        guida['d2'] = "<li>" + translations['att1'][lingua] + "</li>"
        guida['d3_1'] = "<li>" + translations['att0'][lingua] + "</li>"


    if ('indirizzo_alloggio' in request.session):
        guida['e'] = "<h2><u>" + translations['fine'][lingua] + "</u></h2>"
        guida['f'] = translations['f'][lingua] + "<br>" + str(geo_db_locator.sindacati_e_patronati(request.session.get('indirizzo_alloggio')))
        guida['g'] = translations['g'][lingua] + "<br>" + str(geo_db_locator.anagrafe_milano_piu_vicina(request.session.get('indirizzo_alloggio')))
        guida['h'] = translations['h'][lingua] + "<br>" + str(geo_db_locator.idoneita_abitativa_vicina_milano(request.session.get('indirizzo_alloggio')))
        guida['i'] = translations['i'][lingua]


    return guida
