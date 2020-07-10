var colour = [color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250)),color(0,random(0,100),random(100,250))];

var xPositions = [0,0,0,0,0,0,0,0,0,0];
var yPositions = [0,0,0,0,0,0,0,0,0,0];

var rain = function() {
draw = function() {
    background(133, 204, 217);

    noStroke();
    fill(0, 200, 255);



        
      
        for (var i = 0; i < xPositions.length; i++ ) {
        
        fill(colour[i]);
        if (i === 1) {
        image(getImage("avatars/aqualine-seed"), xPositions[i], yPositions[i], 30, 30);    
        }
        else{    
        ellipse(xPositions[i], yPositions[i], 10, 10);
        }
        yPositions[i] += random(2,50);
        
        
        if (yPositions[i] > 400) {
         yPositions[i] = 0;
         xPositions[i] = random(0,400);
         //playSound(getSound("retro/laser1"));   
        }
        
        
        
        }


};
};
rain();

