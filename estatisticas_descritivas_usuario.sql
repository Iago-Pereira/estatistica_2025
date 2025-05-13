WITH tb_usuario AS (
    SELECT idUsuario,
           SUM(qtdPontos) AS qtdPontos
    FROM points
    GROUP BY idUsuario
),

tb_subset_mediana AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM tb_usuario)
    OFFSET (SELECT 2 * count(*) / 4
            FROM tb_usuario)
),

tb_mediana AS (
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

tb_subset_quartil_1 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM tb_usuario)
    OFFSET (SELECT 1 * count(*) / 4
            FROM tb_usuario)
),

tb_quartil_1 AS (
    SELECT AVG(qtdPontos) As Quartil_1
    FROM tb_subset_quartil_1
),

tb_subset_quartil_3 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0
               FROM tb_usuario)
    OFFSET (SELECT 3 * count(*) / 4
            FROM tb_usuario)
),

tb_quartil_3 AS (
    SELECT AVG(qtdPontos) AS Quartil_3
    FROM tb_subset_quartil_3
),

tb_stats AS (
    SELECT MIN(qtdPontos) AS Minimo,
           AVG(qtdPontos) AS Media,
           MAX(qtdPontos) AS Maximo
    FROM tb_usuario
)

SELECT *
FROM tb_stats, tb_mediana, tb_quartil_1, tb_quartil_3