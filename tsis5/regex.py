#1
import re

pattern = 'ab*'
text = 'abbbbb abb'
matching = re.findall(pattern,text)
print(matching)

#2
pattern = 'ab{2,3}'
text = 'abb abbbdb shdb'
matching = re.findall(pattern,text)
print(matching)

#3
text = 'asnsaj_ udhu_ egwhb sjbj_ asjbwj'
pattern = '[a-z]+_'
matching = re.findall(pattern, text)
print(matching)

#4
pattern = '[A-Z][a-z]*'
text = 'Asdf hbsdha Fghskj'
matching = re.findall(pattern, text)
print(matching)

#5
text = input()
pattern = r'a.+b'
matching = re.search(pattern, text)
print(matching)

#6
pattern = '[,. ]'
text = input()
matching = re.sub(pattern, ':' , text)
print(matching)

#7
text = 'hello_world_im_from_kz'
text = text.split('_')
for i in range(0, len(text)):
    text[i] = re.sub(text[i][0], text[i][0].upper(),text[i])
ans = ''.join(text)
print(ans)

#8
pattern = '[A-Z][^A-Z]*'
text = 'HelloWorldImFromKz'
matching = re.findall(pattern,text)
print(matching)

#9
pattern = '[A-Z][a-z]*'
text = 'FalseTrueLiePain'
matching = re.findall(pattern,text)
print(' '.join(matching))

#10
text = 'EasyPeasyLemonSqueezyStressedDepressedLemonZest'
pattern = r'[A-Z][a-z]*'
matching = re.findall(pattern, text)
ans = '_'.join(matching)
print(ans.lower())