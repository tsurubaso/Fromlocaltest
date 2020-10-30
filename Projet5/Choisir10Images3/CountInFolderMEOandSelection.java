package com.company;

import tech.tablesaw.api.DoubleColumn;
import tech.tablesaw.api.StringColumn;
import tech.tablesaw.api.Table;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class CountInFolderMEOandSelection {

    public static void countInFolderMEOandSelection(String nomDossier) throws Exception {

       // List<File> result3 = CheckNumberOfFolders.checkNumberOfFolders2(nomDossier); //selection

        List<File> result = EraseKokaiSelectionInsideMeo.eraseKokaiSelectionInsideMeo1(nomDossier); //Simple MEO file

        List<Double> nombre1a = new ArrayList<>();

        List<String> nom1a = new ArrayList<>();



        //List<Double> nombre2a = new ArrayList<>();

        Table t = Table.create();

        for (File file : result) { //
            System.out.println(file.getName()); //
            File[] listOfFiles = file.listFiles();
            assert listOfFiles != null;
            System.out.println("Nombres de Files/Directory dans le dossier: " + listOfFiles.length);
            nombre1a.add((double) listOfFiles.length);
            nom1a.add(file.getName());

        }

        Double[] nombreBB = new Double[nombre1a.size()];
        String[] nom = new String[nom1a.size()];

        nombreBB = nombre1a.toArray(nombreBB);
        nom = nom1a.toArray(nom);

        DoubleColumn column1a = DoubleColumn.create("Nombres pour MEO",nombreBB  ); //pour compter contenu des dossiers
        StringColumn column0 = StringColumn.create("Nom fichier MEO", nom);//nom2

        t.addColumns(column1a);
        t.addColumns(column0);

        t.write().csv("test.csv");//"\uFEFF" t6.write().csv("test.csv");



        //

    }








}
