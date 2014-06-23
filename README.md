Using Bower In Django
=======================

This repository illustrates how to use [Bower](http://bower.io/) to manage front end dependencies in [Django](https://www.djangoproject.com/) projects.

![](https://raw.githubusercontent.com/PabloVallejo/django-bower/master/screenshot.png)

## Original Article
> [View Original Article](http://axiacore.com/blog/effective-dependency-management-django-using-bower).

## Setup

In order to run the example project locally, issue the following commands.

```bash
# Clone the repo
$ git clone https://github.com/axiacore/django-bower & cd django-bower

# Install requirements
$ pip install -U -r requirements.txt

# Sync database
$ ./manage.py syncdb

# Run the server
$ ./manage.py runserver
```

## Contributing

1. Fork the repo.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

## License
[MIT License](http://opensource.org/licenses/MIT)
