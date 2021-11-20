$(document).ready(function () {
    console.warn = (e) => {console.log(`Error ${e} has occured. `)};
    var cookie = getCookie('user');
    $(".edit-report").click(function(){
        $.ajax({
            url:"/./requestHandler/reports/scHandler/",
            type:"get",
            data: {
                requestcookie : cookie.replace('"',''),
                requestId     : $(this).attr('something')
            },
            success: function(response){
                console.log(response.response);
                $('#invoiceId').val(response.invoiceId);
                $('#noItem').val(response.noitem);
                $('#breakage').val(response.breakage);
                $('#damaged').val(response.damaged);
                $('#shortage').val(response.shortage);
                $('#remarks').val(response.remarks);
                $('#model').modal('show');
            },
            error: function(response){
                window.location = '/./dashboard/notice/'
                console.log('HERE')
            }
        });
    });
});


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }