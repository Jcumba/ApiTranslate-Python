# Importa la libreria Google Cloud Client
from google.cloud import translate

# Creamos la instancia Cliente
translate_client = translate.Client()

# Establecemos el texto a traducir
text = u'Hello, world!'
# El idioma en el que quisieramos traducir IDIOMA TEST:
target = 'es' #Lista de idiomas permitidos https://cloud.google.com/translate/docs/languages

# Traducimos el texto
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))


# Se realizo de la propia DOCUMENTACIÓN DE GOOGLE CLOUD TRANSLATE: https://cloud.google.com/translate/docs/reference/libraries#client-libraries-resources-python
# Donde se investigo:
# Part1: https://www.youtube.com/watch?v=WH7EQFbuIrI&t=20s
# Part2: https://www.youtube.com/watch?v=wSDJumicV0o


# Agregando credenciales para el uso del json  GOOGLE_APPLICATION_CREDENTIALS