$(document).ready(function () {
    $("#clicking").click(function(){
        var input_text = document.getElementById('texting').value;
        console.log('Texting');
        $.ajax({
            url:"/./requestHandler/notifications/",
            type:"get",
            data: {
                button_tex: input_text
            },
            success: function(response){
                jQuery('#texting').attr("id","texted");
                jQuery('#clicking').attr("id","clicked");
                $("#app").append(`
                <form action="javascript:void(0);">
                    <input id="texting" type="text" placeholder="Type text here" />&nbsp;
                    <button id="clicking">
                        Click
                    </button>
                </form>
                `);
                

            }
    
        });

    });
});