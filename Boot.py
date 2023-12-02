import telebot
from telebot import types
import re

# Conexion con BOT telegram
TOKEN = '6603797732:AAGtMmAy1mVUTRuZv2ayKvrXb5nQ_zQDAOw'
bot = telebot.TeleBot(TOKEN)

#Creacion de comandos simples (Saludo)
@bot.message_handler(commands=['Hola', 'Hello', 'Saludos'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! Me llamo GaBot y estaré a tu servicio')

#Creacion de comandos simples (Despedida)
@bot.message_handler(commands=['Adiós', 'Bye', 'Hasta pronto', 'adiós', 'adios', 'Adios'])
def send_welcome(message):
    bot.reply_to(message, 'Fue un gusto conversar contigo, cuídate')


# Manejador de mensajes para el comando /estado de emocion y para Genshin Impact
palabras_clave = ['fondos', 'wallpapers', 'juego', 'diferente', 'emocion', 'siento', 'genshin',
                  'jugar', 'gusta', 'mejor', 'prefieres', 'emoticon']

@bot.message_handler(func=lambda message: any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in palabras_clave))
def detect_estado(message):

    if any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in ['estoy', 'diferente', 'emocion', 'siento']):
        # Crear un markup con botones en línea (No. de botones)
        markup = types.InlineKeyboardMarkup(row_width=4)

        # Crear botones "Bien" y "Mal"
        btn_bien = types.InlineKeyboardButton('Bien', callback_data='estado_bien')
        btn_regular = types.InlineKeyboardButton('Regular', callback_data='estado_regular')
        btn_mal = types.InlineKeyboardButton('Mal', callback_data='estado_mal')
        btn_raro = types.InlineKeyboardButton('Raro', callback_data='estado_raro')

        # Agregar botones al markup
        markup.add(btn_bien, btn_regular, btn_mal, btn_raro)

        # Enviar mensaje con los botones
        bot.reply_to(message, "¿Cómo crees sentirte hoy?", reply_markup=markup)

    elif any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in ['genshin', 'impact']):
        # Crear un markup con botones en línea (No. de botones)
        markup = types.InlineKeyboardMarkup(row_width=4)

        # Crear botones
        btn_tao = types.InlineKeyboardButton('Hu Tao', callback_data='genshi_1')
        btn_furi = types.InlineKeyboardButton('Furina', callback_data='genshi_2')
        btn_yae = types.InlineKeyboardButton('Yae Miko', callback_data='genshi_3')
        btn_ayaka = types.InlineKeyboardButton('Kamisato Ayaka', callback_data='genshi_4')

        # Agregar botones al markup
        markup.add(btn_tao, btn_furi, btn_yae, btn_ayaka)

        # Enviar mensaje con los botones
        bot.reply_to(message, "Pues es un juego de mundo abierto y mis personajes favoritos son las siguientes, ¿Te interesa alguna?", reply_markup=markup)


    elif any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in ['gusta', 'mejor', 'prefieres']):
        bot.reply_to(message, "No tengo respuesta a eso ya que todas son únicas y especiales a su forma") 

    elif any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in ['jugar']):
        bot.reply_to(message, "Me encantaría, sirve de que subo de nivel") 



# Manejador de consultas de botones en línea
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id  # Obtiene el ID del chat del mensaje original    

#Estado emocional    
    if call.data == 'estado_bien':
        bot.send_message(chat_id, 'Genial! Es bueno saber que te encuentras de esa forma')
    elif call.data == 'estado_regular':
        bot.send_message(chat_id, 'Mmmmm ¿Te gustaría hacer algo divertido?')
    elif call.data == 'estado_mal':
        bot.send_message(chat_id, 'Lamento escuchar eso, ¿Qué puedo hacer para que te sientas mejor?')
    elif call.data == 'estado_raro':
        bot.send_message(chat_id, '¿Si desayunaste? ¿Te peinaste? ¿Olvidaste algo quizás?')

