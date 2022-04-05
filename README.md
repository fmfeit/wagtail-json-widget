# Wagtail JSON Widget

JSON editing for Wagtail Admin.

## Installation

Install from [PyPI](https://pypi.org/project/wagtail-json-widget/):

```
pip install wagtail-json-widget
```

Then add the following to your project's `INSTALLED_APPS`.

```
'wagtail_json_widget',
```

## Usage

```python
from wagtail_json_widget.blocks import JsonBlock

class MyBlock(blocks.StructBlock):
 
    my_json = JsonBlock()
    ...
    
```