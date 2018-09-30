
function stretchMap() {
    $("#mainMap").width($("html").width())
    $("#mainMap").height($("html").height())
}

function MoscowMap(id) {
    return new ymaps.Map(
        id,
        {
            center: [55.76, 37.64],
            zoom: 10,
            controls: []
        },
        {
            restrictMapArea : true
        }
    );
}

function addSpeedBumpView(map) {
    $.get(
        '/SpeedBumps',
        function(data) {
            bumpCollection = new ymaps.GeoObjectCollection();
            for (speedbump in data) {
                bumpCollection.add(new ymaps.Placemark(data[speedbump].coordinates, {
                    balloonContent: data[speedbump].street
                }, {
                    preset: 'islands#circleIcon',
                    openEmptyBaloon: true
                }));
            }
            map.geoObjects.add(bumpCollection);
        }
    )
}

function addCarCountView(map) {
    $.get(
        '/CarCount',
        function(data) {
            countCollection = new ymaps.GeoObjectCollection();
            for (c in data) {
                countCollection.add(
                    new ymaps.Placemark(data[c].coordinates, {
                        iconContent : data[c].count,
                        balloonContent : "<b>Количество проехавших машин</b>: " + data[c].count + "<br><b>Суммарная масса</b>: " + data[c].summaryWeight + " (тонн)"
                    }, {
                        preset : "islands#redCircleIcon"
                    })
                )
            }
            map.geoObjects.add(countCollection);
        }
    )
}

function headerAlign() {
    headerJ = $('#header');
    headerJ.children().css('display', 'block');
    headerJ.children().css('width', 100/headerJ.children().length + '%');
}

function switchView(map, view_func_add) {
    return function() {
        map.geoObjects.removeAll();
        view_func_add(map);
    }
}

function setupPage() {
    stretchMap();
    headerAlign();
    $("#header").prop('hidden', false);
    $(window).resize(stretchMap);
    $(window).resize(headerAlign);
    ymaps.ready(function() {
        var map = MoscowMap("mainMap");
        addSpeedBumpView(map);
        $("#speedbump-button").click(switchView(map, addSpeedBumpView));
        $("#carcount-button").click(switchView(map, addCarCountView));
        window.map = map;
    });
}
