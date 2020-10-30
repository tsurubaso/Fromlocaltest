package com.company;

import tech.tablesaw.api.DoubleColumn;
import tech.tablesaw.api.Table;

import java.awt.*;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CheckIfEnoughFiles {


    public static void  checkIfEnoughFiles(String nomDossier3) throws Exception {

        Table t3 = ListDirectoryInFolder.listDirectoryInFolder(nomDossier3);
        //System.out.println(t3.columnNames());
        t3.sortAscendingOn("Nom fichier");
        //System.out.println(t3);
        DoubleColumn nc = DoubleColumn.create("nombreDePhotos",t3.rowCount());
        t3.addColumns(nc);
        String input;
        double selectParDossier=0;
        for (int i = 0; i <t3.rowCount(); ) { //t3.rowCount()
            String Lepatha = t3.get(i, 1).toString();
            String Lepath2a =  t3.get(i, 3).toString();
            System.out.println("le dossier d'origine: "+ Lepatha);
            System.out.println("le dossier de destination: "+ Lepath2a);
            Scanner myObj = new Scanner(System.in);
            System.out.println("Entre le nombre necessaire de photos:");
            double nbrphnec = myObj.nextDouble();
            nc.set(i,nbrphnec);
            File dir = new File(Lepath2a);
            File dirOrig = new File(Lepatha);
            double nbrSelecionesa = nbrphnec;
            System.out.println("nombre de photos necessaires: "+ nbrSelecionesa);
            String[] files = dir.list();
            String[] filesOrig = dirOrig.list();
            assert files != null;
            System.out.println( "Nombres d'images dans le dossier Selection: "+files.length);
            List<Integer> hazardNumbers = new ArrayList<>();
            int nbrrestant= (int) (nbrSelecionesa-files.length);
            System.out.println("le nombre de files necessaire est "+nbrrestant);
            while (hazardNumbers.size()<nbrrestant){
                assert filesOrig != null;
                int idz=(int)(Math.random()*filesOrig.length);
                if (filesOrig[idz].endsWith(".JPG")) {
                    if (!hazardNumbers.contains(idz)) {
                        hazardNumbers.add(idz);
                    }
                }

            }

            System.out.println("les photos choisies au Hasard: "+ hazardNumbers);
            //System.out.println(hazardNumbers.get(0));
            int ia = 0;
            while (ia<hazardNumbers.size()) {

                Path temp = Files.move (Paths.get(Lepatha+"\\"+filesOrig[hazardNumbers.get(ia)]),
                        Paths.get(Lepath2a+"\\"+filesOrig[hazardNumbers.get(ia)]));
                ia++;
            }
            Desktop.getDesktop().open(dir);
            Desktop.getDesktop().open(dirOrig);
            Scanner myObj3 = new Scanner(System.in);
            System.out.println("On augmente de combien la boucle?:");
            int boucleavance = myObj3.nextInt();
            i=i+boucleavance;
            System.out.println("Bon, maintenant i est egal a: "+i);
            //System.out.println(t3);
        }

    }
















}
