## PreEntrega Documentacion

Esta es una pagina de una compania que ingresa datos a una compania de alquiler.

El nombre del proyecto es "AlquilerCarro" y el nombre de la aplicacion es "autorental"

En la Home de localhost:port/ --> Va a estar el home del proyecto, solo cargando texto y tambien la posibilidad de irnos con hipervinculo a la APP.

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

Testing