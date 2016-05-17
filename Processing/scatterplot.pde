void setup() {
size(1000,500); 
background(255);
scale(1, -1);
translate(0, -height);

Table table = loadTable("data.csv", "header");

  for (TableRow row : table.rows()) {
    
    float health = row.getFloat("health");
    float income = row.getFloat("income");
    int population = row.getInt("population");
    
    float health_m = map(health,50,90,0,height);
    float income_log = log(income);
    float income_m = map(income_log,2.7, 5.13,0,width/4);
    float population_m =map(population,0,1376048943,1,140);
    
    ellipse(income_m,health_m,population_m,population_m);
  }
}