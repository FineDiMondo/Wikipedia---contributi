param(
    [Parameter(Mandatory = $true)]
    [string]$Nome,

    [ValidateSet("biografia", "famiglia")]
    [string]$Tipo = "biografia",

    [switch]$Vivente
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function ConvertTo-Slug {
    param([string]$Value)

    $normalized = $Value.Normalize([Text.NormalizationForm]::FormD)
    $chars = foreach ($c in $normalized.ToCharArray()) {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($c) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            $c
        }
    }

    $ascii = -join $chars
    $ascii = $ascii.ToLowerInvariant()
    $ascii = [Regex]::Replace($ascii, "[^a-z0-9]+", "-")
    $ascii = $ascii.Trim("-")

    if ([string]::IsNullOrWhiteSpace($ascii)) {
        throw "Impossibile generare uno slug valido da '$Value'."
    }

    return $ascii
}

function Render-Template {
    param(
        [string]$TemplatePath,
        [hashtable]$Tokens
    )

    $content = Get-Content -Path $TemplatePath -Raw
    foreach ($key in $Tokens.Keys) {
        $content = $content.Replace($key, $Tokens[$key])
    }

    return $content
}

$root = Split-Path -Parent $PSScriptRoot
$templates = Join-Path $root "templates"
$slug = ConvertTo-Slug -Value $Nome
$targetDir = Join-Path (Join-Path $root "dossier") $slug

if (Test-Path -Path $targetDir) {
    throw "Il dossier '$targetDir' esiste gia'."
}

New-Item -ItemType Directory -Path $targetDir | Out-Null

$tokens = @{
    "{{NOME_SOGGETTO}}" = $Nome
    "{{TIPO_SOGGETTO}}" = $Tipo
    "{{VIVENTE}}" = $(if ($Vivente.IsPresent) { "si" } else { "no" })
    "{{RUOLO_O_MOTIVO_DI_NOTORIETA}}" = "..."
    "{{CONTESTO_STORICO_O_GEOGRAFICO}}" = "..."
}

$files = @(
    @{ Source = "scheda.md"; Target = "scheda.md" },
    @{ Source = "fonti.md"; Target = "fonti.md" },
    @{ Source = "valutazione.md"; Target = "valutazione.md" },
    @{
        Source = $(if ($Tipo -eq "famiglia") { "bozza-famiglia.wiki" } else { "bozza-biografia.wiki" })
        Target = "bozza.wiki"
    }
)

foreach ($file in $files) {
    $templatePath = Join-Path $templates $file.Source
    $targetPath = Join-Path $targetDir $file.Target
    $rendered = Render-Template -TemplatePath $templatePath -Tokens $tokens
    Set-Content -Path $targetPath -Value $rendered -Encoding UTF8
}

Write-Output "Creato dossier: $targetDir"
