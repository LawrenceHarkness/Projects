var bodyW = 200;
var faceW = bodyW/2;
var bodyX = 0;
var bodyY = 0;
bodyX = bodyW/1;
bodyY = bodyW/1;



draw = function() {
    background(207, 254, 255);
    fill(106, 161, 145);
    ellipse(bodyX, bodyY, bodyW, bodyW/2.5); // body?
    fill(93, 176, 49);
    ellipse(bodyX, bodyY, faceW, faceW/2); // face?
    
    fill(93, 176, 49);
    ellipse(bodyX/0.75, bodyY/0.86, bodyW/4, bodyW/4);
    ellipse(bodyX/1.5, bodyY/0.86, bodyW/4, bodyW/4);
    fill(255, 255, 255);
    ellipse(bodyX/1.28, bodyY, bodyW/10,bodyW/10); 
    ellipse(bodyX/0.82, bodyY, bodyW/10,bodyW/10);
    ellipse(bodyX/1.28, bodyY, bodyW/100,bodyW/100); 
    ellipse(bodyX/0.82, bodyY, bodyW/100,bodyW/100);

    bodyW = bodyW + 1;   

};
