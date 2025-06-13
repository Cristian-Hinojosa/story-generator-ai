import os
import json

class DataLoader:
    def __init__(self, data_dir='data/stories'):
        self.data_dir = data_dir
    
    def load_stories(self):
        """Carga las historias desde el directorio de datos."""
        stories = []
        if os.path.exists(self.data_dir):
            for filename in os.listdir(self.data_dir):
                if filename.endswith('.txt'):
                    with open(os.path.join(self.data_dir, filename), 'r') as f:
                        stories.append(f.read())
        return stories
