# Model Visual

![GitHub](https://img.shields.io/github/license/YuamLu/ModelVisual)
![GitHub](https://img.shields.io/badge/powered%20by-YuAN%20Lu-orange)
![Github stars](https://img.shields.io/github/stars/YuamLu/ModelVisual.svg)
![PyPI](https://img.shields.io/pypi/v/Model-Visual)

⭐ Star us on GitHub — it motivates us a lot!

[Model Visual](https://github.com/YuamLu/ModelVisual) is a lightweight deep learning model visualization suite based on [Mermaid](https://github.com/mermaid-js/mermaid).This kit will convert model schemas into Mermaid code and output code snippets or complete web pages. Users can easily adjust the color and border of the chart.

> Only support tensorflow now. More frameworks will comming soon!

## Contents

- [Model Visual](#model-visual)
  - [Contents](#contents)
  - [Demo](#demo)
  - [Tutorial](#tutorial)
    - [Isnstallation](#isnstallation)
    - [Create object](#create-object)
    - [Run and get result](#run-and-get-result)
  - [APIs](#apis)

## Demo

This is the suite's demo. Suite will generate a web page that include a chart.

![Demo img](/Images/Demo_web.png)

## Tutorial

### Isnstallation

First,install the suite by using pip.

```
pip install Model-Visual
```

### Create object

Then,creat an object and set some parameter.

Test is the name of an object, you can take any name you want. And model is your keras model's name.(Notice: the model has to be compiled)

```
from model_visual import ModelVisual

test = ModelVisual(model)
```

### Run and get result

```
test.run()
test.save_web_page()
```

Beside ``save_web_page()``,you can also use ``return_js_code()`` or ``return_web_page()``.

``save_web_page()`` will create a html file,
 ``return_js_code()`` and ``save_web_page()`` will return you sourse code.

## APIs

```

set_name(): # set the html file name

set_path(): # set the html path name

set_chart_fill_color(): # set the cart fill color

set_chart_stroke_color(): # set the chart strole color

set_chart_stroke_width(): # set the chart stroke width

set_model(): # set the keras model

```
