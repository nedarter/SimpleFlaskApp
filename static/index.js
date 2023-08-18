

function DrawGraphs()
{

    //Pull the period from our drop down list
    period = d3.select("#Period").property("value")

    //Call into your flask route called  /LoadData/<period>
    //This is running off of your server that you created, so it will run whatever
    //python code you want
    d3.json("/LoadData/" + period).then(data=> {
    
        trace = {
            x : data.map(obj => obj.Sex), 
            y : data.map(obj => obj.AvgScore),
            type : "bar"
        }
    
        Plotly.newPlot("Plot", [trace] )  

    })

}

//Call Draw Graphs whenever the dropdown is changed
d3.select("#Period").on("change", DrawGraphs)

//Call DrawGraphs when the page loads
DrawGraphs()

