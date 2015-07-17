import processing.net.*;

Server server;
Client client;
String input;
int data[];

void setup() {
 size(450, 255);
 background(204);
 stroke(0);
 frameRate(5);
 server = new Server(this, 12345); 
}

void draw() {
 if (mousePressed == true) {
  stroke(255);
  line(pmouseX, pmouseY, mouseX, mouseY);
  //server.write(pmouseX + " " + pmouseX + " " + mouseX + " " + mouseY + "\n");
 } 
 
 client = server.available();
 if (client != null) {
  input = client.readString();
  println(input);
  input = input.substring(0, input.indexOf("\n"));
  data = int(split(input, ' '));
  stroke(0);
  line(data[0], data[1], data[2], data[3]); 
 }
}
