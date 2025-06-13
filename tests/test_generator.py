import pytest
from src.model.transformer import StoryGenerator
from src.utils.text_formatting import clean_text, format_story

def test_story_generator_initialization():
    generator = StoryGenerator()
    assert generator is not None
    assert generator.model is not None
    assert generator.tokenizer is not None

def test_text_cleaning():
    text = '  Este es  un   texto   con espacios   extras  '
    cleaned = clean_text(text)
    assert cleaned == 'Este es un texto con espacios extras.'

def test_story_formatting():
    story = 'Esta es una historia de prueba'
    title = 'Mi Historia'
    formatted = format_story(story, title)
    assert formatted == 'Mi Historia\n\nEsta es una historia de prueba'
