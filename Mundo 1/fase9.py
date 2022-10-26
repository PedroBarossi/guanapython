frase = 'Curso em Vídeo Python'
print(frase[9]) #V
print(frase[9:13]) #Víde
print(frase[9:21:2]) #VdoPto
print(frase[:5]) #Curso
print(frase[15:]) #Python
print(frase[9::3]) #VePh

print(len(frase)) #21
print(frase.count('o')) #3
print(frase.count('o', 0, 13)) #1
print(frase.find('deo')) #11
print(frase.find('Android')) #-1 (não encontrado)
print('Curso' in frase) #True
print(frase.replace('Python', 'Android')) #Curso em Vídeo Android
print(frase.upper()) #CURSO EM VÍDEO PYTHON
print(frase.lower()) #curso em vídeo python
print(frase.capitalize()) #Curso em vídeo python
print(frase.title()) #Curso Em Vídeo Python

frase = '   Aprenda Python  '
print(frase.strip()) #Aprenda Python
print(frase.rstrip()) #'   Aprenda Python'
print(frase.lstrip()) #'Aprenda Python  '

frase = 'Curso em Vídeo Python'
palavras = frase.split()
print(palavras) #['Curso', 'em', 'Vídeo', 'Python']
print('-'.join(palavras)) #Curso-em-Vídeo-Python

#print multilinhas
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Etiam semper consequat rutrum.
Nulla pharetra consequat lorem eu pellentesque.
Suspendisse pharetra ultricies dolor vel volutpat.
Donec vehicula enim sagittis tempor ultrices.
Sed egestas vel ante at molestie.""")