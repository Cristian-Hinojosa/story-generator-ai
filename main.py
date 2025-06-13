from src.model.transformer import StoryGenerator
from src.utils.text_formatting import clean_text, format_story

def main():
    # Inicializar el generador
    generator = StoryGenerator()
    
    # Ejemplo de prompt
    prompt = input('Ingresa un inicio para tu historia: ')
    
    # Generar la historia
    print('Generando historia...')
    story = generator.generate_story(prompt)
    
    # Limpiar y formatear el texto
    story = clean_text(story)
    formatted_story = format_story(story, title='Mi Historia Generada')
    
    print('\nHistoria generada:')
    print('-----------------')
    print(formatted_story)

if __name__ == '__main__':
    main()
