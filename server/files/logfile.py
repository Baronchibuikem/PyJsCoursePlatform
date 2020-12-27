Internal Server Error: /
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\view.py", line 45, in get_operation
    responses = self.get_responses()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\view.py", line 180, in get_responses
    response_serializers = self.get_response_serializers()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\view.py", line 235, in get_response_serializers
    responses = self.get_default_responses()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\view.py", line 211, in get_default_responses
    default_schema = self.serializer_to_schema(default_schema) or ''
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\openapi.py", line 690, in setdefault
    ret = maker()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\drf_yasg\inspectors\field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `image` is not valid for model `CustomUser`.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 57, in validate_password
    if self.password == self.confirm_password:
AttributeError: 'RegistrationSerializer' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 57, in validate_password
    if payload["password"] == payload["confirm_password"]:
TypeError: string indices must be integers
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 57, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 57, in validate_password
    if self.password == self.confirm_password:
AttributeError: 'RegistrationSerializer' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 57, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 58, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 58, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 58, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 61, in validate_password
    if payload.password == payload.confirm_password:
AttributeError: 'str' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 58, in validate_password
    password = data.get('password')
AttributeError: 'str' object has no attribute 'get'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 80, in validate_type
    if self.type != payload['INSTRUCTOR'] or self.type != payload["STUDENTS"] or payload is None:
AttributeError: 'RegistrationSerializer' object has no attribute 'type'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 86, in validate_type
    if self.type != payload['INSTRUCTOR'] or self.type != payload["STUDENTS"] or payload is None:
AttributeError: 'RegistrationSerializer' object has no attribute 'type'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 87, in validate_type
    if self.type != payload['INSTRUCTOR'] or self.type != payload["STUDENTS"] or payload is None:
AttributeError: 'RegistrationSerializer' object has no attribute 'type'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 21, in post
    'user': user.pk,
