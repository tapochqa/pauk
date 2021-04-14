
RUSSIAN_ALPHABET = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split(' ')
ENGLISH_ALPHABET = 'A B C D E F G H I J K L M N O P Q R S T V U W X Y Z'.split(' ')
PAUK_STEP_ONE = 'A B V G D E YO ZH Z I IY K L M N O P R S T U F H TS CH SH SHCH ` Y ` E YU YA'.split(' ')
PAUK_STEP_TWO = 'А В С Д Е Г Ж Н I Ь К Л М И О Р Ц Я Ы Т Ф Ю Ш Х У П'.split(' ')

STEP_ONE_DICT = dict(zip(RUSSIAN_ALPHABET, PAUK_STEP_ONE))
STEP_TWO_DICT = dict(zip(ENGLISH_ALPHABET, PAUK_STEP_TWO))


def paukize(phrase):
	

	phrase = phrase.lower()


	for k, v in STEP_ONE_DICT.items():
		phrase = phrase.replace(k, v)


	
	for k, v in STEP_TWO_DICT.items():
		phrase = phrase.replace(k, v)
	
	return phrase