function correct(){
swal("Thanks !", "Data Uploaded !",  {
    position: 'top-end',
    icon: 'success',
    button: false, 
    title: 'Thanks',
    showConfirmButton: false,
    timer: 1300,
});
}
function incorrect(){
swal("Sorry !", "Data Invalid !",  {
    position: 'top-end',
    icon: 'error',
    button: false, 
    title: 'Sorry !',
    showConfirmButton: false,
    timer: 1300,
});
}
function warning(){
swal("Warning !", "Not Right !",  {
    position: 'top-end',
    icon: 'warning',
    button: false, 
    title: 'Warning !',
    showConfirmButton: false,
    timer: 1300,
});
}
function custom_alert(title, message, icon, time){
swal(title, message,  {
    position: 'top-end',
    icon: icon,
    button: false, 
    title: title,
    showConfirmButton: false,
    timer: time,
});
}