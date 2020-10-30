package com.company;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class ViderKokaizumi {

    public static void viderKokaizumi(String nomDossier) throws Exception {
        List<File> result = viderKokaizumi1(nomDossier);
        viderKokaizumi2(result);
    }

    public static List<File> viderKokaizumi1(String nomDossier) throws Exception {
        File file = new File(nomDossier);
        File[] listOfFiles = file.listFiles();
        List<File> result = new ArrayList<>();

        for (int i = 0; i < Objects.requireNonNull(listOfFiles).length; i++) {
            if (listOfFiles[i].isDirectory()) {
                        if (listOfFiles[i].getName().startsWith("Kokaizumi")) {

                            System.out.println("Directory Name: " + listOfFiles[i].getName());
                            //
                            result.add(listOfFiles[i]);
                            //
                        }
                    }
                }
        return result;
            }

    public static void viderKokaizumi2(List<File> result) throws Exception {

        List<File> result2 = new ArrayList<>();

        for (int i = 0; i < result.size(); i++) {
            System.out.println("Valeur de i est:" + i);
            String leNoma = result.get(i).getName();
            System.out.println("Le nom du dossier est:" + leNoma);

            File[] listFilesInResult = result.get(i).listFiles();
            assert listFilesInResult != null;
            System.out.println("Dans le dossier il y a : " + listFilesInResult.length + " files");
            for (File file : listFilesInResult) {
                if (file.exists()) {
                    file.delete();

                }
            }
        }


    }









    }




