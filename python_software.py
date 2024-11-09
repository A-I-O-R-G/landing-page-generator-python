import json

class LandingPageGenerator:
    def __init__(self, description: str):
        self.description = description
        self.title = ""
        self.subtitle = ""
        self.images = []
        self.texts = []
        self.call_to_action = ""
        self.form = ""
    
    def interpret_description(self):
        # Simulando a interpretação da descrição
        data = json.loads(self.description)
        
        self.title = data.get("title", "Título Padrão")
        self.subtitle = data.get("subtitle", "Subtítulo Padrão")
        self.images = data.get("images", [])
        self.texts = data.get("texts", [])
        self.call_to_action = data.get("call_to_action", "Clique Aqui")
        self.form = data.get("form", "")
        
    def generate_html(self) -> str:
        # Inicia a construção do HTML
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; }}
                .container {{ padding: 20px; max-width: 1200px; margin: auto; }}
                .img {{ max-width: 100%; height: auto; }}
                .cta {{ background-color: #0066cc; color: white; padding: 10px 20px; text-align: center; display: inline-block; margin: 20px 0; }}
                @media (max-width: 600px) {{
                    .container {{ padding: 10px; }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{self.title}</h1>
                <h2>{self.subtitle}</h2>
                {"".join(f'<img class="img" src="{img}" alt="Imagem" />' for img in self.images)}
                {"".join(f'<p>{text}</p>' for text in self.texts)}
                <a href="#" class="cta">{self.call_to_action}</a>
                {self.form}
            </div>
        </body>
        </html>
        """
        return html_content
    
    def save_to_file(self, filename: str):
        html_content = self.generate_html()
        with open(filename, "w") as file:
            file.write(html_content)
        print(f"Landing page salva como {filename}")

if __name__ == "__main__":
    description_json = """
    {
        "title": "Bem-vindo à Nossa Plataforma",
        "subtitle": "Otimize seu aprendizado",
        "images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        "texts": ["Texto introdutório sobre a plataforma.", "Mais informações sobre os serviços oferecidos."],
        "call_to_action": "Inscreva-se Agora",
        "form": "<form><input type='text' placeholder='Seu nome'><input type='email' placeholder='Seu email'><button type='submit'>Enviar</button></form>"
    }
    """
    generator = LandingPageGenerator(description_json)
    generator.interpret_description()
    generator.save_to_file("landing_page.html")