import os
import hashlib
import sys
import json


pasta = "monitored_files"


def calculate_hash(arquivo):
    with open(arquivo, "rb") as file:
        conteudo = file.read()

    return hashlib.sha256(conteudo).hexdigest()


def create_baseline():
    hashes = {}

    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)

        if not os.path.isfile(caminho):
            continue

        hash_atual = calculate_hash(caminho)

        hashes[arquivo] = hash_atual

    with open("baseline.json", "w") as file:
        json.dump(hashes, file, indent=4)

    print("[OK] Baseline criado com sucesso.")


def check_integrity():
    try:
        with open("baseline.json", "r") as file:
            baseline = json.load(file)

    except FileNotFoundError:
        print("[ERRO] baseline.json não encontrado.")
        print("Execute o programa com --baseline primeiro.")
        return

    arquivos_atuais = os.listdir(pasta)

    for arquivo in arquivos_atuais:
        caminho = os.path.join(pasta, arquivo)

        if arquivo not in baseline:
            print(f"[NOVO] {arquivo} foi encontrado!")
            continue

        hash_atual = calculate_hash(caminho)
        hash_original = baseline[arquivo]

        if hash_original == hash_atual:
            print(f"[OK] {arquivo} está íntegro.")
        else:
            print(f"[ALERTA] {arquivo} foi alterado!")
            print(f"Hash original: {hash_original}")
            print(f"Hash atual:    {hash_atual}")

    for arquivo in baseline:
        if arquivo not in arquivos_atuais:
            print(f"[ALERTA] {arquivo} foi removido!")


if len(sys.argv) != 2:
    print("Uso:")
    print("python integrity.py --baseline")
    print("python integrity.py --check")
    sys.exit()


modo = sys.argv[1]


if modo == "--baseline":
    create_baseline()

elif modo == "--check":
    check_integrity()

else:
    print("Modo inválido.")