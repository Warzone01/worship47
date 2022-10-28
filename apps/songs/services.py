

class AntiYoService:
    def cleanup_yo(self, text: str) -> str:
        yos = {
            'Ё': 'Е',
            'ё': 'е',
            'Ѐ': 'Е',
            'ѐ': 'е',
        }

        for yo, ye in yos.items():
            text = text.replace(yo, ye)

        return text
