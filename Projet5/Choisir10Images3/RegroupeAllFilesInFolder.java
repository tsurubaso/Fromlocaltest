package com.company;

import java.io.File;
import java.io.IOException;
import java.nio.file.*;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

//Never use this 2 times in a row!!!
//All moved files will be erased!!!!
//You have only 2 chances
public class RegroupeAllFilesInFolder {

    public static void regroupeAllFilesInFolder(String nomDossier) throws Exception {
        List<String> result = listfilesnotfolders(nomDossier);
        Path path=createFolder(nomDossier);
        moveAllFilesFromAtoB (result, path);


    }

    public static List<String> listfilesnotfolders(String nomDossier) throws Exception {
        List<String> result = null;
        try (Stream<Path> walk = Files.walk(Paths.get(nomDossier))) {

            result = walk.filter(Files::isRegularFile)
                    .map(Path::toString).collect(Collectors.toList());
            // result.forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
        //result.forEach(System.out::println);
        return result;

    }

    public static Path createFolder(String nomDossier) throws Exception {
        Path path= null;
        try {

           path = Paths.get(nomDossier + "\\AllFilesContainer");


            //java.nio.file.Files;
            if (!path.toFile().exists()) {
                Files.createDirectories(path);
                System.out.println("Directory is created!");
            }
            else {
                path = Paths.get(nomDossier + "\\AllFilesContainer2");
                Files.createDirectories(path);
                System.out.println("Second Directory is created!");
            }



        } catch (IOException e) {

            System.err.println("Failed to create directory!" + e.getMessage());

        }
        System.out.println("nomDossier = " + path);
        return path;
    }

    public static void moveAllFilesFromAtoB(List<String> listfiles, Path toFile) throws Exception {




        listfiles.forEach((file) ->  {        // --> Iterate through the filenames and move
                {
                    File Grapu = new File(file);
                    String Gname = Grapu.getName();

                    // renaming the file and moving it to a new location
                    if(Grapu.renameTo
                            (new File(toFile+"\\"+Gname)))
                    {
                        // if file copied successfully then delete the original file
                        Grapu.delete();
                        System.out.println("File moved successfully");
                    }
                    else
                    {
                        System.out.println("Failed to move the file");
                    }
                }



        });


    }

}
