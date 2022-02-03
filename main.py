# <div class="im-mess--text wall_module _im_log_body">И возвращаюсь</div>

f = open('chat.html', 'r')
text = f.read()
words = []

position = text.find('<div class="im-mess--text wall_module _im_log_body">')
while text and position != -1:
    text = text[position+52:]
    check_pose = text.find('<')
    position = text.find('</div>')
    if position == check_pose:
        words.append(text[:position])
    position = text.find('<div class="im-mess--text wall_module _im_log_body">')

print(words)

