function mjview(ed1)
{
    var currentcol=$(ed1).closest('tr');
    var col1=currentcol.find('td:eq(0)').text();
    console.log(col1)
    $.ajax({
        url :"websiteviews",
        type:'POST',
        dataType: "json",
        contentType: "application/json", 
        data:JSON.stringify({
            'newwebget':col1
        })
    });
    window.location="/load"
}

function mjedit(ed1)
{
    var currentcol=$(ed1).closest('tr');
    var col1=currentcol.find('td:eq(0)').text();
    $.ajax({
        url :"websiteform",
        type:'POST',
        dataType: "json",
        contentType: "application/json", 
        data:JSON.stringify({
            'newwebget':col1
        })
    });
    window.location="/loadform"

}

function mjdelete(ed1)
{
    var currentcol=$(ed1).closest('tr');
    var col1=currentcol.find('td:eq(0)').text();
    
    $.ajax({
        url :"del",
        type:'POST',
        dataType: "json",
        contentType: "application/json", 
        data:JSON.stringify({
            'newwebget':col1
        })
    });
    window.location="/"
    


}

function redirect_to_home()
{
    window.location="/home"
}

function mjdel(ed1)
{
    var currentcol=$(ed1).closest('tr');
    var col1=currentcol.find('td:eq(0)').text();
    var col2=currentcol.find('td:eq(1)').text();
    
    $.ajax({
        url :"delview",
        type:'POST',
        dataType: "json",
        contentType: "application/json", 
        data:JSON.stringify({
            'newwebget':col1,
            'keyword':col2
        })
    });
    window.location="/load"
    


}