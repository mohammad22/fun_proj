// This should be put at the end of html template. It dynamically populates the links for the images in the markup version of the html document. 
// the template should provide <a> elemnets of class
// "imager 'title'", where 'title' matches the value of 'alt' property 
// of the image in the markup 
(function(){
    var a_imagers = $("a.imager");
    if (a_imagers.length > 0){ 
        $("img").each(function (idx){
            var image = $(this);
            var title = "." + image.prop('alt');
            var link = a_imagers.filter(title).prop('href');
            image
                .prop('src', link)
                .addClass('img-responsive') 
                .load();
        });
    }
})();