AttributeError: 'collections.OrderedDict' object has no attribute 'pk'
Internal Server Error: /accounts/account/customuser/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\options.py", line 607, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\utils\decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\cache.py", line 44, in _wrapped_view_func
    response = view_func(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\sites.py", line 231, in inner
    return view(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\utils\decorators.py", line 43, in _wrapper
    return bound_method(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\utils\decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\options.py", line 1720, in changelist_view
    response = self.response_action(request, queryset=cl.get_queryset(request))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\options.py", line 1390, in response_action
    response = func(self, request, queryset)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\actions.py", line 40, in delete_selected
    modeladmin.delete_queryset(request, queryset)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\admin\options.py", line 1091, in delete_queryset
    queryset.delete()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 722, in delete
    deleted, _rows_count = collector.delete()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\deletion.py", line 308, in delete
    signals.pre_delete.send(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 173, in send
    return [
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\models.py", line 97, in photo_delete
    cloudinary.uploader.destroy(instance.image.public_id)
AttributeError: 'CustomUser' object has no attribute 'image'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\fields.py", line 565, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 18, in to_internal_value
    return getattr(self._choices, data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\enum.py", line 341, in __getattr__
    raise AttributeError(name) from None
AttributeError: Student
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\fields.py", line 565, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 18, in to_internal_value
    return getattr(self._choices, data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\enum.py", line 341, in __getattr__
    raise AttributeError(name) from None
AttributeError: INSTRUCT
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\fields.py", line 565, in run_validation
    value = self.to_internal_value(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 18, in to_internal_value
    return getattr(self._choices, data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\enum.py", line 341, in __getattr__
    raise AttributeError(name) from None
AttributeError: Instructr
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 436, in run_validation
    value = self.validate(value)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 98, in validate
    payload = payload.capitalize()
AttributeError: 'collections.OrderedDict' object has no attribute 'capitalize'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 39, in post
    user = serializer.save()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 43, in create
    user = CustomUser(first_name=validated_data["first_name"],
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 500, in __init__
    raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
TypeError: CustomUser() got an unexpected keyword argument 'type'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 17, in post
    print(serializer.data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 562, in data
    ret = super().data
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 20, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 242, in is_valid
    raise ValidationError(self.errors)
rest_framework.exceptions.ValidationError: {'data': [ErrorDetail(string='Incorrect Credentials', code='invalid')], 'status': [ErrorDetail(string='400', code='invalid')]}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 30, in post
    raise Error()
utils.errors.Error
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 20, in post
    if serializer.is_valid(raise_exception=True):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 242, in is_valid
    raise ValidationError(self.errors)
rest_framework.exceptions.ValidationError: {'data': [ErrorDetail(string='Incorrect Credentials', code='invalid')], 'status': [ErrorDetail(string='400', code='invalid')]}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 30, in post
    raise Error(serializer.errors)
utils.errors.Error: {'data': [ErrorDetail(string='Incorrect Credentials', code='invalid')], 'status': [ErrorDetail(string='400', code='invalid')]}
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 43, in post
    user = CustomUser.objects.get(email, user_data['email'])
NameError: name 'email' is not defined
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 43, in post
    user = CustomUser.objects.get(user_data['email'])
TypeError: 'CustomUser' object is not subscriptable
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    relative_link = reverse("email-verify")
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' not found. 'email-verify' is not a valid view function or pattern name.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    relative_link = reverse("email-verify")
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' not found. 'email-verify' is not a valid view function or pattern name.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 48, in post
    absolute_url = f'{http://{current_site}{relative_link}+token={token.access}}'
NameError: name 'http' is not defined
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 48, in post
    absolute_url = f'http://{current_site}{relative_link}+token={token.access}'
AttributeError: 'str' object has no attribute 'access'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 8, in send_mail
    subject=data["email_message"], body=data["email_body"], to=data["to_email"]
KeyError: 'email_message'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 7, in send_mail
    email = EmailMessage(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 195, in __init__
    raise TypeError('"to" argument must be a list or tuple')
TypeError: "to" argument must be a list or tuple
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 8, in send_mail
    subject=data["email_subject"], body=data["email_body"], to=data["to_email", ]
KeyError: ('to_email',)
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 7, in send_mail
    email = EmailMessage(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 195, in __init__
    raise TypeError('"to" argument must be a list or tuple')
TypeError: "to" argument must be a list or tuple
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 56, in post
    "user": user_data.pk,
AttributeError: 'ReturnDict' object has no attribute 'pk'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials y4sm13470537wmj.2 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials t6sm17715351wre.30 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials 205sm15228720wme.38 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials d2sm14910269wrq.34 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials y4sm13501137wmj.2 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials v6sm13728639wmj.6 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 7, in send_mail
    email = EmailMessage(
TypeError: __init__() got an unexpected keyword argument 'from_mail'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials a3sm16139365wrh.94 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 7, in send_mail
    email = EmailMessage(
TypeError: __init__() got an unexpected keyword argument 'fail_silently'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials l8sm15524985wrn.28 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials i126sm15299900wmi.0 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials c129sm14679360wmd.7 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials m1sm14451748wmm.34 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials u15sm15671271wrm.77 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials z18sm14279306wrs.82 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 14, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials o129sm14189728wmb.25 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 62, in open
    self.connection = self.connection_class(self.host, self.port, **connection_params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 308, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 787, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 10109] getaddrinfo failed
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials v19sm14270728wmj.31 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials k18sm15850616wrx.96 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials 205sm16491818wme.38 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials n9sm18670807wrq.72 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials l8sm16944603wrn.28 - gsmtp')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 109, in send_messages
    sent = self._send(message)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 125, in _send
    self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 871, in sendmail
    raise SMTPSenderRefused(code, resp, from_addr)
smtplib.SMTPSenderRefused: (530, b'5.7.0 Authentication Required. Learn more at\n5.7.0  https://support.google.com/mail/?p=WantAuthError t5sm19158407wrb.21 - gsmtp', 'webmaster@localhost')
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    Email.send_mail(data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\utils\sendEmail.py", line 11, in send_mail
    email.send()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\message.py", line 276, in send
    return self.get_connection(fail_silently).send_messages([self])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 102, in send_messages
    new_conn_created = self.open()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\mail\backends\smtp.py", line 69, in open
    self.connection.login(self.username, self.password)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 734, in login
    raise last_exception
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials y4sm16699557wrp.74 - gsmtp')
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 51, in post
    print(username, password)
NameError: name 'username' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 52, in post
    user = authenticate(request, username=username, password=password)
NameError: name 'username' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    user = authenticate(request, email=email, password=password)
NameError: name 'email' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 52, in post
    print(serializer.data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 562, in data
    ret = super().data
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 58, in post
    request, email=user["email"], password=user["password"])
TypeError: 'bool' object is not subscriptable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 56, in post
    print(user.email)
AttributeError: 'bool' object has no attribute 'email'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 56, in post
    print(user.data["email"])
AttributeError: 'bool' object has no attribute 'data'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 56, in post
    print(user["email"])
TypeError: 'bool' object is not subscriptable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 58, in post
    print(**user)
TypeError: 'email' is an invalid keyword argument for print()
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 59, in post
    print(user.is_active)
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 60, in post
    print(user.is_active)
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 53, in post
    login(request, user)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\__init__.py", line 99, in login
    if _get_user_session_key(request) != user.pk or (
AttributeError: 'ReturnDict' object has no attribute 'pk'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 70, in post
    serializer.is_valid(raise_exception=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 227, in is_valid
    assert hasattr(self, 'initial_data'), (
AssertionError: Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 70, in post
    serializer.is_valid(raise_exception=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 227, in is_valid
    assert hasattr(self, 'initial_data'), (
AssertionError: Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 71, in post
    serializer.is_valid(raise_exception=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 227, in is_valid
    assert hasattr(self, 'initial_data'), (
AssertionError: Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 68, in post
    login(request, serializer.data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\__init__.py", line 99, in login
    if _get_user_session_key(request) != user.pk or (
AttributeError: 'ReturnDict' object has no attribute 'pk'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    "token": AuthToken.objects.create(user)[1],
NameError: name 'user' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    "token": AuthToken.objects.create(user_info)[1],
NameError: name 'user_info' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    "token": AuthToken.objects.create(user_obj)[1],
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\knox\models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 782, in save_base
    updated = self._save_table(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 924, in _do_insert
    return manager._insert(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\sql\compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 100, in execute
    return super().execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    email=serializer.data["email"], password=serializer.data["password"])
KeyError: 'password'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    email=serializer.data["email"], password=serializer.data["password"])
KeyError: 'password'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    email=serializer.data["email"], password=serializer.data["password"])
KeyError: 'password'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 47, in post
    email=serializer.data["email"], password=serializer.data["password"])
KeyError: 'password'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 46, in post
    print('serializer.data..................', serializer.data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 562, in data
    ret = super().data
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 46, in post
    print('serializer.data..................', serializer.data)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 562, in data
    ret = super().data
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 34, in post
    "token": AuthToken.objects.create(user_obj)[1],
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\knox\models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 782, in save_base
    updated = self._save_table(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 924, in _do_insert
    return manager._insert(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\sql\compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 100, in execute
    return super().execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 34, in post
    "token": AuthToken.objects.create(user_obj),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\knox\models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 782, in save_base
    updated = self._save_table(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 924, in _do_insert
    return manager._insert(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\sql\compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 100, in execute
    return super().execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 411, in initial
    self.check_permissions(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 331, in check_permissions
    for permission in self.get_permissions():
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 278, in get_permissions
    return [permission() for permission in self.permission_classes]
TypeError: 'BasePermissionMetaclass' object is not iterable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 30, in post
    user = login(request, user_obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\__init__.py", line 125, in login
    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
AttributeError: 'AnonymousUser' object has no attribute '_meta'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 30, in post
    user = login(request, user_obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\__init__.py", line 125, in login
    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
AttributeError: 'AnonymousUser' object has no attribute '_meta'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 30, in post
    user = login(request, user_obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\__init__.py", line 125, in login
    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
AttributeError: 'AnonymousUser' object has no attribute '_meta'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type AuthToken is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type AuthToken is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 325, in _iterencode_list
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type AuthToken is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 34, in post
    "token": AuthToken.objects.create(user_obj)[1],
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\knox\models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 782, in save_base
    updated = self._save_table(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 924, in _do_insert
    return manager._insert(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\sql\compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 100, in execute
    return super().execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type AccessToken is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 143, in _get_response
    response = response.render()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\response.py", line 105, in render
    self.content = self.rendered_content
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\renderers.py", line 100, in render
    ret = json.dumps(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 234, in dumps
    return cls(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 201, in encode
    chunks = list(chunks)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 438, in _iterencode
    o = _default(o)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\utils\encoders.py", line 67, in default
    return super().default(obj)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type AccessToken is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 36, in post
    "token": AuthToken.objects.create(user_obj)[1],
NameError: name 'AuthToken' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 36, in post
    "token": AuthToken.objects.create(user_obj)[1],
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\knox\models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 782, in save_base
    updated = self._save_table(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 924, in _do_insert
    return manager._insert(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\sql\compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 100, in execute
    return super().execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\sqlite3\base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: knox_authtoken.user_id
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 73, in VerifyEmail
    return render(request, "templates/email_auth_confirmation.html")
NameError: name 'render' is not defined
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 73, in VerifyEmail
    return render(request, "templates/email_auth_confirmation.html")
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: account/templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: account/templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: /account/templates/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 74, in VerifyEmail
    return render(request, template, {})
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: account/email_auth_confirmation.html
Internal Server Error: /api/v1/email-verify/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 73, in VerifyEmail
    token = request.get("token")
AttributeError: 'WSGIRequest' object has no attribute 'get'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 54, in post
    user = CustomUser.objects.get(email=user_data['email'])
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\query.py", line 415, in get
    raise self.model.DoesNotExist(
account.models.CustomUser.DoesNotExist: CustomUser matching query does not exist.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 51, in post
    serializer.save()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 195, in save
    assert not hasattr(self, '_data'), (
AssertionError: You cannot call `.save()` after accessing `serializer.data`.If you need to access data before committing to the database then inspect 'serializer.validated_data' instead. 
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 50, in post
    serializer.save()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 32, in create
    user.save()
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\models.py", line 40, in save
    super().save(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 769, in save_base
    pre_save.send(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 173, in send
    return [
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
TypeError: user_to_inactive() missing 2 required positional arguments: 'created' and 'updated_fields'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 50, in post
    serializer.save()
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\serializers.py", line 32, in create
    user.save()
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\models.py", line 40, in save
    super().save(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\contrib\auth\base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\base.py", line 769, in save_base
    pre_save.send(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 173, in send
    return [
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
TypeError: user_to_inactive() missing 1 required positional argument: 'created'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 52, in post
    print(user.data["id"], "user id")
UnboundLocalError: local variable 'user' referenced before assignment
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    relative_link = reverse("account:email-verify")
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' with no arguments not found. 1 pattern(s) tried: ['api/v1/email\\-verify/(?P<token>[0-9]+)/(?P<id>[0-9]+)/$']
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    relative_link = reverse("account:email-verify")
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' with no arguments not found. 1 pattern(s) tried: ['api/v1/email\\-verify/(?P<token>[0-9]+)/(?P<id>[0-9]+)/$']
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 57, in post
    relative_link = reverse(
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\urls\resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' with arguments '(79, 'a78af4ceef00dc171542799df05fd52ffe929418d3b3a22d090ee27b1b86cc13')' not found. 1 pattern(s) tried: ['api/v1/email\\-verify/$']
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
TypeError: VerifyEmail() got an unexpected keyword argument 'id'
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 77, in VerifyEmail
    user = CustomUser.object.get(id=id)
AttributeError: type object 'CustomUser' has no attribute 'object'
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 80, in VerifyEmail
    user, context=self.get_serializer_context()).data,
NameError: name 'self' is not defined
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
TypeError: VerifyEmail() missing 1 required positional argument: 'sender'
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
TypeError: VerifyEmail() missing 1 required positional argument: 'sender'
Internal Server Error: /api/v1/email-verify/80/859296664d10854b98942192a6d01c42a6c653a04e67f463973cf9d61e795f39/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 80, in VerifyEmail
    change_user_status.send(sender=CustomUser, user=user)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 173, in send
    return [
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\dispatch\dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\signals.py", line 23, in user_to_active
    self.user.is_active = True
NameError: name 'self' is not defined
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 32, in post
    print(user_obj.is_active, "user is active")
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 32, in post
    print(user_obj.is_active, "user is active")
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 476, in raise_uncaught_exception
    raise exc
  File "C:\Users\Baron\AppData\Local\Programs\Python\Python38\lib\site-packages\rest_framework\views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "C:\Users\Baron\Documents\projects\Vue\PyJs\PyJs\account\views.py", line 32, in post
    print(user_obj.is_active, "user is active")
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 33, in post
    print(login(request, user_obj))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 125, in login
    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
AttributeError: 'AnonymousUser' object has no attribute '_meta'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 42, in post
    if user_obj.is_active:
AttributeError: 'NoneType' object has no attribute 'is_active'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 38, in post
    print(serializer.data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 562, in data
    ret = super().data
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/users/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 411, in initial
    self.check_permissions(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 331, in check_permissions
    for permission in self.get_permissions():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 278, in get_permissions
    return [permission() for permission in self.permission_classes]
TypeError: 'BasePermissionMetaclass' object is not iterable
Internal Server Error: /api/v1/users/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 411, in initial
    self.check_permissions(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 331, in check_permissions
    for permission in self.get_permissions():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 278, in get_permissions
    return [permission() for permission in self.permission_classes]
TypeError: 'BasePermissionMetaclass' object is not iterable
Internal Server Error: /api/v1/users/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 411, in initial
    self.check_permissions(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 331, in check_permissions
    for permission in self.get_permissions():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 278, in get_permissions
    return [permission() for permission in self.permission_classes]
TypeError: 'BasePermissionMetaclass' object is not iterable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 100, in render
    ret = json.dumps(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/utils/json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "/usr/lib/python3.8/json/__init__.py", line 234, in dumps
    return cls(
  File "/usr/lib/python3.8/json/encoder.py", line 201, in encode
    chunks = list(chunks)
  File "/usr/lib/python3.8/json/encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "/usr/lib/python3.8/json/encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "/usr/lib/python3.8/json/encoder.py", line 438, in _iterencode
    o = _default(o)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/utils/encoders.py", line 67, in default
    return super().default(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 29, in post
    'user': user.pk,
AttributeError: 'collections.OrderedDict' object has no attribute 'pk'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 30, in post
    "token": AuthToken.objects.create(user)[1],
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "OrderedDict([('email', 'awesomebaron007@gmail.com'), ('password', 'admin12345')])": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 30, in post
    "token": AuthToken.objects.create(user)[1],
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "OrderedDict([('email', 'awesomebaron007@gmail.com'), ('password', 'admin12345')])": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 30, in post
    "token": AuthToken.objects.create(user)[1],
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "OrderedDict([('email', 'awesomebaron007@gmail.com'), ('password', 'admin12345')])": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 486, in to_internal_value
    for field in fields:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 369, in _writable_fields
    for field in self.fields.values():
AttributeError: 'tuple' object has no attribute 'values'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 38, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 486, in to_internal_value
    for field in fields:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 369, in _writable_fields
    for field in self.fields.values():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1013, in get_fields
    assert hasattr(self, 'Meta'), (
AssertionError: Class LoginSerializer missing "Meta" attribute
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 41, in post
    email_exist = CustomUser.objects.get(email=email)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 415, in get
    raise self.model.DoesNotExist(
account.models.CustomUser.DoesNotExist: CustomUser matching query does not exist.
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 45, in get_operation
    responses = self.get_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 180, in get_responses
    response_serializers = self.get_response_serializers()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 235, in get_response_serializers
    responses = self.get_default_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 211, in get_default_responses
    default_schema = self.serializer_to_schema(default_schema) or ''
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `user_type` is not valid for model `CustomUser`.
Internal Server Error: /accounts/account/student/add/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 607, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/cache.py", line 44, in _wrapped_view_func
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/sites.py", line 231, in inner
    return view(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1638, in add_view
    return self.changeform_view(request, None, form_url, extra_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 43, in _wrapper
    return bound_method(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1522, in changeform_view
    return self._changeform_view(request, object_id, form_url, extra_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1569, in _changeform_view
    self.log_addition(request, new_object, change_message)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 807, in log_addition
    object_repr=str(object),
TypeError: __str__ returned non-string (type CustomUser)
Internal Server Error: /accounts/account/student/add/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 607, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/cache.py", line 44, in _wrapped_view_func
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/sites.py", line 231, in inner
    return view(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1638, in add_view
    return self.changeform_view(request, None, form_url, extra_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 43, in _wrapper
    return bound_method(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1522, in changeform_view
    return self._changeform_view(request, object_id, form_url, extra_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1569, in _changeform_view
    self.log_addition(request, new_object, change_message)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/admin/options.py", line 807, in log_addition
    object_repr=str(object),
TypeError: __str__ returned non-string (type NoneType)
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 45, in get_operation
    responses = self.get_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 180, in get_responses
    response_serializers = self.get_response_serializers()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 235, in get_response_serializers
    responses = self.get_default_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 211, in get_default_responses
    default_schema = self.serializer_to_schema(default_schema) or ''
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `user_type` is not valid for model `CustomUser`.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 655, in get_context
    raw_data_post_form = self.get_raw_data_form(data, view, 'POST', request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 563, in get_raw_data_form
    data = serializer.data.copy()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 562, in data
    ret = super().data
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 264, in data
    self._data = self.get_initial()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 412, in get_initial
    for field in self.fields.values()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1013, in get_fields
    assert hasattr(self, 'Meta'), (
AssertionError: Class StudentSerializer missing "Meta" attribute
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 62, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 37, in validate_confirm_password
    print(self.password, "initial data")
AttributeError: 'CustomUserSerializer' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 655, in get_context
    raw_data_post_form = self.get_raw_data_form(data, view, 'POST', request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 563, in get_raw_data_form
    data = serializer.data.copy()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 562, in data
    ret = super().data
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 264, in data
    self._data = self.get_initial()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 412, in get_initial
    for field in self.fields.values()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1038, in get_fields
    field_names = self.get_field_names(declared_fields, info)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1134, in get_field_names
    assert field_name in fields, (
AssertionError: The field 'custom_user' was declared on serializer StudentSerializer, but has not been included in the 'fields' option.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 62, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 37, in validate_confirm_password
    print(self.password, "initial data")
AttributeError: 'UserSerializer' object has no attribute 'password'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 62, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 492, in to_internal_value
    validated_value = validate_method(validated_value)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 36, in validate_confirm_password
    data = self.get_initial("data")
TypeError: get_initial() takes 1 positional argument but 2 were given
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 167, in create
    raise NotImplementedError('`create()` must be implemented.')
NotImplementedError: `create()` must be implemented.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 655, in get_context
    raw_data_post_form = self.get_raw_data_form(data, view, 'POST', request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 563, in get_raw_data_form
    data = serializer.data.copy()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 562, in data
    ret = super().data
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 264, in data
    self._data = self.get_initial()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 410, in get_initial
    return OrderedDict([
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 411, in <listcomp>
    (field.field_name, field.get_initial())
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 412, in get_initial
    for field in self.fields.values()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `confirm_password` is not valid for model `CustomUser`.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 948, in create
    instance = ModelClass._default_manager.create(**validated_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 500, in __init__
    raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
TypeError: CustomUser() got an unexpected keyword argument 'confirm_password'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 68, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 967, in create
    raise TypeError(msg)
TypeError: Got a `TypeError` when calling `CustomUser.objects.create()`. This may be because you have a writable field on the serializer class that is not a valid argument to `CustomUser.objects.create()`. You may need to make the field read-only, or override the UserSerializer.create() method to handle this correctly.
Original exception was:
 Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 948, in create
    instance = ModelClass._default_manager.create(**validated_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 500, in __init__
    raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
TypeError: CustomUser() got an unexpected keyword argument 'confirm_password'

Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 62, in post
    if serializer.is_valid(raise_exception=True):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 234, in is_valid
    self._validated_data = self.run_validation(self.initial_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 490, in to_internal_value
    validated_value = field.run_validation(primitive_value)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 433, in run_validation
    value = self.to_internal_value(data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 486, in to_internal_value
    for field in fields:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 369, in _writable_fields
    for field in self.fields.values():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1038, in get_fields
    field_names = self.get_field_names(declared_fields, info)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1134, in get_field_names
    assert field_name in fields, (
AssertionError: The field 'confirm_password' was declared on serializer UserSerializer, but has not been included in the 'fields' option.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 948, in create
    instance = ModelClass._default_manager.create(**validated_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 500, in __init__
    raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
TypeError: CustomUser() got an unexpected keyword argument 'confirm_password'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 967, in create
    raise TypeError(msg)
TypeError: Got a `TypeError` when calling `CustomUser.objects.create()`. This may be because you have a writable field on the serializer class that is not a valid argument to `CustomUser.objects.create()`. You may need to make the field read-only, or override the UserSerializer.create() method to handle this correctly.
Original exception was:
 Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 948, in create
    instance = ModelClass._default_manager.create(**validated_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 500, in __init__
    raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
TypeError: CustomUser() got an unexpected keyword argument 'confirm_password'

Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 68, in create
    user = CustomUser(first_name=validated_data["first_name"],
KeyError: 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 68, in create
    user = CustomUser(first_name=validated_data["user.first_name"],
KeyError: 'user.first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 68, in create
    user = CustomUser(first_name=validated_data.user["first_name"],
AttributeError: 'dict' object has no attribute 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 167, in create
    raise NotImplementedError('`create()` must be implemented.')
NotImplementedError: `create()` must be implemented.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 167, in create
    raise NotImplementedError('`create()` must be implemented.')
NotImplementedError: `create()` must be implemented.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 167, in create
    raise NotImplementedError('`create()` must be implemented.')
NotImplementedError: `create()` must be implemented.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = UserSerializer.create(UserSerializer(), validated_data=user_data)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 167, in create
    raise NotImplementedError('`create()` must be implemented.')
NotImplementedError: `create()` must be implemented.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    user = CustomUser(first_name=validated_data["first_name"],
KeyError: 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 68, in create
    user = CustomUser(first_name=validated_data["first_name"],
KeyError: 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 66, in create
    print(validated_data.first_name, "validated _data first name")
AttributeError: 'dict' object has no attribute 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 69, in create
    user = CustomUser(first_name=validated_data["first_name"],
KeyError: 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 69, in create
    user = CustomUser(first_name=validated_data["first_name"],
KeyError: 'first_name'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: account_student.age

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 77, in create
    student = Student.objects.create(user=user)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 782, in save_base
    updated = self._save_table(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 924, in _do_insert
    return manager._insert(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: account_student.age
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 67, in create
    print(validated_data["fage"], 'user data--------------------------')
KeyError: 'fage'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: account_student.age

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 77, in create
    student = Student.objects.create(user=user)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 782, in save_base
    updated = self._save_table(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 924, in _do_insert
    return manager._insert(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: account_student.age
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: account_student.age

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 77, in create
    student = Student.objects.create(user=user)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 782, in save_base
    updated = self._save_table(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 924, in _do_insert
    return manager._insert(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: account_student.age
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: NOT NULL constraint failed: account_student.age

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 63, in post
    serializer.save()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/home/baron/Documents/projects/pyjs/backend/account/serializers.py", line 77, in create
    student = Student.objects.create(user=user)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 782, in save_base
    updated = self._save_table(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 924, in _do_insert
    return manager._insert(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1391, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: NOT NULL constraint failed: account_student.age
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 65, in post
    user = CustomUser.objects.get(email=user_data['email'])
KeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 65, in post
    print(user_data.user, "user_data.user")
AttributeError: 'ReturnDict' object has no attribute 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 65, in post
    print(user_data.user["email"], "user_data.user{'email")
AttributeError: 'ReturnDict' object has no attribute 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    print(serializer.data.user["email"])
AttributeError: 'ReturnDict' object has no attribute 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    print(serializer.data["email"])
KeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    print(serializer.data["email"])
KeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 65, in post
    user = CustomUser.objects.get(email=user_data['email'])
KeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 507, in dispatch
    self.response = self.finalize_response(request, response, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 419, in finalize_response
    assert isinstance(response, HttpResponseBase), (
AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 65, in post
    deactivate_user_status.send(sender=CustomUser, user=user)
NameError: name 'user' is not defined
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    token = AuthToken.objects.create(user_data)[1]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "<Student: oluwapelumi.sodeinde@e4email.net>": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 70, in post
    "account:email-verify", args=[user_data['id'], token])
TypeError: 'Student' object is not subscriptable
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    relative_link = reverse(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/urls/base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/urls/resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' with arguments '(13,)' not found. 1 pattern(s) tried: ['api/v1/email\\-verify/(?P<id>[^/]+)/(?P<token>[^/]+)/$']
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    token = AuthToken.objects.create(user_data)[1]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "<Student: urchmawni@gmail.com>": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 75, in post
    relative_link = reverse(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/urls/base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/urls/resolvers.py", line 677, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'email-verify' with arguments '(16,)' not found. 1 pattern(s) tried: ['api/v1/email\\-verify/(?P<id>[^/]+)/(?P<token>[^/]+)/$']
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 724, in render
    context = self.get_context(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 680, in get_context
    'content': self.get_content(renderer, data, accepted_media_type, renderer_context),
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 413, in get_content
    content = renderer.render(data, accepted_media_type, renderer_context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/renderers.py", line 100, in render
    ret = json.dumps(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/utils/json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "/usr/lib/python3.8/json/__init__.py", line 234, in dumps
    return cls(
  File "/usr/lib/python3.8/json/encoder.py", line 201, in encode
    chunks = list(chunks)
  File "/usr/lib/python3.8/json/encoder.py", line 431, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "/usr/lib/python3.8/json/encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "/usr/lib/python3.8/json/encoder.py", line 438, in _iterencode
    o = _default(o)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/utils/encoders.py", line 67, in default
    return super().default(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 68, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 62, in post
    print(request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 66, in post
    print(serializer.data.user, "serializer data")
AttributeError: 'ReturnDict' object has no attribute 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 76, in __getitem__
    list_ = super().__getitem__(key)
KeyError: 'email'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 69, in post
    user_data = CustomUser.objects.get(email=request.data["email"])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/datastructures.py", line 78, in __getitem__
    raise MultiValueDictKeyError(key)
django.utils.datastructures.MultiValueDictKeyError: 'email'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_email)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 15, in user_to_inactive
    user.is_active = False
AttributeError: 'str' object has no attribute 'is_active'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_email)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 15, in user_to_inactive
    user.is_active = False
AttributeError: 'str' object has no attribute 'is_active'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_email)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 15, in user_to_inactive
    user.is_active = False
AttributeError: 'str' object has no attribute 'is_active'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 16, in user_to_inactive
    user.save()
AttributeError: 'ReturnDict' object has no attribute 'save'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 14, in user_to_inactive
    user = kwargs["user_obj"]
KeyError: 'user_obj'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 17, in user_to_inactive
    user.save()
AttributeError: 'ReturnDict' object has no attribute 'save'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 74, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 17, in user_to_inactive
    user.save()
AttributeError: 'ReturnDict' object has no attribute 'save'
Internal Server Error: /api/v1/email-verify/17/4284a3173e2a7f457c9216a99cb8082691fc556e4a573be407f84fd3163b97e3/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 91, in VerifyEmail
    user = CustomUser.objects.get(id=id)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 415, in get
    raise self.model.DoesNotExist(
account.models.CustomUser.DoesNotExist: CustomUser matching query does not exist.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 68, in post
    token = AuthToken.objects.create(user_obj)[1]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "{'id': 32, 'first_name': 'Urch', 'last_name': 'Mawni', 'email': 'urchmawni@gmail.com', 'password': 'pbkdf2_sha256$180000$LXxwEG7uT9Bu$ig44B7wv4vLla5ytz8Uq4MxyP/Bm68kWVlishVxvQXY=', 'username': 'urchmawni', 'is_active': True}": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 45, in get_operation
    responses = self.get_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 180, in get_responses
    response_serializers = self.get_response_serializers()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 235, in get_response_serializers
    responses = self.get_default_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 211, in get_default_responses
    default_schema = self.serializer_to_schema(default_schema) or ''
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `user_type` is not valid for model `CustomUser`.
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 45, in get_operation
    responses = self.get_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 180, in get_responses
    response_serializers = self.get_response_serializers()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 235, in get_response_serializers
    responses = self.get_default_responses()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 211, in get_default_responses
    default_schema = self.serializer_to_schema(default_schema) or ''
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1062, in get_fields
    field_class, field_kwargs = self.build_field(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1208, in build_field
    return self.build_unknown_field(field_name, model_class)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/serializers.py", line 1323, in build_unknown_field
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Field name `user_type` is not valid for model `CustomUser`.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 68, in post
    token = AuthToken.objects.create(user_obj)[1]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/knox/models.py", line 20, in create
    instance = super(AuthTokenManager, self).create(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 431, in create
    obj = self.model(**kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/base.py", line 482, in __init__
    _setattr(self, field.name, rel_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 214, in __set__
    raise ValueError(
ValueError: Cannot assign "{'id': 33, 'first_name': 'Urch', 'last_name': 'Mawni', 'email': 'urchmawni@gmail.com', 'password': 'pbkdf2_sha256$180000$1pVp4Bo2xpX8$jS3w0NHrh2jW0PF4f91RatzSL7PM7vfykm2pJ/T1jCo=', 'username': 'urchmawni', 'is_active': True}": "AuthToken.user" must be a "CustomUser" instance.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 73, in post
    "account:email-verify", args=[user_obj.id, token])
AttributeError: 'ReturnDict' object has no attribute 'id'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 68, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 17, in user_to_inactive
    user.save()
AttributeError: 'ReturnDict' object has no attribute 'save'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/backend/account/views.py", line 68, in post
    deactivate_user_status.send(sender=CustomUser, user=user_obj)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 173, in send
    return [
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/dispatch/dispatcher.py", line 174, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "/home/baron/Documents/projects/pyjs/backend/account/signals.py", line 16, in user_to_inactive
    user.is_active = False
AttributeError: 'str' object has no attribute 'is_active'
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/usr/local/lib/python3.6/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 32, in get_operation
    body = self.get_request_body_parameters(consumes)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 85, in get_request_body_parameters
    schema = self.get_request_body_schema(serializer)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 142, in get_request_body_schema
    return self.serializer_to_schema(serializer)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 446, in serializer_to_schema
    self.field_inspectors, 'get_schema', serializer, {'field_inspectors': self.field_inspectors}
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 238, in probe_field_inspectors
    swagger_object_type=swagger_object_type, use_references=use_references, **kwargs
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/usr/local/lib/python3.6/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/usr/local/lib/python3.6/site-packages/rest_framework/serializers.py", line 1015, in get_fields
    serializer_class=self.__class__.__name__
AssertionError: Class LoginSerializer missing "Meta" attribute
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/usr/local/lib/python3.6/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/usr/local/lib/python3.6/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 32, in get_operation
    body = self.get_request_body_parameters(consumes)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 85, in get_request_body_parameters
    schema = self.get_request_body_schema(serializer)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/view.py", line 142, in get_request_body_schema
    return self.serializer_to_schema(serializer)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 446, in serializer_to_schema
    self.field_inspectors, 'get_schema', serializer, {'field_inspectors': self.field_inspectors}
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 238, in probe_field_inspectors
    swagger_object_type=swagger_object_type, use_references=use_references, **kwargs
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/usr/local/lib/python3.6/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/usr/local/lib/python3.6/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/usr/local/lib/python3.6/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/usr/local/lib/python3.6/site-packages/rest_framework/serializers.py", line 1015, in get_fields
    serializer_class=self.__class__.__name__
AssertionError: Class LoginSerializer missing "Meta" attribute
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 199, in _get_session
    return self._session_cache
AttributeError: 'SessionStore' object has no attribute '_session_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.UndefinedTable: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 410, in initial
    self.perform_authentication(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 324, in perform_authentication
    request.user
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 220, in user
    self._authenticate()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 373, in _authenticate
    user_auth_tuple = authenticator.authenticate(self)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/authentication.py", line 123, in authenticate
    if not user or not user.is_active:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 224, in inner
    self._setup()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 360, in _setup
    self._wrapped = self._setupfunc()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
    request.user = SimpleLazyObject(lambda: get_user(request))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
    request._cached_user = auth.get_user(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 173, in get_user
    user_id = _get_user_session_key(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 58, in _get_user_session_key
    return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 64, in __getitem__
    return self._session[key]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 204, in _get_session
    self._session_cache = self.load()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
    s = self._get_session_from_db()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 32, in _get_session_from_db
    return self.model.objects.get(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 411, in get
    num = len(clone)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 258, in __len__
    self._fetch_all()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^

Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 199, in _get_session
    return self._session_cache
AttributeError: 'SessionStore' object has no attribute '_session_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.UndefinedTable: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 410, in initial
    self.perform_authentication(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 324, in perform_authentication
    request.user
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 220, in user
    self._authenticate()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 373, in _authenticate
    user_auth_tuple = authenticator.authenticate(self)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/authentication.py", line 123, in authenticate
    if not user or not user.is_active:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 224, in inner
    self._setup()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 360, in _setup
    self._wrapped = self._setupfunc()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
    request.user = SimpleLazyObject(lambda: get_user(request))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
    request._cached_user = auth.get_user(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 173, in get_user
    user_id = _get_user_session_key(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 58, in _get_user_session_key
    return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 64, in __getitem__
    return self._session[key]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 204, in _get_session
    self._session_cache = self.load()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
    s = self._get_session_from_db()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 32, in _get_session_from_db
    return self.model.objects.get(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 411, in get
    num = len(clone)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 258, in __len__
    self._fetch_all()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^

Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 199, in _get_session
    return self._session_cache
AttributeError: 'SessionStore' object has no attribute '_session_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.UndefinedTable: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 410, in initial
    self.perform_authentication(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 324, in perform_authentication
    request.user
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 220, in user
    self._authenticate()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 373, in _authenticate
    user_auth_tuple = authenticator.authenticate(self)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/authentication.py", line 123, in authenticate
    if not user or not user.is_active:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 224, in inner
    self._setup()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 360, in _setup
    self._wrapped = self._setupfunc()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
    request.user = SimpleLazyObject(lambda: get_user(request))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
    request._cached_user = auth.get_user(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 173, in get_user
    user_id = _get_user_session_key(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 58, in _get_user_session_key
    return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 64, in __getitem__
    return self._session[key]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 204, in _get_session
    self._session_cache = self.load()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
    s = self._get_session_from_db()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 32, in _get_session_from_db
    return self.model.objects.get(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 411, in get
    num = len(clone)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 258, in __len__
    self._fetch_all()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^

Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 199, in _get_session
    return self._session_cache
AttributeError: 'SessionStore' object has no attribute '_session_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.UndefinedTable: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 410, in initial
    self.perform_authentication(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/views.py", line 324, in perform_authentication
    request.user
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 220, in user
    self._authenticate()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/request.py", line 373, in _authenticate
    user_auth_tuple = authenticator.authenticate(self)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/rest_framework/authentication.py", line 123, in authenticate
    if not user or not user.is_active:
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 224, in inner
    self._setup()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/utils/functional.py", line 360, in _setup
    self._wrapped = self._setupfunc()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
    request.user = SimpleLazyObject(lambda: get_user(request))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
    request._cached_user = auth.get_user(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 173, in get_user
    user_id = _get_user_session_key(request)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 58, in _get_user_session_key
    return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 64, in __getitem__
    return self._session[key]
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 204, in _get_session
    self._session_cache = self.load()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
    s = self._get_session_from_db()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 32, in _get_session_from_db
    return self.model.objects.get(
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 411, in get
    num = len(clone)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 258, in __len__
    self._fetch_all()
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/pyjs/env_pyjs/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: relation "django_session" does not exist
LINE 1: ...ession_data", "django_session"."expire_date" FROM "django_se...
                                                             ^

Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 199, in _get_session
    return self._session_cache
AttributeError: 'SessionStore' object has no attribute '_session_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such table: django_session

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 493, in dispatch
    self.initial(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 410, in initial
    self.perform_authentication(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 324, in perform_authentication
    request.user
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/request.py", line 220, in user
    self._authenticate()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/request.py", line 373, in _authenticate
    user_auth_tuple = authenticator.authenticate(self)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/authentication.py", line 123, in authenticate
    if not user or not user.is_active:
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/utils/functional.py", line 224, in inner
    self._setup()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/utils/functional.py", line 360, in _setup
    self._wrapped = self._setupfunc()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 24, in <lambda>
    request.user = SimpleLazyObject(lambda: get_user(request))
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/auth/middleware.py", line 12, in get_user
    request._cached_user = auth.get_user(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 173, in get_user
    user_id = _get_user_session_key(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/auth/__init__.py", line 58, in _get_user_session_key
    return get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 64, in __getitem__
    return self._session[key]
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py", line 204, in _get_session
    self._session_cache = self.load()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 43, in load
    s = self._get_session_from_db()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/contrib/sessions/backends/db.py", line 32, in _get_session_from_db
    return self.model.objects.get(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/query.py", line 411, in get
    num = len(clone)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/query.py", line 258, in __len__
    self._fetch_all()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such table: django_session
Internal Server Error: /api/v1/login
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/utils/deprecation.py", line 93, in __call__
    response = self.process_request(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/middleware/common.py", line 54, in process_request
    path = self.get_full_path_with_slash(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/middleware/common.py", line 87, in get_full_path_with_slash
    raise RuntimeError(
RuntimeError: You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to 127.0.0.1:8003/api/v1/login/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
Internal Server Error: /api/v1/login
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/utils/deprecation.py", line 93, in __call__
    response = self.process_request(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/middleware/common.py", line 54, in process_request
    path = self.get_full_path_with_slash(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/middleware/common.py", line 87, in get_full_path_with_slash
    raise RuntimeError(
RuntimeError: You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to 127.0.0.1:8003/api/v1/login/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 61, in post
    serializer.save()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/serializers.py", line 56, in create
    user_data = validated_data.pop('user')
KeyError: 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 61, in post
    serializer.save()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 212, in save
    self.instance = self.create(validated_data)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/serializers.py", line 59, in create
    user = CustomUser(first_name=user_data["first_name"],
NameError: name 'user_data' is not defined
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 63, in post
    user_email = serializer.data["user"]["email"]
KeyError: 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 63, in post
    print(serializer.data["user"])
KeyError: 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 64, in post
    user_email = serializer.data["user"]["email"]
KeyError: 'user'
Internal Server Error: /api/v1/register/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 64, in post
    user_email = serializer.data["user"]["email"]
KeyError: 'user'
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 37, in post
    print(serializer.data['email'])
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 562, in data
    ret = super().data
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 256, in data
    raise AssertionError(msg)
AssertionError: When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.
You should either call `.is_valid()` first, or access `.initial_data` instead.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/http/response.py", line 51, in __init__
    self.status_code = int(status)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'CustomUser'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/server/account/views.py", line 45, in post
    return Response(status.HTTP_200_OK, user_obj)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/response.py", line 30, in __init__
    super().__init__(None, status=status)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/template/response.py", line 36, in __init__
    super().__init__('', content_type, status, charset=charset)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/http/response.py", line 290, in __init__
    super().__init__(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/http/response.py", line 53, in __init__
    raise TypeError('HTTP status code must be an integer.')
TypeError: HTTP status code must be an integer.
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/renderers.py", line 100, in render
    ret = json.dumps(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "/usr/lib/python3.8/json/__init__.py", line 234, in dumps
    return cls(
  File "/usr/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/encoders.py", line 67, in default
    return super().default(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/renderers.py", line 100, in render
    ret = json.dumps(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "/usr/lib/python3.8/json/__init__.py", line 234, in dumps
    return cls(
  File "/usr/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/encoders.py", line 67, in default
    return super().default(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type CustomUser is not JSON serializable
Internal Server Error: /api/v1/login/
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/renderers.py", line 100, in render
    ret = json.dumps(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/json.py", line 25, in dumps
    return json.dumps(*args, **kwargs)
  File "/usr/lib/python3.8/json/__init__.py", line 234, in dumps
    return cls(
  File "/usr/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/utils/encoders.py", line 67, in default
    return super().default(obj)
  File "/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type GetUserSerializer is not JSON serializable
Internal Server Error: /
Traceback (most recent call last):
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/views.py", line 94, in get
    schema = generator.get_schema(request, self.public)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/generators.py", line 254, in get_schema
    paths, prefix = self.get_paths(endpoints, components, request, public)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/generators.py", line 412, in get_paths
    operation = self.get_operation(view, path, prefix, method, components, request)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/generators.py", line 454, in get_operation
    operation = view_inspector.get_operation(operation_keys)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 32, in get_operation
    body = self.get_request_body_parameters(consumes)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 85, in get_request_body_parameters
    schema = self.get_request_body_schema(serializer)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/view.py", line 142, in get_request_body_schema
    return self.serializer_to_schema(serializer)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 445, in serializer_to_schema
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 42, in get_schema
    return self.probe_field_inspectors(serializer, openapi.Schema, self.use_definitions)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 236, in probe_field_inspectors
    return self.probe_inspectors(
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/base.py", line 118, in probe_inspectors
    result = method(obj, **kwargs)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 135, in field_to_swagger_object
    actual_schema = definitions.setdefault(ref_name, make_schema_definition)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/openapi.py", line 690, in setdefault
    ret = maker()
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/drf_yasg/inspectors/field.py", line 102, in make_schema_definition
    for property_name, child in serializer.fields.items():
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 363, in fields
    for key, value in self.get_fields().items():
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 1038, in get_fields
    field_names = self.get_field_names(declared_fields, info)
  File "/home/baron/Documents/projects/personalprojects/pyjs/env/lib/python3.8/site-packages/rest_framework/serializers.py", line 1134, in get_field_names
    assert field_name in fields, (
AssertionError: The field 'password' was declared on serializer LoginSerializer, but has not been included in the 'fields' option.
