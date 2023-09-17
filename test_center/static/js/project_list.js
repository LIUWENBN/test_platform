$('#project_add').click(function(){
    var project_name = $('#proj_name').val();
    var project_code = $('#proj_code').val();
    var project_type = $('#proj_type').val();
    var base_url = $('#proj_base_url').val();
    var project_header = $('#proj_header').val();
    var project_method = $('#proj_method').val();
    var login_url = $('#proj_login_url').val();
    var project_data = $('#proj_data').val();
    var token_name = $('#proj_token_name').val();
    var project_info = $('#proj_info').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            project_name: project_name,
            project_code: project_code,
            project_type: project_type,
            base_url: base_url,
            project_header: project_header,
            project_method: project_method,
            login_url: login_url,
            project_data: project_data,
            token_name: token_name,
            project_info: project_info
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/projectList?page=1';
            }
        },
        fail: function(e){
            alert(e)
        }
    });


});

$('#project_edit').click(function(){
    var project_name = $('#proj_name').val();
    var project_code = $('#proj_code').val();
    var project_type = $('#proj_type').val();
    var base_url = $('#proj_base_url').val();
    var project_header = $('#proj_header').val();
    var project_method = $('#proj_method').val();
    var login_url = $('#proj_login_url').val();
    var project_data = $('#proj_data').val();
    var token_name = $('#proj_token_name').val();
    var project_info = $('#proj_info').val();
    var project_id = $('#proj_id').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            project_name: project_name,
            project_code: project_code,
            project_type: project_type,
            base_url: base_url,
            project_header: project_header,
            project_method: project_method,
            login_url: login_url,
            project_data: project_data,
            token_name: token_name,
            project_id: project_id,
            project_info: project_info
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/projectList?page=1';
            }
        },
        fail: function(e){
            alert(e)
        }
    });


});
