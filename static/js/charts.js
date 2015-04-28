google.load("visualization", "1", {packages:["geochart"]});
google.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {

    var data = google.visualization.arrayToDataTable([
      ['Название аудитории', 'Количесвто', "Бюджет"],
      ['Germany', 200, 1000],
      ['United States', 300, 1000],
      ['Brazil', 400, 1000],
      ['Canada', 500, 1000],
      ['France', 600, 1000],
      ['RU', 700, 1000]
    ]);

    var options = {
        backgroundColor: { fill:'transparent' }
    };

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
}
google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Year', 'Sales', 'Expenses'],
      ['2013',  1000,      400],
      ['2014',  1170,      460],
      ['2015',  660,       1120],
      ['2016',  1030,      540]
    ]);

    var options = {
        backgroundColor: { fill:'transparent' },
      title: 'Company Performance',
      hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
      vAxis: {minValue: 0}
    };

    var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
    chart.draw(data, options);


}
google.load("visualization", "1", {packages:["timeline"]});
google.setOnLoadCallback(drawChartTimeline);
function drawChartTimeline() {
    var container = document.getElementById('timeline');
    var chart = new google.visualization.Timeline(container);
    var dataTable = new google.visualization.DataTable();

    dataTable.addColumn({ type: 'string', id: 'President' });
    dataTable.addColumn({ type: 'date', id: 'Start' });
    dataTable.addColumn({ type: 'date', id: 'End' });
    dataTable.addRows([
      [ 'Marketing activity', new Date(2015, 1, 1), new Date(2015, 1, 30) ],
      [ 'Inside activity',      new Date(2015, 2, 1),  new Date(2015, 2, 30) ],
      [ 'Revenue streams',      new Date(2015, 3, 1),  new Date(2015, 3, 30) ],
      [ 'KPI',      new Date(2015, 1, 1),  new Date(2015, 3, 1) ],
      [ 'Costs',      new Date(2015, 1, 1),  new Date(2015, 3, 1) ],
      [ 'Total revenue',  new Date(2015, 1, 1),  new Date(2015, 3, 1) ]]);

    chart.draw(dataTable);
}
