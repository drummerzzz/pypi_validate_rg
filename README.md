# validate-rg

[![pipy](https://img.shields.io/pypi/v/validate_rg.svg)](https://pypi.python.org/pypi/validate_rg)

Validates Brazilian RG (SSP SP)

## Features

- RG Validation with mask
- RG Validation without mask

## Modes of use

```python
#!/usr/bin/python
import validate_rg

# Without mask
validate_rg.is_valid('505675092') # True

# With mask
validate_rg.is_valid('50.567.509-2') # True
```

or

```python
#!/usr/bin/python
from validate_rg import is_valid

# Without mask
is_valid('111111111') # False

# With mask
is_valid('11.111.111-1') # False
```

# Author

[João Filho](https://joaofilho.dev)
[Github](https://github.com/drummerzzz)

# Credits

This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)

[DV calculation](https://www.ngmatematica.com/2014/02/como-determinar-o-digito-verificador-do.html)