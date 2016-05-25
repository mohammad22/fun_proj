(function($){
    var tag_position = $('div#load-tags');
    var url = $('#tags-url', tag_position).attr('href');
    //console.log(url);
    $.getJSON(url, function(data){
        var items = [];
        $.each(data, function(key, val){
            var label = $('<span ><a></a></span> ')
                        .attr('style', 'font-size:1em')
                        .attr('line-height', '200%')
                        .addClass('label label-info')
                        .find('a')
                        .attr('href', val)
                        .text(key)
                        .end()
                        .appendTo(tag_position);
            var dummy = $('<p></p>').appendTo(tag_position); 
        });
    });
})(jQuery);
