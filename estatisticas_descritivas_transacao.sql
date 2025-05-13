WITH tb_subset_mediana AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM points)
    OFFSET (SELECT 2 * count(*) / 4
            FROM points)
),

tb_mediana AS (
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

tb_subset_quartil_1 AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM points)
    OFFSET (SELECT 1 * count(*) / 4
            FROM points)
),

tb_quartil_1 AS (
    SELECT AVG(qtdPontos) As Quartil_1
    FROM tb_subset_quartil_1
),

tb_subset_quartil_3 AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM points)
    OFFSET (SELECT 3 * count(*) / 4
            FROM points)
),

tb_quartil_3 AS (
    SELECT AVG(qtdPontos) AS Quartil_3
    FROM tb_subset_quartil_3
),

tb_stats AS (
    SELECT MIN(qtdPontos) AS Minimo,
           AVG(qtdPontos) AS Media,
           MAX(qtdPontos) AS Maximo
    FROM points
)

SELECT *
FROM tb_stats, tb_mediana, tb_quartil_1, tb_quartil_3