## Entrega Final Documentacion


## AutoRental Project

Bienvenido a AutoRental, esta es una aplicacion, desarrollada y escrita en python con Django framework como backend. Esta pagina tiene como uso, el de una compania que administra e ingresa datos a una compania de alquiler de autos.

El nombre del proyecto es "AlquilerCarro" y el nombre de la aplicacion es "autorental"

En la Home de localhost:port/ --> Va a estar el home del proyecto, solo cargando texto y tambien la posibilidad de irnos con hipervinculo a la APP.

## Informacion del Contenido
Tenemos la home de Auto Rental con diferentes opciones para realizar, entre esas:

- Agregar Carro
- Crear Reserva para cliente
- Buscar Reserva por nombre
- Ver todas las Reservas
- Crear seguro
- Ver toda la lista de Carros creados


* Si hacemos click en cada una de las opciones vamos a irnos a las URLs contenidas en urls.py:

    ("", home_view),
    ("listofcars/", list_view), --> lista de los carros
    ("crear-carro-con-form/", agregar_carro, name ="yyy"), -----> URL para crear nuevos carros
    ("detail-carro/<auto_id>", detail_auto_view), ---> URL para observar detalles de un carro recien creado
    ("crear-reserva-form/", crear_reserva, name="zzz"), ----> vista para crear reserva.
    ("buscar-con-formulario/", search_with_form_view, name="xyz"), ---> buscar reserva ya creada
    ("listareservas/", reservas_lista, name="zyz"), ----> lista de reservas creadas
    ("seguros/", segurosautos), ---> aun no realizada esta view, no va arrojar resultado, pero es para obtener lista de seguros.
    ("seguros/crear", crearseguro, name="jjj"), --->crear seguro

## Informacion del Funcionamiento
Aqui tambien podemos observar el View o vista de cada URL, que se encuentra en views.py y en el view, se pueden ver las funciones que van a crear objetos siguiendo el esquema MVT.

Tenemos 3 models:
- Carro
- Reserva
- Seguro

Por ejemplo en Crear Reserva.
Vamos a usar el modelo en models.py llamado Reserva, para crear este objeto en base de datos usando un formulario.

Este formulario va a utilizar forms.py para modelar los fields que van a enviarse en el form.


Los forms van a estar alojados en templates/autorental , con nombres sugestivos, por ejemplo para crear reserva sera form-create.html, para crear carro form-create-carro.html.

en la entrega tenemos form-search.html para buscar una reserva.

tenemos tambien form-create, form-create-seguro y form-create-carro para insertar datos a las clases de los models.

Estos forms son hijos que heredan de base.html tambien autorental/template el estilo del entorno del sitio y se puede observar el envio del form con el metodo form = POST y la action que es la URL a la que pertenece la vista, por ejemplo para crear es 'zzz'.

Estamos usando casi la misma estructura que tenia el profesor en las clases.

Estamos usando tambien el mismo bootsrap css que puso el profe.

## Login

El funcionamiento del login es evitar que un usuario que no este logueado pueda entrar a "crear usuario" "crear reserva" "crear auto" "crear seguro" esto lo hacemos con el decorator de loginrequired en cada URL.

##  Admin Users

Tenemos tambien la posibilidad de crear y administrar desde el backend side que usuarios son de staff y que usuarios son los administradores del servidor, esto lo podemos ver si vamos a localhost:4000/admin , desde ahi tambien podemos ver que tenemos dos tablas la de reserva y de carro y ahi tambien observar las tablas y editarlas.

Desde aca tambien podemos agregar otros usuarios con otros permisos y podemos estar haciendo uso del CRUD.

El super admin que cree para mi es admin y el password es cisco123.

## Edicion y eliminado de objetos (Carro)

Tenemos la opcion de crear carro con formulario y luego, desde la vista de lista de los carros, podemos tambien eliminar o modificar las caracteristicas de estos vehiculos.

## Busqueda de Reserva usando nombre

Tenemos tambien la posibilidad de buscar objetos ya instalados en nuestra base de datos, como ejemplo podemos buscar una reserva usando un nombre de un cliente que ha reservado y desde ahi tambien observar detalles de esta reserva.

## About Me

Dentro del contenido del home de la aplicacion Autorental, observamos la opcion de irnos a leer informacion personal del creador del proyecto con el boton "About Me" desde aca tambien podemos regresar a Home.

## Navegabilidad

Observamos que tenemos la posibilidad de irnos a cualquier elemento como:
Carros
Agregar Carros
Crear Reserva
Buscar Reserva
Lista de todas reservas
Crear Seguro
About me

Y desde cada una de estas secciones tambien podemos navegar de vuelta.

Tambien tenemos un redirect hacia login para que nadie pueda acceder directamente a todas nuestras opciones sin antes loguearse, esto lo concretamos desde urls.py del proyecto "AlquilerCarros" con esta linea     "path("", RedirectView.as_view(url="/autorental/login", permanent=True))"


