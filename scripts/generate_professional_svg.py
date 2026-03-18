import base64

def generate_professional_svg():
    # Definizioni di stile e dimensioni
    width = 800
    height = 600
    padding = 40
    
    # Palette colori professionale
    color_principale = "#e6f2ff" # Blu chiaro
    stroke_principale = "#0056b3"
    color_estinto = "#ffe6e6"    # Rosso chiaro
    stroke_estinto = "#cc0000"
    color_lite = "#fff9e6"       # Arancio/Oro per la lite
    stroke_lite = "#e67e22"
    text_color = "#2c3e50"
    
    # Template SVG con font sans-serif e ombreggiature leggere
    svg = f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="2" />
            <feOffset dx="1" dy="1" result="offsetblur" />
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.2"/>
            </feComponentTransfer>
            <feMerge>
                <feMergeNode />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#7f8c8d" />
        </marker>
    </defs>
    
    <!-- Sfondo -->
    <rect width="100%" height="100%" fill="white" />
    
    <!-- Connessioni (Linee) -->
    <g stroke="#7f8c8d" stroke-width="1.5" fill="none">
        <!-- Luigi Arias -> Biforcazione -->
        <path d="M 400 100 L 400 130" marker-end="url(#arrowhead)" />
        <path d="M 400 130 L 200 130 L 200 160" marker-end="url(#arrowhead)" />
        <path d="M 400 130 L 600 130 L 600 160" marker-end="url(#arrowhead)" />
        
        <!-- Ramo Bellacera -->
        <path d="M 200 220 L 200 250" marker-end="url(#arrowhead)" />
        <path d="M 200 310 L 200 340" marker-end="url(#arrowhead)" />
        <path d="M 200 400 L 200 430" marker-end="url(#arrowhead)" />
        
        <!-- Ramo Gibellini -->
        <path d="M 600 220 L 600 250" marker-end="url(#arrowhead)" />
        <path d="M 600 310 L 600 340" marker-end="url(#arrowhead)" />
        
        <!-- Lite Successoria -> Luigi Gerardo -->
        <path d="M 200 490 L 200 520 L 600 520 L 600 400" stroke-dasharray="5,5" marker-end="url(#arrowhead)" />
        
        <!-- Grimaldi, Naselli, Iaci -->
        <path d="M 600 400 L 600 430" marker-end="url(#arrowhead)" />
        <path d="M 600 490 L 600 520" marker-end="url(#arrowhead)" />
    </g>

    <!-- Nodi -->
    
    <!-- Livello 0 -->
    <g filter="url(#shadow)">
        <rect x="300" y="40" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="2" />
        <text x="400" y="65" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{text_color}">LUIGI ARIAS GIARDINA</text>
        <text x="400" y="85" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{text_color}">I Marchese S. Ninfa (1621)</text>
    </g>

    <!-- Livello 1: Ramo Bellacera -->
    <g filter="url(#shadow)">
        <rect x="100" y="160" width="200" height="60" rx="5" fill="{color_estinto}" stroke="{stroke_estinto}" stroke-width="2" />
        <text x="200" y="185" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{text_color}">RAMO BELLACERA</text>
        <text x="200" y="205" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{text_color}">(Orsola Giardina)</text>
    </g>

    <!-- Livello 1: Ramo Gibellini -->
    <g filter="url(#shadow)">
        <rect x="500" y="160" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="2" />
        <text x="600" y="185" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{text_color}">RAMO GIBELLINI</text>
        <text x="600" y="205" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{text_color}">(Diego Giardina)</text>
    </g>

    <!-- Evoluzione Bellacera -->
    <g filter="url(#shadow)">
        <rect x="100" y="250" width="200" height="60" rx="5" fill="{color_estinto}" stroke="{stroke_estinto}" stroke-width="1" />
        <text x="200" y="275" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{text_color}">SIMONE II BELLACERA</text>
        <text x="200" y="295" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="{text_color}">P.pe di Monteleone (1671)</text>
        
        <rect x="100" y="340" width="200" height="60" rx="5" fill="{color_estinto}" stroke="{stroke_estinto}" stroke-width="1" />
        <text x="200" y="375" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{text_color}">GIUSEPPE BELLACERA</text>
        <text x="200" y="390" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{stroke_estinto}">† 1699 (Estinzione)</text>
    </g>

    <!-- Lite Successoria -->
    <g filter="url(#shadow)">
        <rect x="100" y="430" width="200" height="60" rx="5" fill="{color_lite}" stroke="{stroke_lite}" stroke-width="2" stroke-dasharray="4" />
        <text x="200" y="455" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{text_color}">LITE SUCCESSORIA</text>
        <text x="200" y="475" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{text_color}">1699 – 1703</text>
    </g>

    <!-- Evoluzione Gibellini / Ficarazzi -->
    <g filter="url(#shadow)">
        <rect x="500" y="250" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="1" />
        <text x="600" y="285" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{text_color}">DIEGO GIARDINA</text>
        
        <rect x="500" y="340" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="2" />
        <text x="600" y="365" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{text_color}">LUIGI GERARDO GIARDINA</text>
        <text x="600" y="385" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="{text_color}">I Principe di Ficarazzi (1733)</text>
    </g>

    <!-- Biforcazioni Matrimoniali -->
    <g filter="url(#shadow)">
        <rect x="500" y="430" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="1" />
        <text x="600" y="455" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{text_color}">RAMO GRIMALDI / NASELLI</text>
        <text x="600" y="475" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{text_color}">P.pe Santa Caterina (1742)</text>
        
        <rect x="500" y="520" width="200" height="60" rx="5" fill="{color_principale}" stroke="{stroke_principale}" stroke-width="2" />
        <text x="600" y="545" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{text_color}">ANTONINO GIARDINA-IACI</text>
        <text x="600" y="565" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{text_color}">Culmine Titolare (1831)</text>
    </g>

    <!-- Legenda -->
    <rect x="40" y="500" width="150" height="80" rx="5" fill="white" stroke="#bdc3c7" stroke-width="1" />
    <rect x="50" y="515" width="15" height="15" fill="{color_principale}" stroke="{stroke_principale}" />
    <text x="75" y="527" font-family="Arial, sans-serif" font-size="10" fill="{text_color}">Linea Principale</text>
    <rect x="50" y="535" width="15" height="15" fill="{color_estinto}" stroke="{stroke_estinto}" />
    <text x="75" y="547" font-family="Arial, sans-serif" font-size="10" fill="{text_color}">Linea Estinta</text>
    <rect x="50" y="555" width="15" height="15" fill="{color_lite}" stroke="{stroke_lite}" />
    <text x="75" y="567" font-family="Arial, sans-serif" font-size="10" fill="{text_color}">Transizione Legale</text>

</svg>
"""
    return svg

if __name__ == "__main__":
    with open("docs/manuali/files_extracted/biforcazioni_giardina_diagram.svg", "w", encoding="utf-8") as f:
        f.write(generate_professional_svg())
    print("SVG Professionale generato con successo in docs/manuali/files_extracted/biforcazioni_giardina_diagram.svg")