#Estado genshin 
    elif call.data == 'genshi_1':
        img_url = 'https://static.wikia.nocookie.net/gen-impact/images/5/5b/Carta_de_personaje_Hu_Tao.png/revision/latest?cb=20210303043002&path-prefix=es'
        bot.send_photo(chat_id=chat_id, photo=img_url, caption='Hu Tao es la 77.ᵃ directora de la Funeraria El Camino, es la encargada de todos los asuntos funerarios de Liyue')

    elif call.data == 'genshi_2':
        img_url = 'https://static.wikia.nocookie.net/gen-impact/images/8/8b/Carta_de_personaje_Furina.png/revision/latest?cb=20230925144334&path-prefix=es'
        bot.send_photo(chat_id=chat_id, photo=img_url, caption='Furina fue maldecida con la inmortalidad mientras su yo divino siguiese existiendo, teneniedo que supervisar a Fontaine como la Arconte Hydro')

    elif call.data == 'genshi_3':
        img_url = 'https://static.wikia.nocookie.net/gen-impact/images/e/ed/Carta_de_personaje_Yae_Miko.png/revision/latest?cb=20211231174549&path-prefix=es'
        bot.send_photo(chat_id=chat_id, photo=img_url, caption='La Suma Sacerdotisa del Gran Santuario Narukami y editora en jefe de la Editorial Yae. Bajo su increíble encanto esconde una inteligencia y una astucia inimaginables.')

    elif call.data == 'genshi_4':
        img_url = 'https://static.wikia.nocookie.net/gen-impact/images/8/84/Carta_de_personaje_Kamisato_Ayaka.png/revision/latest?cb=20210607112554&path-prefix=es'
        bot.send_photo(chat_id=chat_id, photo=img_url, caption='Ella es la hija menor del Clan Kamisato y hermana de Kamisato Ayato. Siendo hermosa, elegante y agraciada, la gente común no tiene nada de qué hablar mal de Kamisato Ayaka')


def callback_query(call):
    chat_id = call.message.chat.id  # Obtiene el ID del chat del mensaje original
    
    if call.data == 'genshi_1':
        bot.send_message(chat_id, 'Por el momento puedo proporcionarte estos fondos, espero te gusten')

        # Enviar imágenes (sustituye 'URL_DE_IMAGEN1', 'URL_DE_IMAGEN2', 'URL_DE_IMAGEN3' con las URLs reales de las imágenes)
        img_urls = [
            'https://p4.wallpaperbetter.com/wallpaper/329/461/165/genshin-impact-kamisato-ayaka-genshin-impact-yoimiya-genshin-impact-hd-wallpaper-preview.jpg',
            'https://p4.wallpaperbetter.com/wallpaper/485/23/591/genshin-impact-kamisato-ayaka-genshin-impact-hd-wallpaper-preview.jpg',
            'https://images8.alphacoders.com/129/1299271.jpg'
        ]

        for img_url in img_urls:
            bot.send_photo(chat_id=chat_id, photo=img_url)

# Manejador para solicitudes de fondos de pantalla
palabras_clave_fondos = ['fondo','fondos', 'wallpapers']
@bot.message_handler(func=lambda message: any(re.search(rf'\b{palabra}\b', message.text, re.IGNORECASE) for palabra in palabras_clave_fondos))
def solicitar_fondos(message):
    # Crear un markup con botones en línea (No. de botones)
    markup = types.InlineKeyboardMarkup(row_width=4)

    # Crear botones
    btn_tao = types.InlineKeyboardButton('Hu Tao', callback_data='genshi_1')
    btn_furi = types.InlineKeyboardButton('Furina', callback_data='genshi_2')
    btn_yae = types.InlineKeyboardButton('Yae Miko', callback_data='genshi_3')
    btn_ayaka = types.InlineKeyboardButton('Kamisato Ayaka', callback_data='genshi_4')

    # Agregar botones al markup
    markup.add(btn_tao, btn_furi, btn_yae, btn_ayaka)

    # Enviar mensaje con los botones
    bot.reply_to(message, "Claro, dime de quién te gustaría?", reply_markup=markup)    


if __name__ == "__main__":
    bot.polling(none_stop=True)