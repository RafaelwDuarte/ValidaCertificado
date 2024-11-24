import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def carregar_certificados(pasta_raiz):
    """
    Carrega os certificados confiáveis (AC-Raiz) de uma pasta.
    """
    certificados_raiz = []
    for arquivo in os.listdir(pasta_raiz):
        if arquivo.endswith(".crt"):
            caminho_certificado = os.path.join(pasta_raiz, arquivo)
            with open(caminho_certificado, "rb") as f:
                cert = x509.load_pem_x509_certificate(f.read(), default_backend())
                certificados_raiz.append(cert)
    return certificados_raiz

def verificar_cadeia(cert_user, certificados_raiz):
    """
    Verifica a cadeia de confiança do certificado fornecido.
    """
    for raiz in certificados_raiz:
        try:
            if cert_user.issuer == raiz.subject:
                print(f"Certificado é confiável e foi emitido por: {raiz.subject}")
                return True
        except Exception as e:
            print(f"Erro ao verificar: {e}")
    return False

def main():
    # Caminho para o certificado do usuário e a pasta de certificados confiáveis
    pasta_raiz = input("Informe o caminho da pasta com certificados confiáveis (AC-Raiz): ")
    caminho_cert_user = input("Informe o caminho do certificado do usuário (.crt): ")

    # Carrega os certificados confiáveis
    certificados_raiz = carregar_certificados(pasta_raiz)

    if not certificados_raiz:
        print("Nenhum certificado confiável encontrado na pasta especificada.")
        return

    # Carrega o certificado do usuário
    try:
        with open(caminho_cert_user, "rb") as f:
            cert_user = x509.load_pem_x509_certificate(f.read(), default_backend())
    except Exception as e:
        print(f"Erro ao carregar o certificado do usuário: {e}")
        return

    # Verifica a cadeia de confiança
    confiavel = verificar_cadeia(cert_user, certificados_raiz)

    if confiavel:
        print("Certificado do usuário é confiável.")
    else:
        print("Certificado do usuário NÃO é confiável.")

if __name__ == "__main__":
    main()
