package com.company;

//Notes

//https://api.lexicala.com/

//https://www.programmableweb.com/category/dictionary/api

//http://kong.github.io/unirest-java/



import kong.unirest.HttpResponse;
import kong.unirest.JsonNode;

import kong.unirest.Unirest;
import kong.unirest.json.JSONArray;
import kong.unirest.json.JSONObject;
import tech.tablesaw.api.DateColumn;
import tech.tablesaw.api.StringColumn;
import tech.tablesaw.api.Table;
import tech.tablesaw.columns.Column;


import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;


public class Main {

    //Values

    String motacherch = "porte";



    public void  gettest(){



       HttpResponse<JsonNode> response = Unirest.get("https://dictapi.lexicala.com/search?source=global&language=fr&text="+motacherch+"&analyzed=true")
               .basicAuth("user", "password")
               .asJson();
       Object Resultat = response.getBody().getObject().get("n_results");
       System.out.println( Resultat);
       JSONObject responsejson = response.getBody().getObject();
       //JSONArray results = responsejson//.getJSONArray("n_results");
       // System.out.println( results);
        System.out.println( "---------------------------------------------" );
/*
    HttpResponse<JsonNode> response2 = Unirest.get("https://dictapi.lexicala.com/users/me")
            .basicAuth("tsurubaso", "25decembre73")
            .asJson();
        System.out.println( response2.getBody());
        JSONObject responsejson = response2.getBody().getObject();
        JSONObject results = responsejson.getJSONObject("usage").getJSONObject("today");
        Object results2=results.get("count");
        System.out.println( results2);

*/
}



    public static void main(String[] args) {
        Main client = new Main();

        client.gettest();
    }
}
