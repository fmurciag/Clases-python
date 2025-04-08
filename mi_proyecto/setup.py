from setuptools import setup
from pathlib import Path


# Leer el archivo requirements.txt
def read_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        with open(requirements_file) as f:
            return f.read().splitlines()
    return []


setup(
    name="mi_proyecto",
    version="0.1",
    description="Un proyecto de ejemplo en Python",
    author="Tu Nombre",
    author_email="tu_email@example.com",
    packages=["mi_proyecto"],
    install_requires=read_requirements(),
)
