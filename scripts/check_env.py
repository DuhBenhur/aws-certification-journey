"""Verifica se o ambiente de estudos está pronto: Python, venv, pacotes e AWS.

Uso:
    python scripts/check_env.py                 # checagem completa
    python scripts/check_env.py --allow-default # permite usar o perfil AWS 'default'

Por segurança, a chamada à AWS só acontece se AWS_PROFILE apontar para um
perfil diferente de 'default' (que costuma ser a conta do trabalho).
A única chamada feita é sts:GetCallerIdentity, que é somente leitura e gratuita.
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
from importlib import metadata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# nome do pacote no pip -> nome do módulo no import
PACKAGES = {
    "boto3": "boto3",
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "jupyterlab": "jupyterlab",
    "python-dotenv": "dotenv",
}

OK, WARN, FAIL = "[ OK ]", "[WARN]", "[FAIL]"


def check_python() -> bool:
    v = sys.version_info
    ok = v >= (3, 11)
    print(f"{OK if ok else FAIL} Python {v.major}.{v.minor}.{v.micro}")

    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        print(f"{OK} Ambiente virtual ativo ({Path(sys.prefix).name})")
    else:
        print(f"{WARN} Ambiente virtual NÃO ativo. Rode: .\\.venv\\Scripts\\Activate.ps1")
    return ok


def check_packages() -> bool:
    all_ok = True
    for pip_name, module_name in PACKAGES.items():
        try:
            importlib.import_module(module_name)
            print(f"{OK} {pip_name} {metadata.version(pip_name)}")
        except ImportError:
            print(f"{FAIL} {pip_name} não instalado. Rode: pip install -r requirements.txt")
            all_ok = False
    return all_ok


def load_env_file() -> None:
    env_file = ROOT / ".env"
    if not env_file.exists():
        print(f"{WARN} Arquivo .env não encontrado. Copie de .env.example (veja docs/setup.md)")
        return
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv(env_file)
    print(f"{OK} .env carregado")


def mask_account(account_id: str) -> str:
    return account_id[:2] + "*" * (len(account_id) - 6) + account_id[-4:]


def check_aws(allow_default: bool) -> bool:
    profile = os.getenv("AWS_PROFILE")
    if not profile or profile == "default":
        if not allow_default:
            print(
                f"{WARN} AWS_PROFILE não definido (ou 'default'). Chamada à AWS PULADA.\n"
                "       Configure um perfil só de estudos e aponte o .env para ele (docs/setup.md)."
            )
            return True
        print(f"{WARN} Usando o perfil 'default' (permitido com --allow-default)")

    try:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError
    except ImportError:
        print(f"{FAIL} boto3 indisponível. Não é possível testar a AWS")
        return False

    try:
        session = boto3.Session()
        identity = session.client("sts").get_caller_identity()
    except NoCredentialsError:
        print(f"{FAIL} Nenhuma credencial encontrada para o perfil '{profile}'")
        return False
    except (ClientError, BotoCoreError) as exc:
        print(f"{FAIL} Erro ao validar credenciais: {exc}")
        return False

    account = identity["Account"]
    masked = mask_account(account)
    arn = identity["Arn"].replace(account, masked)
    region = session.region_name or "(não definida)"
    print(f"{OK} AWS: perfil '{profile or 'default'}', conta {masked}, região {region}")
    print(f"       identidade: {arn}")
    if ":root" in arn:
        print(f"{WARN} Você está usando o usuário ROOT. Crie um usuário/role administrador.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--allow-default", action="store_true", help="permite o perfil AWS 'default'")
    args = parser.parse_args()

    print("== Python ==")
    py_ok = check_python()
    print("\n== Pacotes ==")
    pkg_ok = check_packages()
    print("\n== AWS ==")
    load_env_file()
    aws_ok = check_aws(args.allow_default)

    all_ok = py_ok and pkg_ok and aws_ok
    print("\nAmbiente pronto." if all_ok else "\nHá itens a corrigir acima.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
