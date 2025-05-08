WITH tb_freq_abs AS(
    
    SELECT descProduto,
        count(idTransacao) AS FreqAbs

 FROM points

 GROUP BY descProduto

),

tb_freq_abs_cum AS(
    
    SELECT *,
            sum(FreqAbs) OVER (ORDER BY descProduto) AS FreqAbsAcum,
            1.0 * FreqAbs / (SELECT sum(FreqAbs) FROM tb_freq_abs) AS FreqRel

        FROM tb_freq_abs

)

SELECT *,
        sum(FreqRel) OVER (ORDER BY descProduto) AS FreqRelAcum

FROM tb_freq_abs_cum