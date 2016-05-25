(function($){
    var tag_position = $('div#load-tags');
    var url = $('#tags-url', tag_position).attr('href');
    //console.log(url);
    $.getJSON(url, function(data){
        $.each(data, function(key, val){
            var label = $('<span><a></a></span> ')
                        .attr('style', 'font-size:1em')
                        .attr('line-height', '300%')
                        .addClass('label label-info')
                        .find('a')
                        .attr('href', val)
                        .text(key)
                        .end()
                        .appendTo(tag_position);
            var dummy = $('<span> </span>').appendTo(tag_position); 
        });
    });
})(jQuery);
