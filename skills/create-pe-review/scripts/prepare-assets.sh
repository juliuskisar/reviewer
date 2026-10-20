#!/usr/bin/env bash
# Copia imagens do caderno para assets/ com nomes page-001.jpg, page-002.jpg, …
# Uso: prepare-assets.sh <pasta_origem> <pasta_destino_assets>
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Uso: $0 <pasta_origem> <pasta_destino>" >&2
  exit 1
fi

SRC="$1"
DST="$2"

if [[ ! -d "$SRC" ]]; then
  echo "Origem não encontrada: $SRC" >&2
  exit 1
fi

mkdir -p "$DST"

# Remove páginas numeradas anteriores (não apaga manifest.yaml)
find "$DST" -maxdepth 1 -name 'page-*.jpg' -delete 2>/dev/null || true

i=1
shopt -s nullglob
files=("$SRC"/*.{jpg,JPG,jpeg,JPEG,png,PNG})
shopt -u nullglob

if [[ ${#files[@]} -eq 0 ]]; then
  echo "Nenhuma imagem em $SRC" >&2
  exit 1
fi

IFS=$'\n' sorted=($(printf '%s\n' "${files[@]}" | sort))
unset IFS

for f in "${sorted[@]}"; do
  printf -v num "%03d" "$i"
  cp "$f" "$DST/page-${num}.jpg"
  i=$((i + 1))
done

echo "Copiadas $((i - 1)) imagens para $DST"
