from scripts.db_utils import get_db_connection

def mass_enrichment():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Dataset Certificato (Wiki/Docs/ASPa)
    # Struttura: (id, description, notes)
    enrichment_data = [
        ('@I501@', 'Capostipite del ramo palermitano Giardina.', 'Matrimonio con Giulia Del Castillo (c. 1530) segna l\'ingresso nella nobiltà di servizio palermitana.'),
        ('@I502@', 'Nobile palermitano, figlio di Pietro.', 'Sposò una nobile della famiglia Corvino (XVI sec). Padre di Luigi Arias.'),
        ('@I505@', 'I Marchese di Santa Ninfa (1621), Fondatore della fortuna feudale.', 'Acquisto Rampinzeri (1605), Licentia Populandi Santa Ninfa (1609). Testamento rogato 2/05/1627 (ASPa, Notai Defunti, vol. 1201).'),
        ('@I116@', 'Barone di Gibellini, capostipite del ramo Gibellini-Lucchesi.', 'Sposò Vincenza Marquet (c. 1610), figlia di Guiscardo, collegando i Giardina ai baroni di Ucria.'),
        ('@I104@', 'I Principe di Ficarazzi (1733), protagonista dell\'ascesa della casata.', 'Vittoria lite successoria contro Napoli di Resuttano (1703). Sposò Giulia Massa (1703), dote utile per l\'acquisto di Ficarazzi.'),
        ('@I73@', 'Nobile dei Principi di Ficarazzi.', 'Unione con Emilia Grimaldi (1742) che porta il Principato di Santa Caterina in dote.'),
        ('@I57@', 'Nobile dei Principi di Ficarazzi e Santa Caterina.', 'Sposò Giuseppa Naselli (1775) dei Principi d\'Aragona.'),
        ('@I35@', 'Culmine titolare della casata (1831), detentore di 7 titoli nobiliari.', 'Sposò Maddalena Iaci (c. 1820), riunendo i rami Giardina e Iaci.'),
        ('@I504@', 'Avvocato delle Ferrovie dello Stato (ramo Giardina-Lipari).', 'Padre dei fratelli Marco (sindacalista) e Franco (militare).'),
        ('@I503@', 'Sottotenente carrista, martire della Resistenza.', 'Fucilato ad Arcole (12/09/1943). Laurea ad honorem alla memoria (UniPi, 1948).')
    ]
    
    # Update PERSON
    print("--- 1. ARRICCHIMENTO DESCRIZIONI E NOTE ---")
    update_query = "UPDATE PERSON SET description = %s, notes = %s WHERE person_id = %s"
    for pid, desc, notes in enrichment_data:
        cursor.execute(update_query, (desc, notes, pid))
        print(f"Aggiornato ID {pid}")

    # 2. Dataset Citazioni (Cross-Reference)
    # Struttura: (citation_id, source_id, person_id, page)
    citations = [
        (3001, 1004, '@I505@', 'Protonotaro, reg. 256, f. 112'), # Investitura S. Ninfa
        (3002, 1003, '@I505@', 'pp. 45-48'),                     # Documenti Ferrara
        (3003, 1002, '@I104@', 'vol. III, p. 308'),              # Ficarazzi SMS
        (3004, 1001, '@I35@', 'voce Giardina'),                  # Mango
        (3005, 1004, '@I104@', 'Sentenze Gran Corte, reg. 142')  # Lite 1703
    ]
    
    print("\n--- 2. INSERIMENTO CITAZIONI CERTIFICATE ---")
    cite_query = "INSERT INTO CITATION (citation_id, source_id, person_id, page_number) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE page_number = VALUES(page_number)"
    for c in citations:
        cursor.execute(cite_query, c)
        print(f"Citazione {c[0]} collegata a {c[2]}")

    conn.commit()
    print("\n[OK] Arricchimento DB completato con successo.")
    conn.close()

if __name__ == "__main__":
    mass_enrichment()
