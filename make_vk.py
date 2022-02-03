#подключение библиотек
#для формирования картинки
from wordcloud import WordCloud
#чтобы хоть как-то отсеить действительно самые частые слова)
from stop_words import get_stop_words

#функция генерации картинки
def make():
    #получение стоп слов (которые сразу будут исключены из анализа)
    stopwords = get_stop_words("ru")
    punct = ['.', ',', '!', '?', ')', '(']
    #строка, в которой будет лежать вся переписка
    data_string = ''
    #открытие файла
    with open('chat.html', 'r', encoding='windows-1251') as f:
        text = f.read()
    f.close()
    words = []
    position = text.find('<div class="im-mess--text wall_module _im_log_body">')
    while text and position != -1:
        text = text[position + 52:]
        check_pose = text.find('<')
        position = text.find('</div>')
        if position == check_pose:
            words.append(text[:position])
        position = text.find('<div class="im-mess--text wall_module _im_log_body">')
        #перебор всех сообщений
        for i in words:
                word = i.lower()
                #исключение знаков пунктуации
                for c in punct:
                    word = i.replace(c, '').lower()
                #добавление слова в строку со всей перепиской
                data_string += word + ' '

    #настройка картинки
    wc = WordCloud(
        #цвет фона (можно менять)
        background_color='white',
        stopwords=set(stopwords),
        #высота картинки (можно менять)
        height=500,
        #ширина картинки (можно менять)
        width=500,
        #количество слов на картинке (можно менять, чем больше слов, тем дольше работает программа)
        max_words=1000
    )
    #генерация картинки
    wc.generate(data_string)
    #сохранение картинки
    wc.to_file('word_cloud.png')

