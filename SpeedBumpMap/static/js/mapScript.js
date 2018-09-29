
function stretchMap() {
    $("#mainMap").width($("html").width())
    $("#mainMap").height($("html").height())
}

function setupMap() {
    stretchMap();
    $(window).resize(stretchMap);
    ymaps.ready(function() {
        var map = new ymaps.Map(
            "mainMap",
            {
                center: [55.76, 37.64],
                zoom: 10,
                'options' : {
                    'restrictMapArea' : [[55.924852, 37.275692], [55.572014, 37.938992]]
                }
            }
        );
    });
}
