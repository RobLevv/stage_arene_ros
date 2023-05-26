# Stage_Ros

Ce contient un résumé de mon avancement pendant le stage, il complète le fichier avancement.txt qui énumère simplement les tâches.
Je vais aussi essayer d'expliquer mes choix.

On a dans le dossier urdf les fichiers qui contiennent les objets barrier et traffic_lights, ils sont ensuite utilisé dans le monde arene.world

Le fichier arene.world a été sauvegardé avec tous les objets à l'intérieur, les fichiers urdf ont donc été utilisés une seule fois à la première création du monde. Pour modifier la position initiale des objets il faut aller dans la section ll.150-360 les objets en fin de fichiers sont là pour décrire leur dynamique.

Dans les scripts on a plusieurs essais, actuellement la barrière est controlée en applicant un moment à l'endroit du moteur pendant 1 seconde puis il y a des frottements sur le liaisons pour éviter qu'elle redescende. De la même façon, les feux sont controlés en les déplacant selon une glissière linéaire, il y a aussi des frottements pour éviter qu'ils redescendent. Pour l'instant j'utilise des rosservice pour appliquer les forces mais je vois que ca rend lent le programme par dessus gazebo qui demande déjà beaucoup de ressources. Je vais essayer de passer par des topics ce qui sera plus rapide, j'ai trouvé comment agir sur les liaisons avec le topic "/gazebo/set_link_state" mais il y a trop de paramètres à rentrer pour que ca soit pratique. Je vais essayer de trouver un autre topic qui permet de controler la position des objets.

Mon objectif est de pouvoir contrôler avec précision les position des objets (barrière et feux) peut etre que je peux contrôler un peu de la même facon qu'avec les forces puisque tous les déplacements sont limités, je peux essayer d'applliquer une vitesse constante pendant un temps donné pour atteindre la position limite, cela paraitra contrôlé.

Dans les launch on a le checkup.launch pour vérifier l'état des robots réels, les display pour barrier et traffic_lights pour afficher dans Rviz et le world_arene.launch pour lancer le monde gazebo avec tous les obstacles.

J'ai créé un type de message pour le contrôle, je m'en servirait surement pour faire l'interface entre le robot et l'arene. Il est dans le dossier msg.
