def clear_msg(request):
    request.session.peek_flash('msg').clear()

def flash_msg(request, message):
    request.session.flash(message, 'msg')

def pop_msg(request):
    return request.session.pop_flash('msg')[0]

def delete_whitespace(text):
    import re
    return re.sub(r"\s", "", text)
