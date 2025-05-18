# 🕵️‍♂️ Analisador de Logs de Segurança

## 🔍 Detecte padrões suspeitos e mantenha seus sistemas protegidos

---

### 📖 Sobre o projeto

Este script automatiza a análise de arquivos de log do sistema — como logs de autenticação, firewall ou sistema — para identificar padrões suspeitos, tentativas de acesso não autorizadas e atividades anômalas.  

Ideal para administradores, analistas de segurança e profissionais de TI que precisam monitorar a segurança de seus ambientes de forma eficiente e proativa.

O projeto traz uma abordagem simples, porém poderosa, para detectar possíveis ameaças antes que elas causem danos, facilitando a resposta rápida a incidentes de segurança.

---

### 🚀 Funcionalidades principais

- Análise de arquivos de log padrão (ex: `/var/log/auth.log`, logs do Windows Event Viewer exportados).  
- Identificação de padrões comuns de ataque, como tentativas de login falhas em sequência, acessos de IPs suspeitos, e ações fora do comum.  
- Geração de relatórios resumidos com alertas destacados.  
- Configurável para diferentes formatos de log.  
- Fácil integração em pipelines de monitoramento e resposta automatizada.

---

### ⚙️ Como usar

#### Pré-requisitos

- Python 3.x instalado.  
- Arquivos de log acessíveis para análise.  

#### Passos para executar

1. Clone o repositório:
```bash
git clone https://github.com/viniciusldiniz/analisadorlogsseguranca.git
cd analisadorlogsseguranca
