from django.shortcuts import redirect


__all__ = [ 'home' ]


def home(_):
    return redirect('bolsista_list')
