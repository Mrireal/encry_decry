# Encry/Decry Project

Repositorio con utilidades simples para encriptar y desencriptar texto usando AES-CBC en Python.

## Status Badges

![Tests](https://github.com/TU_USUARIO/TU_REPOSITORIO/actions/workflows/tests.yml/badge.svg)
![Format Check](https://github.com/TU_USUARIO/TU_REPOSITORIO/actions/workflows/format.yml/badge.svg)

Nota: reemplaza TU_USUARIO y TU_REPOSITORIO por tu usuario y nombre real del repositorio en GitHub.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en requirements.txt

## Uso local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Encriptar:

```bash
python encrypt.py "texto" "mi-clave"
```

Desencriptar:

```bash
python decrypt.py "encrypted_text" "mi-clave" "iv"
```

## Tests

```bash
pytest -q
```

## Formato

```bash
black --check .
```

## CI/CD

Este repositorio ejecuta GitHub Actions para:

- Tests en Ubuntu 22.04 y 24.04
- Python 3.8 y 3.12
- Verificacion de formato con black
