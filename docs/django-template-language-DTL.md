[Django template language](https://docs.djangoproject.com/en/2.0/topics/templates/)

A Django template is simply a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.

The syntax of the Django template language involves four constructs.

* Variables

* Tags

* Filters

* Comments

[Built-in template tags and filters](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#ref-templates-builtins-filters)

Loops, Blocks, If-else, Tags etc. [Read this great document](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#ref-templates-builtins-filters)

```
{{ value|add:"2" }}
```

[Django template language for Python programmers](https://docs.djangoproject.com/en/2.0/ref/templates/api/)

[Writing custom filters](https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#howto-writing-custom-template-filters)