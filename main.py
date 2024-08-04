import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Preguntas y respuestas sobre el ITLA
    response('El ITLA está ubicado en las America Highway, Km 27, la caleta, Santo Domingo, República Dominicana.', 
             ['donde', 'ubicado', 'direccion', 'ubicacion', 'itla'], required_words=['itla'])
    
    response('El ITLA ofrece carreras técnicas en áreas como Software, Redes, Multimedia, Mecatrónica y más.', 
             ['que', 'carreras', 'ofrecen', 'oferta', 'academica', 'itla'], required_words=['carreras'])
    
    response('El ITLA es un instituto técnico superior especializado en tecnología y formación técnica profesional.', 
             ['que', 'es', 'significa', 'itla', 'instituto'], required_words=['itla'])
    
    response('Para inscribirte en el ITLA debes visitar su sitio web y seguir el proceso de admisión en línea.', 
             ['como', 'inscribirme', 'inscripcion', 'admisión', 'entrar', 'itla'], required_words=['inscribirme'])
    
    response('La duración de las carreras en el ITLA varía, pero generalmente son programas de 2 a 3 años.', 
             ['cuanto', 'dura', 'tiempo', 'duración', 'carrera', 'itla'], required_words=['carrera'])
    
    response('El ITLA es conocido por su calidad educativa en el área de la tecnología y la formación técnica.', 
             ['porque', 'destaca', 'reconocido', 'famoso', 'itla'], required_words=['itla'])
    
    response('Sí, el ITLA ofrece becas para estudiantes con excelente rendimiento académico.', 
             ['hay', 'ofrecen', 'becas', 'ayuda', 'financiamiento', 'itla'], required_words=['becas'])
    
    response('Puedes contactar al ITLA llamando al (809) 738-4852 o visitando su página web.', 
             ['como', 'contactar', 'telefono', 'contacto', 'itla'], required_words=['contactar'])
    
    response('El ITLA tiene convenios con diversas empresas para facilitar la inserción laboral de sus egresados.', 
             ['hay', 'bolsa', 'trabajo', 'insercion', 'laboral', 'itla'], required_words=['trabajo'])
    
    response('El ITLA organiza talleres, charlas y eventos tecnológicos abiertos al público en general.', 
             ['que', 'eventos', 'actividades', 'talleres', 'organiza', 'itla'], required_words=['eventos'])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir', 'Búscalo en Google a ver qué tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('Tú: ')))
