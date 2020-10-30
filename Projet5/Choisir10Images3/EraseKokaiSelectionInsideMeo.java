package com.company;



import java.awt.*;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;


public class EraseKokaiSelectionInsideMeo {

    public static List<File> eraseKokaiSelectionInsideMeo1(String nomDossier) throws Exception {

        File file = new File(nomDossier);
        File[] listOfFiles = file.listFiles();
        List<File> result = new ArrayList<>();



        for (int i = 0; i < Objects.requireNonNull(listOfFiles).length; i++) {
            if (listOfFiles[i].isDirectory()) {
                if (!(listOfFiles[i].getName().startsWith("selection"))) {
                    if (!(listOfFiles[i].getName().startsWith("Selection"))) {
                        if (!(listOfFiles[i].getName().startsWith("Kokaizumi"))) {

                            System.out.println("Directory Name: " + listOfFiles[i].getName());
                            // assert result != null;
                             result.add(listOfFiles[i]);
                            //

                        }
                    }

                }
            }
        }

        return result;


    }

    public static List<File> eraseKokaiSelectionInsideMeo2(List<File> result) throws Exception {

        List<File> result2 = new ArrayList<>();

        for (int i = 0; i < result.size(); i++) {
            System.out.println("Valeur de i est:" + i);
            String leNoma = result.get(i).getName();
            System.out.println("Le nom du dossier est:" + leNoma);

            File[] listFilesInResult = result.get(i).listFiles();
            assert listFilesInResult != null;
            System.out.println("Dans le dossier il y a : " + listFilesInResult.length + " files");
            for (File file : listFilesInResult) {
                if (file.isDirectory()) {
                    assert false;
                    result2.add(file);
                }
            }
        }

        return result2;
    }

    public static void eraseKokaiSelectionInsideMeo3(List<File> result) throws Exception {


        for (int i = 0; i < result.size(); i++) {
            System.out.println("Valeur de i est:" + i);

            String leNoma = result.get(i).getName();
            System.out.println("Le nom du dossier est:" + leNoma);


            Scanner myObja = new Scanner(System.in);
            System.out.println("Est ce que j'efface o/n ?:");
            String boucleavance = myObja.nextLine();
            if (boucleavance.startsWith("o")) {

                result.get(i).delete();
            } else {
                System.out.println("Bon, ok on efface pas");
                Desktop.getDesktop().open(new File(result.get(i).getPath()));
            }
        }
    }

    public static void eraseKokaiSelectionInsideMeo(String nomDossier) throws Exception {
        List<File> result = eraseKokaiSelectionInsideMeo1(nomDossier);
        List<File> result2 = eraseKokaiSelectionInsideMeo2(result);
        eraseKokaiSelectionInsideMeo3(result2);



    }

}
