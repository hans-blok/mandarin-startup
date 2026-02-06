"""
Hypothese-vormer Agent — Formuleer Hypothese

Implementeert de logica uit het agent-contract en de charter.
Logt automatisch alle lees- en schrijfacties via mandarin_agent_runner.py.
"""

import sys
import subprocess
from datetime import datetime
from pathlib import Path
import argparse
import re

# --- Logging helper ---
def log_agent_action(agent_naam, gelezen=None, aangepast=None, aangemaakt=None):
    cmd = [
        sys.executable, "scripts/mandarin_agent_runner.py", agent_naam
    ]
    if gelezen:
        cmd += ["--gelezen"] + list(gelezen)
    if aangepast:
        cmd += ["--aangepast"] + list(aangepast)
    if aangemaakt:
        cmd += ["--aangemaakt"] + list(aangemaakt)
    subprocess.run(cmd, check=True)

# --- Hypothese generator ---
def formuleer_hypothese(thema_epic, probleemruimte, status_quo, verbetering, aannames, positionering):
    datum = datetime.now().strftime("%Y-%m-%d")
    md = f"""# Hypothese — Probleemkader {thema_epic}

**Thema/Epic**: {thema_epic}
**Datum**: {datum}

## Hypothese
Wij geloven dat {verbetering}\nbeter is dan {status_quo},\nomdat {probleemruimte}.

## Aannames (max 3, als risico’s)
"""
    for i, aanname in enumerate(aannames, 1):
        md += f"{i}. {aanname}\n"
    md += f"\n## Positionering\n{positionering}\n"
    return md

# --- Main CLI ---
def parse_markdown_input(md_path):
    content = Path(md_path).read_text(encoding="utf-8")
    # Zoek kopjes en inhoud
    fields = {
        'thema-epic': '',
        'probleemruimte': '',
        'status-quo': '',
        'verbetering': '',
        'aanname': [],
        'positionering': ''
    }
    current = None
    for line in content.splitlines():
        h = re.match(r"^#+\s*(.+)", line)
        if h:
            key = h.group(1).strip().lower()
            if 'thema' in key:
                current = 'thema-epic'
            elif 'probleemruimte' in key:
                current = 'probleemruimte'
            elif 'status' in key:
                current = 'status-quo'
            elif 'verbetering' in key:
                current = 'verbetering'
            elif 'aanname' in key:
                current = 'aanname'
            elif 'positionering' in key:
                current = 'positionering'
            else:
                current = None
        elif current:
            if current == 'aanname':
                m = re.match(r"^[-*\d+\.]\s*(.+)", line)
                if m:
                    fields['aanname'].append(m.group(1).strip())
            else:
                if line.strip():
                    if fields[current]:
                        fields[current] += " " + line.strip()
                    else:
                        fields[current] = line.strip()
    return fields

def main():
    parser = argparse.ArgumentParser(description="Formuleer een hypothese volgens het Click-format.")
    parser.add_argument("--input-md", help="Pad naar markdownbestand met velden als kopjes")
    parser.add_argument("--thema-epic")
    parser.add_argument("--probleemruimte")
    parser.add_argument("--status-quo")
    parser.add_argument("--verbetering")
    parser.add_argument("--aanname", action="append", help="Max 3 aannames, als risico's")
    parser.add_argument("--positionering")
    parser.add_argument("--output", default=None, help="Pad voor outputbestand")
    args = parser.parse_args()

    if args.input_md:
        fields = parse_markdown_input(args.input_md)
        thema_epic = fields['thema-epic'] or args.thema_epic
        probleemruimte = fields['probleemruimte'] or args.probleemruimte
        status_quo = fields['status-quo'] or args.status_quo
        verbetering = fields['verbetering'] or args.verbetering
        aannames = fields['aanname'] or (args.aanname or [])
        positionering = fields['positionering'] or args.positionering
    else:
        thema_epic = args.thema_epic
        probleemruimte = args.probleemruimte
        status_quo = args.status_quo
        verbetering = args.verbetering
        aannames = args.aanname or []
        positionering = args.positionering

    # Genereer hypothese
    hypothese_md = formuleer_hypothese(
        thema_epic,
        probleemruimte,
        status_quo,
        verbetering,
        aannames,
        positionering
    )

    # Outputbestand bepalen
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(f"artefacten/hypothese-vormer/hypothese-probleemkader-{thema_epic}-{datetime.now().strftime('%Y%m%d')}.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(hypothese_md, encoding="utf-8")

    # Logging uitvoeren
    log_agent_action(
        agent_naam="hypothese-vormer",
        gelezen=[args.input_md] if args.input_md else [],
        aangepast=[],
        aangemaakt=[str(output_path)]
    )
    print(f"Hypothese opgeslagen in: {output_path}")

if __name__ == "__main__":
    main()
