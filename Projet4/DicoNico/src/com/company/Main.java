package com.company;

//Notes

//https://api.lexicala.com/

//https://www.programmableweb.com/category/dictionary/api

//http://kong.github.io/unirest-java/
/*



 */
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.ObjectMapper;


import kong.unirest.HttpResponse;
import kong.unirest.JsonNode;

import kong.unirest.Unirest;
import kong.unirest.json.JSONObject;


import java.io.*;
import java.util.*;


public class Main {

    //Values

    String motacherch = "briser";



    public void  gettest() throws IOException {



        HttpResponse<JsonNode> response = Unirest.get("https://dictapi.lexicala.com/search?source=global&language=fr&text="+motacherch)
                .basicAuth("tsurubaso", "25decembre73")
                .asJson();
        System.out.println( "---------------------------------------------" );

        JSONObject responsejson = (JSONObject) response.getBody().getObject();
        System.out.println( responsejson);

        System.out.println( "---------------------------------------------" );

        Map<String, Object> map;
        map = (HashMap<String, Object>) new ObjectMapper().readValue(responsejson.toString(), LinkedHashMap.class);
        System.out.println(map.get("results"));

        System.out.println( "---------------------------------------------" );

        List<Map<String, Object>> results = (List<Map<String, Object>>)map.get("results");

        System.out.println( "---------------------------------------------" );
        //System.out.println( results );
        List<Map<String, Object>> results33 = (List<Map<String, Object>>)results.get(0).get("senses");
        System.out.println( results33.get(0).get("definition") );
        System.out.println( results33.get(1).get("definition") );




    }



    public static void main(String[] args) throws IOException {
        Main client = new Main();

        client.gettest();
    }
}
