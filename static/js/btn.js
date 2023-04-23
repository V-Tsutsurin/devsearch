var floatingButton = document.getElementById('floating-button');
var popup = document.querySelector('.popup');
var close = document.querySelector('.close');
floatingButton.addEventListener('click', function(){
   popup.style.display = 'block';
});
close.addEventListener('click', function(){
  popup.style.display = 'none';
  });

//
// $(document).ready(function (){
//     function heightBlock(column){
//         var myblock = 0;
//
//         column.each(function (){
//             thisHight = $(this).height();
//             if (thisHight > myblock){
//                 myblock = thisHight;
//             }
//         });
//         column.height(myblock);
//     }
//
//     heightBlock($(".row > li"));
//     });