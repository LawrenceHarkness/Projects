var book = [
            {
             title: "The Giver",
            stars: 4,
            color: color(161, 237, 215),
            author: "Jimmy King",
            recommend: "yes"
            },     
            {   
            title: "The Taker",
            stars: 2,
            color: color(250, 225, 5),
            author: "King Jimmy",
             recommend: "es"
            },
            {
            title: "Bread",
            stars: 4,            
            color: color(237, 229, 185),
            author: "John Dough",
            recommend: "yes"
            
            },
            {
            title: "MekMan",
            stars: 1,            
            color: color(215, 155, 219),
            author: "Charlie Brown",
            recommend: "no"
            
            },
            {
             title: "James Bond",
            stars: 4,
            color: color(94, 94, 130),
            author: "Ian Fleming",
            recommend: "yes"
            },     
            {   
            title: "Flying away",
            stars: 1,
            color: color(5, 250, 50),
            author: "Jamie Cowl",
             recommend: "es"
            },
            {
            title: "Dread",
            stars: 2,            
            color: color(230, 0, 50),
            author: "Carl Hogin",
            recommend: "no"
            
            },
            {
            title: "MekMan2",
            stars: 2,            
            color: color(151, 86, 156),
            author: "Charlie Brown",
            recommend: "no"
            
            },
            {
            title: "Flying Pigs",
            stars: 4,            
            color: color(199, 196, 255),
            author: "KJ",
            recommend: "yes"
            
            },
            {
            title: "MekMan3",
            stars: 1,            
            color: color(122, 38, 128),
            author: "Charlie Brown",
            recommend: "no"
            
            },
            {
            title: "FN guid ",
            stars: 1,            
            color: color(79, 70, 19),
            author: "Ninja",
            recommend: "no"
            
            },
            {
            title: "MC guide",
            stars: 4,            
            color: color(152, 255, 115),
            author: "Lawrence",
            recommend: "yes"
            
            },
];





// draw shelf
for (var i = 0; i < 3 ;i++){
var jump = i * 130;
fill(173, 117, 33);
rect(0, 120 + jump, width, 10);
}



// draw lots of books
var rowNum = -1;
var colNum = -1;
for (var a = 0; a < book.length ; a++ ){
    if ((a % 4)=== 0){
    rowNum++;
    colNum = -1;
    
    }
    colNum++;
    var jumpY = rowNum * 130;
    var jump = colNum * 97;
    fill(book[a].color);
    rect(10 + jump, 20 + jumpY, 90, 100);
    fill(0, 0, 0);
    text(book[a].title, 15 + jump, 29 + jumpY, 70, 100);
    text(book[a].author, 15 + jump, 44 + jumpY, 70, 100);
    if (book[a].recommend === "yes") {
        image(getImage("cute/Heart"), 40 + jump, 55 + jumpY, 18, 38);
    }
    else{
    image(getImage("creatures/OhNoes"), 40 + jump, 74 + jumpY, 18, 20);        
        
    }
    for (var i = 0; i < book[a].stars; i++) {
        image(getImage("cute/Star"), 13 + i * 20 + jump, 90 + jumpY, 20, 30);


    }    
}

