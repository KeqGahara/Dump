SELECT titre FROM FILM WHERE titre LIKE 'M%[rs]';

SELECT titre FROM FILM WHERE annee BETWEEN 2002 AND 2004;

SELECT nom, naissance FROM PERSONNE WHERE nom LIKE 'Ro%' AND pays = 'France' ORDER BY nom;

SELECT MIN(annee) AS "Film le plus ancien", MAX(annee) AS "Film le plus récent" FROM FILM;

SELECT AVG(nbSpectateurs) FROM FILM;

SELECT g.nomG, COUNT() FROM FILM f INNER JOIN GENRE g ON f.idGenre = g.idGenre GROUP BY g.nomG ORDER BY COUNT() DESC;

SELECT f.titre FROM FILM f INNER JOIN JOUE j ON f.idFilm = j.idFilm GROUP BY f.idFilm HAVING AVG(j.salaire) > 2000000 ORDER BY AVG(j.salaire) DESC;

SELECT SUM(nbSpectateurs) * 8 AS "Recette totale" FROM FILM f INNER JOIN PERSONNE p ON f.idRealisateur = p.idPersonne WHERE p.pays = 'USA' AND f.annee = 2010;

SELECT f.titre, COUNT(*) AS nbActeurs FROM FILM f INNER JOIN JOUE j ON f.idFilm = j.idFilm GROUP BY f.idFilm ORDER BY nbActeurs DESC LIMIT 10;

///

