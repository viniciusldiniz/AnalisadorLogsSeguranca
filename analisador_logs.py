import argparse
import re
from collections import Counter

def analisar_log(caminho_arquivo):
    """Analisa o arquivo de log e detecta padrões suspeitos."""
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
        linhas = f.readlines()

    # Exemplo simples: contar tentativas de login falhas
    padrao_falha_login = re.compile(r'failed password', re.IGNORECASE)
    ips = []

    for linha in linhas:
        if padrao_falha_login.search(linha):
            # Extrair IP (exemplo comum em logs Linux)
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', linha)
            if ip_match:
                ips.append(ip_match.group(1))

    contagem_ips = Counter(ips)
    print("Tentativas de login falhas por IP:")
    for ip, qtd in contagem_ips.most_common():
        print(f"{ip}: {qtd} tentativas")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analisador de Logs de Segurança")
    parser.add_argument('--log', required=True, help="Caminho para o arquivo de log")
    args = parser.parse_args()

    analisar_log(args.log)
