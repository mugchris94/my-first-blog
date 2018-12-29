$(windows).scroll(function(){
    var headtop= $('.header');
    var scroll= $(windows).scrollTop();
    if (scroll > 500){
      headtop.addClass('animateheader');
      headtop.slideDown(300);

    }
    else{
      headtop.removeClass('animateheader');
    }

});
