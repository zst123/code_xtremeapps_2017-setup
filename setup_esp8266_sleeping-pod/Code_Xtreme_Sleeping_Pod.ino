#include <ESP8266WiFi.h>
#include "SensitiveDetails.h"
#include <ESP8266HTTPClient.h>

#define SERVER_IP "cxa2017-ws1.sensorup.com"   //port: 80
#define PORT 80
#define AUTH_ENCODED "Authorization: Basic bWFpbjpmMDk2MTFlYy02MGY2LTUyM2ItOGU3NC05NjYwMTkxMjU3N2I=" //cxa2017-ws1 encoded to Base64
#define AUTH_USER "main"
#define AUTH_PASS "f09611ec-60f6-523b-8e74-96601912577b"
#define DATASTREAM_ID_TEMP  491371

unsigned long datastream[] = {DATASTREAM_ID_TEMP};

void setup() {
    Serial.begin(115200);
    delay(3000);
    
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(D2, INPUT);

    // connected
    WiFi.hostname("ESP8266_Jimmy-Neutron");
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);

    // Attempt to connect to Wifi network:
    Serial.print("Connecting Wifi: ");
    Serial.println(NETWORK_SSID);
    WiFi.begin(NETWORK_SSID, NETWORK_PASSWORD);

    while (WiFi.status() != WL_CONNECTED) {
        delay(250);
        digitalWrite(LED_BUILTIN, HIGH); 
        delay(250);
        digitalWrite(LED_BUILTIN, LOW);  
        Serial.print(".");
        delay(250);
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void loop() {
    // LED to the level of input, LED is active-LOW
    digitalWrite(LED_BUILTIN, digitalRead(D2));
    // Post to the server the value of the input
    httpPostToServer(!digitalRead(D2), DATASTREAM_ID_TEMP);
    // Post every 1 sec
    delay(1000);
}

// https://github.com/esp8266/Arduino/issues/1390
void httpPostToServer(double value, unsigned long datastreamId) {
    Serial.println(">> Doing POST");
    Serial.print(">> Value: ");
    Serial.println(value);
    Serial.print(">> Datastream: ");
    Serial.println(datastreamId);

    HTTPClient http;
    http.begin(SERVER_IP, PORT, "/v1.0/Datastreams(" + String(datastreamId) + ")/Observations");
    http.addHeader("Content-Type", "application/json");
    http.setAuthorization(AUTH_USER, AUTH_PASS);

    String str = "{ \"result\": ";
    str += value;
    str += " }";

    int httpCode = http.POST(str);

    // httpCode will be negative on error
    if(httpCode > 0) {
        Serial.println("POST success");
        if(httpCode == HTTP_CODE_OK) {
            String payload = http.getString();
            Serial.println(payload);
        }
    } else {
        Serial.print("POST failed. Error Code: ");
        Serial.println(httpCode);
    }
    http.writeToStream(&Serial);
    http.end();
}

/*
void postToServer(double value,unsigned long datastreamId) {
    Serial.println("connecting...");
    String str = "{ ";
    str += " \"result\":";
    str +=          value;
    str += "}";
    Serial.println(str);

    WiFiClient client;

    // if you get a connection, report back via serial:
    if (client.connect(SERVER_IP, PORT)) {
        Serial.println("connected");
        // Make a HTTP request:
        /*
        client.println("POST /st-playground/proxy/v1.0/Datastreams("+ String(datastreamId) +")/Observations HTTP/1.1");
        String host = "Host: ";
        host.concat(SERVER_IP);
        client.println(host);
        client.println("Connection: close");
        client.println("Content-Type: application/json");
        //String token = "St-P-Access-Token:";
        //token += ACCESS_TOKEN;
        String token = AUTH_ENCODED;

        client.println(token);
        client.println("Cache-Control: no-cache");
        client.print("Content-Length: ");
        client.print(str.length());
        client.print("\n\n");
        client.print(str);*/

      client.println("POST /v1.0/Datastreams(" + String(datastreamId) + ")/Observations HTTP/1.1\r"); 
      Serial.println("POST /v1.0/Datastreams(" + String(datastreamId) + ")/Observations HTTP/1.1\r");
      String observationJson = str;
      /* String host = "Host: ";
      host.concat(SERVER_IP);
      client.println(host);
      Serial.println(host);*/
      
      client.print("Host: ");
      Serial.print("Host: ");
      client.println(SERVER_IP "\r");
      Serial.println(SERVER_IP "\r");
      
      client.println("Connection: close");
      Serial.println("Connection: close");
      client.println("Content-Type: application/json");
      Serial.println("Content-Type: application/json");
      
      client.println(AUTH_ENCODED);     //encoded to Base64 format *** to be commented for scratchpad
      Serial.println(AUTH_ENCODED); 
      
      client.println("Cache-Control: no-cache");
      Serial.println("Cache-Control: no-cache");
      client.print("Content-Length: ");
      Serial.print("Content-Length: ");
      client.println(observationJson.length());
      Serial.println(observationJson.length());
      client.println("");
      Serial.println("");
      //client.print("\n\n");
      //Serial.print("\n\n");
      client.print(observationJson);
      Serial.println("Observation: " + observationJson);
      
        while(true)
        {
            // if there are incoming bytes available
            // from the server, read them and print them:
            if (client.available()) {
                char c = client.read();
                Serial.print(c);
            }

            // if the server's disconnected, stop the client:
            if (!client.connected()) {
                Serial.println();
                Serial.println("disconnecting.");
                client.stop();
                break;
            }
        }
    } else {
        // if you didn't get a connection to the server:
        Serial.println("connection failed");
    }
}
*/
