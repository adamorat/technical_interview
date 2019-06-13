star_wars
=========

Entrevista técnica: Información sobre Star Wars

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Como arrancar el servicio
-------------------------

En primer lugar debemos acceder a la ruta en la que se encuentra el proyecto clonado o descomprimido mediante terminal.
Tras esto ejecutamos las siguientes lineas.

Importante seguir los siguientes pasos.

* Desde windows:

    $ cd star_wars

    $ venv\\Scripts\\activate

    $ python manage.py runserver

* Desde linux:

    $ cd star_wars

    $ linux_venv/bin/activate

    $ python star_wars/manage.py runserver

Hecho esto, nos dirigimos al navegador (Google Chrome) e introducimos la siguiente URL: http://localhost:8000/


Uso de la plataforma
--------------------

El aplicativo está basado íntegramente en las instrucciones aportadas.

Para realizar las pruebas se ha creado un usuario admin en caso de que fuera necesario:

* username: admin

* password: string1234

En primer lugar, tenemos la pagina de "login" donde se podrá acceder con un usuario ya creado o pulsar sobre
"Crear una cuenta"

Una vez dentro, podremos visualizar el carrusel de personajes y el buscador de películas en la barra superior.

En el menú lateral izquierdo tenemos dos opciones:

* Buscador de Películas: Sería la página actual.

* Historial de Páginas Visitadas: Histórico con las url visitadas, fecha y hora de la visita.

Por último, para ver información sobre una película solo tenemos que comenzar una búsqueda en el formulario de la barra
superior (accesible desde cualquier vista). Una vez se empiezan a introducir caracteres, se mostrarán las sugerencias
seleccionables por el usuario.

En la esquina superior derecha tendrá un desplegable desde el cual podrá escoger la opción de "Logout" (cerrar sesión)




