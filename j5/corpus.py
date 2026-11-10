"""Base de connaissances FICTIVE d'une entreprise, pour le mini-projet du J5.

Chaque document : id, titre, texte, groupes autorisés à le lire.
Les documents « rh » et « securite » ne doivent JAMAIS sortir pour un utilisateur qui n'a pas ce groupe.
"""

DOCUMENTS = [
    ("D01", "Demander un congé", "Les demandes de congé se font dans l'outil RH au moins deux semaines à l'avance. Le responsable valide la demande.", {"tous"}),
    ("D02", "Jours fériés", "La liste des jours fériés de l'année est publiée en janvier sur l'intranet. Les jours de pont sont annoncés séparément.", {"tous"}),
    ("D03", "Télétravail", "Le télétravail est possible deux jours par semaine après accord du responsable. Une connexion VPN est obligatoire.", {"tous"}),
    ("D04", "Configurer le VPN", "Installez le client VPN depuis le portail logiciel, puis connectez-vous avec votre compte et l'authentification multifacteur.", {"tous"}),
    ("D05", "Mot de passe oublié", "Pour réinitialiser votre mot de passe, utilisez le portail en libre-service. Le support ne demande jamais votre mot de passe.", {"tous"}),
    ("D06", "Authentification multifacteur", "L'authentification multifacteur est obligatoire pour la messagerie, le VPN et les outils cloud. Utilisez l'application d'authentification.", {"tous"}),
    ("D07", "Signaler un hameçonnage", "Un courriel suspect ? Ne cliquez sur aucun lien. Utilisez le bouton de signalement de la messagerie : l'équipe sécurité analyse le message.", {"tous"}),
    ("D08", "Notes de frais", "Les notes de frais sont saisies dans l'outil financier avec les justificatifs scannés, au plus tard à la fin du mois suivant.", {"tous"}),
    ("D09", "Réserver une salle", "Les salles de réunion se réservent dans l'agenda partagé. Annulez la réservation si la réunion est supprimée.", {"tous"}),
    ("D10", "Imprimer un document", "Les imprimantes sont accessibles avec le badge. Les impressions en couleur sont limitées aux documents destinés aux clients.", {"tous"}),
    ("D11", "Données personnelles des clients", "Les données personnelles des clients ne sont utilisées que pour la finalité prévue. Toute nouvelle utilisation demande l'avis du délégué à la protection des données.", {"tous"}),
    ("D12", "Exercer ses droits RGPD", "Un client peut demander l'accès, la rectification ou l'effacement de ses données. La réponse doit être donnée dans un délai d'un mois.", {"tous"}),
    ("D13", "Violation de données", "En cas de fuite de données personnelles, prévenez immédiatement le délégué à la protection des données. La notification à l'autorité doit se faire dans les 72 heures.", {"tous"}),
    ("D14", "Utiliser un assistant IA", "Les assistants IA autorisés sont listés sur l'intranet. N'y copiez jamais de données personnelles de clients ni de code confidentiel.", {"tous"}),
    ("D15", "Formation à l'IA", "Chaque collaborateur suit une formation de base à l'IA : fonctionnement, limites, risques et bonnes pratiques de vérification.", {"tous"}),
    ("D16", "Mettre à jour un poste", "Les mises à jour de sécurité du poste de travail s'installent automatiquement. Redémarrez votre ordinateur au moins une fois par semaine.", {"tous"}),
    ("D17", "Installer un logiciel", "Seuls les logiciels du portail sont autorisés. Une demande d'exception passe par le support avec une justification.", {"tous"}),
    ("D18", "Perte d'un ordinateur", "En cas de perte ou de vol d'un ordinateur portable, prévenez le support immédiatement pour bloquer l'accès à distance.", {"tous"}),
    ("D19", "Sauvegarde des fichiers", "Enregistrez vos fichiers de travail dans l'espace partagé : il est sauvegardé chaque nuit. Le disque local ne l'est pas.", {"tous"}),
    ("D20", "Accueil d'un nouveau collègue", "Le jour d'arrivée, le nouveau collègue reçoit son badge, son ordinateur et ses accès. Un parrain l'accompagne le premier mois.", {"tous"}),
    ("D21", "Grille salariale 2026", "Grille des salaires par fonction et ancienneté, révisée au premier janvier. Document strictement réservé aux ressources humaines.", {"rh"}),
    ("D22", "Procédure de licenciement", "Étapes, délais de préavis et documents à préparer pour une procédure de licenciement. Réservé aux ressources humaines.", {"rh"}),
    ("D23", "Évaluations annuelles", "Calendrier et formulaires des entretiens d'évaluation annuels. Les résultats individuels sont confidentiels.", {"rh"}),
    ("D24", "Plan de réponse aux incidents", "Rôles, contacts d'astreinte et étapes de réponse à un incident de sécurité majeur, y compris la notification NIS2 à l'autorité.", {"securite"}),
    ("D25", "Inventaire des vulnérabilités", "Liste des vulnérabilités connues sur les serveurs exposés et l'état de leur correction. Diffusion restreinte à l'équipe sécurité.", {"securite"}),
    ("D26", "Comptes à privilèges", "Liste des comptes administrateurs, de leurs détenteurs et des coffres de mots de passe. Diffusion restreinte.", {"securite"}),
    ("D27", "Calendrier des formations", "Les sessions de formation interne sont publiées chaque trimestre. L'inscription se fait dans l'outil RH.", {"tous"}),
    ("D28", "Note de service : parking", "Le parking souterrain est réservé aux véhicules partagés le lundi. Les vélos ont un local sécurisé au rez-de-chaussée.", {"tous"}),
    ("D29", "Chiffrement des fichiers", "Les fichiers contenant des données sensibles doivent être chiffrés avant tout envoi à l'extérieur. Utilisez l'outil de chiffrement du portail.", {"tous"}),
    ("D30", "Partager un fichier avec un client", "Utilisez l'espace de partage sécurisé avec une date d'expiration. N'envoyez pas de pièce jointe volumineuse par courriel.", {"tous"}),
]

# Questions et documents attendus (vérité terrain pour mesurer le moteur)
QUESTIONS = [
    ("Comment demander un congé ?", {"D01"}),
    ("J'ai oublié mon mot de passe", {"D05"}),
    ("Comment me connecter au VPN en télétravail ?", {"D04", "D03"}),
    ("J'ai reçu un courriel suspect avec un lien", {"D07"}),
    ("Un client demande l'effacement de ses données", {"D12"}),
    ("Fuite de données personnelles : que faire ?", {"D13"}),
    ("Puis-je copier des données de clients dans un assistant IA ?", {"D14", "D11"}),
    ("On m'a volé mon ordinateur portable", {"D18"}),
    ("Où enregistrer mes fichiers pour la sauvegarde ?", {"D19"}),
    ("Envoyer un fichier volumineux à un client", {"D30", "D29"}),
    ("Grille des salaires par fonction", {"D21"}),
    ("Réponse à un incident de sécurité majeur", {"D24"}),
]

# Question piège : aucun mot utile en commun avec D01, alors qu'elle veut dire la même chose.
# Un moteur lexical la rate ou la trouve avec un score très faible, par hasard des trigrammes.
# Un vrai modèle d'embedding rapprocherait « vacances » et « congé ».
QUESTION_SYNONYME = ("Comment poser mes vacances ?", {"D01"})
