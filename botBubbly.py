import telebot

bot = telebot.TeleBot(
    "1687764133:AAGPkKf9QjiEoNlRIRmwwTt-JDohsUIa6BY", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Selamat datang di Bubblymask bot\nPilihan Menu~\n1. /List_product\n2. /Manfaat_product\n3. /Order")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if (message.text == '/List_product'):
        photo = open('masker.jpeg', 'rb')
        chat_id = message.chat.id
        bot.send_photo(chat_id, photo)
        product = 'List produk Bubblymask\n1. Masker Greentea\n2. Masker Strawberry\n3. Masker Coklat\n4. Masker Susu\nCek /Manfaat_product'
        bot.send_message(chat_id, product)
    elif(message.text == '/Manfaat_product'):
        chat_id = message.chat.id
        manfaat = "Manfaat :\n Greentea\n - mencerahkan mata panda\n - memberikan kelembapan wajah\n - mengatasi peradangan pada jerawat\n - mengembalikan tekstur kulit wajah\n - mengatasi kulit yang terbakar\n -mengatasi bruntusan\n\nMILK \n -mencerahkan\n -melembutkan\n -memutihkan lebih cepat-melindungi kulit dari paparan sinar matahari\n -membuat glowing\n\n Coklat \n - sebagai detoksifikasi\n - menghidrasi kulit wajah\n - menutrisi kulit wajah dengan maksimal\n - mencerahkan kulit\n - mengatasi jerawat\n - membersihkan pori pori wajah\n - melembabkan\n\nStrawberry\n-mencerahkan kulit\n -mengangkat sel kulit mati\n -melembabkan\n -mengontrol minyak di wajah\n -cegah penuaan dini\n -mempunyai Vitamin C yg bagus untuk kulit\n -mencegah kulit kusam akibat sinar matahari\n\nTertarik ? klik /Order :)"
        bot.send_message(chat_id, manfaat)
    elif(message.text == '/Order'):
        chat_id = message.chat.id
        url = 'https://api.whatsapp.com/send?phone=62895384273590&text=assalamualaikum%20saya%20mau%20beli%20masker.%20Apa%20masih%20tersedia?'
        bot.send_message(
            chat_id, 'klik url ini dan Anda akan kami arahkan ke Admin :) ' + url)


bot.polling()
