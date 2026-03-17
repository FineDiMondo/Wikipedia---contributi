#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF' >&2
Uso:
  ./scripts/nuovo-soggetto.sh -n "Nome Soggetto" -t biografia|famiglia [-v]
EOF
  exit 1
}

slugify() {
  printf '%s' "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | sed \
      -e 'y/àáâäãå/aaaaaa/' \
      -e 'y/èéêë/eeee/' \
      -e 'y/ìíîï/iiii/' \
      -e 'y/òóôöõ/ooooo/' \
      -e 'y/ùúûü/uuuu/' \
      -e 's/ç/c/g' \
      -e 's/ñ/n/g' \
      -e "s/[’']/ /g" \
      -e 's/[^a-z0-9]/-/g' \
      -e 's/-\{2,\}/-/g' \
      -e 's/^-//' \
      -e 's/-$//'
}

escape_sed() {
  printf '%s' "$1" | sed -e 's/[\/&]/\\&/g'
}

render_template() {
  local template_path="$1"
  local target_path="$2"

  local escaped_name escaped_type escaped_vivente escaped_ruolo escaped_contesto
  escaped_name="$(escape_sed "$NOME")"
  escaped_type="$(escape_sed "$TIPO")"
  escaped_vivente="$(escape_sed "$VIVENTE")"
  escaped_ruolo="$(escape_sed "$RUOLO_O_MOTIVO_DI_NOTORIETA")"
  escaped_contesto="$(escape_sed "$CONTESTO_STORICO_O_GEOGRAFICO")"

  sed \
    -e "s/{{NOME_SOGGETTO}}/${escaped_name}/g" \
    -e "s/{{TIPO_SOGGETTO}}/${escaped_type}/g" \
    -e "s/{{VIVENTE}}/${escaped_vivente}/g" \
    -e "s/{{RUOLO_O_MOTIVO_DI_NOTORIETA}}/${escaped_ruolo}/g" \
    -e "s/{{CONTESTO_STORICO_O_GEOGRAFICO}}/${escaped_contesto}/g" \
    "$template_path" > "$target_path"
}

NOME=""
TIPO=""
VIVENTE="no"
RUOLO_O_MOTIVO_DI_NOTORIETA="..."
CONTESTO_STORICO_O_GEOGRAFICO="..."

while getopts ":n:t:v" opt; do
  case "$opt" in
    n) NOME="$OPTARG" ;;
    t) TIPO="$OPTARG" ;;
    v) VIVENTE="si" ;;
    *) usage ;;
  esac
done

if [[ -z "$NOME" || -z "$TIPO" ]]; then
  usage
fi

if [[ "$TIPO" != "biografia" && "$TIPO" != "famiglia" ]]; then
  echo "Errore: -t deve essere 'biografia' oppure 'famiglia'." >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATES_DIR="$ROOT_DIR/templates"
SLUG="$(slugify "$NOME")"

if [[ -z "$SLUG" ]]; then
  echo "Errore: impossibile generare uno slug valido da '$NOME'." >&2
  exit 1
fi

TARGET_DIR="$ROOT_DIR/dossier/$SLUG"
if [[ -e "$TARGET_DIR" ]]; then
  echo "Errore: il dossier '$TARGET_DIR' esiste gia'." >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

if [[ "$TIPO" == "famiglia" ]]; then
  WIKI_TEMPLATE="bozza-famiglia.wiki"
else
  WIKI_TEMPLATE="bozza-biografia.wiki"
fi

render_template "$TEMPLATES_DIR/scheda.md" "$TARGET_DIR/scheda.md"
render_template "$TEMPLATES_DIR/fonti.md" "$TARGET_DIR/fonti.md"
render_template "$TEMPLATES_DIR/valutazione.md" "$TARGET_DIR/valutazione.md"
render_template "$TEMPLATES_DIR/$WIKI_TEMPLATE" "$TARGET_DIR/bozza.wiki"

printf 'Creato dossier: %s\n' "$TARGET_DIR"
