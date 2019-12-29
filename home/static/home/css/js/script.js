/***************************************************************************
*
* SCRIPT JS
*
***************************************************************************/

$(document).ready(function(){
    
    //Scale in SP
    // if(screen.width < 768) {
    //     $('meta[name=viewport]').attr('content','width=device-width, initial-scale=1');
    // }

    // $(window).resize(function () {
    //     if(screen.width < 768) {
    //         $('meta[name=viewport]').attr('content','width=device-width, initial-scale=1');
    //     }
    // });


    // Hover Button for All Pages
    $('.hoverJS').hover(function(){
        $(this).stop().fadeTo(100,0.8);
    },function(){
        $(this).stop().fadeTo(100,1);
    });
    

    //Click event to scroll to top
    $('.scrollToTop').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
    });


    //Scroll Anchor

    $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });

});