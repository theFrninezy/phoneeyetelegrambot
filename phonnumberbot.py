import telebot
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
#Token and jey
Token = "2093570371:AAF8rT9knG6IJInldfxJ9yfKbjluJOt79oI"
bot = telebot.TeleBot(Token)
key = "7e5552da788f400db1f3f51cd584933f"
#start
@bot.message_handler(commands = ['start'])
def massage_send(massage):
    bot.send_message(massage.chat.id ,"hello enter the phone number(Ex: +10994893894)")
#program
@bot.message_handler(content_types= ['text'])
def number(massage):
    try:
        phone = massage.text
        ch_number = phonenumbers.parse(phone, "CH")
        awnser2 = "Info: " + str(ch_number)
#country
        place = geocoder.description_for_number(ch_number, "en")
        awnser1 = "Country: " + place
#provider
        service = phonenumbers.parse(phone, "RO")
        edo = "provider: " + carrier.name_for_number(service, "en")
#timezone 
        time  = phonenumbers.parse(phone, "en")
        awnser = "timezone: " + str(timezone.time_zones_for_number(time))
#cordinats
        geocoding = OpenCageGeocode(key)
        idk = str(place)
        place_number = geocoding.geocode(idk)
        p_1 = place_number[0]['geometry']['lat']
        p_2 = place_number[0]['geometry']['lng']
        awnser4 = "Country X cordinat are: " + str(p_1)
        awnser3 = 'country Y cordinat are: ' + str(p_2)
#awnser     
        bot.send_message(massage.chat.id, awnser2)
        bot.send_message(massage.chat.id, awnser1)
        bot.send_message(massage.chat.id, edo)
        bot.send_message(massage.chat.id, awnser)
        bot.send_message(massage.chat.id, awnser4)
        bot.send_message(massage.chat.id, awnser3)
    except:
        bot.send_message(massage.chat.id, "Something went wrong!. Wrong number or Wrong command")
bot.infinity_polling()