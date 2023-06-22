setting = document.getElementById('setting')
close= document.getElementById('close_btn')

setting.addEventListener('click', function(){
    document.getElementById('setting_container').style.display= 'grid'
})

close.addEventListener('click',function(){
    document.getElementById('setting_container').style.display= 'none'
})