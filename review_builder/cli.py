"""CLI para etapas do pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.demo import run_demo
from review_builder.packager import PackagingError, package_review
from review_builder.utils import PROJECT_ROOT


def compose_cmd() -> None:
    parser = argparse.ArgumentParser(description="Compõe página HTML estática")
    parser.add_argument("--content", required=True, type=Path)
    parser.add_argument("--exercises", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--assets", type=Path, default=None)
    args = parser.parse_args()
    path = compose_page(args.content, args.exercises, args.output, assets_root=args.assets)
    print(f"Gerado: {path}")


def audit_cmd() -> None:
    parser = argparse.ArgumentParser(description="Audita revisão gerada")
    parser.add_argument("--review-id", required=True)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--html", type=Path, default=None)
    args = parser.parse_args()
    report = audit_and_save(args.review_id, args.workspace, args.html)
    print(f"Status: {report['status']}")


def package_cmd() -> None:
    parser = argparse.ArgumentParser(description="Empacota revisão após auditoria")
    parser.add_argument("--review-id", required=True)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=PROJECT_ROOT / "output")
    parser.add_argument("--audit", required=True, type=Path)
    args = parser.parse_args()
    try:
        dest = package_review(args.review_id, args.source, args.output, args.audit)
        print(f"Empacotado em: {dest}")
    except PackagingError as e:
        print(f"ERRO: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    run_demo()
