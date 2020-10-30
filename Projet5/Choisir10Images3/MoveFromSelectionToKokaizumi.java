package com.company;

import tech.tablesaw.api.Table;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class MoveFromSelectionToKokaizumi {

    public static void moveFromSelectionToKokaizumi(String nomDossier4) throws Exception {
        Table t4 = ListDirectoryInFolder.listDirectoryInFolder(nomDossier4);
        Table t4a= Table.create("Resume")
                .addColumns(t4.column(2), t4.column(4));

        t4.write().csv("test.csv");
        t4a.write().csv("testa.csv");
        System.out.println("regardons la table pour voir si il y a un probleme:");
        System.out.println(t4a);
        Scanner myObj3 = new Scanner(System.in);
        System.out.println("Petite vérif et appuye sur:1 ");
        int boucleavance = myObj3.nextInt();
        if (boucleavance==1){;}
        else {;}
        for (int iz = 0; iz < t4.rowCount(); ) {
            String Lepathz = t4.get(iz, 3).toString();
            String Lepath2z = t4.get(iz, 5).toString();
            System.out.println("le dossier d'origine: " + Lepathz);
            System.out.println("le dossier de destination: " + Lepath2z);
            File dirOrigz = new File(Lepathz);
            String[] filesOrigz = dirOrigz.list();
            int iaz = 0;
            while (iaz < filesOrigz.length) {

                Path temp = Files.move(Paths.get(Lepathz + "\\" + filesOrigz[iaz]), Paths.get(Lepath2z + "\\" + filesOrigz[iaz]));
                iaz++;
            }


            iz = iz + 1;
            System.out.println("Bon, maintenant i est egal a: " + iz);

        }

    }
















}
