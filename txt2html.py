
import re

def color(pattern, color, line):
    matchText = re.findall(pattern, line)
    if len(matchText) > 0:
        for mT in matchText:
            line = re.sub(mT, '<span style="color:colorText;"><b>'+mT+'</b></span>', line)
            line = re.sub('colorText', color, line)

    return line

f = open('output.txt')
lines = f.readlines()
f.close()
bodyText = ''

for line in lines:
    # 색
    line = color('failure', 'red', line)
    line = color('warning', 'red', line)
    line = color('\:\d+', 'red', line)
    line = color('\: line \d+', 'red', line)

    # 제거
    #line = re.sub('\^\[\[\d+m', '', line)
    bodyText += line+'<br>'

html = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>ansible-lint</title></head><body>{}</body></html>'.format(bodyText)

f = open('output.html', 'w')
f.write(html)
f.close()