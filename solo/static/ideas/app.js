  $('#comment_form').submit(function(event) {
    event.preventDefault()
    var form = $(this)
    var post_id = $(this).attr('post_id')

    $.ajax({
      url: `/ideas/${post_id}/add_comment`,
      method: 'post',
      data: form.serialize(),
      success: function(response) {
        console.log(response)
        $('.display_comment').html(response)
      }
    })

  })

  $(document).ready(function() {

    $('.likers').tooltip()
  })



