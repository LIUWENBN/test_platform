$('#business_add').click(function(){
    var business_name = $('#busi_name').val();
    var business_code = $('#busi_code').val();
    var owner_project = $('#busi_owner_project').val();
    var business_info = $('#busi_info').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            business_name: business_name,
            business_code: business_code,
            owner_project: owner_project,
            business_info: business_info
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/businessScene';
            }
        },
        fail: function(e){
            alert(e)
        }
    });

});

$('#business_update').click(function(){
    var business_name = $('#busi_name').val();
    var business_code = $('#busi_code').val();
    var owner_project = $('#busi_owner_project').val();
    var business_info = $('#busi_info').val();
    var business_id = $('#busi_id').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            business_name: business_name,
            business_code: business_code,
            owner_project: owner_project,
            business_info: business_info,
            business_id: business_id
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/businessScene';
            }
        },
        fail: function(e){
            alert(e)
        }
    });

});
