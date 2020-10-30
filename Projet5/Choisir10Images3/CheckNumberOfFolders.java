package com.company;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class CheckNumberOfFolders {

    public static void checkNumberOfFolders1(String nomDossier) throws Exception {

        List<File> result3 =checkNumberOfFolders2(nomDossier); //selection

        List<File> result2 =ViderKokaizumi.viderKokaizumi1(nomDossier); //Kokaizumi

        List<File> result =EraseKokaiSelectionInsideMeo.eraseKokaiSelectionInsideMeo1(nomDossier); //Simple MEO file

        for (int i = 0; i < result.size(); i++) {
            System.out.println("Valeur de i est:" + i);
            String leNoma = result.get(i).getName();
            System.out.println("Le nom du dossier est:" + leNoma);
            System.out.println("Donc maintenant cherchons des Dossiers selection et Kokaizumi du meme nom, Utilisons un Boolean");
            boolean KokaizumiExist = false;
            for (File value : result2) {
                if (value.getName().contains(leNoma)) {
                    KokaizumiExist = true;
                    System.out.println("Directory exists already!");
                    break;
                }
            }
            if (!KokaizumiExist){
                System.out.println("Mes amis, pas de dossier Kokaizumi, creons en un!");
                File file = new File(nomDossier + "\\" + "Kokaizumi " + leNoma);
                file.mkdir();
            }
            boolean selectionExist = false;
            for (File value : result3) {
                if (value.getName().contains(leNoma)) {
                    selectionExist = true;
                    System.out.println("Directory exists already!");
                    break;
                }
            }
            if (!selectionExist){
                System.out.println("Mes amis, pas de dossier Selection, creons en un!");
                File filea = new File(nomDossier + "\\" + "selection " + leNoma);
                filea.mkdir();
            }
        }
    }


    public static List<File> checkNumberOfFolders2(String nomDossier) throws Exception {

            File file = new File(nomDossier);
            File[] listOfFiles = file.listFiles();
            List<File> result3 = new ArrayList<>();

            for (int i = 0; i < Objects.requireNonNull(listOfFiles).length; i++) {
                if (listOfFiles[i].isDirectory()) {
                    if (listOfFiles[i].getName().startsWith("Selection") || listOfFiles[i].getName().startsWith("selection"))
                            { System.out.println("Directory Name: " + listOfFiles[i].getName());
                                // assert result != null;
                                result3.add(listOfFiles[i]);
                                //
                        }
                    }
                }
        return result3;
            }

        }



