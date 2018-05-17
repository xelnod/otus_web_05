# Otus Web 05 Online Store Demo

This is an online store demo created by S.Zenchenko for OTUS Web Lessons using Flask

## Getting Started

### Prerequisites

- Python 3.6+
- Virtualenv
- Pip


### Installing

Make a new virtualenv (you may as well not if you know what you're doing)

```
$ virtualenv -p python3 otus_web_05
```

Clone this repo

```
$ git clone https://github.com/xelnod/otus_web_05.git
```


Install requirements

```
$ pip install -r requirements.txt
```
## Using

### Run
```
$ flask run
```

### Add a category/product
```
$ flask shell
>>> from models import Product, ProductCategory
>>> from app import db
>>> pc = ProductCategory(name='Планшеты', stub='tablets')
>>> db.session.add(pc)
>>> db.session.commit()
>>> p = Product(
    name='iPad Pro', 
    description='This is an iPadPro\n It\'s very cool!',
    image_url='https://assets.logitech.com/assets/65413/base-pdp-refresh.png',
    price_kopeck=10050000,
    categories=[pc,])
>>> db.session.add(p)
>>> db.session.commit()
```

## Features
- Test DB included for demo purposes
- Product categories
- Product List (including pagination and category filters)
- Product detail page
- Human-readable url support via stubs (e.g. /products/laptops)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
