# Brute Force Directory Finder

Ferramenta simples em Python para realizar **brute force de diretórios** em um site utilizando uma **wordlist**.

## 📌 Descrição

Este script testa múltiplos caminhos em um site a partir de uma lista de palavras (wordlist), tentando identificar **diretórios ou páginas ocultas**.

É útil para:
- Estudos de **pentest**
- **CTFs**
- Aprendizado em **segurança ofensiva**

## ⚙️ Requisitos

- Python 3.x
- Biblioteca `requests`

Instale a dependência com:

```bash
pip install requests
```

## 🚀 Uso

Execute o script utilizando um site alvo e uma wordlist.
```bash
python .\brute-force-dirb.py (sitedesejado) .\wordlist.txt
```
OU
```bash
python3 .\brute-force-dirb.py (sitedesejado) .\wordlist.txt
```

## 📂 Estrutura do Projeto
.

├── brute-force-dirb.py

├── wordlist.txt

└── README.md

## ⚠️ Aviso
Esta ferramenta foi criada apenas para fins educacionais.
Não utilize em sites sem autorização explícita.

O uso indevido pode violar leis locais.
