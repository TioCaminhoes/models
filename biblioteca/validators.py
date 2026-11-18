from datetime import date
from django.core.exceptions import ValidationError

def validar_ano_publicado(value):
    ano_atual = date.today().year
    if value < 1450 or value > ano_atual:
        raise ValidationError(
            "O ano de publicação deve estar entre 1450 e %(ano_atual)s. Recebido: %(value)s",
            params={"ano_atual": ano_atual, "value": value},
        )
