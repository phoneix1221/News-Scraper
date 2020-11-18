$(document).ready(function () {

    var count = 0;

    $('#user_dialog').dialog({
        autoOpen: false,
        width: 400
    });

    // $('#filter_dialog').dialog({
    //     autoOpen: false,
    //     width: 400
    // });

    $('#add').click(function () {
        $('#user_dialog').dialog('option', 'title', 'Add Data');
        $('#first_name').val('');
        $('#last_name').val('');
        $('#date').val('');
        $('#location').val('');
        $('#error_first_name').text('');
        $('#error_last_name').text('');
        $('#error_date').text('');
        $('#error_location').text('');
        $('#first_name').css('border-color', '');
        $('#last_name').css('border-color', '');
        $('#date').css('border-color', '');
        $('#location').css('border-color', '');
        $('#save').text('Save');
        $('#user_dialog').dialog('open');
    });



    // filter button
    // $('.filter').click(function () {
    //     $('#filter_dialog').dialog('option', 'title', 'Add Data');
    //     $('#first_name').val('');
    //     $('#last_name').val('');
    //     $('#error_first_name').text('');
    //     $('#error_last_name').text('');
    //     $('#first_name').css('border-color', '');
    //     $('#last_name').css('border-color', '');
    //     $('#save1').text('Save');
    //     $('#filter_dialog').dialog('open');
    // });




    $('#save').click(function () {
        var error_first_name = '';
        var error_last_name = '';
        var first_name = '';
        var last_name = '';
        var error_date = '';
        var error_location = '';
        var date = '';
        var location = '';


        if ($('#first_name').val() == '') {
            error_first_name = 'First Name is required';
            $('#error_first_name').text(error_first_name);
            $('#first_name').css('border-color', '#cc0000');
            first_name = '';
        }
        else {
            error_first_name = '';
            $('#error_first_name').text(error_first_name);
            $('#first_name').css('border-color', '');
            first_name = $('#first_name').val();
        }

        if ($('#last_name').val() == '') {
            error_last_name = 'Last Name is required';
            $('#error_last_name').text(error_last_name);
            $('#last_name').css('border-color', '#cc0000');
            last_name = '';
        }
        else {
            error_last_name = '';
            $('#error_last_name').text(error_last_name);
            $('#last_name').css('border-color', '');
            last_name = $('#last_name').val();
        }

        if ($('#date').val() == '') {
            error_date = 'First Name is required';
            $('#error_date').text(error_date);
            $('#date').css('border-color', '#cc0000');
            date = '';
        }
        else {
            error_date = '';
            $('#error_date').text(error_date);
            $('#date').css('border-color', '');
            date = $('#date').val();
        }
        if ($('#location').val() == '') {
            error_location = 'Last Name is required';
            $('#error_location').text(error_location);
            $('#location').css('border-color', '#cc0000');
            location = '';
        }
        else {
            error_location = '';
            $('#error_location').text(error_location);
            $('#location').css('border-color', '');
            location = $('#location').val();
        }







        if (error_first_name != '' || error_last_name != '' || error_date != '' || error_location != '') {
            return false;
        }
        else {
            if ($('#save').text() == 'Save') {
                count = count + 1;
                output = '<tr id="row_' + count + '">';
                output += '<td>' + first_name + ' <input type="hidden" name="hidden_first_name[]" id="first_name' + count + '" class="first_name" value="' + first_name + '" /></td>';
                output += '<td>' + last_name + ' <input type="hidden" name="hidden_last_name[]" id="last_name' + count + '" value="' + last_name + '" /></td>';
                output += '<td>' + date + ' <input type="hidden" name="hidden_date[]" id="date' + count + '" value="' + date + '" /></td>';
                output += '<td>' + location + ' <input type="hidden" name="hidden_location[]" id="location' + count + '" value="' + location + '" /></td>';

                output += '<td><button type="button" name="view_details" class="btn btn-warning btn-xs view_details" id="' + count + '">View</button></td>';
                output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="' + count + '">Remove</button></td>';
                output += '</tr>';
                // $('#user_data').append(output);

            }
            else {
                var row_id = $('#hidden_row_id').val();
                output = '<td>' + first_name + ' <input type="hidden" name="hidden_first_name[]" id="first_name' + row_id + '" class="first_name" value="' + first_name + '" /></td>';
                output += '<td>' + last_name + ' <input type="hidden" name="hidden_last_name[]" id="last_name' + row_id + '" value="' + last_name + '" /></td>';
                output += '<td>' + date + ' <input type="hidden" name="hidden_date[]" id="date' + row_id + '" value="' + date + '" /></td>';
                output += '<td>' + location + ' <input type="hidden" name="hidden_location[]" id="location' + row_id + '" value="' + location + '" /></td>';

                // output += '<td><button type="button" name="view_details" class="btn btn-warning btn-xs view_details" id="' + row_id + '">View</button></td>';
                // output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="' + row_id + '">Remove</button></td>';
                $('#row_' + row_id + '').html(output);
            }

            $('#user_dialog').dialog('close');
        }
    });




    $(document).on('click', '.view_details', function () {
        var row_id = $(this).attr("id");
        var first_name = $('#first_name' + row_id + '').val();
        var last_name = $('#last_name' + row_id + '').val();
        var date = $('#date' + row_id + '').val();
        var location = $('#location' + row_id + '').val();
        $('#first_name').val(first_name);
        $('#last_name').val(last_name);
        $('#date').val(date);
        $('#location').val(location);
        $('#save').text('Edit');
        $('#hidden_row_id').val(row_id);
        $('#user_dialog').dialog('option', 'title', 'Edit Data');
        $('#user_dialog').dialog('open');
    });


    // filter addition Button
    // $(document).on('click', '.filter', function () {
    //     var row_id = $(this).attr("id");
    //     var date = $('#date' + row_id + '').val();
    //     var location = $('#location' + row_id + '').val();
    //     $('#date').val(date);
    //     $('#location').val(location);
    //     $('#save1').text('Edit');
    //     $('#hidden_row_id').val(row_id);
    //     $('#filter_dialog').dialog('option', 'title', 'Filter Data');
    //     $('#filter_dialog').dialog('open');
    // });



    // $('#save1').click(function () {
    //     var error_date = '';
    //     var error_location = '';
    //     var date = '';
    //     var location = '';

    //     if (error_date != '' || error_location != '') {
    //         return false;
    //     }
    //     else {
    //         if ($('#save1').text() == 'Save') {
    //             count = count + 1;
    //             output = '<tr id="row_' + count + '">';
    //             output += '<td>' + date + ' <input type="hidden" name="hidden_first_name[]" id="first_name' + count + '" class="first_name" value="' + date + '" /></td>';
    //             output += '<td>' + location + ' <input type="hidden" name="hidden_last_name[]" id="last_name' + count + '" value="' + location + '" /></td>';

    //             output += '<td><button type="button" name="filter" class="btn btn-warning btn-xs filter" id="' + count + '">Apply Filter</button></td>';
    //             output += '<td><button type="button" name="view_details" class="btn btn-warning btn-xs view_details" id="' + count + '">View</button></td>';
    //             output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="' + count + '">Remove</button></td>';
    //             output += '</tr>';
    //             $('#user_data1').append(output);

    //         }
    //         else {
    //             var row_id = $('#filter_hidden_row_id').val();
    //             output = '<td>' + date + ' <input type="hidden" name="hidden_first_name[]" id="first_name' + row_id + '" class="first_name" value="' + date + '" /></td>';
    //             output += '<td>' + location + ' <input type="hidden" name="hidden_last_name[]" id="last_name' + row_id + '" value="' + location + '" /></td>';
    //             output += '<td><button type="button" name="filter" class="btn btn-warning btn-xs filter" id="' + row_id + '">Apply Filter</button></td>';
    //             output += '<td><button type="button" name="view_details" class="btn btn-warning btn-xs view_details" id="' + row_id + '">View</button></td>';
    //             output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="' + row_id + '">Remove</button></td>';
    //             $('#row_' + row_id + '').html(output);
    //         }

    //         $('#filter_dialog').dialog('close');
    //     }
    // });






    $(document).on('click', '.remove_details', function () {
        var row_id = $(this).attr("id");
        if (confirm("Are you sure you want to remove this row data?")) {
            $('#row_' + row_id + '').remove();
        }
        else {
            return false;
        }
    });

    $('#action_alert').dialog({
        autoOpen: false
    });

    $('#user_form').on('submit', function (event) {
        event.preventDefault();
        var count_data = 0;
        $('.first_name').each(function () {
            count_data = count_data + 1;
        });
        if (count_data > 0) {
            var form_data = $(this).serialize();
            $.ajax({
                url: "insert.php",
                method: "POST",
                data: form_data,
                success: function (data) {
                    $('#user_data').find("tr:gt(0)").remove();
                    $('#action_alert').html('<p>Data Inserted Successfully</p>');
                    $('#action_alert').dialog('open');
                }
            })
        }
        else {
            $('#action_alert').html('<p>Please Add Atleast one Entry</p>');
            $('#action_alert').dialog('open');
        }
    });




});
