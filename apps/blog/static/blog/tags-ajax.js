(function($){
    var tag_position = $('div#load-tags');
    var url = $('#tags-url', tag_position).attr('href');
    console.log(url);
    $.getJSON(url, function(data){
        var items = [];
        $.each(data, function(key, val){
           items.push("<span style='font-size:1.1em;line-height:200%;' class = 'label label-info'> <a href='" + val + "'>" + key + "</a></span> ");
        });
        tag_position.html(items.join(""));
    });
})(jQuery);
