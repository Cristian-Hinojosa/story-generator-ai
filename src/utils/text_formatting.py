def clean_text(text):
    """Limpia y formatea el texto generado."""
    # Eliminar espacios extra
    text = ' '.join(text.split())
    # Asegurar que las oraciones terminen con punto
    if not text.endswith(('.', '!', '?')):
        text += '.'
    return text

def format_story(text, title=None):
    """Formatea una historia con título opcional."""
    if title:
        return f"{title}\n\n{text}"
    return text
