'use strict';
// with strict mode, you can not, for example, use undeclared variables

// Note: visualization will be put in the div with id=vis1_id

const margin = { top: 20, right: 160, bottom: 35, left: 30 };

const width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;


/* Data in strings like it would be if imported from a csv */

// var parse = d3.time.format("%Y").parse;

function drawData(data) {

    // make sure features are numbers
    data.forEach(function (d) {
        d.Confirmed = +d.Confirmed || 0;
        d.Deaths = +d.Deaths || 0;
        d.Recovered = +d.Recovered || 0;
    });

    // pretty cool ... let us aggregate data
    var aggdata = d3.nest()
        .key(d => d['Country/Region'])
        .rollup(function (v) {
            return {
                recordings: v.length,
                confirmed: d3.sum(v, function (d) { return d['Confirmed'] }),
                deaths: d3.sum(v, function (d) { return d['Deaths'] }),
                recovered: d3.sum(v, function (d) { return d['Recovered'] })
            };
        })
        .entries(data);

    var values = aggdata.map(d => {
        return {
            country: d.key,
            recordings: d.value.recordings,
            confirmed: d.value.confirmed,
            deaths: d.value.deaths,
            recovered: d.value.recovered,
            remaining: d.value.confirmed - d.value.deaths - d.value.recovered,
        }
    }).sort(function (a, b) { return b.confirmed - a.confirmed; });

    console.log('Values:', values)

    // manipulate data into stacked series
    const features = ['deaths', 'recovered', 'remaining']
    var stack = d3.stack().keys(features)
    var series = stack(values)

    // finally data is prepared for our stacked bar
    console.log('Series:', series)

    const barheight = 10

    const getCountry = (id) => {
        return values[id].country
    }

    var yScale = d3.scaleLinear()
        .domain([0, values.length])
        .range([margin.top, height - margin.bottom])
        
    var xScale = d3.scaleLinear()
        .domain(d3.extent(values, function(d) { return d.confirmed; }))
        .range([margin.left, width - margin.right])
    
    var yAxis = d3.axisLeft(yScale)

    var colorScale = d3.scaleOrdinal()
        .domain(features)
        .range(d3.schemeCategory10)

    var svg = d3.select("body").select("#vis1_id")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")


    // div for the tooltip
    var tooltip = d3.select("body").select("#vis1_id")
	.append("div")
	.style("position", "absolute")
	.style("z-index", "10")
    .style("visibility", "hidden")
    .style("background", "white")
    .style("padding", "2px")
    
    // add a group for each row of data
    var layer = svg.selectAll("g")
        .data(series)
        .enter()
        .append("g")
        .style("fill", (d, i) => colorScale(i))

    // add a rect for each data value 
    layer
        .selectAll("rect")
        .data(d => d)
        .enter()
        .append("rect")
        .attr("x", function (d, i) { return xScale(d[0])})
        .attr("y", function (d, i) { return yScale(i)})
        .attr("height", barheight)
        .attr("width", function (d, i) { return xScale(d[1]-d[0])})
        .on("mouseover", function (d, i) { 
            return tooltip.text(getCountry(i)).style("visibility", "visible") 
        })
        .on("mousemove", function() { 
            return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px") 
        })
        .on("mouseout", function (d, i) { 
            return tooltip.text("").style("visibility", "hidden") 
        })

    // add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

}

