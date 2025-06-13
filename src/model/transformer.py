from transformers import GPT2LMHeadModel, GPT2Tokenizer

class StoryGenerator:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
    
    def generate_story(self, prompt, max_length=200):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=0.7
        )
        story = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story
