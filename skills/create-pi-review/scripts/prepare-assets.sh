#!/usr/bin/env bash
# Copia imagens PI (multidisciplinar) para assets/<aluno>_pi_<serie>/
# Espera subpastas por disciplina OU uma pasta plana (numera sequencial).
#
# Uso:
#   prepare-assets.sh <pasta_origem> <pasta_destino_assets>
#
# Com subpastas (recomendado):
#   imagens_pi_pedro/
#     ingles/*.jpg
#     geografia/*.jpg
#     ...
#
# Saída:
#   assets/pedro_pi_6_ano/
#     manifest.yaml
#     ingles/page-001.jpg …
#     geografia/page-001.jpg …
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

# Detectar subpastas (disciplinas)
shopt -s nullglob
subdirs=("$SRC"/*/)
shopt -u nullglob

copy_sorted() {
  local from="$1"
  local to="$2"
  local i=1
  local files=()
  shopt -s nullglob
  files=("$from"/*.{jpg,JPG,jpeg,JPEG,png,PNG})
  shopt -u nullglob
  if (( ${#files[@]} == 0 )); then
    return 1
  fi
  mkdir -p "$to"
  find "$to" -maxdepth 1 -name 'page-*.jpg' -delete 2>/dev/null || true
  IFS=$'\n' sorted=($(printf '%s\n' "${files[@]}" | sort))
  unset IFS
  for f in "${sorted[@]}"; do
    printf -v num "%03d" "$i"
    cp "$f" "$to/page-${num}.jpg"
    i=$((i + 1))
  done
  echo "$((i - 1))"
}

total=0

if [[ ${#subdirs[@]} -gt 0 ]]; then
  # Modo multidisciplinar: uma subpasta = uma disciplina
  manifest_disciplines=()
  for sub in "${subdirs[@]}"; do
    disc=$(basename "$sub")
    count=$(copy_sorted "$sub" "$DST/$disc") || continue
    total=$((total + count))
    manifest_disciplines+=("$disc")
    echo "  $disc: $count imagens"
  done
  if [[ ${#manifest_disciplines[@]} -eq 0 ]]; then
    echo "Nenhuma imagem nas subpastas de $SRC" >&2
    exit 1
  fi
else
  # Modo plano: todas as imagens numa pasta só
  count=$(copy_sorted "$SRC" "$DST") || {
    echo "Nenhuma imagem em $SRC" >&2
    exit 1
  }
  total=$count
  manifest_disciplines=("geral")
  echo "  geral: $count imagens (pasta plana — informar disciplinas manualmente no manifest)"
fi

echo "Total: $total imagens copiadas para $DST"
echo "Disciplinas: ${manifest_disciplines[*]}"
