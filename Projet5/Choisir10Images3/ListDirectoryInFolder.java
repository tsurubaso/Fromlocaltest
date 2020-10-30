package com.company;

import tech.tablesaw.api.StringColumn;
import tech.tablesaw.api.Table;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class ListDirectoryInFolder {


    public static Table listDirectoryInFolder(String nomDossier) throws Exception {

        File file = new File(nomDossier);
        File[] listOfFiles = file.listFiles();
        Table t = Table.create();
        List<String> noma = new ArrayList<>();
        List<String> patha = new ArrayList<>();
        List<String> nomb = new ArrayList<>();
        List<String> pathb = new ArrayList<>();
        List<String> nomc = new ArrayList<>();
        List<String> pathc = new ArrayList<>();
        //Nombre de fichiers dans le dossier



        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isDirectory()) {
                if (listOfFiles[i].getName().startsWith("Selection")||listOfFiles[i].getName().startsWith("selection")){
                    //System.out.println("Directory Name: " + listOfFiles[i].getName());
                    nomb.add(listOfFiles[i].getName());
                    //System.out.println("Directory Path: " + listOfFiles[i].getAbsolutePath());
                    pathb.add(listOfFiles[i].getAbsolutePath());
                }
                else if (listOfFiles[i].getName().startsWith("Kokaizumi")){
                    //System.out.println("Directory Name: " + listOfFiles[i].getName());
                    nomc.add(listOfFiles[i].getName());
                    //System.out.println("Directory Path: " + listOfFiles[i].getAbsolutePath());
                    pathc.add(listOfFiles[i].getAbsolutePath());
                }
                else
                {//System.out.println("Directory Name: " + listOfFiles[i].getName());
                    noma.add(listOfFiles[i].getName());
                    //System.out.println("Directory Path: " + listOfFiles[i].getAbsolutePath());
                    patha.add(listOfFiles[i].getAbsolutePath());}


            }
        }

        String[] nom2 = new String[noma.size()];
        String[] path2 = new String[patha.size()];
        String[] nom3 = new String[nomb.size()];
        String[] path3 = new String[pathb.size()];
        String[] nom4 = new String[nomc.size()];
        String[] path4 = new String[pathc.size()];

        nom2 = noma.toArray(nom2);
        path2 = patha.toArray(path2);
        nom3 = nomb.toArray(nom3);
        path3 = pathb.toArray(path3);
        nom4 = nomc.toArray(nom4);
        path4 = pathc.toArray(path4);

        StringColumn column0 = StringColumn.create("Nom fichier", nom2);//nom2
        StringColumn column1 = StringColumn.create("Path1", path2 ); //path2
        StringColumn column2 = StringColumn.create("Nom dossier selection", nom3); // nom3
        StringColumn column3 = StringColumn.create("Path2", path3 ); //path3
        StringColumn column4 = StringColumn.create("Nom dossier Kokaizumi",nom4); //
        StringColumn column5 = StringColumn.create("Path3",path4 ); //


        t.addColumns(column0);
        t.addColumns(column1);
        t.addColumns(column2);
        t.addColumns(column3);
        t.addColumns(column4);
        t.addColumns(column5);

        //System.out.println(t);
        t.write().csv("test2.csv");
        return t;


    }



























}
