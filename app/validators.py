import re
from wtforms import ValidationError

def validar_senha(form,field):
  padrao_senha = re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&*])(?=.*\d)[a-zA-Z\d!@#$%&*].{8,}",field.data)
  if not padrao_senha:
    raise ValidationError("Por favor, insira uma senha válida.")
