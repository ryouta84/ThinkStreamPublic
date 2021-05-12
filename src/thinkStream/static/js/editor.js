window.onload = function () {
    if ($('.editor').length) {
        var src = $('.editor').val();
        var html = marked(src);
        $('.markdown').html(html);
    }

    if ($('.raw_markdown').length) {
        $('.raw_markdown').each(function () {
            var src = $(this).html();
            var html = marked(src);
            $(this).next('.markdown').html(html)
        });
    }
}

$(function () {
    marked.setOptions({
        langPrefix: ''
    });

    if ($('.editor').length) {
        $('.editor').keyup(function () {
            var src = $(this).val();
            var html = marked(src);
            $('.markdown').html(html);
        });
    }
});
