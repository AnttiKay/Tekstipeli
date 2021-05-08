SELECT DISTINCT paikat.Name, paasee.suunta
FROM paikat, paasee
WHERE (paikat.PaikkaId, paasee.suunta) IN (
SELECT menee, suunta 
FROM paasee, paikat, pelihahmo 
WHERE tulee = paikat.PaikkaId 
and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id
);
