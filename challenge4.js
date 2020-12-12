function spsgame(yourchoice)
{
    console.log(yourchoice);
    console.log(yourchoice.src);
    var humanchoice,botchoice;
    humanchoice=yourchoice.id;
    botchoice=numberchoice(randtoint());
    console.log(botchoice);
    var result=decidewinner(humanchoice,botchoice);
    console.log(result);
    message=finalmessage(result);
    console.log(message);
    frontend(humanchoice,botchoice,message);
    


}

function randtoint()
{

    return Math.floor(Math.random()*3);
}
function numberchoice(number)
{
    return ['rock','paper','scissors'][number];
}
function decidewinner(yourchoice,botchoice)
{
    var data={
        'rock':{ 'paper':0,'rock':0.5,'scissors': 1},
        'paper':{'scissors':0,'rock':1,'paper':.5},
        'scissors':{'paper':1,'rock':0,'scissors':0.5},
    }
    var yourscore=data[yourchoice][botchoice];
    var botscore=data[botchoice][yourchoice];
    return [yourscore , botscore];
}
function finalmessage([yourscore,botscore])
{
    if(yourscore == 0)
    {  
        return {'message':'you lost!', 'color':'red'};
    }
    else if(yourscore == 0.5){
        return {'message':'Tied!','color':'blue'};
    }
    if(yourscore==1){
        return {'message':'you won!','color':'green'};
    }
}
function frontend(humanimgchoice,botimgchoice,finalmessage)
{
    var database={
        'rock':document.getElementById('rock').src,
        'paper':document.getElementById('paper').src,
        'scissors':document.getElementById('scissors').src,
    }
    document.getElementById('rock').remove();
    document.getElementById('paper').remove();
    document.getElementById('scissors').remove();
    var humandiv=document.createElement('div');
    var botdiv=document.createElement('div');
    var messagediv=document.createElement('div');
    humandiv.innerHTML="<img src='" + database[humanimgchoice] + "' height=150 width=150 style='box-shadow: 0px 10px 50px blue'>" ;
    botdiv.innerHTML="<img src='" + database[botimgchoice] + "' height=150 width=150 style='box-shadow: 0px 10px 50px red'>"
    messagediv.innerHTML="<h1 style='color:"+ finalmessage['color'] + ";font-size:60px ; padding:30px;'>" + finalmessage['message'] +"</h1>";
    document.getElementById('container-1').appendChild(humandiv);
    document.getElementById('container-1').appendChild(messagediv);
    document.getElementById('container-1').appendChild(botdiv);
}
function pagereload()
{
    location.reload();
}