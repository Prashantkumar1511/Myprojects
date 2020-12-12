
function generatecat()
{
    var image=document.createElement('img');
    image.src="http://thecatapi.com/api/images/get?format=src&type=gif&size=small";
    document.getElementById('container-2').appendChild(image);
}
