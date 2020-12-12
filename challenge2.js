function table()
{

    var num=prompt('enter the number 1');
    for(var i=1;i<11;i++)
    {
        var product=num*i;
        var v=document.createElement('v');
        var answer=document.createTextNode(num+' * '+ i + ' = ' +product+ ' ');
        


        v.setAttribute('id','result1');
        v.appendChild(answer );
        document.getElementById('result').appendChild(v);
        
    }
    


}
function reset()
{
    document.getElementById('result').innerHTML=" ";
}
