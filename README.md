# Verificador de Certificados Digitais

Este projeto é uma aplicação Python para verificar a confiança de certificados digitais com base em Autoridades Certificadoras Raiz (AC-Raiz). O usuário pode fornecer um certificado digital e uma lista de certificados confiáveis, e o programa verificará se o certificado digital é confiável.

## Funcionalidades

- Carrega certificados confiáveis (AC-Raiz) de uma pasta especificada.
- Verifica a cadeia de confiança de um certificado digital fornecido pelo usuário.
- Exibe o status do certificado: confiável ou não confiável.

## Requisitos

- Python 3.6 ou superior.
- Bibliotecas Python listadas em `requirements.txt`.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/verificador-certificados.git
   cd verificador-certificados
