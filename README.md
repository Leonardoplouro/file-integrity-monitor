file-integrity-monitor
Ferramenta de monitoramento de integridade de arquivos desenvolvida em Python, utilizando hashes SHA-256 para detectar arquivos alterados, adicionados ou removidos.

File Integrity Monitor

Uma ferramenta simples de monitoramento de integridade de arquivos desenvolvida em Python.

Sobre o projeto

Este projeto implementa um sistema básico de **File Integrity Monitoring (FIM)**.

A ferramenta cria uma baseline contendo os hashes SHA-256 dos arquivos monitorados e, posteriormente, verifica se esses arquivos foram alterados, removidos ou se novos arquivos foram adicionados.

Esse tipo de monitoramento pode ser utilizado como uma camada adicional de segurança para identificar modificações não autorizadas em arquivos importantes.

Funcionalidades

* Criação de uma baseline de hashes SHA-256
* Verificação da integridade dos arquivos
* Detecção de arquivos modificados
* Detecção de novos arquivos
* Detecção de arquivos removidos
* Comparação entre o hash original e o hash atual
* Armazenamento da baseline em formato JSON

Tecnologias utilizadas

* Python 3
* hashlib
* os
* json
* sys

Estrutura do projeto

```text
file-integrity-monitor/
│
├── integrity.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── monitored_files/
    └── exemplo.txt
```

Como funciona

### 1. Criação da baseline

O programa calcula o hash SHA-256 de todos os arquivos presentes na pasta `monitored_files`.

Esses hashes são armazenados no arquivo `baseline.json`.

Execute:

```bash
python integrity.py --baseline
```

Exemplo de saída:

```text
[OK] Baseline criado com sucesso.
```

2. Verificação da integridade

Após criar a baseline, execute:

```bash
python integrity.py --check
```

O programa irá comparar os hashes atuais dos arquivos com os hashes armazenados anteriormente.

Possíveis resultados:

```text
[OK] arquivo.txt está íntegro.
```

```text
[ALERTA] arquivo.txt foi alterado!
```

```text
[NOVO] novo_arquivo.txt foi encontrado!
```

```text
[ALERTA] arquivo.txt foi removido!
```

## Exemplo de detecção de alteração

Quando um arquivo é modificado, o hash SHA-256 também é alterado.

A ferramenta detecta essa diferença e exibe:

```text
[ALERTA] arquivo.txt foi alterado!
Hash original: ...
Hash atual:    ...
```

Isso permite identificar alterações realizadas após a criação da baseline.

Objetivo

Este projeto foi desenvolvido como parte do meu aprendizado em Python e Cibersegurança.

O objetivo é praticar conceitos relacionados a:

* Integridade de arquivos
* Funções hash
* SHA-256
* Monitoramento de arquivos
* Detecção de alterações
* Automação com Python
* Fundamentos de File Integrity Monitoring (FIM)

Possíveis melhorias futuras

* Monitoramento automático em tempo real
* Registro de eventos em arquivos de log
* Suporte para subdiretórios
* Interface de linha de comando mais completa
* Configuração de diretórios monitorados
* Data e horário das alterações
* Sistema de alertas
* Exportação de relatórios
* Testes automatizados

Aviso

Este é um projeto educacional desenvolvido para fins de aprendizado e construção de portfólio na área de Cibersegurança.

Autor

Desenvolvido por Leonardo Pereira.
