//alert("hello");
function ageindays()
{
    var birthyear=prompt('When you were born my friend ?');
    var ageindayss=(2020-birthyear)*365;
    console.log(ageindayss);
    var h1=document.createElement('h1');
    var textanswer=document.createTextNode('you are '+ ageindayss+' days old.');
    h1.setAttribute('id','ageindays');
    h1.appendChild(textanswer);
    document.getElementById('result').appendChild(h1);
}
function reset()
{
    document.getElementById('ageindays').remove();
}