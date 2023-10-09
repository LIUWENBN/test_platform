$('#case_add').click(function(){
    var case_name = $('#cas_name').val();
    var owner_project = $('#cas_owner_project').val();
    var owner_business = $('#cas_owner_business').val();
    var case_relation = $('#cas_relation').val();
    var case_relation_key = $('#cas_relation_key').val();
    var case_header = $('#cas_header').val();
    var case_method = $('#cas_method').val();
    var case_url = $('#cas_url').val();
    var case_data = $('#cas_data').val();
    var case_exp_result = $('#cas_exp_result').val();
    var case_verify_type = $('#cas_verify_type').val();
    var case_waite = $('#cas_waite').val();
    var case_info = $('#cas_info').val();
    var serial_num = $('#cas_serial_num').val();
    var verify_value = $('#cas_verify_value').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            case_name: case_name,
            owner_project: owner_project,
            owner_business: owner_business,
            case_relation: case_relation,
            case_relation_key: case_relation_key,
            case_header: case_header,
            case_method: case_method,
            case_url: case_url,
            case_data: case_data,
            case_exp_result: case_exp_result,
            case_verify_type: case_verify_type,
            case_waite: case_waite,
            case_info: case_info,
            serial_num: serial_num,
            verify_value: verify_value
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/caseList';
            }
        },
        fail: function(e){
            alert(e)
        }
    });


});

$('#case_update').click(function(){
    var case_name = $('#cas_name').val();
    var owner_project = $('#cas_owner_project').val();
    var owner_business = $('#cas_owner_business').val();
    var case_relation = $('#cas_relation').val();
    var case_relation_key = $('#cas_relation_key').val();
    var case_header = $('#cas_header').val();
    var case_method = $('#cas_method').val();
    var case_url = $('#cas_url').val();
    var case_data = $('#cas_data').val();
    var case_exp_result = $('#cas_exp_result').val();
    var case_verify_type = $('#cas_verify_type').val();
    var case_waite = $('#cas_waite').val();
    var case_info = $('#cas_info').val();
    var case_id = $('#cas_id').val();
    var serial_num = $('#cas_serial_num').val();
    var verify_value = $('#cas_verify_value').val();
    var url = $(this).attr('data-url');

    $.ajax({
        url: url,
        type: 'post',
        data: {
            case_name: case_name,
            owner_project: owner_project,
            owner_business: owner_business,
            case_relation: case_relation,
            case_relation_key: case_relation_key,
            case_header: case_header,
            case_method: case_method,
            case_url: case_url,
            case_data: case_data,
            case_exp_result: case_exp_result,
            case_verify_type: case_verify_type,
            case_waite: case_waite,
            case_id: case_id,
            serial_num: serial_num,
            verify_value: verify_value,
            case_info: case_info
        },
        success: function(data){
            if (data.log){
                alert(data.msg);
            }else{
                alert(data.msg);
                window.location.href='/face/caseList';
            }
        },
        fail: function(e){
            alert(e)
        }
    });


});

