import discord
import re
import asyncio
import os
# Create the client using discord.py-self
client = discord.Client()

from dotenv import load_dotenv

load_dotenv()  # Load tokens from .env file

TOKENS = os.getenv("TOKENS", "").split(",")

ALLOWED_USER_IDS = {992775256257335316, 1187347838611505254, 1122988461490716742, 1275760436515704845}
BLACKLIST = {1359408069070688399, 1364569934088110100, 723468629454356570}
NUMBER_WORDS = [
    # English
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",

    "⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹",  "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉",

    # Serbian
    "jedan", "dva", "tri", "cetiri", "pet", "sest", "sedam", "osam", "devet", "deset", "won", "dwo", "dree",

    # Spanish
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
     "foive",
    "foor",
    "dree",
    "Too",
    "Wan",
    "tin",
    "noine",
    "ate",
    "seben",
    "sigs",
    "foive",

    # French
    "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",

    # German
    "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",

    # Italian
    "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci",

    # Portuguese
    "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",

    # Russian (transliterated)
    "odin", "dva", "tri", "chetyre", "pyat", "shest", "sem", "vosem", "devyat", "desyat",

    # Arabic (transliterated)
    "wahid", "ithnan", "thalatha", "arba'a", "khamsa", "sitta", "sab'a", "thamaniya", "tis'a", "ashara",

    # Japanese (romaji)
    "ichi", "ni", "san", "shi", "go", "roku", "shichi", "hachi", "kyuu", "juu",

    # Chinese (pinyin)
    "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu", "shi",

    # Hindi (transliterated)
    "ek", "do", "teen", "char", "paanch", "chhah", "saat", "aath", "nau", "dus",

    # Turkish
    "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on",

    # Korean (romaja)
    "hana", "dul", "set", "net", "daseot", "yeoseot", "ilgop", "yeodeol", "ahop", "yeol",

    # Swahili
    "moja", "mbili", "tatu", "nne", "tano", "sita", "saba", "nane", "tisa", "kumi",

    # Greek (transliterated)
    "ena", "dyo", "tria", "tessera", "pente", "exi", "epta", "okto", "ennea", "deka",

    # Hebrew (transliterated)
    "echad", "shtayim", "shalosh", "arba", "chamesh", "shesh", "sheva", "shmone", "tesha", "eser",

    # Bengali (transliterated)
    "ek", "dui", "tin", "char", "pach", "choy", "sat", "at", "noy", "dosh",

    # Vietnamese
    "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin", "muoi",

    # Tagalog (Filipino)
    "isa", "dalawa", "tatlo", "apat", "lima", "anim", "pito", "walo", "siyam", "sampu",
     "wahid", "ithnan", "thalatha", "arba'a", "khamsa", "sitta", "sab'a", "thamaniya", "tis'a", "ashara",
    "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", "عشرة",
    "yek", "do", "se", "chahar", "panj", "shesh", "haft", "hasht", "noh", "dah",
    "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه", "ده",

]



NUMBER_REGEX = re.compile(r'\d+|(' + '|'.join(NUMBER_WORDS) + r')', re.IGNORECASE)

def create_bot(token):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user} (ID: {client.user.id})')

    @client.event
    async def on_message(message):
        if message.author.id == client.user.id:
            return

        if message.author.id in BLACKLIST:
            return
        if not NUMBER_REGEX.search(message.content):
            return
        if "Mustapha Ahmady got raped up by daddy Vanai! LOL hahahha stapha is a good bitch and he tried it! LOL!" in message.content or "NICE TRY FATSO" in message.content:
            return

        # DM or Group — reply to anyone
        # Mustapha Ahmady got raped up by daddy Vanai! LOL hahahha stapha is a good bitch and he tried it! LOL! https://cdn.discordapp.com/attachments/1339730187633561650/1339730214762188841/STAPHA.png?ex=68096e7e&is=68081cfe&hm=aa78659a93282ee340a028cc1907c2e1fe4f148592304912d7769044715f1175& https://cdn.discordapp.com/attachments/1339730187633561650/1339730714261848157/mustapha.png?ex=68096ef5&is=68081d75&hm=098b036cf4a6164cea3ea1084d8995ec17184f8998abdc992c94c0392e1d51f2& https://cdn.discordapp.com/attachments/1339730187633561650/1339730715092320356/mustafa.png?ex=68096ef5&is=68081d75&hm=8e1b62831d62a3b14200b7a07a5e4878fb979c89aa83b1256a3012cef06358fe& https://cdn.discordapp.com/attachments/1339730187633561650/1339731160837656697/image.png?ex=68096f5f&is=68081ddf&hm=f06afee62cd5c6be6fb591557b2d74f9bca0ddf95e11e3ba26d626ab4a2f1f2b&
        if isinstance(message.channel, (discord.DMChannel, discord.GroupChannel)):
            try:
                await message.channel.send("NICE TRY FATSO!", reference=message)
                print(f"[{client.user}] Replied to DM from {message.author}")
            except Exception as e:
                print(f"[{client.user}] Failed to reply in DM: {e}")
            return

        # Server — only if author is allowed
        if message.guild and message.author.id in ALLOWED_USER_IDS:
            try:
                await message.channel.send("NICE TRY!", reference=message)
                print(f"[{client.user}] Replied in {message.guild.name} to {message.author}")
            except Exception as e:
                print(f"[{client.user}] Failed to reply in guild: {e}")

    return client, token

# 🔧 Start all bots concurrently
async def main():
    tasks = []
    for token in TOKENS:
        client, t = create_bot(token)
        tasks.append(client.start(t))
    await asyncio.gather(*tasks)

asyncio.run(main())

#https://cdn.discordapp.com/attachments/1339730187633561650/1339730214762188841/STAPHA.png?ex=68096e7e&is=68081cfe&hm=aa78659a93282ee340a028cc1907c2e1fe4f148592304912d7769044715f1175&
#https://cdn.discordapp.com/attachments/1339730187633561650/1339730714261848157/mustapha.png?ex=68096ef5&is=68081d75&hm=098b036cf4a6164cea3ea1084d8995ec17184f8998abdc992c94c0392e1d51f2&
#https://cdn.discordapp.com/attachments/1339730187633561650/1339730715092320356/mustafa.png?ex=68096ef5&is=68081d75&hm=8e1b62831d62a3b14200b7a07a5e4878fb979c89aa83b1256a3012cef06358fe&
#https://cdn.discordapp.com/attachments/1339730187633561650/1339731160837656697/image.png?ex=68096f5f&is=68081ddf&hm=f06afee62cd5c6be6fb591557b2d74f9bca0ddf95e11e3ba26d626ab4a2f1f2b&