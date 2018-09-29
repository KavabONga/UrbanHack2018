navigator.__defineGetter__('userAgent', function(){
    return 'foo';
});
ymaps.ready( function() {
    var map = new ymaps.Map(
        "map",
        {
            center: [55.76, 37.64],
            zoom: 10
        }
    );
});
