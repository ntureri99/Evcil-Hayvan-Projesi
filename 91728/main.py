import play

player = play.new_image(image='1-9.png', x=0, y=0, size=100)
speech = play.new_text(words=None, x=0, y=-play.screen.height/2 + 40)

i = 0  # Beslenme durumu için global değişken

@play.when_program_starts # başlangıç ayarları
def start():
    tutorial = play.new_text(words='''s - sevmek, b - beslemek, t - temizlemek, o - oyun oynamak, boşluk - çıkış''', 
        x=0, y=play.screen.height/2 - 40, font_size=30)
    speech.words = 'Selam, arkadaş olalım mı? '

@play.repeat_forever # sürekli tekrarlanacak eylemler 
async def do():
    global i

    # Sevme
    if play.key_is_pressed('s') or play.key_is_pressed('S'):
        player.image = 'purr-3.gif'
        speech.words = 'Mmm... Çok güzel'
        await play.timer(seconds=2.0)
        player.image = '2-7.png'
        speech.words = 'Bu kadar mı? Biraz daha sevebilir misin?..'

    # Beslenme
    if play.key_is_pressed('b') or play.key_is_pressed('B'):
        if i < 3: # i=0 o yüzden eşitlik yok. döngü 3 kere çalışacak
            player.image = '3-5.png'
            speech.words = 'Oh, çok lezzetli!'
            await play.timer(seconds=2.0)
            i += 1 # i=i+1

            if i < 3:
                speech.words = f'Bir daha isterim ({i}/3). B tuşuna bas'
            else:
                player.image = '6-6.png'
                speech.words = 'Doydum! Şimdi temizlenmeliyim.'
            await play.timer(seconds=2.0)

    # Temizlenme
    if play.key_is_pressed('t') or play.key_is_pressed('T'):
        player.image = '1-9.png'
        speech.words = 'Yaşasın! Mis gibi oldum!'
        await play.timer(seconds=2.0)
        player.image = '2-7.png'
        speech.words = 'Şimdi ne yapalım?'

    # Oyun zamanı
    if play.key_is_pressed('o') or play.key_is_pressed('O'):
        player.image = '7-5.png'
        speech.words = 'Ahaha, çok eğlenceli birisin!'
        await play.timer(seconds=2.0)
        player.image = '2-7.png'
        speech.words = 'Of, sanırım yorulmuşum'

    # Oyun sonu
    if play.key_is_pressed('space'):
        player.image = '5-5.png'
        speech.words = 'Gidiyor musun? Seni özlerim!'
        await play.timer(seconds=2.0)
        player.hide()

play.start_program()
