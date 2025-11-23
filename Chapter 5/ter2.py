# See https://pypi.org/project/deep-translator/ for translator solutions
# We choose here Google Translator

from deep_translator import GoogleTranslator

def translation(text) -> str:
   return GoogleTranslator(source='auto', target='en').translate(text=text)
# Main program
text = str(input('Please enter a text: '))
while text != 'stop':
   print(translation(text))
   text = str(input('Please enter a text: '))
print('Translation finished.')