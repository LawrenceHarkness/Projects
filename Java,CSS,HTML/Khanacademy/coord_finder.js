fill(17, 0, 255);
fill(255, 0, 255);


draw = function() {
    
    //POINTER
    background(255, 255, 255);
    ellipse(mouseX, mouseY, 12, 12); 
    var MouseX = mouseX;
    var MouseY = mouseY;    
    var label = MouseX + "," + MouseY;
    text(label, mouseX + 10,mouseY+ -5 );
    var x = 0;
    var y = 0;

    //coords
    while(x <= 400) {
    x = x + 50;
    text(x, x, 13);  
    text(x,13,x);
    //cross
    line(mouseX,mouseY,mouseX,0);
    line(mouseX,mouseY,0,mouseY);
    line(mouseX,mouseY,mouseX,400);
    line(MouseX,MouseY,400,MouseY);
   
    }   
    


};






// a handy dandy ruler across the top

