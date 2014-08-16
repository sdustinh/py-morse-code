import time
import pygame

CODES = {
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'0': '-----',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.'
}

def main():
	message = raw_input('MESSAGE: ')
	pygame.init()
	pygame.mixer.init()
	
	for char in message:
		if char != ' ':
			char = char.upper()
		
		if char in CODES:
			print(CODES[char])
			pygame.mixer.music.load('audio/' + char + '.ogg')
			pygame.mixer.music.play()
			time.sleep(0.5 * 2)
		else:
			print ' ' * 7
			time.sleep(0.5 * 7)

if __name__ == "__main__":
	main()
