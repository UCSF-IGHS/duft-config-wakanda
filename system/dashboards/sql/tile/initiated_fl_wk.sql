SELECT SUM(first_line) AS initiated_on_art, PRINTF ('%.1f%%', SUM(first_line) * 100.0 /SUM(initiated_on_art)) AS percentage_initiated FROM vw_art_regimen_lines_for_tiles