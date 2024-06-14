/* .Sql => .txt (if export == True) */

Ex 1

Select nomstation,capacite from Stations
where capacite>200
ORDER by capacite

  SELECT nom, solde from clients
  where nom like 'J%' or solde > 10000
  order by solde desc
  
    select DISTINCT nomstation
    from Activites
    where libelle = 'Plongée'
    
      select nom from Clients
      join Sejours ON Clients.id = Sejours.idclient
      WHERE Station = 'La Bourboule'

        Select distinct stations from sejours as s 
        Join Client as c On c.id = s.IDClient 
        Where C.Region = 'Europe'
  
          /* variation double joint */
          Select DISTINCT nomstation
          from Stations
          join sejours On Sejours.station = Stations.nomstation
          join Clients On sejours.idclient = clients.id
          where Clients.region = 'Europe'
        
Ex 2
  
SELECT COUNT(*) AS Total
FROM SEJOURS
WHERE Station = 'Victoria';

/* output == 2 */

  SELECT AVG(Prix) AS 'Prix Moyen Activités Tanger'
  FROM ACTIVITES
  WHERE #NomStation = 'Tanger';

  /* output == null */ 

Ex 3
    
SELECT NomStation, Lieu, Tarif AS 'Tarif HT', Tarif * 1.20 AS 'Tarif TTC'
FROM STATIONS;
  /* 2) Non la colonne ajoutée est un affichage rajouternon pas une modification permanente */ 

Ex 4:

/* exe uniquement qu'une seule fois */
INSERT INTO CLIENTS (id, Nom, Prenom, Ville, Region, Solde)
VALUES (4/* id == 4 car 3 entité sont deja insérer dans la Table Clients */, 'Karibou', 'Juliette', 'Toronto', 'Canada', 7213);
INSERT INTO SEJOURS (IdClient, Station, Arrivee, NbPlaces)
VALUES (4, 'La Bourboule', '2019-07-10', 3);
  /* Non car dans l'état actuelle l'occurence de Juliette Karibou n'est pas présente dans la table activites */

Ex 5:

UPDATE STATIONS
SET Capacite = 450, Tarif = 2300
WHERE NomStation = 'Courchevel';

  /* Upadate function n'est pas compatible mais voici une façon de le faire */
  ALTER TABLE Activites
  RENAME COLUMN Prix TO Prix_HT;
  