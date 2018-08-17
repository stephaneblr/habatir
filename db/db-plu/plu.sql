-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Hôte : aloadecotp47.mysql.db
-- Généré le :  mar. 14 août 2018 à 18:01
-- Version du serveur :  5.6.39-log
-- Version de PHP :  5.6.36

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `aloadecotp47`
--

-- --------------------------------------------------------

--
-- Structure de la table `ENTREE_GRAPHIQUE`
--

CREATE TABLE `ENTREE_GRAPHIQUE` (
  `id-entree-graphique` int(2) DEFAULT NULL,
  `label-entree-graphique` varchar(167) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `ENTREE_GRAPHIQUE`
--

INSERT INTO `ENTREE_GRAPHIQUE` (`id-entree-graphique`, `label-entree-graphique`) VALUES
(1, 'Zone d\'interdiction reportée sur le document graphiue n°1, liée aux conduites de gaz'),
(2, 'Sentes et itinéraires identifiées sur le document graphique n°2'),
(3, 'Terrains proche des arbres remarquables identifiés au titre de l’article L.123-1-5 III 2°'),
(4, 'Espaces boisés classés'),
(5, 'La Grande Rue (entre le n°60 et le n°120 côtés pair et impair) et la rue Pierre Midrin'),
(6, 'Lisière de 10 mètres mesurée à partir de la limite des massifs boisés identifiés sur le document graphique n°1'),
(7, 'Zone des anciennes carrières '),
(8, 'Terrains dont l’alignement est identifié sur le document graphique n°1 par un trait plein'),
(9, 'Terrains dont l’alignement est identifié sur le document graphique n°1 par un trait pointillé'),
(10, 'Limite du secteur UCV1 avec la zone UR2'),
(11, 'Limite du secteur UCV2 avec la zone UR2'),
(12, 'Terrains comportant au moins une façade sur rue identifiée sur le document graphique n°2 au titre de l’article L.123-1-5 III 2° du code de l’urbanisme.'),
(13, 'Constructions et façades sur rue repérées sur le document graphique n°2 au titre des dispositions l’article L 123-1-5 III 2° du code de l’urbanisme'),
(14, 'Les terrains dont les façades sur rue sont identifiées sur le document graphique n°2 par un liseré plein au titre de l’article L. 123-1-5 III 2° du code de l’urbanisme');

-- --------------------------------------------------------

--
-- Structure de la table `PATH`
--

CREATE TABLE `PATH` (
  `id-path` int(3) DEFAULT NULL,
  `id-parent-path` int(3) DEFAULT NULL,
  `reference-path` varchar(8) DEFAULT NULL,
  `label-path` varchar(143) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `PATH`
--

INSERT INTO `PATH` (`id-path`, `id-parent-path`, `reference-path`, `label-path`) VALUES
(1, 0, '0', 'Some dummy title\r'),
(2, 1, '', 'Risques liés au transport de matière dangereuse\r'),
(3, 1, '', 'Les sentes et itinéraires identifiés au titre de l’article L.123-1-5 IV 1° du code de l’urbanisme\r'),
(4, 1, '0.1', 'Some dummy title\r'),
(5, 1, '0.2', 'Some dummy title\r'),
(6, 1, '0.3', 'Some dummy title\r'),
(7, 0, '1', 'Some dummy title\r'),
(8, 7, '1.1', 'Some dummy title\r'),
(9, 7, '1.2', 'Some dummy title\r'),
(10, 7, '1.3', 'Some dummy title\r'),
(11, 10, '1.3.1', 'Some dummy title\r'),
(12, 10, '1.3.2', 'Some dummy title\r'),
(13, 10, '1.3.3', 'Some dummy title\r'),
(14, 13, '1.3.3.1', 'Some dummy title\r'),
(15, 13, '1.3.3.2', 'Some dummy title\r'),
(16, 7, '1.4', 'Some dummy title\r'),
(17, 16, '1.4.1', 'Some dummy title\r'),
(18, 16, '1.4.2', 'Some dummy title\r'),
(19, 18, '1.4.2.1', 'Some dummy title\r'),
(20, 18, '1.4.2.2', 'Some dummy title\r'),
(21, 16, '1.4.3', 'Some dummy title\r'),
(22, 16, '1.4.4', 'Some dummy title\r'),
(23, 7, '1.5', 'Some dummy title\r'),
(24, 7, '1.6', 'Some dummy title\r'),
(25, 24, '1.6.1', 'Some dummy title\r'),
(26, 24, '1.6.2', 'Some dummy title\r'),
(27, 26, '1.6.2.1', 'Some dummy title\r'),
(28, 26, '1.6.2.2', 'Some dummy title\r'),
(29, 26, '1.6.2.3', 'Some dummy title\r'),
(30, 26, '1.6.2.4', 'Some dummy title\r'),
(31, 26, '1.6.2.5', 'Some dummy title\r'),
(32, 26, '1.6.2.6', 'Some dummy title\r'),
(33, 7, '1.7', 'Some dummy title\r'),
(34, 33, '1.7.1', 'Some dummy title\r'),
(35, 34, '1.7.1.1', 'Some dummy title\r'),
(36, 34, '1.7.1.2', 'Some dummy title\r'),
(37, 34, '1.7.1.3', 'Some dummy title\r'),
(38, 33, '1.7.2', 'Some dummy title\r'),
(39, 38, '1.7.2.1', 'Some dummy title\r'),
(40, 38, '1.7.2.2', 'Some dummy title\r'),
(41, 38, '1.7.2.3', 'Some dummy title\r'),
(42, 38, '1.7.2.4', 'Some dummy title\r'),
(43, 38, '1.7.2.5', 'Some dummy title\r'),
(44, 7, '1.8', 'Some dummy title\r'),
(45, 44, '1.8.1', 'Some dummy title\r'),
(46, 44, '1.8.2', 'Some dummy title\r'),
(47, 7, '1.9', 'Some dummy title\r'),
(48, 47, '1.9.1', 'Some dummy title\r'),
(49, 47, '1.9.2', 'Some dummy title\r'),
(50, 7, '1.10', 'Some dummy title\r'),
(51, 50, '1.10.1', 'Some dummy title\r'),
(52, 51, '1.10.1.1', 'Some dummy title\r'),
(53, 51, '1.10.1.2', 'Some dummy title\r'),
(54, 51, '1.10.1.3', 'Some dummy title\r'),
(55, 51, '1.10.1.4', 'Some dummy title\r'),
(56, 50, '1.10.2', 'Some dummy title\r'),
(57, 56, '1.10.2.1', 'Some dummy title\r'),
(58, 56, '1.10.2.2', 'Some dummy title\r'),
(59, 56, '1.10.2.3', 'Some dummy title\r'),
(60, 56, '1.10.2.4', 'Some dummy title\r'),
(61, 56, '1.10.2.5', 'Some dummy title\r'),
(62, 7, '1.11', 'Some dummy title\r'),
(63, 62, '1.11.1', 'Some dummy title\r'),
(64, 63, '1.11.1.1', 'Some dummy title\r'),
(65, 64, '', 'Toitures\r'),
(66, 64, '', 'Façades\r'),
(67, 64, '', 'Façades commerciales\r'),
(68, 63, '1.11.1.2', 'Some dummy title\r'),
(69, 68, '', 'Les descentes d’eaux pluviales\r'),
(70, 68, '', 'Les rampes de parking\r'),
(71, 68, '', 'Les édicules et gaines techniques\r'),
(72, 68, '', 'Le dévoiement des conduits de cheminée\r'),
(73, 68, '', 'Les antennes\r'),
(74, 68, '', 'Les panneaux solaires ou photovoltaîques\r'),
(75, 63, '1.11.1.3', 'Some dummy title\r'),
(76, 62, '1.11.2', 'Some dummy title\r'),
(77, 76, '', 'Les dispositions particulières applicables aux constructions existantes en zone UCV1\r'),
(78, 76, '', 'Les constructions et façades sur rues repérées sur le document graphique n°2 au titre des dispositions L 123-1-5 III 2° du code de l’urbanisme\r'),
(79, 7, '1.12', 'Some dummy title\r'),
(80, 79, '1.12.1', 'Some dummy title\r'),
(81, 80, '1.12.1.1', 'Some dummy title\r'),
(82, 80, '1.12.1.2', 'Some dummy title\r'),
(83, 82, '', 'Pour les constructions à destination de bureau\r'),
(84, 82, '', 'Pour les constructions à destination d’habitation\r'),
(85, 82, '', 'Pour les constructions à destination de commerce\r'),
(86, 82, '', 'Pour les constructions à destination d’artisanat\r'),
(87, 82, '', 'Pour les constructions à destination d’hébergement hôtelier\r'),
(88, 82, '', 'Pour les constructions et installations nécessaires aux services publics ou d’intérêt collectif\r'),
(89, 80, '1.12.1.3', 'Some dummy title\r'),
(90, 79, '1.12.2', 'Some dummy title\r'),
(91, 79, '1.12.3', 'Some dummy title\r'),
(92, 79, '1.12.4', 'Some dummy title\r'),
(93, 7, '1.13', 'Some dummy title\r'),
(94, 93, '1.13.1', 'Some dummy title\r'),
(95, 93, '1.13.2', 'Some dummy title\r'),
(96, 95, '1.13.2.1', 'Some dummy title\r'),
(97, 95, '1.13.2.2', 'Some dummy title\r'),
(98, 93, '1.13.3', 'Some dummy title\r'),
(99, 93, '1.13.4', 'Some dummy title\r'),
(100, 7, '1.14', 'Some dummy title\r'),
(101, 7, '1.15', 'Some dummy title\r'),
(102, 101, '1.15.1', 'Some dummy title\r'),
(103, 101, '1.15.2', 'Some dummy title\r'),
(104, 7, '1.16', 'Some dummy title');

-- --------------------------------------------------------

--
-- Structure de la table `REGLE_ALTERNATIVE_L1`
--

CREATE TABLE `REGLE_ALTERNATIVE_L1` (
  `id_option` int(1) DEFAULT NULL,
  `regle` int(3) DEFAULT NULL,
  `alternative` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `REGLE_ALTERNATIVE_L1`
--

INSERT INTO `REGLE_ALTERNATIVE_L1` (`id_option`, `regle`, `alternative`) VALUES
(1, 36, 37),
(2, 83, 85),
(2, 84, 85),
(2, 83, 86),
(2, 84, 86),
(3, 88, 89),
(4, 175, 176),
(4, 175, 177),
(5, 206, 215),
(5, 207, 215),
(5, 208, 215),
(5, 209, 215),
(5, 210, 215),
(5, 211, 215),
(5, 212, 215),
(5, 213, 215),
(5, 214, 215),
(5, 206, 216),
(5, 206, 217),
(5, 206, 218),
(5, 206, 219),
(5, 206, 220),
(5, 206, 221),
(5, 206, 222),
(5, 206, 223),
(5, 207, 216),
(5, 207, 217),
(5, 207, 218),
(5, 207, 219),
(5, 207, 220),
(5, 207, 221),
(5, 207, 222),
(5, 207, 223),
(5, 208, 216),
(5, 208, 217),
(5, 208, 218),
(5, 208, 219),
(5, 208, 220),
(5, 208, 221),
(5, 208, 222),
(5, 208, 223),
(5, 209, 216),
(5, 209, 217),
(5, 209, 218),
(5, 209, 219),
(5, 209, 220),
(5, 209, 221),
(5, 209, 222),
(5, 209, 223),
(5, 210, 216),
(5, 210, 217),
(5, 210, 218),
(5, 210, 219),
(5, 210, 220),
(5, 210, 221),
(5, 210, 222),
(5, 210, 223),
(5, 211, 216),
(5, 211, 217),
(5, 211, 218),
(5, 211, 219),
(5, 211, 220),
(5, 211, 221),
(5, 211, 222),
(5, 211, 223),
(5, 212, 216),
(5, 212, 217),
(5, 212, 218),
(5, 212, 219),
(5, 212, 220),
(5, 212, 221),
(5, 212, 222),
(5, 212, 223),
(5, 213, 216),
(5, 213, 217),
(5, 213, 218),
(5, 213, 219),
(5, 213, 220),
(5, 213, 221),
(5, 213, 222),
(5, 213, 223),
(5, 214, 216),
(5, 214, 217),
(5, 214, 218),
(5, 214, 219),
(5, 214, 220),
(5, 214, 221),
(5, 214, 222),
(5, 214, 223);

-- --------------------------------------------------------

--
-- Structure de la table `TEXTE`
--

CREATE TABLE `TEXTE` (
  `id-texte` int(3) DEFAULT NULL,
  `texte` varchar(2970) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `TEXTE`
--

INSERT INTO `TEXTE` (`id-texte`, `texte`) VALUES
(1, '<div class=\"txt\">                 Le présent Plan Local d’Urbanisme s\'applique à l\'ensemble du territoire communal de Sèvres.                <br/><br/></div>'),
(2, '<div class=\"txt\">                     La commune de Sèvres est concernée par trois canalisations sous pression de matières dangereuses, réglementées par un arrêté ministériel en date du 4 août 2006 (voir la fiche d’information et la carte des canalisations de gaz, annexées au PLU).                     <br/><br/></div>'),
(3, '<div class=\"txt\">                     Dans la zone d’interdiction reportée sur le document graphique n°1 sont interdits :                    <ul><li>les constructions et installations nécessaires au fonctionnement du service public ou d’intérêt collectif recevant plus de 100 personnes ;</li><li>les immeubles de grande hauteur.</li></ul><br/></div>'),
(4, '<div class=\"txt\">                     Dans la zone intermédiaire reportée sur le document graphique, l’aménageur ou le constructeur de chaque projet devra s’assurer que les conditions de sécurité sont suffisantes au regard des risques présentés. La mise en œuvre de mesures compensatoires destinées à réduire l’emprise de cette zone est à privilégier. Cependant, malgré la mise en place de mesures compensatoires et dans certaines conditions, la construction ou l’extension d’immeubles de grande hauteur ou de constructions et installations nécessaires au fonctionnement du service public ou d’intérêt collectif recevant plus de 100 personnes peut être interdite. La consultation des services de la DRIRE sera effectuée par la collectivité. Dans la zone justifiant une vigilance et une information, le transporteur sera informé de tout projet par la collectivité.                    <br/><br/></div>'),
(5, '<div class=\"txt\">                     Afin de prévenir les risques d’endommagement des canalisations de transport, les travaux doivent être conduits dans le respect de la procédure de DT/DICT définie par le Décret modifié n°2011-1241 du 5 octobre 2011.                    <br/><br/></div>'),
(6, '<div class=\"txt\">                     Toutes constructions et installations y compris les clôtures, portails et portillons sont interdites dans les sentes et itinéraires identifiés sur le document graphique n° 2 au titre de l’article L.123-1-5 IV1° du code de l’urbanisme afin d’assurer leur préservation.                    <br/><br/></div>'),
(7, '<div class=\"txt\">                     Sous réserve des dispositions du présent règlement, lorsqu\'une construction existante n\'est pas conforme aux dispositions applicables dans la zone où elle se situe, l\'autorisation d\'exécuter des travaux ne peut être accordée que pour des travaux qui n\'aggravent pas la non-conformité de la construction avec ces dispositions, ou qui sont sans effet à leur égard.                    <br/><br/></div>'),
(8, '<div class=\"txt\">                            Le règlement du PLU définit les règles d’occupation du sol. Toutefois, s’appliquent en plus et indépendamment du présent règlement, les articles R. 111-2, R. 111-4, R. 111-15 et R. 111-21 du code de l’urbanisme.                        </div>'),
(9, '<div class=\"txt\">                            Par ailleurs, sont et demeurent applicables sur le territoire communal, les dispositions du code de l’urbanisme suivantes :                            <ul><li>l’article L. 111-10 relatif aux périmètres de travaux publics ;</li><li>les articles L. 111-9 et L. 421-4 relatifs aux périmètres de déclaration d’utilité publique ;</li><li>l’article L. 421-5 relatif à la réalisation de réseaux ;</li><li>l’article L. 111-1-4 relatif aux routes à grande circulation.</li></ul></div>'),
(10, '<div class=\"txt\">                            Aux règles énoncées par le présent PLU s’ajoutent :                            <ul><li>les servitudes d’utilité publique qui font l’objet d’un plan et d’une notice annexés au présent dossier de PLU, notamment le plan de prévention des risques d’inondation (PPRI) et les risques liés à la présence d’anciennes carrières.</li><li>es périmètres de droit de préemption urbain instaurés par délibération du conseil municipal annexée au présent PLU.</li></ul></div>'),
(11, '<div class=\"txt\">                            Les prescriptions prises au titre des autres législations spécifiques concernant l’occupation ou l’utilisation des sols s’ajoutent aux règles propres au PLU.                        </div>'),
(12, '<div class=\"txt\">                            Au titre de la règlementation sur l’archéologie préventive, toute découverte fortuite de vestiges susceptibles de présenter un caractère archéologique doit faire l’objet d’une déclaration immédiate au maire.                        </div>'),
(13, '<div class=\"txt\">                            Les dispositifs de réutilisation des eaux pluviales à usage domestique devront être conformes à la règlementation en vigueur (arrêté du 21 août 2008 relatif à la récupération des eaux de pluie et à leur usage à l’intérieur et à l’extérieur des bâtiments).                        </div>'),
(14, '<div class=\"txt\">                            Le surplomb du domaine public par des constructions nécessite une autorisation délivrée par l’autorité gestionnaire du domaine public en application des dispositions du code de la voirie routière et de celles du code de la construction et de l’habitation.                        </div>'),
(15, '<div class=\"txt\">                            La SNCF doit être consultée pour toutes les demandes de permis de construire ou de permis d’aménager jouxtant la plate-forme ferroviaire.                        </div>'),
(16, '<div class=\"txt\">                     Le territoire couvert par le Plan Local d’Urbanisme est divisé en zones urbaines et zones naturelles.                    <br/><br/></div>'),
(17, '<div class=\"txt\">                     Les zones urbaines, auxquelles s\'appliquent les dispositions du présent règlement, sont repérées sur le document graphique n°1 par un indice commençant par la lettre U.                    <br/><br/></div>'),
(18, '<div class=\"txt\">                     Ce sont les zones :                    <ul><li>UCV : centre-ville ;</li><li>UR : zone résidentielle ;</li><li>UAE : zone à vocation d’activités économiques et d’équipements.</li></ul><br/></div>'),
(19, '<div class=\"txt\">                     Les zones naturelles et forestières, auxquelles s’appliquent les dispositions du présent règlement, sont repérées sur le document graphique n°1 par l’indice N.                    <br/><br/></div>'),
(20, '<div class=\"txt\">                     N : zone naturelle et forestière.                    <br/><br/></div>'),
(21, '<div class=\"txt\">                     Les emplacements réservés aux voies et ouvrages publics, aux installations d\'intérêt général et aux espaces verts au titre de l’article L.123-1-5 V du code de l’urbanisme sont inscrits dans les documents graphiques n°1 et n°3.                    <br/><br/></div>'),
(22, '<div class=\"txt\">                     Les terrains classés comme espaces boisés classés au titre de l’article L.130-1 du code de l’urbanisme sont identifiés sur les documents graphiques n°1et n°2.                    <br/><br/></div>'),
(23, '<div class=\"txt\">                     Les alignements d’arbres et les arbres remarquables à protéger, le bâti et les espaces publics remarquables à protéger au titre de l’article L.123-1-5 III 2° du code de l’urbanisme sont identifiés sur le document graphique n°2.                    <br/><br/></div>'),
(24, '<div class=\"txt\">                     Trois orientations d’aménagement et de programmation complètent les dispositions réglementaires sur certains secteurs de la ville :                    <ul><li>le centre-ville ;</li><li>les berges de la Seine ;</li><li>le quartier des Bruyères.</li></ul><br/></div>'),
(25, '<div class=\"txt\">                     La zone UCV correspond au centre-ville de Sèvres. Multifonctionnelle, elle accueille de l\'habitat, des services et des activités économiques de centre-ville, tels que des commerces, des bureaux, des services publics et privés. Les commerces et services doivent pouvoir s’y développer en complément des équipements publics et des logements.                    <br/><br/></div>'),
(26, '<div class=\"txt\">                     Largement bâtie, elle présente deux catégories de formes urbaines, qui font l’objet de deux secteurs :                    <ul><li>Secteur UCV1 : ilots correspondant au bâti ancien traditionnel de centre-ville,</li><li>Secteur UCV2 : ilots déjà largement bâtis, issus de la rénovation urbaine ou accueillant des constructions édifiées récemment, dont les formes urbaines sont très structurées et la densité importante. Un sous-secteur UCV2a, où la hauteur des constructions est réduite, a été identifié.</li></ul><br/></div>'),
(27, '<div class=\"txt\">                         Sont interdits :                        <ul><li>Les bâtiments à destination d’exploitation agricole ;</li><li>L’aménagement de terrain de camping et de caravaning ;</li><li>Les dépôts de ferrailles, matériaux, véhicules désaffectés, combustibles solides ou liquides, déchets (tels que pneus usés, vieux chiffons, ordures), ainsi que les entreprises de cassage de voitures ;</li><li>Les exhaussements et affouillements du sol à l’exception de ceux indispensables pour la réalisation des types d’occupation ou d’utilisation du sol autorisés ;</li>                            Les exploitations de carrières, nécessitant une autorisation au titre des articles R. 421-19 et R.421-23 du code de l’urbanisme ;                            <li>Les constructions à destination industrielle et les entrepôts ;</li></ul><br/></div>'),
(28, '<div class=\"txt\">                         Au titre de l’article L.123-1-5 II 5° du code de l’urbanisme, la Grande Rue (entre le n°60 et le n°120 côtés pair et impair) et la rue Pierre Midrin sont identifiées comme axes le long desquels la diversité commerciale et artisanale doit être protégée. Le long de ces axes, est interdit le changement de destination des locaux commerciaux et des locaux artisanaux existants situés à rez-de-chaussée en une destination autre que le commerce et l’artisanat.                        <br/><br/></div>'),
(29, '<div class=\"txt\">                         Sont également admises sous conditions, les occupations et utilisations du sol suivantes :                        <ul><li>Au titre de l’article L.123-1-5 II 4° du code de l’urbanisme, les opérations de construction de logements comportant plus de 400 m2 de surface de plancher et/ou au moins 10 logements, doivent comporter au minimum 25% de logements locatifs sociaux, calculés sur le nombre total de logements.</li><li>Dans la lisière de 10 mètres mesurée à partir de la limite des massifs boisés identifiés sur le document graphique n°1, sont uniquement autorisées les annexes dont l’emprise au sol totale n’excède pas 15 m2, et dont la hauteur maximale est limitée à 3,50 mètres, mesurée conformément à l’article UCV 10-1.</li></ul><br/></div>'),
(30, '<div class=\"txt\">                         Pour être constructible ou aménageable, un terrain doit être accessible par une voie carrossable publique ou privée en bon état de viabilité, soit directement, soit, le cas échéant, par l’intermédiaire d’une servitude de passage sur fonds voisin, consentie ou obtenue par l’application de l’article 682 du code civil.                        <br/><br/></div>'),
(31, '<div class=\"txt\">                         La voie d’accès doit être de dimension suffisante compte tenu de la topographie et de la morphologie des lieux, de la nature des voies sur lesquelles elle débouche (intensité du trafic, visibilité, vitesse, alignements d’arbres sur la voie publique et autres espaces verts, dispositifs de signalisation, d’éclairage public et de support de réseaux...), du nombre, de la nature et de l’affectation des constructions existantes et des constructions projetées ou de la surface de plancher projetée, et du trafic engendré par la ou les nouvelles constructions.                        <br/><br/></div>'),
(32, '<div class=\"txt\">                         La voie d’accès doit satisfaire aux normes de desserte et de sécurité des véhicules des services publics (secours, défense incendie, collecte des déchets ménagers, etc.).                        <br/><br/></div>'),
(33, '<div class=\"txt\">                         En cas de construction de moins de trois logements, les sentes piétonnes et escaliers sont considérés comme des dessertes suffisantes.                        <br/><br/></div>'),
(34, '<div class=\"txt\">                         L’accès doit être aménagé de façon à permettre l’entrée et la sortie des véhicules sans manœuvre sur la voie de desserte. Les accès doivent satisfaire aux normes de desserte et de sécurité des véhicules des services publics (secours, défense incendie, collecte des déchets ménagers, etc.).                        <br/><br/></div>'),
(35, '<div class=\"txt\">                         La création d’accès (nombre et positionnement) devra être limitée à ce qui est strictement nécessaire pour desservir une ou des constructions, compte tenu du nombre de logements desservis. Lorsque le terrain est desservi par plusieurs voies, le nombre d’accès et leur positionnement devront être établis là où la gêne pour la circulation sera la moins importante.                        <br/><br/></div>'),
(36, '<div class=\"txt\">                         Dans le cas d’un accès sous porche, la hauteur libre ne doit pas être inférieure à 5 mètres.                        <br/><br/></div>'),
(37, '<div class=\"txt\">                                    Si le chemin d’accès est destiné à desservir moins de 10 logements, l’emprise du chemin d’accès doit avoir une largeur minimum de 3 mètres sur toute la longueur.                                </div>'),
(38, '<div class=\"txt\">                                    Si le chemin d’accès est destiné à desservir au moins 10 logements et pour tous les autres types de constructions autorisés dans cette zone :                                    <ul><li>l\'emprise du chemin d’accès créé doit avoir une largeur minimum de 4 mètres sur toute sa longueur.</li><li>les chemins d’accès doivent satisfaire aux normes de desserte et de sécurité des véhicules des services publics (secours, défense incendie, collecte des déchets ménagers, etc.).</li><li>les chemins d’accès nouveaux se terminant en impasse doivent comporter un aménagement permettant aux véhicules de faire demi-tour à leur extrémité, notamment aux véhicules de ramassage des ordures ménagères, s’ils doivent y accéder pour la collecte, et aux véhicules de secours.</li></ul></div>'),
(39, '<div class=\"txt\">                         Le raccordement aux réseaux publics d’eau potable, d’électricité et d’assainissement est obligatoire.                        <br/><br/></div>'),
(40, '<div class=\"txt\">                         L’alimentation des constructions en eau potable doit se faire par le raccordement au réseau collectif de distribution dans le respect des prescriptions en vigueur.                        <br/><br/></div>'),
(41, '<div class=\"txt\">                         A l’intérieur d’un même terrain, les eaux usées et les eaux pluviales doivent être recueillies séparément, chacune dans un regard situé en limite de terrain.                        <br/><br/></div>'),
(42, '<div class=\"txt\">                         Les installations d’assainissement doivent être réalisées dans le respect des prescriptions en vigueur.                        <br/><br/></div>'),
(43, '<div class=\"txt\">                                        Les eaux usées domestiques doivent être collectées et évacuées, directement et sans stagnation, vers le réseau d’assainissement. La canalisation de raccordement au réseau public d’assainissement doit être équipée d’un dispositif de protection contre le reflux des eaux d’égout.                                    </div>'),
(44, '<div class=\"txt\">                                        Les eaux usées non domestiques peuvent être raccordées au réseau public d’assainissement dans le respect des prescriptions en vigueur. Avant rejet dans le réseau public d’assainissement, les eaux usées non domestiques peuvent être amenées à subir un prétraitement, dans le respect des prescriptions en vigueur.                                    </div>'),
(45, '<div class=\"txt\">                                        Les eaux pluviales doivent dans toute la mesure du possible être retenues et infiltrées ou réutilisées sur le terrain d’assiette du projet. Les techniques alternatives de gestion des eaux pluviales seront privilégiées : infiltration sur l’unité foncière, stockage et réutilisation pour des usages domestiques, conformément à la réglementation en vigueur et sous réserve de la prise en compte des contraintes particulières liées à la présence d’argiles et à l’existence d’anciennes carrières souterraines (Cf. annexes du présent PLU). A défaut, les eaux pluviales doivent être régulées sur le terrain afin de limiter le débit de leur rejet dans le réseau public à 2 litres par seconde et par hectare.                                    </div>'),
(46, '<div class=\"txt\">                                        L’impact de tout rejet ou infiltration peut nécessiter un pré-traitement des eaux notamment à l’exécutoire des aires de stationnement, dans le respect des prescriptions en vigueur.                                    </div>'),
(47, '<div class=\"txt\">                         Les réseaux divers de distribution d’énergie ou de service (eau, gaz, électricité, téléphone, etc.) doivent être souterrains. En cas d’impossibilité technique, ils peuvent être ancrés aux façades d’immeubles.                        <br/><br/></div>'),
(48, '<div class=\"txt\">                         Les projets de construction doivent prévoir un local ou un emplacement spécifique pour le stockage des containers à déchets ménagers hors des voies ou emprises publiques.                        <br/><br/></div>'),
(49, '<div class=\"txt\">                         Sans objet.                        <br/><br/></div>'),
(50, '<div class=\"txt\">                         Les constructions peuvent être implantées soit à l’alignement actuel ou futur des voies ou en limite actuelle ou future des emprises publiques, soit en retrait. En cas de retrait, la marge minimum de retrait est fixée à 3 mètres de l’alignement actuel ou futur des voies ou de la limite actuelle ou future des emprises publiques.                        <br/><br/></div>'),
(51, '<div class=\"txt\">                                En secteur UCV1 et UCV2, les constructions situées sur les terrains dont l’alignement est identifié sur le document graphique n°1 par un trait plein doivent être implantées à l’alignement actuel ou futur des voies ou emprises publiques.                            </div>'),
(52, '<div class=\"txt\">                                En secteur UCV2, les constructions situées sur un terrain dont l’alignement est identifié sur le document graphique n°1 par un trait en pointillé doivent être implantées en retrait de 3 mètres des voies ou emprises publiques.                            </div>'),
(53, '<div class=\"txt\">                                Sont autorisés sur les voies et emprises publiques :                                <ul><li>                                        les saillies à l’alignement, sous réserve de respecter les conditions cumulatives suivantes :                                        <ul><li>de porter sur des voies ou emprises d’une largeur supérieure à 8 mètres ;</li><li>de ne pas dépasser 1,2 mètres ;</li><li>d’être situées à 5,5 mètres au moins du sol ;</li></ul></li><li>les travaux d’isolation permettant l’amélioration de la performance énergétique du bâtiment, réalisés sur une construction existante à la date d’approbation du présent règlement du PLU (18/12/2015), en saillie par rapport à l’alignement.</li></ul><br/>                                Les saillies à l’alignement ne sont toutefois autorisées sur les voies et emprises publiques classées dans le domaine public d’une entité autre que la collectivité, que sous réserve d’un accord de l’autorité gestionnaire de ce domaine public.                            </div>'),
(54, '<div class=\"txt\">                                Sont autorisés dans les marges de retrait définies au paragraphe 6.1 :                                <ul><li>les saillies, à condition qu\'elles ne dépassent pas 1,2 mètres et qu\'elles soient situées à 5,5 mètres au moins du sol ;</li><li>les travaux d\'isolation permettant l’amélioration de la performance énergétique du bâtiment, réalisés sur une construction existante à la date d’approbation du présent règlement du PLU (18/12/2015);</li><li>les accès des bâtiments : perrons, escaliers, passerelles piétonnes, marquises, rampes d’accès au garage et dispositifs permettant ou favorisant l’accessibilité des constructions aux personnes en situation de handicap.</li></ul></div>'),
(55, '<div class=\"txt\">                                Pour les terrains situés à l’angle de deux voies, peut être imposé un alignement nouveau constitué par un segment de droite de 5 mètres de longueur, formant des angles égaux avec chacun des alignements des voies adjacentes, afin d\'assurer un traitement urbain cohérent. Par rapport à ce pan coupé, la marge de retrait définie au paragraphe 6-1 doit être respectée.                            </div>'),
(56, '<div class=\"txt\">                                Les constructions et installations nécessaires aux services publics ou d’intérêt collectif peuvent s’implanter à l’alignement ou en retrait des voies et emprises publiques. En cas de retrait, la marge minimum est fixée à 2 mètres.                            </div>'),
(57, '<div class=\"txt\">                                Dans le secteur UCV 1                                <ul><li>Les constructions situées en façade sur rue doivent être implantées obligatoirement de mitoyen à mitoyen sur les limites séparatives latérales sur une profondeur de 14 à 16 mètres calculée à partir de l’alignement.</li><li>Au-delà de cette profondeur, les constructions peuvent être implantées sur les limites séparatives, ou en retrait de ces limites.</li><li>Dans tous les cas, si la limite séparative correspond à une limite avec la zone UR 2, les constructions doivent être implantées obligatoirement en retrait, conformément à l’article 7.1.3.</li></ul></div>'),
(58, '<div class=\"txt\">                               Dans le secteur UCV 2                                <ul><li>Les constructions peuvent être implantées sur les limites séparatives ou en retrait, conformément à l’article 7.1.3.</li><li>Toutefois, si la limite séparative correspond à une limite avec la zone UR 2, les constructions doivent être implantées obligatoirement en retrait. Cette dernière règle ne s’applique pas au sous-secteur UCV2a.</li></ul></div>'),
(59, '<div class=\"txt\">                                En cas d’implantation en retrait :                                <ul><li>d’une façade comportant des ouvertures créant des vues : la distance à la limite séparative, mesurée normalement et horizontalement en tout point de la façade (saillies et balcons exclus), doit être au moins égale à la moitié de la hauteur mesurée à l’égout du toit ou à l’acrotère de la façade (L=H/2), avec un minimum de 6 mètres.</li><li>d’une façade ne comportant pas d’ouverture, ou comportant des ouvertures ne créant pas de vues : la distance à la limite séparative, mesurée normalement et horizontalement en tout point de la façade (saillies et balcons exclus), doit être au moins égale à la moitié de la hauteur mesurée à l’égout du toit ou à l’acrotère de la façade (L=H/2), avec un minimum de 4 mètres.</li></ul></div>'),
(60, '<div class=\"txt\">                                Lorsque la limite séparative correspond à la limite de l’emprise d’une voie d’accès ouverte à la circulation des véhicules automobiles, sont appliquées les dispositions de l’article 6.                            </div>'),
(61, '<div class=\"txt\">                                Sont admis dans les marges de retrait définies au paragraphe 7.1.3 :                                <ul><li>les travaux d\'isolation permettant l’amélioration de la performance énergétique du bâtiment réalisés sur une construction existante à la date d’approbation du présent règlement du PLU (18/12/2015) ;</li><li>les accès des bâtiments : perrons, escaliers, passerelles piétonnes, marquises, rampes d’accès au garage et les dispositifs permettant ou favorisant l’accessibilité des constructions aux personnes en situation de handicap.</li></ul></div>'),
(62, '<div class=\"txt\">                                Les piscines non couvertes exemptées de permis de construire au titre des articles R. 421-2 et R. 421-9 du code de l’urbanisme doivent respecter une marge de reculement telle que leur bassin soit situé à une distance au moins égale à 1,5 mètre de la limite séparative.                            </div>'),
(63, '<div class=\"txt\">                                Les constructions et installations nécessaires aux services publics ou d’intérêt collectif peuvent être implantées sur les limites séparatives, ou en retrait. En cas de retrait, la marge minimum de retrait est fixée à 2 mètres.                            </div>'),
(64, '<div class=\"txt\">                                Pour les murs pignons supportant des toitures à une ou deux pentes, la hauteur de la construction (H) au sens du présent article est mesurée depuis le sol naturel jusqu’au point médian situé entre le faîtage et l’égout du toit (l’égout le plus élevé en cas d’égouts multiples).                            </div>'),
(65, '<div class=\"txt\">                         La distance minimale entre deux constructions non contiguës, mesurée normalement et horizontalement en tout point de la façade, (saillies et balcons exclus), doit être au moins égale :                        <ul><li>à la hauteur de la façade la plus haute mesurée à l’égout du toit ou à l’acrotère (L=H), avec un minimum de 8 mètres si l’une des façades comporte des ouvertures créant des vues ;</li><li>à la moitié de la hauteur de la façade la plus haute mesurée à l’égout du toit ou à l’acrotère (L=H/2), sans pouvoir être inférieure à 4 mètres, si les façades ne comportent pas d’ouverture, ou comportent des ouvertures ne créant pas de vue.</li></ul><br/></div>'),
(66, '<div class=\"txt\">                         La plus courte distance entre deux constructions doit être au moins égale à 4 mètres. Pour les murs pignons supportant des toitures à une ou deux pentes, la hauteur de la construction (H) au sens du présent article est mesurée depuis le sol naturel jusqu’au point médian situé entre le faîtage et l’égout du toit (l’égout le plus élevé en cas d’égouts multiples).                        <br/><br/></div>'),
(67, '<div class=\"txt\">                         Cette règle ne s’applique pas aux constructions et installations nécessaires aux services publics ou d’intérêt collectif.                        <br/><br/></div>'),
(68, '<div class=\"txt\">                         L’emprise au sol des constructions ne peut excéder 80% de la superficie du terrain.                        <br/><br/></div>'),
(69, '<div class=\"txt\">                         Il n’est pas fixé de règle pour les constructions et installations nécessaires aux services publics ou d’intérêt collectif.                        <br/><br/></div>'),
(70, '<div class=\"txt\">                                Dans la zone UCV, la hauteur des constructions est mesurée verticalement en tout point de la construction par rapport au terrain naturel.                            </div>'),
(71, '<div class=\"txt\"><ul><li>Dans les secteurs UCV1 et UCV2, la hauteur des constructions ne peut excéder 18 mètres au point le plus haut.</li><li>Lorsque la construction présente une ou plusieurs façades sur rue, y compris des façades situées en retrait par rapport à l’alignement mais visibles depuis la rue, la partie de la construction visible depuis la rue doit, à partir de points d’accroches fixés à 15 mètres, s’inscrire dans un gabarit ne dépassant pas un volume délimité par une oblique de pente de 2 pour 1 et une ligne horizontale plafond fixée à 18 mètres (cf. schéma ci-dessous).</li><li>En cas de toiture terrasse, le dernier étage des constructions, à partir de points d’accroche fixés à 15 mètres, doit être réalisé en attique avec un retrait minimum de 1,5 mètre au droit  de la façade sur rue.</li></ul></div>'),
(72, '<div class=\"txt\"><ul><li>Dans le sous-secteur UCV2a, la hauteur des constructions ne peut excéder 9 mètres à l\'égout du toit, quel que soit le type de toiture, et 12 mètres au point le plus haut. La construction, à partir de points d’accroches fixés à 9 mètres, doit s’inscrire dans un gabarit ne dépassant pas un volume délimité par une oblique de pente maximum de 45° sur une profondeur de 3 mètres à compter de l’égout du toit (cf. schéma ci-contre).</li><li>                                        Dans le cas de toiture à la Mansart :                                        <br/>                                        La construction à partir de points d’accroches fixés à 9 mètres doit s’inscrire dans un gabarit ne dépassant pas un volume délimité par une oblique de pente de 60° sur une hauteur maximum de 2 mètres par rapport à l’égout du toit et au-delà par une oblique de pente maximum de 30° sur une hauteur maximum de 1 mètre. (cf. schéma ci-contre).                                    </li></ul></div>'),
(73, '<div class=\"txt\">                                Sur les terrains comportant au moins une façade sur rue identifiée sur le document graphique n°2 au titre de l’article L.123-1-5 III 2° du code de l’urbanisme :                                <ul><li>la hauteur au point le plus haut des constructions existantes situées à l’alignement doit être conservée ;</li><li>en l’absence de construction existante implantée à l’alignement, toute nouvelle construction implantée à l’alignement pourra s’insérer dans la limite de l’héberge existante la plus haute des constructions implantées à l’alignement sur les terrains voisins.</li></ul></div>'),
(74, '<div class=\"txt\">                                Ne sont pas comptées dans le calcul de la hauteur de la construction, les installations techniques sur terrasse, à condition qu’elles ne dépassent pas une hauteur de 3 mètres, qu’elles soient implantées en retrait des façades et des pignons d’une distance au moins égale à leur hauteur, ainsi que les souches de cheminées et de ventilation, les antennes (hormis les paraboles), les acrotères et les garde-corps ceinturant les toitures-terrasses.                            </div>'),
(75, '<div class=\"txt\">                                Dans le cadre de la mise en œuvre d’une isolation ou d’un dispositif énergétique permettant l’amélioration de la performance énergétique du bâtiment, la surélévation de la toiture des bâtiments existants à la date d’approbation du présent règlement peut être autorisée au-dessus du gabarit existant. Cette surélévation doit être entreprise dans le respect des dispositions architecturales originelles du bâtiment, qui le cas échéant doivent être restituées ou adaptées.                            </div>'),
(76, '<div class=\"txt\">                                Lorsqu’une construction existante à la date d’approbation du règlement du PLU (18/12/2015) ne respecte pas les dispositions fixées au paragraphe 10-1, les travaux de réhabilitation et ou extension sont autorisés à condition que les hauteurs au point le plus haut de la construction après travaux ne dépassent pas celles existantes à la date d’approbation du règlement du PLU (18/12/2015), sous réserve du respect des autres articles du présent règlement.                            </div>'),
(77, '<div class=\"txt\">                                La hauteur des constructions annexes mesurée conformément au paragraphe 10.1. ne peut excéder 3,50 mètres.                            </div>'),
(78, '<div class=\"txt\"><ul><li>Dans les secteurs UCV1 et UCV2, la hauteur des constructions et installations nécessaires aux services aux services publics ou d’intérêt collectif ne pourra excéder 18 m au point le plus haut, nonobstant les dispositions du paragraphe 10.1.2.</li><li>Dans le sous-secteur UCV2a, la hauteur des constructions et installations nécessaires aux services aux services publics ou d’intérêt collectif ne pourra excéder 12 m au point le plus haut, nonobstant les dispositions du paragraphe 10.1.3.</li></ul></div>'),
(79, '<div class=\"txt\">                         En application de l’article R. 111-21 du code de l’urbanisme, le projet peut être refusé ou n\'être accepté que sous réserve de l\'observation de prescriptions spéciales si les constructions, par leur situation, leur architecture, leurs dimensions ou l\'aspect extérieur des bâtiments ou ouvrages à édifier ou à modifier, sont de nature à porter atteinte au caractère ou à l\'intérêt des lieux avoisinants, aux sites, aux paysages naturels ou urbains ainsi qu\'à la conservation des perspectives monumentales.                        <br/><br/></div>'),
(80, '<div class=\"txt\">                         Les toitures                        <br/><ul><li>Les combles et toitures doivent présenter une simplicité de volume et une unité de conception.</li><li>Les toitures doivent faire l’objet d’un traitement (volume, matériaux, couleurs) qui garantisse une bonne insertion dans le site.</li><li>Sur les terrains dont les façades sur rue sont identifiées sur le document graphique n°2 par un liseré plein au titre de l’article L. 123-1-5 III 2° du code de l’urbanisme, les toitures doivent être à pente.</li><li>Les cheminées doivent être traitées avec les matériaux et couleurs en harmonie avec ceux de la construction.</li><li>La mise en œuvre de toitures végétalisées, l’installation de système de production d’énergies renouvelables peuvent être admis à condition d\'être intégrés de façon harmonieuse à la construction.</li></ul><br/><br/></div>'),
(81, '<div class=\"txt\">                         Les façades                        <ul><li>Les façades sur rues doivent être percées de baies.</li><br/><li>L’ensemble des façades des constructions doit présenter un aspect et une couleur en harmonie avec les constructions avoisinantes.</li><br/><li>Les constructions annexes et clôtures doivent être traitées avec soin.</li><br/><li>Les matériaux destinés à être recouverts d’un parement ou d’un enduit, ne peuvent être laissés apparents sur les façades des constructions et sur les clôtures (carreaux de plâtre, parpaings, briques creuses ...).</li><br/><li>Les caissons de volets roulants doivent être installés à l’intérieur des constructions. En cas d’impossibilité, ils doivent être camouflés le plus discrètement possible.</li></ul><br/></div>'),
(82, '<div class=\"txt\">                         Les façades commerciales                        <ul><li>Les façades de locaux commerciaux doivent être conçues en harmonie avec les caractéristiques architecturales de l’immeuble dans lequel elles sont situées.</li><br/><li>Dans le cas d’une construction nouvelle, la hauteur des rez-de-chaussée commerciaux doit être au minimum de 3 mètres, calculée depuis la rue.</li><br/><li>                                Les créations ou modifications de façades doivent respecter les prescriptions suivantes :                                <ul><li>les percements destinés à recevoir des vitrines doivent s’adapter à l’architecture de l’immeuble concerné ;</li><li>lorsqu’un même commerce est établi sur plusieurs immeubles contigus, les percements de vitrines doivent en respecter les limites séparatives ;</li><li>l’utilisation de manière uniforme de teintes vives est proscrite ;</li><li>lorsqu’une façade commerciale existante présente un intérêt patrimonial ou architectural (modénatures, panneaux en bois travaillés, appareillage en pierres, etc.), celle-ci doit être, sauf impossibilité technique avérée, préservée ou mise en valeur ;</li><li>lorsque le rez-de-chaussée (des constructions nouvelles ou lors d’une modification) doit comporter l’emplacement d’un bandeau destiné à recevoir une enseigne, Il doit être séparé de façon visible du premier étage, en s’inspirant des systèmes traditionnels (corniches, retraits, etc.).</li><li>Il doit également être proportionné à la taille des locaux, du bâtiment et de la rue. Le bandeau doit également se limiter au linéaire des vitrines commerciales ;</li><li>lors de l’installation de rideaux métalliques, les caissons doivent être intégrés dans le gros œuvre et ne pas présenter de saillie en façade. Ces rideaux sont de préférence ajourés.</li></ul></li></ul><br/></div>'),
(83, '<div class=\"txt\">                         Les descentes d’eaux pluviales                        <ul><li>Les descentes d’eaux pluviales devront être intégrées dans la composition architecturale de la façade.</li></ul><br/></div>'),
(84, '<div class=\"txt\">                         Les rampes de parking                        <ul><li>Les rampes de parking devront être traitées de manière à s’harmoniser avec la construction et les espaces extérieurs.</li></ul><br/></div>'),
(85, '<div class=\"txt\">                         Les édicules et gaines techniques                        <ul><li>Les édicules techniques doivent, par le choix des matériaux et des couleurs, être intégrés aux façades et aux toitures où ils se trouvent.</li><br/><li>Les réseaux techniques en toiture ou en terrasse, tels que les ventilations, sont, sauf impossibilité technique avérée, camouflés par un revêtement identique à la façade ou s’harmonisant avec elle.</li></ul><br/></div>'),
(86, '<div class=\"txt\">                         Les dévoiements des conduits de cheminée                        <ul><li>Lorsqu’une construction nouvelle vient s’accoler à une ou des constructions existantes moins hautes et qu’un dévoiement des conduits de cheminée ou de ventilation est nécessaire, celui-ci doit faire l’objet d’un traitement architectural afin de n’être pas visible dans le paysage.</li><br/><li>La construction ou le rehaussement du ou des conduits à réaliser ne peut pas être laissé en matériau brut (aluminium, acier inox, etc.).</li></ul><br/></div>'),
(87, '<div class=\"txt\">                         Les antennes                        <ul><li>Les infrastructures et les installations doivent être réalisées dans le respect de l’environnement, de la qualité esthétique des lieux et dans les conditions les moins dommageables, tant pour le domaine public que pour le domaine privé.</li><br/><li>Les antennes d’émission ou de réception de signaux radioélectriques (antennes, paraboles, etc.) devront être installées obligatoirement en toiture.</li><br/><li>Lorsqu’elles s’implantent en terrasse, elles doivent être le plus en retrait possible de la façade.</li><br/><li>Elles doivent avoir une couleur qui s’intègre avec la partie de construction sur laquelle elles sont fixées.</li></ul><br/></div>'),
(88, '<div class=\"txt\">                         Les panneaux solaires ou photovoltaïques                        <ul><li>Les panneaux solaires doivent être intégrés dans la composition architecturale d’ensemble de la construction et notamment la pente de la toiture, dans le cas où ils sont posés en toiture, ou adossés sur le bâti.</li><br/><li>La création d’un champ de captage doit être le plus homogène possible en regroupant les panneaux solaires. L’implantation doit être la plus basse et discrète possible, qu’elle soit ou non intégrée au bâti, elle doit respecter les critères paysagés ou architecturaux.</li></ul><br/></div>'),
(89, '<div class=\"txt\">                         Les clôtures participent fortement à la qualité des espaces urbains. A ce titre, leur traitement, le choix des matériaux, les couleurs doivent faire l’objet d’une attention particulière en respectant une harmonie avec les clôtures existantes à proximité.                        <br/><br/></div>'),
(90, '<div class=\"txt\">                         L’emploi à nu de matériaux destinés à être recouverts (carreaux de plâtre, briques creuses, parpaings, plaques de béton,...) ou destinés à un autre usage (tôles ondulées, contreplaqué, etc...) est interdit.                        <br/><br/></div>'),
(91, '<div class=\"txt\">                         La hauteur totale de la clôture, calculée à partir de la voie ou de l’emprise publique, ne peut dépasser 2 mètres. Sur rue, elle doit être composée d\'un ensemble homogène constitué d\'un mur bahut d’une hauteur maximale de 1,20 mètres surmonté d’un élément ajouré sur environ 50% de sa surface (grille, barreaudage vertical métallique,etc.).                        <br/><br/></div>'),
(92, '<div class=\"txt\">                         Les portails, portillons d’accès et piliers seront de forme simple, pleins ou ajourés, sans excès de surcharge décorative. Leur hauteur ne devra pas excéder 2,20 mètres par rapport au trottoir.                        <br/><br/></div>'),
(93, '<div class=\"txt\">                         En cas de mur de soutènement sur rue, les règles précédentes peuvent être adaptées.                        <br/><br/></div>'),
(94, '<div class=\"txt\">                         Sur les autres limites séparatives, la hauteur totale de la clôture ne doit pas dépasser 2 mètres, calculés à partir du terrain naturel.                        <br/><br/></div>'),
(95, '<div class=\"txt\">                         Des exceptions à ces règles peuvent être autorisées dans les cas suivants :                        <ul><li>en cas de constructions ou installations nécessaires aux services publics ou d’intérêt collectif, lorsque des raisons techniques ou de sécurité l’imposent ;</li><li>en cas de nuisances sonores et visuelles.</li></ul><br/></div>'),
(96, '<div class=\"txt\">                         L’architecture (et notamment les modénatures) et la volumétrie des constructions anciennes ou présentant un intérêt architectural doivent être maintenues lors d’un ravalement ou de travaux de réhabilitation.                        <br/><br/></div>'),
(97, '<div class=\"txt\">                         Un soin particulier doit être apporté à la préservation, la restauration et le cas échéant la restitution des éléments de modénature spécifiques à la construction. Toute extension, surélévation de bâtiment doit respecter l’architecture d’origine ou faire l’objet d’un traitement architectural contemporain.                        <br/><br/></div>'),
(98, '<div class=\"txt\">                         La création de nouveaux percements doit s’intégrer dans la composition des façades (reprise des proportions, du rythme et des éléments de modénature).                        <br/><br/></div>'),
(99, '<div class=\"txt\">                         Les murs prévus pour être apparents doivent être préservés (pierre de meulière, brique, etc.).                        <br/><br/></div>'),
(100, '<div class=\"txt\">                         La réfection de toiture doit respecter le style de la construction existante.                        <br/><br/></div>'),
(101, '<div class=\"txt\">                         Les constructions et façades sur rue repérées sur le document graphique n°2 au titre des dispositions l’article L 123-1-5 III 2° du code de l’urbanisme                        <br/><br/></div>'),
(102, '<div class=\"txt\">                         Tous les travaux exécutés sur une construction remarquable faisant l’objet d’une protection au titre de l’article L. 123-1-5 III 2° du code de l’urbanisme doivent être conçus en évitant toute dénaturation des caractéristiques constituant son intérêt esthétique. La démolition de tout ou partie d’une telle construction, et la destruction des éléments architecturaux ou décoratifs caractéristiques des façades, peut être interdite.                        <br/><br/></div>'),
(103, '<div class=\"txt\">                         En cas de démolition-reconstruction d’une façade sur rue, identifiée par un liseré plein sur le document graphique n°2, la typologie architecturale de la construction d’origine doit être conservée.                        <br/><br/></div>'),
(104, '<div class=\"txt\">                         Lors de toute opération de construction, d\'extension, de surélévation ou de changement de destination de locaux, des aires de stationnement doivent être réalisées afin d’assurer, en dehors des voies publiques, le stationnement des véhicules correspondant aux besoins des constructions. Les normes sont définies en fonction de la nature de la construction. Le nombre total de places de stationnement est arrondi au chiffre entier supérieur.                        <br/><br/></div>'),
(105, '<div class=\"txt\">                         Pour les constructions de plus de 3 logements ainsi que pour les constructions à destination autre que d’habitation, 80 % au moins des places de stationnement réglementairement exigibles, devront être couvertes dans le volume de la construction ou dans un bâtiment annexe en surface ou enterré, sauf impossibilité technique en cas de création de places de stationnement supplémentaires réglementairement exigées dans le cadre de travaux de réhabilitation et/ou extension d’un bâtiment existant à la date d’approbation du PLU.                        <br/><br/></div>'),
(106, '<div class=\"txt\">                         La suppression de toute place de stationnement est interdite sur les terrains existants en cas de division. Elle ne peut être autorisée qu’à condition que la ou les places supprimées soient récréées sur le terrain.                        <br/><br/></div>'),
(107, '<div class=\"txt\">                         Les places de stationnement commandées sont interdites.                        <br/><br/></div>'),
(108, '<div class=\"txt\">                         Il est imposé :                        <ul><li>                                Pour les constructions à destination de bureaux :                                <ul><li>une place de stationnement par tranche entamée de 50 m2 de surface de plancher, lorsque la construction est située à plus de 500 mètres d’un point de desserte en transport en commun structurante avec interdiction de réaliser plus de places que cette norme imposée.</li><li>Une place de stationnement par tranche entamée de 60 m2 de surface de plancher, lorsque la construction est située à moins de 500 mètres d’un point de desserte en commun structurante avec interdiction de réaliser plus de places que cette norme imposée.</li></ul></li></ul><br/></div>'),
(109, '<div class=\"txt\">                         Il est exigé au moins :                        <ul><li><div class=\"txt\">                                    Pour les constructions à destination d’habitation :                                    <ul><li>Une place par tranche entamée de 60 m2 de surface de plancher en ne dépassant pas 1,9 places par logement.</li><li>Si le projet porte sur la réalisation de logements locatifs sociaux financés avec un prêt aidé par l’Etat, il doit être réalisé au moins une place de stationnement par logement.</li><li>Toutefois pour les constructions de logements locatifs sociaux financés par un prêt aidé par l’Etat situés à moins de 500 mètres autour d’une gare ou d’une station de transport public en site propre et si la qualité de la desserte le permet, il ne sera pas exigé plus de 0,5 place par logement locatif social financé par un prêt aidé par l’Etat et pas plus d’une place pour les autres catégories de logements.</li></ul></div></li><br/><li><div class=\"txt\">                                    Pour les constructions à destination de commerce :                                    <ul><li>Pour les constructions à destination de commerce dont la surface de plancher est inférieure ou égale à 150 m2, il n’est pas fixé de règle ;</li><li>Pour les constructions à destination de commerce dont la surface de plancher est supérieure à 150 m2 : il est imposé une place par tranche entamée de 40 m2 de surface de plancher avec un minimum de deux places de stationnement. Une place de stationnement dédiée à la livraison doit être réalisée.</li></ul></div></li><br/><li><div class=\"txt\">                                    Pour les constructions à destination d’artisanat :                                    <ul><li>Pour les constructions à destination d’artisanat dont la surface de plancher est inférieure ou égale à 1 500 m2, il n’est pas fixé de règle ;</li><li>Pour les constructions à destination d’artisanat dont la surface de plancher est supérieure à 1 500 m2, il est imposé une place de stationnement pour les livraisons.</li></ul></div></li><br/><li><div class=\"txt\">                                    Pour les constructions à destination d’hébergement hôtelier :                                    <ul><li>Une place de stationnement par chambre ;</li><li>Au-delà de 20 chambres, il sera réalisé deux places par tranche entamée de 20 chambres.</li></ul></div></li><br/><li><div class=\"txt\">                                    Pour les constructions et installations nécessaires aux services publics ou d’intérêt collectif:                                    <ul><li>Le nombre de places de stationnement à réaliser doit être adapté à la nature de l’équipement, à son mode de fonctionnement, à sa localisation sur le territoire communal (proximité des transports en commun, existence de parcs publics de stationnement à proximité, etc.) et au nombre et au type d’utilisateurs concernés.</li></ul></div></li></ul><br/></div>');
INSERT INTO `TEXTE` (`id-texte`, `texte`) VALUES
(110, '<div class=\"txt\">                                    Pour les constructions à destination d’habitation :                                    <ul><li>Une place par tranche entamée de 60 m2 de surface de plancher en ne dépassant pas 1,9 places par logement.</li><li>Si le projet porte sur la réalisation de logements locatifs sociaux financés avec un prêt aidé par l’Etat, il doit être réalisé au moins une place de stationnement par logement.</li><li>Toutefois pour les constructions de logements locatifs sociaux financés par un prêt aidé par l’Etat situés à moins de 500 mètres autour d’une gare ou d’une station de transport public en site propre et si la qualité de la desserte le permet, il ne sera pas exigé plus de 0,5 place par logement locatif social financé par un prêt aidé par l’Etat et pas plus d’une place pour les autres catégories de logements.</li></ul></div>'),
(111, '<div class=\"txt\">                                    Pour les constructions à destination de commerce :                                    <ul><li>Pour les constructions à destination de commerce dont la surface de plancher est inférieure ou égale à 150 m2, il n’est pas fixé de règle ;</li><li>Pour les constructions à destination de commerce dont la surface de plancher est supérieure à 150 m2 : il est imposé une place par tranche entamée de 40 m2 de surface de plancher avec un minimum de deux places de stationnement. Une place de stationnement dédiée à la livraison doit être réalisée.</li></ul></div>'),
(112, '<div class=\"txt\">                                    Pour les constructions à destination d’artisanat :                                    <ul><li>Pour les constructions à destination d’artisanat dont la surface de plancher est inférieure ou égale à 1 500 m2, il n’est pas fixé de règle ;</li><li>Pour les constructions à destination d’artisanat dont la surface de plancher est supérieure à 1 500 m2, il est imposé une place de stationnement pour les livraisons.</li></ul></div>'),
(113, '<div class=\"txt\">                                    Pour les constructions à destination d’hébergement hôtelier :                                    <ul><li>Une place de stationnement par chambre ;</li><li>Au-delà de 20 chambres, il sera réalisé deux places par tranche entamée de 20 chambres.</li></ul></div>'),
(114, '<div class=\"txt\">                                    Pour les constructions et installations nécessaires aux services publics ou d’intérêt collectif:                                    <ul><li>Le nombre de places de stationnement à réaliser doit être adapté à la nature de l’équipement, à son mode de fonctionnement, à sa localisation sur le territoire communal (proximité des transports en commun, existence de parcs publics de stationnement à proximité, etc.) et au nombre et au type d’utilisateurs concernés.</li></ul></div>'),
(115, '<div class=\"txt\">                         La création de places de stationnement n’est pas exigée lors de travaux de réhabilitation, surélévation, aménagement et/ou extension d’une construction existante à destination d’habitation et régulièrement édifiée à la date d’approbation du règlement du PLU (18/12/2015), dans la mesure où il n’est pas créé plus de 50m2 de surface de plancher, et où les travaux ne donnent pas lieu à la création de nouveaux logements. La suppression d’une place de stationnement ne peut être autorisée qu’à condition que la place supprimée soit récréée sur le terrain.                        <br/><br/></div>'),
(116, '<div class=\"txt\">                         Dans le cas d’une extension de plus de 50 m2 de surface de plancher ou de la création de nouveaux logements dans une construction existante, le nombre de places total après achèvement des travaux doit respecter les dispositions du 12.1.2.                        <br/><br/></div>'),
(117, '<div class=\"txt\">                         Dans le cas des travaux sur les constructions à destination autre que d’habitation, la règle à respecter en termes de stationnement ne concernera que les surfaces de plancher créées par le projet, et dans la proportion d’une place par tranche de 60 m2 dès lors que cette dernière norme est moins exigeante que celle prévue au paragraphe 12.1.2. La suppression d’une place de stationnement ne peut être autorisée qu’à condition que la place supprimée soit récréée sur le terrain.                        <br/><br/></div>'),
(118, '<div class=\"txt\">                         Pour les nouvelles constructions à destination d’habitation comportant plus de 2 logements et les nouvelles constructions à destination de bureaux, il doit être créé des espaces dédiés aux vélos.                        <br/><br/></div>'),
(119, '<div class=\"txt\">                         Ces espaces doivent être aisément accessibles, disposer des aménagements adaptés et respecter les règles suivantes :                        <ul><li>Pour les nouveaux bâtiments à destination d’habitation, l’espace possèdera une superficie de 0,75 m2 de surface par logement pour les logements jusqu’à deux pièces, et 1,5 m2 de surface par logement dans les autres cas, avec une superficie minimale de 3 m2 de surface ;</li><br/><li>Pour les nouveaux bâtiments à destination de bureaux, l’espace possèdera une superficie représentant 1,5 % de la surface de plancher. Cet espace peut être constitué de plusieurs emplacements.</li><br/><li>Pour les nouveaux bâtiments à destination de commerce, d’artisanat, d’hébergement hôtelier, de plus de 500 m2 de de surface de plancher : il est exigé au moins 1 place pour 10 employés. Le stationnement devra être dimensionné pour permettre l’accueil des visiteurs.</li><br/><li>La création d’un espace dédié aux vélos est également imposée pour les nouveaux équipements et installations nécessaires aux services publics ou d’intérêt collectif avec à minima 1 place pour 10 employés. La surface de l’espace de stationnement à réaliser doit être adaptée à la nature de l’équipement.</li><br/><li>Pour les nouveaux bâtiments à destination d’équipements scolaires (primaires, collèges, lycées et universités), il est imposé 1 place pour 8 à 12 élèves.</li></ul><br/></div>'),
(120, '<div class=\"txt\">                         Les parcs de stationnement des constructions nouvelles à destination d’habitation et de bureaux doivent comporter des places équipées pour la recharge des véhicules électriques ou hybrides. Pour le snouvelles constructions à destination d’habitation, ces dispositions s’imposent pour les parcs de stationnement liés à un programme comportant de plus de 2 logements.                        <br/><br/></div>'),
(121, '<div class=\"txt\">                         Le nombre de places équipées à réaliser doit être conforme aux dispositions des articles R.111-14-2 et R.111-14-3 du code de la construction et de l’habitation.                        <br/><br/></div>'),
(122, '<div class=\"txt\">                         Chaque emplacement doit respecter les dimensions minimales suivantes :                        <ul><li>longueur : 5 mètres ;</li><li>largeur : 2,50 mètres ;</li><li>longueur de dégagement : 5 mètres.</li></ul><br/></div>'),
(123, '<div class=\"txt\">                         Les aires de plus de 3 emplacements doivent être matérialisées au sol.                        <br/><br/></div>'),
(124, '<div class=\"txt\">                         Les rampes d’accès au sous-sol ne doivent pas modifier la voirie existante (trottoir et chaussée).                        <br/><br/></div>'),
(125, '<div class=\"txt\">                         Sauf impossibilité technique, la pente des rampes d’accès ne doit pas être supérieure à 5 % dans les 5 premiers mètres comptés à partir de l’alignement.                        <br/><br/></div>'),
(126, '<div class=\"txt\">                         Rampes d’accès pour la desserte de 3 logements et plus, et pour les constructions à destination autre que d’habitation :                        <ul><li>sens unique : 3,50 mètres ;</li><li>double sens desservant jusqu’à 30 places de stationnement : 3,50 mètres ;</li><li>double sens desservant plus de 30 places de stationnement : 6,00 mètres.</li></ul>                        Leur rayon intérieur ne peut être inférieur à 5 mètres. Le rayon extérieur doit être égal au rayon intérieur augmenté d’une largeur de 3,50 mètres pour une rampe à sens unique ou de 6 mètres pour une rampe à double sens.                        <br/><br/></div>'),
(127, '<div class=\"txt\">                         Les projets de constructions doivent être étudiés en tenant compte d’une analyse paysagère du site (le terrain et son environnement).                        <br/><br/></div>'),
(128, '<div class=\"txt\">                         Les arbres ne nécessitant pas d\'être abattus pour la réalisation de la construction doivent être préservés, sauf impossibilité technique, ou sauf si leur suppression est rendue nécessaire pour la sécurité des personnes et des biens.                        <br/><br/></div>'),
(129, '<div class=\"txt\">                         Dans le secteur UCV2, 5 % au moins des espaces libres de toute construction doivent être traités en espaces verts ou éco-aménagés.                        <br/><br/></div>'),
(130, '<div class=\"txt\">                         Les espaces végétalisés sur dalle doivent comporter au moins 0,80 mètre d’épaisseur de terre végétale comportant tous les composants techniques nécessaires à la création et au maintien d’un espace vert de qualité.                        <br/><br/></div>'),
(131, '<div class=\"txt\">                         La plantation d’un arbre, d’une hauteur minimale au moment de l’implantation de 2,40 mètres, est imposée par tranche entamée de 200 m2 d’espaces libres. Sont pris en compte les arbres existants conservés ou plantés.                        <br/><br/></div>'),
(132, '<div class=\"txt\">                         Afin de préserver la biodiversité et les écosystèmes locaux, la plantation d’essences végétales locales ou indigènes devra être privilégiée au détriment d’espèces exotiques potentiellement invasives. (Se référer au cahier de recommandations mentionné en annexe).                        <br/><br/></div>'),
(133, '<div class=\"txt\">                         Tout abattage d’arbre remarquable identifié au titre de l’article L.123-1-5 III 2° est interdit, sauf état phytosanitaire qui le justifierait.                        <br/><br/></div>'),
(134, '<div class=\"txt\">                         Dans le cas où un arbre identifié au titre de l’article L.123-1-5 III, 2° du code de l’urbanisme serait abattu, il devra être remplacé par un arbre de même essence ou d’une essence susceptible de redonner une valeur paysagère équivalente.                        <br/><br/></div>'),
(135, '<div class=\"txt\">                         Toute construction nouvelle devra respecter une marge de recul minimale de 5 mètres par rapport au collet des arbres (base du tronc au niveau du sol).                        <br/><br/></div>'),
(136, '<div class=\"txt\">                         Les espaces boisés classés figurant aux documents graphiques n°1 et n°2 sont soumis aux dispositions de l\'article L.130-1 du code de l\'urbanisme.                        <br/><br/></div>'),
(137, '<div class=\"txt\">                         Sans objet.                        <br/><br/></div>'),
(138, '<div class=\"txt\">                         Il doit être recherché un captage solaire maximum à travers les vitrages. L’orientation sud est nettement plus favorable que les orientations est et ouest, elles-mêmes nettement plus favorables que l’orientation nord. Dans le cas de constructions avec des locaux traversants,                        <br/><br/></div>'),
(139, '<div class=\"txt\">                         l’orientation nord/sud est privilégiée à l’orientation est/ouest. Il doit être recherché un maximum de vitrage au sud. Des protections solaires devront être proposées pour le confort d’été. La création d’une véranda ou d’une serre est privilégiée au sud avec un maximum de vitrages proches de la verticale.                        <br/><br/></div>'),
(140, '<div class=\"txt\">                         Le choix de l’emplacement des murs, claustras et des plantations doit tendre à minimiser l’effet des vents dominants sur les constructions et les espaces extérieurs.                        <br/><br/></div>'),
(141, '<div class=\"txt\">                         Les nouvelles constructions à destination d’habitation de plus de 3 logements et les nouvelles constructions à destination de bureaux et d’hébergement hôtelier devront être reliées à un réseau haut débit.                        <br/><br/></div>');

-- --------------------------------------------------------

--
-- Structure de la table `ZONAGE`
--

CREATE TABLE `ZONAGE` (
  `id-zone` int(1) DEFAULT NULL,
  `id-parent-zone` int(2) DEFAULT NULL,
  `nom-zone` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `ZONAGE`
--

INSERT INTO `ZONAGE` (`id-zone`, `id-parent-zone`, `nom-zone`) VALUES
(1, 0, 'UCV\r'),
(2, 0, 'UR\r'),
(3, 0, 'A\r'),
(4, 0, 'N\r'),
(5, 1, 'UCV1\r'),
(6, 1, 'UCV2\r'),
(7, 2, 'UR1\r'),
(8, 2, 'UR2\r'),
(9, 6, 'UCV2a');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
