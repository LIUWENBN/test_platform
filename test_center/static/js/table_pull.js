$(function() {
    $("#table tbody").sortable({
        start: function(event, ui) {
            // 在拖动开始时，记录每个行的原始位置
            let index = ui.item.index();
            ui.item.data('index', index);
        },
        stop: function(event, ui) {
            // 在拖动结束时，获取新的行顺序
            let oldIndex = ui.item.data('index');
            let newIndex = ui.item.index();
            if (oldIndex != newIndex) {
                // 通过 AJAX 请求将新的顺序发送到服务器
                $.ajax({
                    url: '/face/tablePull', // 后端处理排序的URL
                    type: 'POST',
                    data: {
                        newIndex: newIndex,
                        oldIndex: oldIndex,
                        // 你可能还需要发送其他数据给服务器，例如用例ID等
                    },
                    success: function(response) {
                        // 在请求成功后，你可以更新你的表格数据，或者进行其他操作
                    },
                    error: function(error) {
                        // 在请求失败时处理错误
                    }
                });
            }
        }
    });
});