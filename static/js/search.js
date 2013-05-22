$(function(){
    var ajax_search_url = '/ajax-search/'
    var ajax_type_url = '/ajax-type/'
    var vacancy_url = '/ajax-vacancy/'
    var type_box = $('#type_box');
    var result_box = $('#first_result_box');
    var search_btn = $('#search_btn');
    var vacancy_box = $('#vacancy_box');
    type_box.on('change',function(){
        $('#results_table > tbody:last').empty();
        $('#company_search_btn').remove();
        data = {
            'type_box':$(type_box).val(),
            'csrfmiddlewaretoken':window.csrf
        }
        console.log($('#vacancy_box'));
        if ($('#vacancy_box').css('display') == 'inline-block') {
                    $('#vacancy_box').css('display','none');
                    $('#vacancy_search_btn').remove()
        }
        $.post(ajax_type_url,data)
                .done(function(res){
                result_box.empty();
                result_box.css('display','inline');
            $.each(res, function(i, value) {
            result_box.append($('<option>').text(value.name).attr({'value': value.name, 'id': value.cand_id}));
        });
        })
    });
    result_box.on('change',function(){
        $('#company_search_btn').remove();
        if ($(type_box).val() == 'candidate'){
            if ($('#search_btn').length < 1){
                console.log('renew');
            }
        }else{
            data = {
                'company_id':$('#first_result_box').children(":selected").attr("id")
            }
            $.post(vacancy_url,data)
                .done(function(res){
                vacancy_box.empty();
                vacancy_box.css('display','inline');
                console.log(data);
            $.each(res, function(i, value) {
            vacancy_box.append($('<option>').text(value.name).attr({'value': value.name,'id':value.cand_id}));
            });
        });
    }
    });
    result_box.on('change', function(){
        if ($(type_box).val() == 'candidate'){
        data = {
            'candidate_id':$('#first_result_box').children(":selected").attr("id")
        }
        $.post(ajax_search_url,data).done(function(res){
            $('#results_table > tbody:last').empty()
            $.each(res,function(i,value){
                $('#results_table > tbody:last').append($('<tr>').append(function(){
                    s = '';
                    $.each(value,function(i,json){
                        s = s + ("<td>"+json+"</td>")
                    })
                    return s
                }));
            })
        })
    }
    });
    vacancy_box.on('change',function(){
        data = {
            'vacancy_id':$('#vacancy_box').children(":selected").attr("id")
        }
        $.post(ajax_search_url,data).done(function(res){
            console.log(data);
          $('#results_table > tbody:last').empty();
            $.each(res,function(i,value){
                $('#results_table > tbody:last').append($('<tr>').append(function(){
                    s = '';
                    $.each(value,function(i,json){
                        s = s + ("<td>"+json+"</td>")
                    })
                    return s
                }));
            })
        })
    });

});
