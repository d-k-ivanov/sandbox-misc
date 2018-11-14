#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dis

class C: pass
def my_func(): pass

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__ == '__main__':
    print('---------------------------------------------------------------------------')
    obj = C()
    print(dir(obj))
    print()
    print(dir(my_func))
    print()
    print(sorted(set(dir(my_func)) - set(dir(obj))))

    print('---------------------------------------------------------------------------')

    print(dis.dis(my_func.__code__))
    print(dis.code_info(my_func.__code__))

    print('---------------------------------------------------------------------------')

    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name="img"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))

    print('---------------------------------------------------------------------------')

    def f(a, *, b):
        return a, b
    print(f(1, b=2))

    print('---------------------------------------------------------------------------')

    import inspect

    sig2 = inspect.signature(tag)
    print(type(sig2))
    print(repr(sig2))
    print(str(sig2))
    for name, param in sig2.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    bound_args = sig2.bind(**my_tag)
    print(bound_args)

    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    print('---------------------------------------------------------------------------')
