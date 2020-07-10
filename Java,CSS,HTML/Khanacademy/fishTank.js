background(89, 216, 255);

function fish(centerX,centerY,bodyColor,bodyLength){






var bodyHeight = 74;


noStroke();
fill(bodyColor);
// body
ellipse(centerX, centerY, bodyLength, bodyHeight);
// tail
var tailWidth = bodyLength/4;
var tailHeight = bodyHeight/2;
triangle(centerX-bodyLength/2, centerY,
         centerX-bodyLength/2-tailWidth, centerY-tailHeight,
         centerX-bodyLength/2-tailWidth, centerY+tailHeight);
// eye
fill(33, 33, 33);
ellipse(centerX+bodyLength/4, centerY, bodyHeight/5, bodyHeight/5);
}         

function SeaWeed(x1,y1,cx1,cy1,cx2,cy2,x2,y2,SeaColor){
fill(SeaColor);
bezier(x1,y1,cx1,cy1,cx2,cy2,x2,y2);    
}
function pebble(x,y,w,h,rockColor){
    
fill(rockColor);
ellipse(x,y,w,h);
}


mouseClicked = function() {
    fish(mouseX, mouseY, color(random(0,244), random(0,244), random(0,244)),random(-200, 200));
};

pebble(439,380,155,62,color(199, 189, 189));
pebble(203,397,155,36,color(199, 189, 189));
pebble(54,380,155,62,color(199, 189, 189));
fish(232,269,color(156, 224, 197),135);
SeaWeed(401, 432, 267, 209, 335, 164, 276, 408,color(178, 178, 189));
SeaWeed(136, 403, 296, 233, 243, 294, 25, 406,color(178, 178, 189));
SeaWeed(120, 465, 226, 268, 9, 121, 48, 348,color(66, 173, 87));
SeaWeed(157, 416, 288, 258, 211, 137, 102, 403,color(66, 173, 87));
SeaWeed(390, 408, 210, 130, 472, 73, 298, 409,color(66, 173, 87));

fish(242,59,color(0, 153, 255),-147);
fish(175,110,color(0, 183, 255),-126);
