print("""
_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                          Fr3dywood                              
""")

print("Bienvenue, noble aventurier, sur l’Île aux Merveilles Perdues. Votre quête, si vous l’acceptez, est de découvrir le légendaire Saphir des Âges, un artefact aux pouvoirs incommensurables.")

premier_choix = input("\nVous pénétrez dans une grotte scintillante où des runes anciennes illuminent faiblement les parois. "
                      "Deux tunnels s’ouvrent devant vous : l’un exhale une brume violette mystique, l’autre semble vibrer d’une lueur dorée. "
                      "Où allez-vous ? (V pour violette, D pour dorée) : ")

if premier_choix.upper() == "D":
    print("\nÀ peine avez-vous franchi l’arche dorée qu’un vortex temporel vous aspire ! "
          "Vous vous retrouvez piégé dans une boucle infinie, condamné à revivre cette décision pour l’éternité. Fin tragique.")
elif premier_choix.upper() == "V":
    deuxieme_choix = input("\nVous avancez prudemment et découvrez un gobelin spectral gardant un coffre ancien. "
                           "Il ne semble pas vous voir... Voulez-vous attaquer ou attendre patiemment qu'il s’éloigne ? "
                           "(A pour attaquer, P pour patienter) : ")

    if deuxieme_choix.upper() == "A":
        print("\nVous frappez avec bravoure, mais le gobelin se transforme en un dragon fantôme ! "
              "Dans un souffle ardent, il réduit votre corps en poussière cosmique. GAME OVER.")
    elif deuxieme_choix.upper() == "P":
        troisieme_choix = input("\nVous vous tapissez dans l’ombre et attendez. Le gobelin spectral marmonne des incantations avant de disparaître dans un tourbillon de fumée violette. "
                                "Un frisson vous parcourt l’échine tandis que vous avancez prudemment dans une immense salle illuminée par des cristaux flottants, vibrant au rythme d’une énergie ancienne.\n\n"
                                "Deux portes se dressent devant vous :\n"
                                "- Une porte bleue, parcourue d’arcs électriques mystiques, pulsant d’une énergie magique indéchiffrable.\n"
                                "- Une porte rouge, plus discrète, gravée de symboles anciens et dégageant une chaleur inquiétante.\n\n"
                                "Laquelle choisissez-vous ? (B pour la porte bleue, R pour la porte rouge) : ")

        if troisieme_choix.upper() == "R":
            print("\nVous rentrez tout doucement, puis vous entendez un murmure... Vous vous approchez et BAM ! "
                  "La porte se ferme violemment derrière vous. Les murs commencent à se resserrer lentement... Vous êtes piégé. GAME OVER.")
        elif troisieme_choix.upper() == "B":
            print("\nVous franchissez prudemment la porte bleue. À l’instant où vous posez le pied de l’autre côté, "
                  "une sensation électrique parcourt votre corps.\n"
                  "Soudain, la salle s’illumine d’un bleu éclatant et une silhouette éthérée apparaît devant vous : "
                  "un Gardien d’Arcane, un être de pure magie aux yeux scintillants comme des étoiles.\n")

            quatrieme_choix = input("Le Gardien vous fixe et prononce d’une voix résonnante :\n"
                                    "'Seul l’élu digne du Saphir des Âges pourra franchir cette épreuve.'\n"
                                    "Sur un piédestal, trois objets flottent en lévitation :\n"
                                    "- Une plume dorée iridescente.\n"
                                    "- Une dague ornée de runes argentées.\n"
                                    "- Un cristal brisé dégageant une lueur fantomatique.\n\n"
                                    "Quel objet choisissez-vous ? (P pour la plume, D pour la dague, C pour le cristal) : ")

            if quatrieme_choix.upper() == "P":
                print("\nDès que vous saisissez la plume, elle se transforme en une clé lumineuse !\n"
                      "Le Gardien incline la tête en signe d’acceptation, et une porte secrète s’ouvre derrière lui, "
                      "révélant un escalier menant aux profondeurs cachées de l’île...\n"
                      "Votre aventure continue vers le Saphir des Âges !")
            elif quatrieme_choix.upper() == "D":
                print("\nVous saisissez la dague runique, mais dès que vous la brandissez, le Gardien s’agite violemment.\n"
                      "Ses yeux deviennent flamboyants et, d’un geste, il invoque une tempête d’éclairs qui vous foudroie sur place.\n"
                      "Votre aventure s’achève ici... GAME OVER.")
            elif quatrieme_choix.upper() == "C":
                print("\nEn touchant le cristal brisé, une étrange sensation de vide s’empare de vous.\n"
                      "Soudain, vous réalisez avec horreur que votre corps devient transparent.\n"
                      "Vous êtes piégé entre les mondes, condamné à errer à jamais dans ce temple oublié...\n"
                      "GAME OVER.")